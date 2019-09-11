#!/bin/sh
#
# LSB compatible service control script; see http://www.linuxbase.org/spec/
#
### BEGIN INIT INFO
# Provides:          hv_fcopy_daemon
# Required-Start:    $null
# Should-Start:      $syslog $remote_fs $time
# Required-Stop:     $null
# Should-Stop:       $syslog $remote_fs $time
# Default-Start:     3 5
# Default-Stop:      0 1 2 6
# Short-Description: hv_fcopy_daemon receives files from the host
# Description:       Start hv_fcopy_daemon to allow the host to copy files into this guest
### END INIT INFO

# Check for missing binaries (stale symlinks should not happen)
# Note: Special treatment of stop for LSB conformance
HV_FCOPY_BIN=/usr/sbin/hv_fcopy_daemon
test -x $HV_FCOPY_BIN || { echo "$HV_FCOPY_BIN not installed"; 
	if [ "$1" = "stop" ]; then exit 0;
	else exit 5; fi; }

. /etc/rc.status

# Reset status of this service
rc_reset

case "$1" in
    start)
	echo -n "Starting Hyper-V FCOPY daemon "
	env PATH=/usr/lib/hyper-v/bin:$PATH \
	startproc $HV_FCOPY_BIN
	rc_status -v
	;;
    stop)
	echo -n "Shutting down Hyper-V FCOPY daemon "
	killproc -TERM $HV_FCOPY_BIN
	rc_status -v
	;;
    try-restart|condrestart)
	if test "$1" = "condrestart"; then
		echo "${attn} Use try-restart ${done}(LSB)${attn} rather than condrestart ${warn}(RH)${norm}"
	fi
	$0 status
	if test $? = 0; then
		$0 restart
	else
		rc_reset	# Not running is not a failure.
	fi
	# Remember status and be quiet
	rc_status
	;;
    restart)
	## Stop the service and regardless of whether it was
	## running or not, start it again.
	$0 stop
	$0 start

	# Remember status and be quiet
	rc_status
	;;
    force-reload)
	echo -n "Reload service Hyper-V FCOPY daemon "
	$0 try-restart
	rc_status
	;;
    reload)
	rc_failed 3
	rc_status -v
	;;
    status)
	echo -n "Checking for service Hyper-V FCOPY daemon "
	checkproc $HV_FCOPY_BIN
	rc_status -v
	;;
    *)
	echo "Usage: $0 {start|stop|status|try-restart|restart|force-reload|reload}"
	exit 1
	;;
esac
rc_exit
