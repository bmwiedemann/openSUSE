#!/bin/sh

# to be sourced

# If we are running the MATE session, source ~/.materc

if [ -z "${STARTUP}" ] && [ -n "${WINDOWMANAGER}" ]; then
    # We are likely in a display-manager running on a distro such as openSUSE...
    STARTUP="${WINDOWMANAGER}"
fi

BASESTARTUP=${STARTUP%% *}
BASESTARTUP=${BASESTARTUP##*/}
if [ "$BASESTARTUP" = x-session-manager ]; then
    BASESTARTUP=$(basename $(readlink /etc/alternatives/x-session-manager))
fi
case "$BASESTARTUP" in
  mate-session*)
    MATERC=$HOME/.materc
    if [ -r "$MATERC" ]; then
      . "$MATERC"
    fi
    # We prepend /usr/share/mate since its defaults.list actually points
    # to /etc so it is configurable.
    if [ -z "$XDG_DATA_DIRS" ]; then
      XDG_DATA_DIRS=/usr/share/mate:/usr/local/share/:/usr/share/
    else
      XDG_DATA_DIRS=/usr/share/mate:"$XDG_DATA_DIRS"
    fi
    export XDG_DATA_DIRS
    ;;
esac
