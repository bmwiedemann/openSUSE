#!/bin/bash

set -o errexit

# This script enables IP forwarding only for the time of ocserv running
#
# The script should be run as a pre and post script via the systemd service
# unit.
#
# It only touches a sysctl if it doesn't have the required value and is able
# to restore it back to the original value by keeping track of changed
# settings in a state file.

STATEDIR="/run/ocserv"
STATEFILE="$STATEDIR/changed_sysctls"
# the sysctls that need to be at '1' for ocserv to work properly
CONTROLS=("net.ipv4.ip_forward" "net.ipv6.conf.default.forwarding" "net.ipv6.conf.all.forwarding")

errecho() {
	echo $* 1>&2
}

usage() {
	errecho "Usage: $0 [--enable|--disable]"
	errecho
	errecho "--enable: enable IP forwarding kernel settings, if necessary"
	errecho "--disable: restore IP forwarding kernel settings that have previously been changed via --enable"
	errecho
	errecho "This script temporarily enables IP forwarding while ocserv is running"
	exit 1
}

# make sure we don't create anything world readable for other users
umask 077

if [ $# -ne 1 ]; then
	usage
fi

SYSCTL=`which sysctl`
if [ -z "$SYSCTL" ]; then
	errecho "Couldn't find 'sysctl'. You need to be root to run this script."
	exit 1
fi

operation="$1"

if [ "$operation" = "-h" -o "$operation" = "--help" ]; then
	usage
elif [ "$operation" = "--enable" ]; then
	changed=()
	for control in ${CONTROLS[@]}; do
		val=$($SYSCTL -n "$control")
		if [ $? -ne 0 ]; then
			errecho "failed to run sysctl"
			exit 2
		fi

		if [ "$val" -eq 0 ]; then
			echo -n "enabling $control: "
			$SYSCTL "${control}=1"
			if [ $? -eq 0 ]; then
				changed+=("$control")
			fi
		fi
	done

	if (( ${#changed[@]} )); then
		mkdir -p "$STATEDIR"
		for changed in ${changed[@]}; do
			echo "$changed" >>"$STATEFILE"
		done
	fi
elif [ "$operation" = "--disable" ]; then
	if [ ! -f "$STATEFILE" ]; then
		# nothing to restore
		exit 0
	fi

	for control in `cat $STATEFILE`; do
		echo -n "restoring $control: "
		$SYSCTL "${control}=0" || continue
	done

	rm -f "$STATEFILE"
else
	errecho "invalid argument: $operation"
	usage
fi
