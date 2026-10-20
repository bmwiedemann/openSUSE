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
	sdbootutil -v --no-random-seed --arch "$arch" --esp-path /boot/efi --entry-token=auto --no-variables install

	echo "add kernels"
	export hostonly_l=no # for dracut
	sdbootutil -v --arch "$arch" --esp-path /boot/efi --entry-token=auto add-all-kernels
	# Set a 5s timeout, the "hold a key down" method doesn't work effectively.
	sdbootutil -v --arch "$arch" --esp-path /boot/efi set-timeout 5

	rm -f /boot/mbrid

	find /boot
fi
