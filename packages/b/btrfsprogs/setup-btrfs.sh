#!/bin/bash
#
#%stage: filesystem

mkdir -p $tmp_mnt/etc/udev/rules.d
cp /usr/lib/udev/rules.d/64-btrfs.rules $tmp_mnt/etc/udev/rules.d
