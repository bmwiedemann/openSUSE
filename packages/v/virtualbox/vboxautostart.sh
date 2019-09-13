#!/bin/sh
# VirtualBox autostart service init script.

#
# Copyright (C) 2012-2019 Oracle Corporation
#
# This file is part of VirtualBox Open Source Edition (OSE), as
# available from http://www.virtualbox.org. This file is free software;
# you can redistribute it and/or modify it under the terms of the GNU
# General Public License (GPL) as published by the Free Software
# Foundation, in version 2 as it comes in the "COPYING" file of the
# VirtualBox OSE distribution. VirtualBox OSE is distributed in the
# hope that it will be useful, but WITHOUT ANY WARRANTY of any kind.
#

# chkconfig: 345 35 65
# description: VirtualBox autostart service
#
### BEGIN INIT INFO
# Provides:       vboxautostart-service
# Required-Start: vboxdrv
# Required-Stop:  vboxdrv
# Default-Start:  2 3 4 5
# Default-Stop:   0 1 6
# Description:    VirtualBox autostart service
### END INIT INFO

PATH=/sbin:/bin:/usr/sbin:/usr/bin:$PATH
SCRIPTNAME=vboxautostart.sh

# read vbox config
[ -f /etc/vbox/vbox.cfg ] && . /etc/vbox/vbox.cfg

# read autostart config
[ -r /etc/default/virtualbox ] && . /etc/default/virtualbox

begin_msg()
{
    test -n "${2}" && echo "${SCRIPTNAME}: ${1}."
    logger -t "${SCRIPTNAME}" "${1}."
}

succ_msg()
{
    logger -t "${SCRIPTNAME}" "${1}."
}

fail_msg()
{
    echo "${SCRIPTNAME}: failed: ${1}." >&2
    logger -t "${SCRIPTNAME}" "failed: ${1}."
}

vboxdrvrunning() {
    lsmod | grep -q "vboxdrv[^_-]"
}

start_vms()
{
    OLD_IFS=$IFS
    IFS=$'\n'
    [ -z "$VBOXAUTOSTART_DB" ] && return
    [ -z "$VBOXAUTOSTART_CONFIG" ] && return
    begin_msg "Starting VirtualBox VMs configured for autostart" console;
    vboxdrvrunning || {
        fail_msg "VirtualBox kernel module not loaded!"
        exit 0
    }
    # read autostart config file
    if [ -r $VBOXAUTOSTART_CONFIG ]; then
	# prevent inheriting this setting to VBoxSVC
	unset VBOX_RELEASE_LOG_DEST
	# find all the files of type username.start
        var=$(ls $VBOXAUTOSTART_DB | grep start | grep -v auto)
	# process each file of that type
        for i in $var; do
	    # Extract the user name - the first word on the line            
            user=$(echo $i | head -n1 | cut -d "." -f1)
	    # autostart the VMs for that user
	    begin_msg "Starting VMs for user $user" console
	    su - $user -c "/usr/lib/virtualbox/VBoxAutostart --start --config $VBOXAUTOSTART_CONFIG"
	    succ_msg "VMs for user $user started"
        done
    fi
    IFS=$OLD_IFS
}

stop_vms()
{
    OLD_IFS=$IFS
    IFS=$'\n'
    [ -z "$VBOXAUTOSTART_DB" ] && return
    [ -z "$VBOXAUTOSTART_CONFIG" ] && return
    # read autostart config file
    if [ -r $VBOXAUTOSTART_CONFIG ]; then
	# prevent inheriting this setting to VBoxSVC
	unset VBOX_RELEASE_LOG_DEST
	# find all the files of type username.stop
	var=$(ls $VBOXAUTOSTART_DB | grep stop | grep -v auto)
	# process each file of that type
	for i in $var; do
	    # Extract the user name - the first word on the line            
	    user=$(echo $i | head -n1 | cut -d "." -f1)
	    # autostop the VMs for that user
	    begin_msg "Stopping VMs for user $user" console
	    su - $user -c "/usr/lib/virtualbox/VBoxAutostart --stop --config $VBOXAUTOSTART_CONFIG"
	    succ_msg "VMs for user $user stopped"
	done
    fi
    IFS=$OLD_IFS
}


case "$1" in
start)
    start_vms
    ;;
stop)
    stop_vms
    ;;
*)
    echo "Usage: $0 {start|stop}"
    exit 1
esac

exit 0
