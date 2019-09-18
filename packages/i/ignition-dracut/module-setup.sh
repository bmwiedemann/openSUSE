#!/bin/bash
# -*- mode: shell-script; indent-tabs-mode: nil; sh-basic-offset: 4; -*-
# ex: ts=8 sw=4 sts=4 et filetype=sh

depends() {
    echo ignition
}

install() {
    inst_simple "$moddir/ignition-mount-initrd-fstab.service" \
        "$systemdsystemunitdir/ignition-mount-initrd-fstab.service"
    inst_simple "$moddir/ignition-userconfig-timeout.conf" \
	"$systemdsystemunitdir/dev-disk-by\x2dlabel-ignition.device.d/ignition-userconfig-timeout.conf"
    inst_simple "$moddir/ignition-suse-generator" \
        "$systemdutildir/system-generators/ignition-suse-generator"
}

installkernel() {
    hostonly='' instmods iso9660
}
