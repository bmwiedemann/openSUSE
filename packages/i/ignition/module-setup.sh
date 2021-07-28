#!/bin/bash
# -*- mode: shell-script; indent-tabs-mode: nil; sh-basic-offset: 4; -*-
# ex: ts=8 sw=4 sts=4 et filetype=sh

depends() {
    echo ignition
}

install() {
    inst_simple "$moddir/ignition-enable-network.service" \
        "$systemdsystemunitdir/ignition-enable-network.service"
    inst_simple "$moddir/ignition-mount-initrd-fstab.service" \
        "$systemdsystemunitdir/ignition-mount-initrd-fstab.service"
    inst_simple "$moddir/ignition-userconfig-timeout.conf" \
	"$systemdsystemunitdir/dev-disk-by\x2dlabel-ignition.device.d/ignition-userconfig-timeout.conf"
    inst_simple "$moddir/ignition-suse-generator" \
        "/etc/systemd/system-generators/ignition-generator"
    inst_script "$moddir/ignition-enable-network.sh" \
        "/usr/sbin/ignition-enable-network"
    inst_script "$moddir/ignition-setup-user-suse.sh" \
        "/usr/sbin/ignition-setup-user-suse"
    inst_multiple awk systemd-detect-virt
}

installkernel() {
    # Make sure we can read configuration from ISO image and vfat formated USB drives
    hostonly='' instmods iso9660 vfat =fs/nls
}
