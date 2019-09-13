#!/bin/bash
#
### BEGIN INIT INFO
# Provides:lsyncd
# Required-Start:       $local_fs $remote_fs $network
# Required-Stop:        $local_fs $remote_fs $network
# Default-Start:3 5
# Default-Stop:0 1 2 6
# Short-Description:Start lsyncd
# chkconfig: - 85 15
# Description:Lsyncd uses rsync to synchronize local directories with a remote machine running rsyncd.
#
# processname:  lsyncd
# config:       /etc/lsyncd.conf
# config:       /etc/sysconfig/lsyncd
# pidfile:      /var/run/lsyncd.pid
### END INIT INFO

# Source function library
. /etc/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0

LSYNCD_OPTIONS="-pidfile /var/run/lsyncd.pid /etc/lsyncd.conf"

if [ -e /etc/sysconfig/lsyncd ]; then
  . /etc/sysconfig/lsyncd
fi

RETVAL=0

prog="lsyncd"
thelock=/var/lock/subsys/lsyncd

start() {
	[ -f /etc/lsyncd.conf ] || exit 6
        echo -n $"Starting $prog: "
        if [ $UID -ne 0 ]; then
                RETVAL=1
                failure
        else
                daemon /usr/bin/lsyncd $LSYNCD_OPTIONS
                RETVAL=$?
                [ $RETVAL -eq 0 ] && touch $thelock
        fi;
        echo
        return $RETVAL
}

stop() {
        echo -n $"Stopping $prog: "
        if [ $UID -ne 0 ]; then
                RETVAL=1
                failure
        else
                killproc lsyncd
                RETVAL=$?
                [ $RETVAL -eq 0 ] && rm -f $thelock
        fi;
        echo
        return $RETVAL
}

reload(){
        echo -n $"Reloading $prog: "
        killproc lsyncd -HUP
        RETVAL=$?
        echo
        return $RETVAL
}

restart(){
        stop
        start
}

condrestart(){
    [ -e $thelock ] && restart
    return 0
}

case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart)
        restart
        ;;
  reload)
        reload
        ;;
  condrestart)
        condrestart
        ;;
  status)
        status lsyncd
        RETVAL=$?
        ;;
  *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart|reload}"
        RETVAL=1
esac

exit $RETVAL
