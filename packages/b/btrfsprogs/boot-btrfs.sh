#!/bin/bash -e
#%stage: filesystem
#%depends: dm dmraid lvm2 udev md luks
#%programs: btrfs
#%programs: btrfs-convert
#%programs: btrfs-find-root
#%programs: btrfs-image
#%programs: btrfs-select-super
#%programs: btrfsck
#%programs: btrfstune
# for fsck(8): listed twice so that a copy really ends up in /sbin
#%programs: /sbin/fsck.btrfs
#%programs: fsck.btrfs
#%programs: mkfs.btrfs
#%modules: btrfs

modprobe btrfs

btrfs dev scan >& /dev/null
