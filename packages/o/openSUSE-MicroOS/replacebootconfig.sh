#!/bin/bash
set -euxo pipefail

# Note: There is a copy of this in editbootinstall_{rpi,pine64}.sh!

echo "Recreating the bootloader config"

# This is fragile, but better fail hard than silently
root="$(echo /tmp/kiwi_mount_manager.*/usr)"
root=${root%/usr}
rootdev=$(findmnt -nrvo SOURCE "${root}")

# Needed by the snapper integration
mount -osubvol=@/.snapshots "${rootdev}" "${root}/.snapshots"

# KIWI does not escape the variable
sed -i 's/ $ig/ \\$ig/g' "${root}/etc/default/grub"

# Make sure the link exists
ln -s "${rootdev}" "/dev/disk/by-uuid/$(chroot "${root}" grub2-probe / --target=fs_uuid)"

chroot "${root}" grub2-mkconfig -o /boot/grub2/grub.cfg

umount "${root}/.snapshots"
