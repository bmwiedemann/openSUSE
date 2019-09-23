#!/bin/bash
export QT_NO_KDE_INTEGRATION=1
# make certain that the user/group combination is valid
/usr/bin/id -nG | grep -v -e "root" -e "vboxusers" >/dev/null && /usr/lib/virtualbox/VBoxPermissionMessage && exit
#
# Handle the issue regarding USB passthru
# The following conditions apply:
# 1. If ~/.vbox/enable exists, the user accepts the security risk.
# 2. If ~/.vbox/disable exists, the user does not accept the risk. That file will contain the inode of /usr/lib/udev/rules.d/60-vboxdrv.rules.
#    When that changes, the VBoxUSB_DevRules will again be displayed as that means that VB has been reloaded. 
#
devrules()
{
    /usr/lib/virtualbox/VBoxUSB_DevRules
    if [ $? -eq 0 ] ; then
	# User accepts the risk
	touch ~/.vbox/enable
	rm -f ~/.vbox/disable
    else
	# User declines the risk - save the inode
	echo "" > ~/.vbox/disable
	rm -f ~/.vbox/enable
    fi
}
# Start of main routine
#
# Ensure that ~/.vbox exists
mkdir -p ~/.vbox/
# Get the inode for /usr/lib/udev/rules.d/60-vboxdrv.rules
INODE=$(stat /usr/lib/udev/rules.d/60-vboxdrv.rules | grep Inode | cut -d' ' -f3)
if [ ! -f ~/.vbox/enable ] && [ ! -f ~/.vbox/disable ] ; then
	# Neither file exists - find what the user wants
	devrules
fi
# Get the original Inode if it exists
if [ -f ~/.vbox/disable ] ; then
    read LINE < ~/.vbox/disable
else
    LINE=" "
fi
# If user originally declined, make certain that /usr/lib/udev/rules.d/60-vboxdrv.rules has not been changed
if [ -f ~/.vbox/disable ] && [ "$LINE" != "$INODE" ] && [ "$LINE" != "" ] ; then
    # disable is selected and the Inode has changed - ask again
    devrules
fi
if [ -f ~/.vbox/disable ] ; then
    echo $INODE > ~/.vbox/disable
    if [ "$LINE" != "$INODE" ] ; then
	if [ -f /usr/bin/kdesu ] ; then
	    kdesu /sbin/vbox-fix-usb-rules.sh
	fi
	if [ -f /usr/bin/gnomesu ] ; then
	    gnomesu /sbin/vbox-fix-usb-rules.sh
	fi
    fi
fi
# Check that /usr/lib/virtualbox/VirtualBoxVM has SUID permissions
PERM=$(ls -l /usr/lib/virtualbox/VirtualBoxVM | grep rwsr)
if [ -z "$PERM" ]
then
    logger  -s "Wrong permissions for VirtualBoxVM - use 'sudo chmod 4711 /usr/lib/virtualbox/VirtualBoxVM' to fix"
    /usr/lib/virtualbox/VBoxSUIDMessage
    exit 1
fi
# Now run the VB GUI
LD_LIBRARY_PATH="/usr/lib/virtualbox${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}" /usr/lib/virtualbox/VirtualBox6 $@
