#!/bin/sh
#
# LSB compatible service control script; see http://www.linuxbase.org/spec/
#
### BEGIN INIT INFO
# Provides:          hv_kvp_daemon
# Required-Start:    $null
# Should-Start:      $syslog $remote_fs $time
# Required-Stop:     $null
# Should-Stop:       $syslog $remote_fs $time
# Default-Start:     3 5
# Default-Stop:      0 1 2 6
# Short-Description: hv_kvp_daemon provides info to the host
# Description:       Start hv_kvp_daemon to allow the host to query this guest
### END INIT INFO

# Check for missing binaries (stale symlinks should not happen)
# Note: Special treatment of stop for LSB conformance
HV_KVP_BIN=/usr/sbin/hv_kvp_daemon
test -x $HV_KVP_BIN || { echo "$HV_KVP_BIN not installed"; 
	if [ "$1" = "stop" ]; then exit 0;
	else exit 5; fi; }

. /etc/rc.status

# Reset status of this service
rc_reset

case "$1" in
    start)
	echo -n "Starting Hyper-V KVP daemon "
	# The service can not be restarted
	# IF the currently running kernel is too old, the new daemon is started
	# anyway. Due to a flaw in the old kernel-user protocol the kernel 
	# will flood /var/log/messages with messages like:
	# "hv_utils: KVP: user-mode registering done."
	# This is also caused by old hyper-v.rpms which have a restart command
	# in their post install script. Catch those old kernels and avoid the
	# flood, which will easily fill the root partition during an upgrade.
	case "`uname -r`" in
		2.*)      rc_failed 3 ;;
		3.0.13-*) rc_failed 3 ;;
		3.0.26-*) rc_failed 3 ;;
		3.0.31-*) rc_failed 3 ;;
		3.0.34-*) rc_failed 3 ;;
		3.0.38-*) rc_failed 3 ;;
		3.0.42-*) rc_failed 3 ;;
		*)
		env PATH=/usr/lib/hyper-v/bin:$PATH \
		startproc $HV_KVP_BIN
		;;
	esac
	rc_status -v
	;;
    stop)
	echo -n "Shutting down Hyper-V KVP daemon "
	killproc -TERM $HV_KVP_BIN
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
	echo -n "Reload service Hyper-V KVP daemon "
	$0 try-restart
	rc_status
	;;
    reload)
	rc_failed 3
	rc_status -v
	;;
    status)
	echo -n "Checking for service Hyper-V KVP daemon "
	checkproc $HV_KVP_BIN
	rc_status -v
	;;
    *)
	echo "Usage: $0 {start|stop|status|try-restart|restart|force-reload|reload}"
	exit 1
	;;
esac
rc_exit
