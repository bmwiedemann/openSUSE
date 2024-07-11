#!/bin/bash
#
# Small helper script to create a vnstat database
# by Pascal Bleser <pascal.bleser@opensuse.org>
# This script is under the same license as vnstat, GPL version 2.
#

VNSTAT_DB_DIR="/var/lib/vnstat"
VNSTAT_USER="vnstat"
SCRIPT_NAME="${0##*/}"

die() { echo "ERROR: $*" >&2; exit 1; }

niclist() { /sbin/ip -o link list | awk '{print $2}' | cut -f1 -d: | grep -vx lo; }

_help() {
    cat<<EOF
${SCRIPT_NAME} - script to create vnstat databases

Usage: ${SCRIPT_NAME} <interface>

Note that this script must be called as root to create the vnstat database,
for example like this:

    su -c "${SCRIPT_NAME} eth0"

If you run this script without passing parameters, it will display the list
of network interfaces available on your host.

EOF
}

if [ -n "$1" -a "$1" = "--help" -o "$1" = "-h" ]; then
    _help
    exit 0
fi
if [ -n "$1" ]; then
    [ -e "$VNSTAT_DB_DIR/$1" ] && die "The vnstat database $VNSTAT_DB_DIR/$1 already exists"
    [ "$UID" = "0" ] || die "this operation must be performed as root, e.g. su -c \"${SCRIPT_NAME} $1\""
    /bin/su -c "/usr/bin/vnstat -u -i $1" "$VNSTAT_USER"
else
    cat<<EOF
Please select a network interface for which to create a vnstat database,
and pass it as the first parameter to this script, e.g.:

  ${SCRIPT_NAME} eth0

Here is a list of the network interfaces present on your host:
EOF
    niclist
    exit 1
fi

