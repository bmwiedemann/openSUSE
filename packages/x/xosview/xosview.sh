#!/bin/sh

net="-net"
if   test -e /proc/net/ip_acct ; then
     net="+net"
elif test -e /proc/net/ip_fwchains -o /proc/net/dev ; then
     net="+net"
fi 

bat="-bat"
if test -d /proc/acpi/battery ; then
    for entry in /proc/acpi/battery/* ; do
	test -e "$entry" || break
    	# We a ACPI kernel interface
	bat="+bat"
	break
    done
    unset entry
fi
if test -e /proc/apm -a -e /proc/devices ; then
    # We have a APM kernel interface
    while read line ; do
	# See /usr/src/linux/arch/i386/kernel/apm.c
	case "$line" in
	    *[0-9]*pcmcia*)
		# PCMCIA found, let's read APM kernel interface
		read DRVver APMver APMflg AC BATstat BATflg BATload Units < /proc/apm
		break
	esac
    done < /proc/devices
    case "$DRVver" in
	1.*)
	   # 0xff means status unknown, 0x80 means no system battery
	   if test "$BATstat" != "0xff" -a "$BATflg" != "0x80" ; then
		# percentage of charge should be not less than zero
		case "$BATload" in
		    [0-9]*%) bat="+bat"
		esac
	   fi
    esac
fi
if xrdb -query | grep -qiE 'xosview\*battery:[[:space:]]*(true|on)' ; then
    bat="+bat"
fi

arg0=""
test -n "$BASH_VERSINFO" && arg0="-a $0"

exec $arg0 @@BINDIR@@/xosview.bin $net $bat ${1+"$@"}
