#!/bin/bash
# -*- mode: shell-script; indent-tabs-mode: nil; sh-basic-offset: 4; -*-
# ex: ts=8 sw=4 sts=4 et filetype=sh

depends() {
    echo ignition
}

install_ignition_unit() {
    local unit="$1"; shift
    local target="${1:-ignition-complete.target}"; shift
    local instantiated="${1:-$unit}"; shift
    inst_simple "$moddir/$unit" "$systemdsystemunitdir/$unit"
    # note we `|| exit 1` here so we error out if e.g. the units are missing
    # see https://github.com/coreos/fedora-coreos-config/issues/799
    systemctl -q --root="$initdir" add-requires "$target" "$instantiated" || exit 1
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
    inst_script "$moddir/ignition-setup-user.sh" \
        "/usr/sbin/ignition-setup-user"
    inst_multiple awk systemd-detect-virt
    install_ignition_unit ignition-setup-user.service
}

installkernel() {
    # Make sure we can read configuration from ISO image and vfat formated USB drives
    hostonly='' instmods iso9660 vfat =fs/nls
}
