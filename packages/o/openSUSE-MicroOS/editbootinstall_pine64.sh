#!/bin/bash

set -x

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
# The GPT spans the first 33 sectors, but we need to write our
# at sector 16. Shrink the GPT to only span 5 sectors
# (16 partitions) to give us some space.
#------------------------------------------
# echo -e 'x\ns\n16\nw\ny' > gdisk.tmp
# Shrink GPT does not work anymore, so let's use legacy MBR for now
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

#==========================================
# Installing All-in-one U-Boot/SPL
#------------------------------------------
echo "Installing All-in-one U-Boot/SPL..."
if ! dd if=boot/u-boot-sunxi-with-spl.bin of=$diskname bs=1024 seek=8 conv=notrunc; then
	echo "Couldn't install SPL on $diskname"
	exit 1
fi
