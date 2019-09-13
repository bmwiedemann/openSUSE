#!/bin/bash
# Create an openSUSE image with lvm on dm-crypt partition
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
#  The password for the crypted partition is "123456".
#  The password for root is "root".
#  The guest has also network access to the outside.
#
# Expected runtime: ca. 200 seconds
# Requires at least 1.24.5 because this includes the required crypt modules
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
final_repo=http://download.opensuse.org/distribution/13.1/repo/oss/
initial_repo=http://download.opensuse.org/distribution/12.3/repo/oss/
force=false
guest_zypper_in__pattern_name="base"
guest_zypper_in__package_list="
grub
less
master-boot-code
nfs-utils
parted
vim
"
guest_root_password="root"
guest_crypt_password="123456"
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
guestfish_version="`guestfish --version | awk '{print \$2}'`"
case "${guestfish_version}" in
	1.20*) _exit ;;
	1.21*) _exit ;;
	1.22*) _exit ;;
	1.23*) _exit ;;
	1.24.[0-4]) _exit ;;
	*) ;;
esac

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
mkdir -p boot/grub
cat > etc/grub.conf <<EOF
setup --stage2=/boot/grub/stage2 --force-lba (hd0,1) (hd0,1)
quit
EOF
echo "(hd0) ${diskname_inside_vm}" > boot/grub/device.map
cat > boot/grub/menu.lst <<EOF
serial --unit=0 --speed=115200
terminal --timeout=10 console serial
title ${0} $*
	kernel /boot/vmlinuz panic=9 quiet video=800x600
	initrd /boot/initrd
EOF
du -sm .
find ${dir_cache} -xdev -name "*.rpm" -delete
(
echo "${guest_crypt_password}"
echo "${guest_crypt_password}"
) | \
guestfish \
	-x \
	--keys-from-stdin \
	\
sparse ${output_diskimage} 2048M : \
set-smp 2 : \
set-memsize 1024 : \
set-network true : \
run : \
list-devices : \
part-init          ${diskname_inside_vm} mbr : \
part-add           ${diskname_inside_vm} primary 1                             $(( ((1024*1024)* 256)/512 - 1)) : \
part-add           ${diskname_inside_vm} primary $(( ((1024*1024)* 256)/512 )) $(( ((1024*1024)*1024)/512 - 1)) : \
part-add           ${diskname_inside_vm} primary $(( ((1024*1024)*1024)/512 )) $(( ((1024*1024)*1555)/512 - 1)) : \
part-add           ${diskname_inside_vm} primary $(( ((1024*1024)*1555)/512 )) $(( ((1024*1024)*2024)/512 - 1)) : \
part-list          ${diskname_inside_vm} : \
mkswap-opts        ${diskname_inside_vm}1 label:SWAP : \
mke2fs             ${diskname_inside_vm}2 label:ROOT fstype:ext4 blocksize:1024 : \
pvcreate           ${diskname_inside_vm}3 : \
vgcreate uncrypted ${diskname_inside_vm}3 : \
luks-format        ${diskname_inside_vm}4 0 : \
luks-open          ${diskname_inside_vm}4 crypt_part4 : \
pvcreate           /dev/mapper/crypt_part4 : \
vgcreate   crypted /dev/mapper/crypt_part4 : \
lvcreate-free root uncrypted 50 : \
lvcreate-free work uncrypted 50 : \
lvcreate-free home   crypted 50 : \
lvcreate-free mail   crypted 50 : \
list-devices : \
list-partitions : \
pvs-full : \
vgs-full : \
lvs-full : \
mke2fs /dev/uncrypted/root label:LV_ROOT fstype:ext4 blocksize:1024 : \
mke2fs /dev/uncrypted/work label:LV_WORK fstype:ext4 blocksize:1024 : \
mke2fs /dev/crypted/home   label:LV_HOME fstype:ext4 blocksize:1024 : \
mke2fs /dev/crypted/mail   label:LV_MAIL fstype:ext4 blocksize:1024 : \
part-set-bootable ${diskname_inside_vm} 2 true : \
list-filesystems : \
swapon-label SWAP : \
mount-options discard ${diskname_inside_vm}2 / : \
set-verbose false : \
copy-in `echo *` / : \
set-verbose true : \
command /sbin/ldconfig : \
cat /etc/resolv.conf : \
command "ip a" : \
command "curl google.com" : \
command "zypper help" : \
command "zypper -v -v ar -c -K -f ${final_repo} tmp" : \
sh "(set -x -e ; z_in='zypper -v -v --gpg-auto-import-keys --no-gpg-checks --non-interactive in --auto-agree-with-licenses --no-recommends' ; \$z_in -t pattern ${guest_zypper_in__pattern_name} ; chkstat --set /etc/permissions /etc/permissions.easy ; echo root:${guest_root_password} | chpasswd ; \$z_in `eval echo ${guest_zypper_in__package_list}` ) 2>&1 " : \
sh "depmod -a \$(get_kernel_version /boot/vmlinuz) ; mkinitrd -B" : \
sh "dd if=/usr/lib/boot/MBR of=${diskname_inside_vm}" : \
sh "cp --verbose --sparse=never --remove-destination --target-directory=/boot/grub /usr/lib/grub/*" : \
sh "grub --batch --verbose < /etc/grub.conf" : \
sh "echo crypt_part4 ${diskname_inside_vm}4 none luks,timeout=0 >> /etc/crypttab" : \
mkdir /LV_ROOT : \
sh "echo LABEL=LV_ROOT /LV_ROOT ext4 noatime 1 2 >> /etc/fstab" : \
mkdir /LV_WORK : \
sh "echo LABEL=LV_WORK /LV_WORK ext4 noatime 1 2 >> /etc/fstab" : \
mkdir /LV_HOME : \
sh "echo LABEL=LV_HOME /LV_HOME ext4 noatime 1 2 >> /etc/fstab" : \
mkdir /LV_MAIL : \
sh "echo LABEL=LV_MAIL /LV_MAIL ext4 noatime 1 2 >> /etc/fstab" : \
sh "echo BOOTPROTO='dhcp' >> /etc/sysconfig/network/ifcfg-eth0"  : \
sh "echo STARTMODE='auto' >> /etc/sysconfig/network/ifcfg-eth0" : \
sh "echo 'Password for User root is: ${guest_root_password}' >> /etc/issue" : \
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
	-device sga \
	-netdev user,id=usernet,net=169.254.0.0/16 \
	-device virtio-net-pci,netdev=usernet

exit 0
