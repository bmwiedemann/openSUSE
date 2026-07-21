#!/bin/bash
set -euxo pipefail

echo "Setting up /etc as subvolume"
/usr/libexec/setup-etc-subvol

echo "Adjusting snapper configuration"
grep -E '^SNAPPER_CONFIGS="root"' /etc/sysconfig/snapper # assert that kiwi created and registered the default config
snapper --no-dbus set-config TIMELINE_CREATE=no NUMBER_LIMIT=2-10 NUMBER_LIMIT_IMPORTANT=4-10

if [ -x /usr/bin/sdbootutil ]; then
	echo "Installing bootloader using sdbootutil"
	arch="$(uname -m)"
	case "$arch" in
		aarch64) arch=aa64 ;;
		riscv64) arch=riscv64 ;;
		x86_64) arch=x64 ;;
		*) echo "Unknown arch $arch"; exit 1 ;;
	esac

	echo "install boot loader"
	loader_type="grub2-bls"
	secure_boot="no"
	rpm -q systemd-boot && loader_type="systemd-boot"
	rpm -q shim && secure_boot="yes"
	if [ -s /etc/sysconfig/bootloader ]; then
		sed -i "s/^LOADER_TYPE=.*$/LOADER_TYPE=\"$loader_type\"/g" /etc/sysconfig/bootloader
		sed -i "s/^SECURE_BOOT=.*$/SECURE_BOOT=\"$secure_boot\"/g" /etc/sysconfig/bootloader
	else
		echo "LOADER_TYPE=\"${loader_type}\"" >> /etc/sysconfig/bootloader
		echo "SECURE_BOOT=\"${secure_boot}\"" >> /etc/sysconfig/bootloader
	fi

	sdbootutil -v --no-random-seed --arch "$arch" --esp-path /boot/efi --entry-token=auto --no-variables install

	echo "add kernels"
	export hostonly_l=no # for dracut
	sdbootutil -v --arch "$arch" --esp-path /boot/efi --entry-token=auto add-all-kernels
	# Set a 5s timeout, the "hold a key down" method doesn't work effectively.
	sdbootutil -v --arch "$arch" --esp-path /boot/efi set-timeout 5

	rm -f /boot/mbrid

	find /boot
fi
