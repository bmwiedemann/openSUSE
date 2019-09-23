#!/bin/bash

set -ex

diskname=$1
devname="$2"
loopname="${devname%*p2}"
loopdev=/dev/${loopname#/dev/mapper/*}

## Preparation for replacebootconfig.sh
root=/tmp/kiwi_mount_manager.asdf
mkdir ${root}
mount ${devname} ${root}
for i in proc dev sys; do mount --bind /${i} ${root}/${i}; done
for i in tmp var boot/writable; do mount -o subvol=@/${i} ${devname} ${root}/${i}; done
findmnt ||:
# END

## Same as replacebootconfig.sh
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
## END Same as replacebootconfig.sh

## Clean up after preparations
for i in boot/writable proc dev sys tmp var .; do umount ${root}/$i; done
# END

#==========================================
# copy Raspberry Pi firmware to EFI partition
#------------------------------------------
echo "RPi EFI system, installing firmware on ESP"
mkdir -p ./mnt-pi
mount ${loopname}p1 ./mnt-pi
( cd boot/vc; tar c . ) | ( cd ./mnt-pi/; tar x )
umount ./mnt-pi
rmdir ./mnt-pi

#==========================================
# Change partition label type to MBR
#------------------------------------------
#
# The target system doesn't support GPT, so let's move it to
# MBR partition layout instead.
#
# Also make sure to set the ESP partition to type 0xc so that
# broken firmware (Rpi) detects it as FAT.
#
# Use tabs, "<<-" strips tabs, but no other whitespace!
cat > gdisk.tmp <<-'EOF'
		x
		r
		g
		t
		1
		c
		w
		y
	EOF
dd if=$loopdev of=mbrid.bin bs=1 skip=440 count=4
gdisk $loopdev < gdisk.tmp
dd of=$loopdev if=mbrid.bin bs=1 seek=440 count=4
rm -f mbrid.bin
rm -f gdisk.tmp
