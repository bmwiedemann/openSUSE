#!/bin/bash
#
# Launch a GNU Emacs
#
# The environment variable EMACS_TOOLKIT is used to determine
# the prefered GUI. Possible values/types of EMACS_TOOLKIT are
#
#   nox -- for pure console based GNU Emacs 
#   gtk -- for full GTK2/3  based GNU Emacs
#   x11 -- for full LUCID   based GNU Emacs (used Xaw3d)
#
# Should work but remember history
#   bnc#345669 -- Emacs doesn't un-maximize in KDE/KWin
#   bnc#342385 -- Emacs doesn't keep the iconic information in KDE/KWin
#
# if test -z "$EMACS_TOOLKIT" ; then
#     EMACS_TOOLKIT=gtk
#     KDE_FULL_SESSION=$(xprop -root KDE_FULL_SESSION 2>/dev/null)
#     case "$KDE_FULL_SESSION" in
#     *true*) EMACS_TOOLKIT=x11
#     esac
# fi
#
: ${EMACS_TOOLKIT:=gtk}
if test "$EMACS_TOOLKIT" = gtk; then
    # Currently (2013/05/24) the parser of the GNOME libs
    # are broken that is it is not independent from locale
    LC_NUMERIC=POSIX
    XLIB_SKIP_ARGB_VISUALS=1
    GDK_RGBA=0
    export LC_NUMERIC XLIB_SKIP_ARGB_VISUALS GDK_RGBA
fi
arg0=$0
argv=("$@")
if   test -x ${arg0}-${EMACS_TOOLKIT}
then
    set --   ${arg0}-${EMACS_TOOLKIT}
elif test -x ${arg0}-x11
then
    set --   ${arg0}-x11
elif test -x ${arg0}-nox
then
    set --   ${arg0}-nox
else
    echo "no emacs binary found"
    exit 1
fi
dbusdaemon=$(type -p dbus-daemon 2>/dev/null)
#
# Now check for valid dbus, e.g. after su/sudo/slogin
#
if test -n "$dbusdaemon" ; then
    #
    # Currently (2013/05/24) the option --autolaunch for scanning for an
    # already existing session is an internal option of dbus-launch(1).
    #
    if test -s /var/lib/dbus/machine-id ; then
	read -t1 mid < /var/lib/dbus/machine-id
    elif test -s /etc/machine-id ; then
	read -t1 mid < /etc/machine-id
    else
	mid=
    fi
    if test -n "$DBUS_SESSION_BUS_ADDRESS" ; then
	# Determine dbus identifier
	for guid in ${DBUS_SESSION_BUS_ADDRESS//,/ } ; do
	    case "$guid" in
	    guid=*) break
	    esac
	done
	# Check if dbus-daemon is active
	dpid=
	for suid in "${HOME}/.dbus/session-bus/"${mid}* ; do
	    test -e "$suid" || break
	    grep -q $guid "$suid" || continue
	    dpid=$(grep -E '^DBUS_SESSION_BUS_PID=[[:digit:]]+' "$suid")
	    test /proc/${dpid#*=}/exe -ef $dbusdaemon && continue
	    unset DBUS_SESSION_BUS_ADDRESS
	    break
	done
	if test -z "$dpid" ; then
	    case ":$DBUS_SESSION_BUS_ADDRESS" in
	    *:path=/run/user/${UID}/bus*) ;;
	    *)  unset DBUS_SESSION_BUS_ADDRESS
	    esac
	fi
    fi
    # Find a valid dbus-daemon if active
    if test -z "$DBUS_SESSION_BUS_ADDRESS" ; then
	for suid in "${HOME}/.dbus/session-bus/"${mid}* ; do
	    test -e "$suid" || break
	    dpid=$(grep -E '^DBUS_SESSION_BUS_PID=[[:digit:]]+' "$suid")
	    test /proc/${dpid#*=}/exe -ef $dbusdaemon || continue
	    dadd=$(grep -E '^DBUS_SESSION_BUS_ADDRESS=' "$suid")
	    DBUS_SESSION_BUS_ADDRESS=${dadd#*=}
	    export DBUS_SESSION_BUS_ADDRESS
	done
	if test -z "$DBUS_SESSION_BUS_ADDRESS" -a -S "${XDG_RUNTIME_DIR}/bus" ; then
	    DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"
	    export DBUS_SESSION_BUS_ADDRESS
	fi
    fi
    unset mid guid suid dadd
    # Oops ... no dbus-daemon then launch a new session
    if test -z "$DBUS_SESSION_BUS_ADDRESS" ; then
	dbuslaunch=$(type -p dbus-launch 2>/dev/null)
	dbusession=$(type -p dbus-run-session 2>/dev/null)
	if test -z "$dbusession" -a -n "$dbuslaunch" ; then
	    set -- $dbuslaunch --sh-syntax --close-stderr --exit-with-session ${1+"$@"}
	    arg0=$dbuslaunch
	elif test -n "$dbusession" ; then
	    set -- $dbusession -- ${1+"$@"}
	    arg0=$dbusession
	else
	    arg0=emacs
	fi
    elif test -S "${XDG_RUNTIME_DIR}/bus" ; then
	dbusupdate=$(type -p dbus-update-activation-environment 2>/dev/null)
	dbusstatus=$(systemctl --user is-active dbus.service 2>/dev/null)
	if test -n "$dbusupdate" -a "$dbusstatus" != active ; then
	    $dbusupdate --systemd DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"
        fi
    fi
    unset dbuslaunch dbusdaemon
fi
#
# Disable AT bridge if not accessible
#
if test -z "NO_AT_BRIDGE" ; then
    gsettings=$(gsettings get org.gnome.desktop.interface toolkit-accessibility 2>/dev/null)
    if test -z "$gsettings" -o "$gsettings" = false ; then
	NO_AT_BRIDGE=1
	export NO_AT_BRIDGE
    fi
    unset gsettings
fi
unset G_MESSAGES_DEBUG G_DEBUG G_MESSAGES_PREFIXED
exec -a $arg0 ${1+"$@"} "${argv[@]}"
