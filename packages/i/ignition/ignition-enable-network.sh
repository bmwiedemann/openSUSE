#!/bin/bash

. /lib/dracut-lib.sh

if [ -f /run/ignition/neednet ] && ! getargbool 0 'rd.neednet'; then
    echo "rd.neednet=1" > /etc/cmdline.d/40-ignition-neednet.conf

    # Re-trigger generation of network rules
    . /lib/dracut/hooks/pre-udev/60-net-genrules.sh
    udevadm control --reload
    udevadm trigger --subsystem-match net --action add
fi
