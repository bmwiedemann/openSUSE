#!/bin/bash

# this removes some 3rd party libraries from the src tar that are not needed to build the unix port
# in order to make the legal review easier

set -e

version=$(rpmspec --query micropython.spec | head -1 | cut -d- -f2)

osc rm -fv micropython-*.tar.xz
wget "https://micropython.org/resources/source/micropython-${version}.tar.xz" -O "micropython-${version}.tar.xz"
tar xf "micropython-${version}.tar.xz"
pushd "micropython-${version}"
rm -rv "lib/fsp"
rm -rv "lib/alif-security-toolkit"
rm -rv "lib/alif_ensemble-cmsis-dfp"
rm -rv "lib/asf4"
rm -rv "lib/cyw43-driver"
rm -rv "lib/axtls"
rm -rv "lib/tinyusb"
rm -rv "lib/stm32lib"
rm -rv "lib/btstack"
rm -rv "lib/pico-sdk"
rm -rv "lib/nrfx"
rm -rv "lib/lwip"
rm -rv "lib/libffi"
rm -rv "lib/protobuf-c"
rm -rv "lib/nxp_driver"
rm -rv "lib/arduino-lib"
rm -rv "lib/mynewt-nimble"
pushd "ports"
find . -maxdepth 1 -type d | grep -v unix | grep -v esp | grep -v rp2 | grep -v minimal | grep -v qemu | grep -v webassembly | xargs rm -rv || :
popd
popd
tar caf "micropython-${version}.tar.xz" "micropython-${version}"
rm -r "micropython-${version}"
osc add micropython-*.tar.xz
