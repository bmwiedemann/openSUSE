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
#
# Enabled again
#
if test "$EMACS_TOOLKIT" = gtk; then
    # Currently (2013/05/24) the parser of the GNOME libs
    # are broken that is it is not independent from locale
    LC_NUMERIC=POSIX
    GDK_RGBA=0
    export LC_NUMERIC GDK_RGBA
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
if [[ "$1" =~ .*-nox ]] ; then
    exec -a $arg0 ${1+"$@"} "${argv[@]}"
fi
dbusdaemon=$(type -p dbus-daemon 2>/dev/null)
#
# Now check for valid dbus, e.g. after su/sudo/slogin
#
if test -n "$dbusdaemon" ; then
    #
    # Workaround for boo#1205109
    #
    if test "$EUID" = 0 -a "$XDG_RUNTIME_DIR" != /run/user/0; then
	unset XDG_CONFIG_HOME XDG_CACHE_HOME XDG_DESKTOP_DIR XDG_RUNTIME_DIR XDG_DATA_DIRS
#	unset DBUS_SESSION_BUS_ADDRESS
	if test ! -d /run/user/0; then 
	    systemctl start user@0 >/dev/null 2>&1
	fi
	if test -S /run/user/0/bus; then
	    DBUS_SESSION_BUS_ADDRESS=unix:/run/user/0/bus
	fi
    fi

    # Standard on modern systems
    : ${XDG_RUNTIME_DIR:=/run/user/${EUID}}
    export XDG_RUNTIME_DIR

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
	    export DBUS_SESSION_BUS_ADDRESS="unix:path=${XDG_RUNTIME_DIR}/bus"
	    $dbusupdate --systemd "DBUS_SESSION_BUS_ADDRESS"
        fi
    fi
    unset dbuslaunch dbusdaemon
fi
#
# Disable AT bridge if not accessible
#
if test -z "$NO_AT_BRIDGE" ; then
    gsettings=$(gsettings get org.gnome.desktop.interface toolkit-accessibility 2>/dev/null)
    if test -z "$gsettings" -o "$gsettings" = false ; then
	NO_AT_BRIDGE=1
	export NO_AT_BRIDGE
    fi
    unset gsettings
fi
#
# Check input method for working ibus setup
#
case "$XMODIFIERS" in
@im=ibus*)
    _arch=$(getconf LONG_BIT)
    if test "$_arch" != 64
    then
	unset _arch
    else
	_arch=-64
    fi
    if type -p gtk-query-immodules-3.0${_arch} &> /dev/null
    then
	_ibus=$(gtk-query-immodules-3.0${_arch} | grep im-ibus)
    else
	unset _ibus
    fi
    if test -n "$_ibus"
    then
	if test -z "$GTK_IM_MODULE" -o "$GTK_IM_MODULE" != ibus
	then
	    export GTK_IM_MODULE=ibus
	fi
    else
	unset XMODIFIERS
    fi
    unset _ibus _arch
    if ! ibus list-engine &> /dev/null
    then
	unset GTK_IM_MODULE XMODIFIERS
    fi
    ;;
*)
esac
unset G_MESSAGES_DEBUG G_DEBUG G_MESSAGES_PREFIXED
exec -a $arg0 ${1+"$@"} "${argv[@]}"
