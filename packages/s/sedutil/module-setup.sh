#!/bin/bash

# called by dracut
check() {
    require_binaries linuxpba sedutil-cli || return 1
    return 255
}

# called by dracut
depends() {
    return 0
}

# called by dracut
install() {
    inst_hook cmdline 00 "$moddir/linuxpba.sh"
    inst_multiple linuxpba sedutil-cli
}

