#!/bin/bash
set -euxo pipefail

diskname=$1
devname="$2"
loopname="${devname%*p?}"
loopdev=/dev/${loopname#/dev/mapper/*}

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

echo "Installing idbloader..."

if ! dd if=boot/idbloader.img of=$diskname bs=512 seek=64 conv=notrunc; then
    echo "Failed to install"
    exit 1
fi

echo "Installing u-boot..."

if ! dd if=boot/u-boot.itb of=$diskname bs=512 seek=16384 conv=notrunc; then
    echo "Failed to install"
    exit 1
fi

echo "Installing startup.nsh..."

mkdir ./mnt-rock64
mount ${loopname}p1 ./mnt-rock64

echo "bootaa64" > mnt-rock64/startup.nsh

umount ./mnt-rock64
rmdir ./mnt-rock64
