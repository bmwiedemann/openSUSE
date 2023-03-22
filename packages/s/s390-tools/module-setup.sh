#!/bin/bash

# called by dracut
check() {
    arch=${DRACUT_ARCH:-$(uname -m)}
    [ "$arch" = "s390" -o "$arch" = "s390x" ] || return 1

    require_binaries chzdev || return 1

    [[ $hostonly ]] || return 0

    # or on request
    return 255
}

# called by dracut
depends() {
    echo bash
    return 0
}

# called by dracut
installkernel() {
    instmods ctcm lcs qeth qeth_l2 qeth_l3  dasd_diag_mod dasd_eckd_mod dasd_fba_mod
}

# called by dracut
install() {
    inst_hook cmdline     41 "$moddir/parse-zdev-suse.sh"
    inst_hook cleanup     41 "$moddir/write-udev-live-suse.sh"
    inst_multiple chzdev 
}
