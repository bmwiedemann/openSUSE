#!/bin/bash

unset ${!LC_*} LANGUAGE
export LANG="POSIX"
export PATH="/sbin:/usr/sbin:/bin:/usr/bin"

[ "$PRELEVEL" = "N" ] && exit

CONFNAME="$1"
IFACE="$2"

[ "$IFACE" = "lo" ] && exit

[ -x /usr/bin/vnstat ] || exit
[ -w "/var/lib/vnstat/$IFACE" ] || exit

case $0 in
    *if-up.d*)   /usr/bin/vnstat -r --enable -i "$IFACE" ;;
    *if-down.d*) /usr/bin/vnstat -r --disable -i "$IFACE" ;;
esac

