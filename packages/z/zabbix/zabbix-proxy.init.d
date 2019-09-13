#!/bin/sh
#
# /etc/init.d/zabbix-proxy
#   and its symbolic link
# /(usr/)sbin/rczabbix-proxy
#
### BEGIN INIT INFO
# Provides:          zabbix-proxy
# Required-Start:    $network $remote_fs $syslog
# Should-Start:      $time
# Required-Stop:     $syslog $remote_fs
# Should-Stop: $time ypbind smtp
# Default-Start:     3 5
# Default-Stop:      0 1 2 6
# Short-Description: ZABBIX proxy
# Description:       Start ZABBIX proxy
### END INIT INFO

# Check for missing binaries (stale symlinks should not happen)
# Note: Special treatment of stop for LSB conformance
ZABBIX_PROXY_BIN=/usr/sbin/zabbix-proxy
test -x $ZABBIX_PROXY_BIN || { echo "$ZABBIX_PROXY_BIN not installed"; 
	if [ "$1" = "stop" ]; then exit 0;
	else exit 5; fi; }

# Check for existence of needed config file and read it
ZABBIX_PROXY_CONFIG=/etc/zabbix/zabbix-proxy.conf
test -r $ZABBIX_PROXY_CONFIG || { echo "$ZABBIX_PROXY_CONFIG not existing";
	if [ "$1" = "stop" ]; then exit 0;
	else exit 6; fi; }

# Get PidFile from config	
PidFile=$(grep ^PidFile $ZABBIX_PROXY_CONFIG|cut -d "=" -f 2)

# Source LSB init functions
# providing start_daemon, killproc, pidofproc, 
# log_success_msg, log_failure_msg and log_warning_msg.
# This is currently not used by UnitedLinux based distributions and
# not needed for init scripts for UnitedLinux only. If it is used,
# the functions from rc.status should not be sourced or used.
#. /lib/lsb/init-functions

# Shell functions sourced from /etc/rc.status:
#      rc_check         check and set local and overall rc status
#      rc_status        check and set local and overall rc status
#      rc_status -v     be verbose in local rc status and clear it afterwards
#      rc_status -v -r  ditto and clear both the local and overall rc status
#      rc_status -s     display "skipped" and exit with status 3
#      rc_status -u     display "unused" and exit with status 3
#      rc_failed        set local and overall rc status to failed
#      rc_failed <num>  set local and overall rc status to <num>
#      rc_reset         clear both the local and overall rc status
#      rc_exit          exit appropriate to overall rc status
#      rc_active        checks whether a service is activated by symlinks
. /etc/rc.status

# Reset status of this service
rc_reset

# Return values acc. to LSB for all commands but status:
# 0       - success
# 1       - generic or unspecified error
# 2       - invalid or excess argument(s)
# 3       - unimplemented feature (e.g. "reload")
# 4       - user had insufficient privileges
# 5       - program is not installed
# 6       - program is not configured
# 7       - program is not running
# 8--199  - reserved (8--99 LSB, 100--149 distrib, 150--199 appl)
# 
# Note that starting an already running service, stopping
# or restarting a not-running service as well as the restart
# with force-reload (in case signaling is not supported) are
# considered a success.

case "$1" in
    start)
	echo -n "Starting zabbix proxy "
	## Start daemon with startproc(8). If this fails
	## the return value is set appropriately by startproc.
	mkdir -p `dirname $PidFile` 2> /dev/null
	chown zabbixs.zabbixs `dirname $PidFile`
	/sbin/startproc -u zabbixs -g zabbixs -p $PidFile $ZABBIX_PROXY_BIN

	# Remember status and be verbose
	rc_status -v
	;;
    stop)
	echo -n "Shutting down zabbix proxy "
	## Stop daemon with killproc(8) and if this fails
	## killproc sets the return value according to LSB.

	/sbin/killproc -p $PidFile -TERM $ZABBIX_PROXY_BIN

	# Remember status and be verbose
	rc_status -v
	;;
    try-restart|condrestart)
	## Do a restart only if the service was active before.
	## Note: try-restart is now part of LSB (as of 1.9).
	## RH has a similar command named condrestart.
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
	## Signal the daemon to reload its config. Most daemons
	## do this on signal 1 (SIGHUP).
	## If it does not support it, restart the service if it
	## is running.

	echo -n "Reload service zabbix proxyd "
	## if it supports it:
	/sbin/killproc -p $PidFile -HUP $ZABBIX_PROXY_BIN
	#touch /var/run/zabbix/zabbix-proxy.pid
	rc_status -v

	## Otherwise:
	#$0 try-restart
	#rc_status
	;;
    reload)
	## Like force-reload, but if daemon does not support
	## signaling, do nothing (!)

	# If it supports signaling:
	echo -n "Reload service zabbix proxyd "
	/sbin/killproc -p $PidFile -HUP $ZABBIX_PROXY_BIN
	#touch /var/run/zabbix/zabbix-proxy.pid
	rc_status -v
	
	## Otherwise if it does not support reload:
	#rc_failed 3
	#rc_status -v
	;;
    status)
	echo -n "Checking for service zabbix proxyd "
	## Check status with checkproc(8), if process is running
	## checkproc will return with exit status 0.

	# Return value is slightly different for the status command:
	# 0 - service up and running
	# 1 - service dead, but /var/run/  pid  file exists
	# 2 - service dead, but /var/lock/ lock file exists
	# 3 - service not running (unused)
	# 4 - service status unknown :-(
	# 5--199 reserved (5--99 LSB, 100--149 distro, 150--199 appl.)
	
	# NOTE: checkproc returns LSB compliant status values.
	/sbin/checkproc -p $PidFile $ZABBIX_PROXY_BIN
	# NOTE: rc_status knows that we called this init script with
	# "status" option and adapts its messages accordingly.
	rc_status -v
	;;
    probe)
	## Optional: Probe for the necessity of a reload, print out the
	## argument to this init script which is required for a reload.
	## Note: probe is not (yet) part of LSB (as of 1.9)

	test $ZABBIX_PROXY_CONFIG -nt $PidFile && echo reload
	;;
    *)
	echo "Usage: $0 {start|stop|status|try-restart|restart|force-reload|reload|probe}"
	exit 1
	;;
esac
rc_exit
