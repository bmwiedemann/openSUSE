#!/bin/bash
set -euxo pipefail
[ -x /usr/bin/sdbootutil ] || exit 0
echo "#######DISK"
rootuuid=$(findmnt / -n --output uuid)
sed -i -e "s,\$, root=UUID=$rootuuid rootflags=subvol=@/.snapshots/1/snapshot," /etc/kernel/cmdline
arch="$(uname -m)"
case "$arch" in
	aarch64) arch=arm64 ;;
	x86_64) arch=x64 ;;
	*) echo "Unknown arch $arch"; exit 1 ;;
esac
echo "install boot loader"
sdbootutil -v --arch "$arch" --esp-path /boot/efi --entry-token=auto --no-variables install
echo "add kernels"
export hostonly_l=no # for dracut
sdbootutil --arch "$arch" --esp-path /boot/efi --entry-token=auto add-all-kernels
echo "##### AFTER ####"
rm -f /boot/mbrid
find /boot
