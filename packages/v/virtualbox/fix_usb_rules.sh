#!/bin/bash
# script to disable USB passthru in /etc/udev/rules.d/60-vboxdrv.rules
# if already disabled, clear the comment character
sed -i 's/#SUBSYSTEM==\"usb/SUBSYSTEM==\"usb/' /usr/lib/udev/rules.d/60-vboxdrv.rules
# now comment the usb lines
sed -i 's/SUBSYSTEM==\"usb/#SUBSYSTEM==\"usb/' /usr/lib/udev/rules.d/60-vboxdrv.rules

