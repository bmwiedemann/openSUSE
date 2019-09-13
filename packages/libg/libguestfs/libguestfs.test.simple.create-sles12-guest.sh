#!/bin/bash
# Create an openSUSE image with just enough packages to allow boot to login prompt
#
# Theory of operation:
#  This script uses zypper from the host to resolve dependencies 
#  for zypper which runs within the appliance. If zypper on the host
#  is too old, it will be unable to handle repo data from 13.1:
#    http://lists.opensuse.org/zypp-devel/2013-11/msg00000.html
#    "[zypp-devel] Package conflicting with itself"
#  For this reason zypper from 12.3 can be used to install the pattern
#  of the final repo.
#  First the dependencies of zypper are resolved, the required packages
#  are downloaded and extracted with unrpm. Now the guest is started and
#  the partitions in the diskimage are prepared. Then the extracted
#  package content is copied into the guest. Once that is done zypper
#  inside the guest will install the base pattern and a few extra packages.
#  Finally the bootloader grub is configured. Once all that is done
#  kvm is started. If all goes well a login prompt appears.
#  The password for root is "root".
#  The guest has also network access to the outside.
#
# Expected runtime: ca. 180 seconds
#
# Expected output:
# guest should start
# no "obvious" errors should be shown during the disk operation
# at the end kvm is started with the generated disk image
# login should be possible
#
set -e
unset LANG
unset ${!LC_*}
cpus=`grep -Ec 'cpu[0-9]' /proc/stat || echo 1`

output_diskimage=/dev/shm/$LOGNAME/testcase.img
final_repo=http://dist.suse.de/install/SLP/SLE-12-Server-LATEST/x86_64/DVD1
initial_repo=http://dist.suse.de/install/SLP/SLE-12-Server-LATEST/x86_64/DVD1
force=false
guest_zypper_in__pattern_name="base"
guest_zypper_in__package_list="
grub2
kernel-default
less
master-boot-code
nfs-utils
parted
vim
"
guest_root_password="root"
diskname_inside_vm=/dev/sda

