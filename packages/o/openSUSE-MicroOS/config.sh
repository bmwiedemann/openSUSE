#!/bin/bash
# Copyright (c) 2020 SUSE LLC
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
#======================================
# Functions...
#--------------------------------------

test -f /.kconfig && . /.kconfig
test -f /.profile && . /.profile

set -euxo pipefail

echo "Configure image: [$kiwi_iname]-[$kiwi_profiles]..."

# Systemd controls the console font now
echo FONT="eurlatgr.psfu" >> /etc/vconsole.conf

#======================================
# prepare for setting root pw, timezone
#--------------------------------------
echo "** reset machine settings"
rm -f /etc/machine-id \
      /var/lib/zypp/AnonymousUniqueId \
      /var/lib/systemd/random-seed

#======================================
# Specify default systemd target
#--------------------------------------
baseSetRunlevel multi-user.target

#======================================
# Import trusted rpm keys
#--------------------------------------
suseImportBuildKey

#======================================
# Set hostname by DHCP
#--------------------------------------
baseUpdateSysConfig /etc/sysconfig/network/dhcp DHCLIENT_SET_HOSTNAME yes

# Add repos from /etc/YaST2/control.xml
if [ -x /usr/sbin/add-yast-repos ]; then
	add-yast-repos
	zypper --non-interactive rm -u live-add-yast-repos
fi

# Adjust zypp conf
sed -i 's/^multiversion =.*/multiversion =/g' /etc/zypp/zypp.conf

#=====================================
# Configure snapper
#-------------------------------------
if [ "${kiwi_btrfs_root_is_snapshot-false}" = 'true' ]; then
        echo "creating initial snapper config ..."
        cp /etc/snapper/config-templates/default /etc/snapper/configs/root \
		|| cp /usr/share/snapper/config-templates/default /etc/snapper/configs/root
        baseUpdateSysConfig /etc/sysconfig/snapper SNAPPER_CONFIGS root

	# Adjust parameters
	sed -i'' 's/^TIMELINE_CREATE=.*$/TIMELINE_CREATE="no"/g' /etc/snapper/configs/root
	sed -i'' 's/^NUMBER_LIMIT=.*$/NUMBER_LIMIT="2-10"/g' /etc/snapper/configs/root
	sed -i'' 's/^NUMBER_LIMIT_IMPORTANT=.*$/NUMBER_LIMIT_IMPORTANT="4-10"/g' /etc/snapper/configs/root
fi

#=====================================
# Enable chrony if installed
#-------------------------------------
if [ -f /etc/chrony.conf ]; then
	systemctl enable chronyd
fi

# Enable jeos-firstboot if installed, disabled by combustion/ignition
if rpm -q --whatprovides jeos-firstboot >/dev/null; then
	mkdir -p /var/lib/YaST2
	touch /var/lib/YaST2/reconfig_system
	systemctl enable jeos-firstboot.service
fi

# The %post script can't edit /etc/fstab sys due to https://github.com/OSInside/kiwi/issues/945
# so use the kiwi custom hack
cat >/etc/fstab.script <<"EOF"
#!/bin/sh
set -eux

/usr/sbin/setup-fstab-for-overlayfs
# If /var is on a different partition than /...
if [ "$(findmnt -snT / -o SOURCE)" != "$(findmnt -snT /var -o SOURCE)" ]; then
	# ... set options for autoexpanding /var
	gawk -i inplace '$2 == "/var" { $4 = $4",x-growpart.grow,x-systemd.growfs" } { print $0 }' /etc/fstab
fi
EOF

cat >>/etc/fstab.script <<"EOF"
# Relabel /etc. While kiwi already relabelled it earlier, there are some files created later (boo#1210604).
# The "gawk -i inplace" above also removes the label on /etc/fstab.
if [ -e /etc/selinux/config ]; then
	. /etc/selinux/config
	touch /etc/sysconfig/bootloader # Make sure this exists so it gets labelled
	setfiles -e /proc -e /sys -e /dev /etc/selinux/${SELINUXTYPE}/contexts/files/file_contexts /etc
fi
EOF

chmod a+x /etc/fstab.script

# To make x-systemd.growfs work from inside the initrd
cat >/etc/dracut.conf.d/50-microos-growfs.conf <<"EOF"
install_items+=" /usr/lib/systemd/systemd-growfs "
EOF

#======================================
# Disable recommends on virtual images (keep hardware supplements, see bsc#1089498)
#--------------------------------------
sed -i 's/.*solver.onlyRequires.*/solver.onlyRequires = true/g' /etc/zypp/zypp.conf

#======================================
# Disable installing documentation
#--------------------------------------
sed -i 's/.*rpm.install.excludedocs.*/rpm.install.excludedocs = yes/g' /etc/zypp/zypp.conf

#======================================
# Add default kernel boot options
#--------------------------------------
serialconsole='console=ttyS0,115200'
[[ "$kiwi_profiles" == *"RaspberryPi2" ]] && serialconsole='console=ttyAMA0,115200'
[[ "$kiwi_profiles" == *"Rock64" ]] && serialconsole='console=ttyS2,1500000'

cmdline=('quiet' 'systemd.show_status=yes' "${serialconsole}" 'console=tty0')
rpm -q wicked && cmdline+=('net.ifnames=0')

