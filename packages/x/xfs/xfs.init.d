#!/bin/sh
# Copyright (c) 1996, 2000 S.u.S.E. GmbH Fuerth, Germany.  All rights reserved.
#
#         Mike Fabian <mfabian@suse.de>, 2001
#
# /usr/sbin/rcxfs
#
### BEGIN INIT INFO
# Provides:       xfs
# Required-Start: $network $named $remote_fs
# Required-Stop:  $network $named $remote_fs
# Default-Start:  3 5
# Default-Stop:
# Description:    X Font Server
# Short-Description:    X Font Server
### END INIT INFO

. /etc/rc.status

XFS_BIN=/usr/bin/xfs
test -x $XFS_BIN || exit 5

# First reset status of this service
rc_reset

if [ ! -f /etc/X11/fs/config ] ; then
    echo "can't find /etc/X11/fs/config"
    # program is not configured
    exit 6
fi

case "$1" in
    start)
    	echo -n "Starting X Font Server"
        if checkproc $XFS_BIN; then
                echo -n "X Font Server is already running."
                rc_status -v
                exit
        fi
	# create new fonts.dir files if necessary
	/sbin/conf.d/SuSEconfig.fonts > /dev/null
	find /tmp/.font-unix -type f -exec safe-rm {} \; 2> /dev/null
	find /tmp/.font-unix -type d -exec safe-rmdir {} \; 2> /dev/null
	rm -rf /tmp/.font-unix
	mkdir --mode=0700 /tmp/.font-unix > /dev/null || { echo "can not create directory '/tmp/.font-unix'"; exit -1;}
	chown nobody.nobody /tmp/.font-unix
	startproc -l /var/log/fs-errors $XFS_BIN -nodaemon -user nobody -port 7100
	rc_status -v
	;;
    stop)
	echo -n "Shutting down X Font Server"
	killproc -TERM $XFS_BIN > /dev/null
	rc_status -v
	;;
    try-restart)
        $0 status >/dev/null && $0 restart
        rc_status
        ;;
    restart)
        $0 stop
        $0 start
        rc_status
        ;;
    reload|force-reload)
	if checkproc $XFS_BIN ; then
	    # create new fonts.dir files if necessary
            /sbin/conf.d/SuSEconfig.fonts > /dev/null
            echo -n "Reloading config file of X Font Server"
	    killproc $XFS_BIN -USR1  # re-read config file
	    rc_status -v
	else
	    $0 start
	fi
	echo
	;;
    status)
        echo -n "Checking for X Font Server: "
        checkproc $XFS_BIN
	rc_status -v
	;;
    *)
	echo "Usage: $0 {start|stop|try-restart|restart|reload|force-reload|status}"
	exit 1
	;;
esac

rc_exit
