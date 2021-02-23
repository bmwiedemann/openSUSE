#!/bin/bash
# SPDX-FileCopyrightText: 2021 Fabian Vogt <fvogt@suse.de>
# SPDX-License-Identifier: GPL-2.0-or-later
set -eu

if [ $# != 2 ]; then
	echo "Usage: $0 microos.qcow2 target/dir"
	exit 1
fi

if ! [ -r "$1" ]; then
	echo "Need qcow2"
	exit 1
fi
qcow2="$1"

if ! [ -d "$2" ]; then
	echo "Need target dir"
	exit 1
fi
targetdir="$2"

cleanup() {
	qemu-nbd --disconnect /dev/nbd0
}

trap cleanup EXIT

# Make the qcow partitions available 
modprobe nbd
qemu-nbd --read-only --connect=/dev/nbd0 "${qcow2}"
# It needs some time to be properly available (I/O errors otherwise...)
sleep 1

# Copy over the bios partition
dd status=progress bs=1M if=/dev/nbd0p1 "of=${targetdir}/biospart"

# Put the root partition into an .xz archive
dd status=progress bs=1M if=/dev/nbd0p3 | xz -2 > "${targetdir}/rootpart.xz"
