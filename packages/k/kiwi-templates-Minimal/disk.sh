#!/bin/bash
set -euxo pipefail
[ -x /usr/bin/sdbootutil ] || exit 0
echo "#######DISK"
rootuuid=$(findmnt / -n --output uuid)
sed -i -e "s,\$, root=UUID=$rootuuid," /etc/kernel/cmdline
arch="$(uname -m)"
case "$arch" in
	aarch64) arch=aa64 ;;
	x86_64) arch=x64 ;;
	*) echo "Unknown arch $arch"; exit 1 ;;
esac
echo "install boot loader"
sdbootutil -v --arch "$arch" --esp-path /boot/efi --entry-token=auto --no-variables install
echo "add kernels"
export hostonly_l=no # for dracut
sdbootutil --arch "$arch" --esp-path /boot/efi --entry-token=auto add-all-kernels
rm -f /boot/mbrid
# Set a 5s timeout, the "hold a key down" method doesn't work effectively.
echo "timeout 5" >> /boot/efi/loader/loader.conf
echo "##### AFTER ####"
mkdir /efi
find /boot
