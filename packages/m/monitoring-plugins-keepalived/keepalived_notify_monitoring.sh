#!/bin/bash
#
# Notify script for keepalived used by check_keepalived
#
# Please add the following in your Keepalived configuration:
#        vrrp_instance MyVRRPInstance {
#          [...]
#          notify /usr/bin/keepalived_notify_monitoring.sh
#        } 
#
# The script is called after any state change with the following 
# parameters:
#
#   $1 = "GROUP" or "INSTANCE"
#   $2 = name of group or instance
#   $3 = target state of transition (“MASTER”, “BACKUP”, “FAULT”)
#   $4 = priority value
#
# If you want to execute other scripts as well, please create a file
#    /etc/keepalived/keepalived_notify_monitoring.conf
# and assign the path to your script in the variable EXEC_SCRIPT like:
#    EXEC_SCRIPT=/usr/local/bin/foo
# this script here will execute your script with the parameters 
# from the initial call.
#
umask 0027
LOGFILE='/var/log/keepalived_notify.log'
CONFIG='/etc/keepalived/keepalived_notify_monitoring.conf'
STATEFILE='/var/run/keepalived.state'

if [ -r "$CONFIG" ]; then
    . "$CONFIG"
fi

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    echo "Usage: $(basename $0) <group or instance> <name of group or instance> <target state of transition>"
    echo
    echo "       $(basename $0) should be used as notify script for keepalived and"
    echo "       writes the given values into a statefile ($STATEFILE)"
    echo "       for further processing (by check_keepalived for example)."
    echo 
    echo "       Please add the following in your Keepalived configuration:"
    echo "        vrrp_instance MyVRRPInstance {"
    echo "            [...]"
    echo "            notify $0"
    echo "        }"
    echo "       After a reload, the script is called after any state change."
    echo
    echo "       If you want to execute other scripts as well, please create a file"
    echo "          /etc/keepalived/keepalived_notify_monitoring.conf"
    echo "       and assign the path to your script in the variable EXEC_SCRIPT like:"
    echo "          EXEC_SCRIPT=/usr/local/bin/foo"
    echo "       this script here will execute your script with the parameters "
    echo "       from the initial call."
    exit 0
fi

DATE=$(date)
echo "$DATE : $1 $2 is in $3 state (Priority: $4)" >> "$LOGFILE"

touch "$STATEFILE" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "$0 : can not create $STATEFILE, exiting" >&2
    exit 1
else
    echo "$1 $2 is in $3 state (Priority: $4)" > "$STATEFILE"
	chmod 644 "$STATEFILE"
fi
if [ -n "$EXEC_SCRIPT" ]; then
    "$EXEC_SCRIPT" "$1" "$2" "$3" "$4"
fi

