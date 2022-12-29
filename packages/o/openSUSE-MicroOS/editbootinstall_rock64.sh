#!/bin/bash
set -euxo pipefail

diskname=$1
devname="$2"
loopname="${devname%*p?}"
loopdev=${loopname#/dev/mapper/*}

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
