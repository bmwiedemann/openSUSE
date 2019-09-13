#!/bin/sh

set -e

fallback_entry () {

  local saved=$1
  local FALLBACK_MATCH=`echo $saved | sed -e '/>/!d' -e '/>/s/>.*$//'`

  if [ -n "$FALLBACK_MATCH" ]; then
    for i in $MENU_ENTRIES; do
      if expr match "$i" "^$FALLBACK_MATCH" >/dev/null ; then
        echo "$i"
        return 0
      fi
    done
  fi
  return 0
}

run_command () {
  [ x"$DEBUG_RUN" = x1 ] && echo $@ || $@ 
}

debug_print () {
  [ x"$DEBUG_RUN" = x1 ] && echo $@ || true
}

case $1 in
-d|--debug)
  DEBUG_RUN=1
  ;;
esac

GRUB_EDITENV="/usr/bin/grub2-editenv"
GRUB_SET_DEFAULT="/usr/sbin/grub2-set-default"

SAVED_ENTRY=`${GRUB_EDITENV} list | sed -ne "/^saved_entry=/{s@\"\(.*\)\"@\1@;t 1;s@'\(.*\)'@\1@;: 1;s@^[^=]\+=@@;p;b}"`

debug_print "SAVED_ENTRY=$SAVED_ENTRY"

if [ -z "$SAVED_ENTRY" ] || expr match "$SAVED_ENTRY" "^[0-9]\+$" >/dev/null; then
  exit 0
fi

MENU_ENTRIES=`awk '
  BEGIN {
    bracket = 0
  }
  {
    patsplit($0, words, "([^[:blank:]]+)|(\"[^\"]+\")|('\''[^'\'']*'\'')", sep)

    cmd = words[1]
    arg1 = words[2]

    if (substr(arg1, 1, 1) == "\"" || substr(arg1, 1, 1) == "'\''") {
      len = length(arg1)
      arg1 = substr(arg1, 2, len - 2)
    }

    if (cmd == "submenu") {
      submenu[bracket] = arg1
    } else if (cmd == "menuentry") {
      title = ""
      for (i = 0; i < bracket; i++) {
        if (i in submenu)
        title = title submenu[i] ">"
      } 
      print title arg1
    } 

    for (w in words) {
      if (words[w] == "{") {
        bracket++
      } else if (words[w] == "}") {
        bracket--
      }
    }
  }
' /boot/grub2/grub.cfg`

IFS=$'\n'

debug_print "MENU_ENTRIES="
for i in $MENU_ENTRIES; do
  debug_print "$i"
done

for i in $MENU_ENTRIES; do
  if [ "$SAVED_ENTRY" = "$i" ]; then
    exit 0
  fi
done

FALLBACK=`fallback_entry $SAVED_ENTRY`

if [ -n "$FALLBACK" ]; then
  run_command ${GRUB_SET_DEFAULT} "$FALLBACK"
  exit 0
fi

source /etc/os-release

NEW_SAVED_ENTRY=`echo $SAVED_ENTRY | sed -ne "s/$NAME [0-9a-zA-Z_.-]\\+/$NAME $VERSION/pg"`

debug_print "NEW_SAVED_ENTRY=$NEW_SAVED_ENTRY"

if [ -z "$NEW_SAVED_ENTRY" -o  "$NEW_SAVED_ENTRY" = "$SAVED_ENTRY" ]; then
  exit 0
fi

IFS=$'\n'
for i in $MENU_ENTRIES; do
  if [ "$NEW_SAVED_ENTRY" = "$i" ]; then
    run_command ${GRUB_SET_DEFAULT} "$NEW_SAVED_ENTRY"
    exit 0
  fi
done

FALLBACK=`fallback_entry $NEW_SAVED_ENTRY`

if [ -n "$FALLBACK" ]; then
  run_command ${GRUB_SET_DEFAULT} "$FALLBACK"
  exit 0
fi

exit 0
