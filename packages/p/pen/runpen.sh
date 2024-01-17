#!/bin/sh
#set -x
#
# Script that monitors and restarts a pen load balancer instance
#
# Parameters: name of the configuration file
#
# Original author: Torsten.Goedicke@wlw.de
# Modified for SUSE LINUX by joe@suse.de

DAEMON=/usr/bin/pen
CFFILE="$1"

test ! -x "$DAEMON" && echo "Error: pen binary missing" && exit 0
test ! -f "$CFFILE" && echo "Error: pen configuration file missing" && exit 0

RUN=yes
while [ $RUN = "yes" ]
do
    PARAM=`cat $CFFILE`
    $DAEMON -f $PARAM &
    PID="$!"
    wait $PID
done