case "$0" in
	/*) progname="$0" ;;
	*) progname="$PWD/$0" ;;
esac

_exit() {
	echo "Exiting '$0 $*'."
	exit 1
}

_unrpm() {
	CPIO_OPTS="--extract --unconditional --preserve-modification-time --make-directories"
	FILES="$@"
	for f in $FILES; do
		echo -ne "$f:\t"
		rpm2cpio $f | cpio ${CPIO_OPTS}
	done
}

until test $# -lt 1
do
	case "$1" in
		--unrpm) shift ; _unrpm "$@" ; exit 0 ;;
		-n) diskname_inside_vm="$2" ; shift ;;
		-o) output_diskimage="$2" ; shift ;;
		-R) initial_repo="$2" ; shift ;;
		-r) final_repo="$2" ; shift ;;
		-f) force=true ;;
		-x) set -x ;;
		*) echo "Unknown option '$1'" ; exit 1 ;;
	esac
	shift
done
if test -z "${initial_repo}"
then
	echo "URL to initial repo required. Wrong -R option."
	_exit
fi
if test -z "${final_repo}"
then
	echo "URL to final repo required. Wrong -r option."
	_exit
fi
if test -z "${output_diskimage}"
then
	echo "Filename for temporary disk image required. Wrong -o option."
	_exit
fi
if test -e "${output_diskimage}"
then
	if test "${force}" = "false"
	then
		echo "Output diskimage '${output_diskimage}' exists."
		echo "It will not be overwritten. Option '-f' exists to force overwrite."
		_exit
	fi
fi
zypper --version
cpio --version
guestfish --version
kvm="qemu-system-`uname -m`"
if $kvm --version
then
	: good
else
	kvm="qemu-kvm"
	if $kvm --version
	then
		:
	else
		echo "No qemu-kvm found."
		_exit
	fi
fi

mkdir -vp "${output_diskimage%/*}"
td=`mktemp -d --tmpdir=/dev/shm/${LOGNAME}`
tf=`mktemp    --tmpdir=/dev/shm/${LOGNAME}`
_exit() {
rm -rf "$tf"
rm -rf "$td"
}
trap _exit EXIT
dir_repo=${td}/repos.d
dir_root=${td}/root
dir_cache=${td}/cache
mkdir -vp \
	${dir_root} \
	${dir_cache} \
	${dir_repo}
cat > ${tf} <<EOF
[main]
reposdir = ${dir_repo}
EOF
cat > ${dir_repo}/tmp.repo <<EOF
[tmp]
name=tmp
enabled=1
autorefresh=1
keeppackages=0
baseurl=${initial_repo}
EOF
packages="
curl
iproute2
zypper
"
head ${dir_repo}/tmp.repo ${tf}
zypper \
	--verbose \
	--verbose \
	--config ${tf} \
	--root ${dir_root} \
	--reposd-dir ${dir_repo} \
	--cache-dir ${dir_cache} \
	--gpg-auto-import-keys \
	--no-gpg-checks \
	--non-interactive \
	lr -d
zypper \
	--verbose \
	--verbose \
	--config ${tf} \
	--root ${dir_root} \
	--reposd-dir ${dir_repo} \
	--cache-dir ${dir_cache} \
	--gpg-auto-import-keys \
	--no-gpg-checks \
	--non-interactive \
        install \
	--auto-agree-with-licenses \
	--no-recommends \
	--dry-run \
	--download-only \
	${packages}
cd ${dir_root}
find ${dir_cache} -xdev -name "*.rpm" -print0 | sort -z | xargs -0 -n 1 -P ${cpus} bash "${progname}" --unrpm
mkdir -vp etc/zypp/repos.d
grep -w search /etc/resolv.conf >> etc/resolv.conf
echo nameserver 169.254.2.3 >> etc/resolv.conf
grep -w root /etc/passwd > etc/passwd
grep -w root /etc/group  > etc/group
echo 'root::15209::::::' > etc/shadow
cat > etc/fstab <<EOF
LABEL=SWAP swap swap  defaults 0 0
LABEL=ROOT /    ext4  noatime  1 2
EOF
du -sm .
find ${dir_cache} -xdev -name "*.rpm" -delete
guestfish \
	-x \
	\
sparse ${output_diskimage} 1024M : \
set-smp 2 : \
set-memsize 1024 : \
set-network true : \
run : \
list-devices : \
part-init          ${diskname_inside_vm} mbr : \
part-add           ${diskname_inside_vm} primary 1                             $(( ((1024*1024)*  64)/512 - 1)) : \
part-add           ${diskname_inside_vm} primary $(( ((1024*1024)*  64)/512 )) $(( ((1024*1024)*1024)/512 - 1)) : \
part-list          ${diskname_inside_vm} : \
mkswap-opts        ${diskname_inside_vm}1 label:SWAP : \
mke2fs             ${diskname_inside_vm}2 label:ROOT fstype:ext4 blocksize:1024 : \
list-devices : \
list-partitions : \
part-set-bootable ${diskname_inside_vm} 2 true : \
list-filesystems : \
swapon-label SWAP : \
mount-options noatime ${diskname_inside_vm}2 / : \
set-verbose false : \
copy-in `echo *` / : \
set-verbose true : \
command /sbin/ldconfig : \
cat /etc/resolv.conf : \
command "ip a" : \
command "curl google.com" : \
command "zypper help" : \
command "zypper -v -v ar -c -K -f ${final_repo} tmp" : \
sh "(set -x -e ; z_in='zypper -v -v --gpg-auto-import-keys --no-gpg-checks --non-interactive in --auto-agree-with-licenses --no-recommends ' ; \$z_in -t pattern ${guest_zypper_in__pattern_name} ; chkstat --set /etc/permissions /etc/permissions.easy ; echo root:${guest_root_password} | chpasswd ; \$z_in `eval echo ${guest_zypper_in__package_list}` ) < /dev/null &>/dev/kmsg " : \
sh "depmod -a \$(get_kernel_version /boot/vmlinuz) ; mkinitrd -B" : \
sh "dd if=/usr/lib/boot/MBR of=${diskname_inside_vm}" : \
sh "echo GRUB_DISABLE_OS_PROBER=true >> /etc/default/grub " : \
sh "echo GRUB_DISABLE_LINUX_RECOVERY=true >> /etc/default/grub " : \
sh "echo GRUB_CMDLINE_LINUX_DEFAULT=\'quiet panic=9 video=800x600 \' >> /etc/default/grub " : \
sh "grub2-mkconfig > /boot/grub2/grub.cfg " : \
sh "grub2-install --force --verbose ${diskname_inside_vm}2 " : \
sh "echo BOOTPROTO='dhcp' >> /etc/sysconfig/network/ifcfg-eth0"  : \
sh "echo STARTMODE='auto' >> /etc/sysconfig/network/ifcfg-eth0" : \
sh "echo 'Password for User root is: ${guest_root_password}' >> /etc/issue" : \
sh "echo >> /etc/issue" : \
cat /etc/fstab : \
quit
ls -lhsS "${output_diskimage}"

: ${diskname_inside_vm}
case "${diskname_inside_vm}" in
	*vda*)
	qemu_drive_options="
	-drive file=${output_diskimage},cache=writeback,id=hd0,if=none \
	-device virtio-blk-pci,drive=hd0 \
	"
	;;
	*sda*)
	qemu_drive_options="
	-device virtio-scsi-pci,id=scsi \
	-drive file=${output_diskimage},cache=unsafe,format=raw,id=hd0,if=none \
	-device scsi-hd,drive=hd0 \
	"
	;;
	*)
	echo "${diskname_inside_vm} not handled"
	_exit
esac
$kvm -enable-kvm \
	-global virtio-blk-pci.scsi=off \
	-enable-fips \
	-machine accel=kvm:tcg \
	-cpu host,+kvmclock \
	-m 500 \
	-no-reboot \
	-no-hpet \
	${qemu_drive_options} \
	-device virtio-serial-pci \
	-serial stdio \
	-device VGA \
	-netdev user,id=usernet,net=169.254.0.0/16 \
	-device virtio-net-pci,netdev=usernet

exit 0
