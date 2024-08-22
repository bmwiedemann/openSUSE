#!/bin/bash

__mkosi_initrd_chroot_call() {
    mount --rbind / /.mkosi-root --mkdir
    cd /.mkosi-root
    mount --move . /
    chroot . /usr/libexec/mkosi-initrd/mkosi-initrd $@
    exit
}
export -f __mkosi_initrd_chroot_call

unshare --mount /bin/bash -c '__mkosi_initrd_chroot_call $@' -- $@
