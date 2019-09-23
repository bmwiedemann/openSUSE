#!/bin/sh
#
# /etc/init.d/zabbix-java-gateway
#   and its symbolic link
# /(usr/)sbin/rczabbix-java-gateway
#
### BEGIN INIT INFO
# Provides:          zabbix-java-gateway
# Required-Start:    $network $remote_fs $syslog
# Should-Start:      $time
# Required-Stop:     $syslog $remote_fs
# Should-Stop: $time ypbind smtp
# Default-Start:     3 5
# Default-Stop:      0 1 2 6
# Short-Description: ZABBIX java gateway
# Description:       Start ZABBIX java jmx gateway
### END INIT INFO

. /etc/rc.status

# Reset status of this service
rc_reset

case "$1" in
    start)
	echo -n "Starting zabbix java gateway "
	/usr/bin/zabbix-java-gateway start
	# Remember status and be verbose
	rc_status -v
	;;
    stop)
	echo -n "Shutting down zabbix java gateway "
	/usr/bin/zabbix-java-gateway stop
	# Remember status and be verbose
	rc_status -v
	;;
    restart)
	## Stop the service and regardless of whether it was
	## running or not, start it again.
	$0 stop
	$0 start

	# Remember status and be quiet
	rc_status
	;;
    status)
	echo -n "Checking for service zabbix java gateway "
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
	/usr/bin/zabbix-java-gateway status
	# NOTE: rc_status knows that we called this init script with
	# "status" option and adapts its messages accordingly.
	rc_status -v
	;;
    reload)
    	# make rpmlint happy
    	;;
    *)
	echo "Usage: $0 {start|stop|status|reload|restart}"
	exit 1
	;;
esac
rc_exit
