#!/bin/bash
#
# setup_cio_ignore
#
# Remove the device ids found in /boot/zipl/active_devices.txt
# from cio_ignore
#

if [ -e /boot/zipl/active_devices.txt ] ; then
    while read dev etc ; do
        [ "$dev" = "#" -o "$dev" = "" ] && continue;
	cio_ignore -r $dev
    done < /boot/zipl/active_devices.txt
fi

exit 0
