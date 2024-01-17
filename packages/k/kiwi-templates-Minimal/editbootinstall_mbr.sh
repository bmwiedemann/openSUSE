#!/bin/bash
set -euxo pipefail

[ "$(uname -m)" = 'x86_64' ] || exit 0

diskname="$1"
devname="$2"
loopdev="${devname%*p?}"

dd if=./usr/lib/uefi_mbr/uefi_mbr.bin of="$loopdev" conv=notrunc
