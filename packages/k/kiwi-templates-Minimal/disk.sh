#!/bin/bash
set -euxo pipefail

echo "####### BOOTLOADER INSTALL (disk.sh)"

if [ -x /usr/bin/sdbootutil ]; then
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

echo "####### END BOOTLOADER INSTALL (disk.sh)"
