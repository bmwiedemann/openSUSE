#!/bin/bash
set -euxo pipefail

diskname=$1
devname="$2"
loopname="${devname%*p?}"
loopdev=${loopname#/dev/mapper/*}

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
