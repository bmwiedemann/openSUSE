#!/bin/bash
#
# ISDN udev policy
#
# called: isdn.sh [cardtype] [modelnr]
#
# cardtype: string to identfy the card driver
# modelnr: count up number for one cardtype
#
# $Id$
#

. /etc/sysconfig/isdn/scripts/functions

if [ "$ACTION" = "" -o "$SUBSYSTEM" = "" ]; then
    err_mesg Bad hotplug agent invocation, no action
    exit 1
fi

info_mesg $0 $* ACTION=$ACTION

CONFIGS=""
if [ -d /etc/sysconfig/network ]; then
	cd /etc/sysconfig/network

	# find all isdn interface configuration files. These files start with
	# ifcfg-ippp or ifcfg-isdn and do not end in '~', '.rpm*' or similar
	# backup file extensions. They might contain '.', but since this
	# happens very rarely, we drop them all.
	for a in ifcfg-{ippp,isdn}*; do 
		case $a in 
			*~*|*.*) 
				# drop backup files, rpm{save,new,orig}
				;; 
			*)
				if [ "$1" != stop ] ; then
					CONFIGS="$CONFIGS ${a#ifcfg-}"
				else
					CONFIGS="${a#ifcfg-} $CONFIGS"
				fi
				;;
		esac
	done
fi

RET=0

if [ "$ACTION" = "remove" ]; then
	for CONF in $CONFIGS; do
		/sbin/ifdown $CONF -o hotplug || RET=$?
	done
fi

case $SUBSYSTEM in

pcmcia)
	if [ -x /etc/sysconfig/isdn/scripts/hotplug_pcmcia ]; then
		/etc/sysconfig/isdn/scripts/hotplug_pcmcia $*
	else
		err_mesg $0 $* ACTION=$ACTION ISDN not installed
		exit 1
	fi
	;;
usb)
	if [ -x /etc/sysconfig/isdn/scripts/hotplug_usb ]; then
		/etc/sysconfig/isdn/scripts/hotplug_usb $*
	fi
	;;
*)
	info_mesg "ISDN subsys='$SUBSYSTEM' event '$ACTION' not supported"
	;;

esac

if [ "$ACTION" = "add" ]; then
	for CONF in $CONFIGS; do
		/sbin/ifup $CONF -o hotplug || RET=$?
	done
fi

