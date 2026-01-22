#!/bin/bash

. /lib/dracut-lib.sh

if [ -f /run/ignition/neednet ] && ! getargbool 0 'rd.neednet'; then
    echo "rd.neednet=1" > /etc/cmdline.d/40-ignition-neednet.conf

    # Re-trigger generation of network rules and apply them
    if [ -e /lib/dracut/hooks/pre-udev/60-net-genrules.sh ]; then
        # Wicked
        . /lib/dracut/hooks/pre-udev/60-net-genrules.sh
        udevadm control --reload
        udevadm trigger --subsystem-match net --action add
    else
        # NetworkManager
        . /lib/dracut/hooks/cmdline/99-nm-config.sh
        if [ -e /usr/lib/systemd/system/NetworkManager-config-initrd.service ]; then
            systemctl restart NetworkManager-config-initrd.service
        fi
    fi
fi
