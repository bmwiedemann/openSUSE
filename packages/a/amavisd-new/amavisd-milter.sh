#!/bin/bash

. /etc/sysconfig/amavis
AMAVIS_MILTER_BIN=/usr/sbin/amavisd-milter
AMAVIS_MILTER_SOCK=local:/var/spool/amavis/amavis-milter.sock
AMAVIS_MILTER_PID=/var/spool/amavis/amavisd-milter.pid

case "$1" in
    start)
	if [ "$AMAVIS_SENDMAIL_MILTER" = "yes" ]; then
	    startproc -u vscan $AMAVIS_MILTER_BIN -s $AMAVIS_MILTER_SOCK \
	      -p $AMAVIS_MILTER_PID > /dev/null 2>&1
	fi
    ;;
    stop)
        if [ "$AMAVIS_SENDMAIL_MILTER" = "yes" ]; then
            killproc -TERM $AMAVIS_MILTER_BIN
        fi
    ;;
esac
exit 0