ignition_platform='metal'
case "${kiwi_profiles}" in
	*kvm*) ignition_platform='qemu' ;;
	*DigitalOcean*) ignition_platform='digitalocean' ;;
	*VMware*) ignition_platform='vmware' ;;
	*OpenStack*) ignition_platform='openstack' ;;
	*VirtualBox*) ignition_platform='virtualbox' ;;
	*HyperV*) ignition_platform='metal'
		  cmdline+=('rootdelay=300') ;;
	*Pine64*|*RaspberryPi*|*Rock64*|*Vagrant*) ignition_platform='metal' ;;
	# Use autodetection on selfinstall. The first boot doesn't use the grub
	# cmdline anyway, it's started with kexec using kiwi's builtin default.
	*SelfInstall*) ignition_platform='' ;;
	*) echo "Unhandled profile?"
	   exit 1
	   ;;
esac

if [ -n "${ignition_platform}" ]; then
	cmdline+=("ignition.platform.id=${ignition_platform}")
fi

#======================================
# If SELinux is installed, configure it like transactional-update setup-selinux
#--------------------------------------
if [[ -e /etc/selinux/config ]]; then
	cmdline+=("security=selinux selinux=1")
	# Adjust selinux config
	sed -i -e 's|^SELINUX=.*|SELINUX=enforcing|g' \
	    -e 's|^SELINUXTYPE=.*|SELINUXTYPE=targeted|g' \
	    "/etc/selinux/config"

	# Move an /.autorelabel file from initial installation to writeable location
	test -f /.autorelabel && mv /.autorelabel /etc/selinux/.autorelabel
fi

if [ -e /etc/default/grub ]; then
	sed -i "s#^GRUB_CMDLINE_LINUX_DEFAULT=.*\$#GRUB_CMDLINE_LINUX_DEFAULT=\"${cmdline[*]}\"#" /etc/default/grub
fi

#======================================
# Wicked specific configuration (in addition to the net.ifnames=0 above)
#--------------------------------------
if rpm -q wicked; then
	# Enable DHCP on eth0
	cat >/etc/sysconfig/network/ifcfg-eth0 <<EOF
BOOTPROTO='dhcp'
STARTMODE='auto'
EOF

	# Workaround: Force network-legacy, network-wicked is not usable (boo#1182227)
	if rpm -q combustion; then
		# Modify module-setup.sh, but undo the modification on the first call
		mv /usr/lib/dracut/modules.d/40network/module-setup.sh{,.orig}
		sed 's#echo "kernel-network-modules $network_handler"$#echo kernel-network-modules network-legacy; mv /usr/lib/dracut/modules.d/40network/module-setup.sh{.orig,}#' \
			/usr/lib/dracut/modules.d/40network/module-setup.sh.orig > /usr/lib/dracut/modules.d/40network/module-setup.sh
	fi
else
	systemctl enable NetworkManager
fi

#======================================
# Configure Pine64 specifics
#--------------------------------------
if [[ "$kiwi_profiles" == *"Pine64"* ]]; then
	echo 'add_drivers+=" fixed sunxi-mmc axp20x-regulator axp20x-rsb "' > /etc/dracut.conf.d/sunxi_modules.conf
fi

#======================================
# Configure Raspberry Pi specifics, unless done by raspberrypi-firmware already (on TW)
#--------------------------------------
if [[ "$kiwi_profiles" == *"RaspberryPi"* ]] && ! [[ -e /usr/lib/dracut/dracut.conf.d/raspberrypi_modules.conf ]]; then
	# Add necessary kernel modules to initrd (will disappear with bsc#1084272)
	echo 'add_drivers+=" bcm2835_dma dwc2 "' > /etc/dracut.conf.d/raspberrypi_modules.conf

	# Add necessary kernel modules to initrd (will disappear with boo#1162669)
	echo 'add_drivers+=" pcie-brcmstb "' >> /etc/dracut.conf.d/raspberrypi_modules.conf

	# Work around network issues
  	cat > /etc/modprobe.d/50-rpi3.conf <<-EOF
		# Prevent too many page allocations (bsc#1012449)
		options smsc95xx turbo_mode=N
	EOF

	cat > /usr/lib/sysctl.d/50-rpi3.conf <<-EOF
		# Avoid running out of DMA pages for smsc95xx (bsc#1012449)
		vm.min_free_kbytes = 2048
	EOF
fi

#======================================
# Configure Vagrant specifics
#--------------------------------------
if [[ "$kiwi_profiles" == *"Vagrant"* ]]; then
        # create vagrant user
        useradd vagrant
        # allow password-less sudo
        echo "vagrant ALL=(ALL)NOPASSWD:ALL" > /etc/sudoers.d/vagrant
        # add vagrant's insecure key
        mkdir -p /home/vagrant/.ssh
        chmod 0700 /home/vagrant/.ssh
        cat > /home/vagrant/.ssh/authorized_keys << EOF
ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key
EOF
        chmod 0600 /home/vagrant/.ssh/authorized_keys
        chown -R vagrant /home/vagrant
fi

#======================================
# Configure FDE/BLS specifics
#--------------------------------------
# [[ "$kiwi_profiles" == *"kvm-and-xen-"* ]]
if rpm -q sdbootutil; then
 	for d in /usr/lib/modules/*; do
 		test -d "$d" || continue
 		depmod -a "${d##*/}"
 	done
 	ENTRY_TOKEN=$(. /usr/lib/os-release; echo $ID)
 	mkdir -p /etc/kernel
 	echo "$ENTRY_TOKEN" > /etc/kernel/entry-token
 	# FIXME: kiwi needs /boot/efi to exist before syncing the disk image
 	mkdir -p /boot/efi

        echo "${cmdline[*]}" > /etc/kernel/cmdline
fi
