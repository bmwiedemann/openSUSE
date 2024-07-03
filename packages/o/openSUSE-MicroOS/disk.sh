#!/bin/bash
set -euxo pipefail
[ -x /usr/bin/sdbootutil ] || exit 0

echo "####### BOOTLOADER INSTALL (disk.sh)"

# [[ "$kiwi_profiles" == *"kvm-and-xen-"* ]]
if rpm -q sdbootutil; then
    rootuuid=$(findmnt / -n --output uuid)
    sed -i -e "s,\$, root=UUID=$rootuuid," /etc/kernel/cmdline
    arch="$(uname -m)"
    case "$arch" in
	aarch64) arch=aa64 ;;
	x86_64) arch=x64 ;;
	*) echo "Unknown arch $arch"; exit 1 ;;
    esac

    echo "install boot loader"
    sdbootutil -v --no-random-seed --arch "$arch" --esp-path /boot/efi --entry-token=auto --no-variables install
    echo "add kernels"
    export hostonly_l=no # for dracut
    sdbootutil -v --arch "$arch" --esp-path /boot/efi --entry-token=auto add-all-kernels
    # Set a 5s timeout, the "hold a key down" method doesn't work effectively.
    echo "timeout 5" >> /boot/efi/loader/loader.conf

    rm -f /boot/mbrid

    find /boot
fi

echo "####### ENDS BOOTLOADER INSTALLER (disk.sh)"
