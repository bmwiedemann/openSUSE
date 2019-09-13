#!/bin/bash
#
# use consolekit to support legacy at_console setting
#
reason="$1"

dir=/var/run/dbus/at_console

# for at_console we are only interested in local sessions
test "$CK_SESSION_IS_LOCAL" = true || exit 0
test "$reason" = "session_added" -o "$reason" = "session_removed" || exit 0

sessid=${CK_SESSION_ID##*/}
sessid=${sessid//[^A-Za-z0-9]/_}
test -n "$sessid" || exit 1

name=`getent passwd "$CK_SESSION_USER_UID" 2>/dev/null | awk -F: '{print $1}'`

test -n "$name" || exit 1

if test "$reason" = "session_added"; then
	mkdir -p "$dir/$name"
	touch "$dir/$name/$sessid"
else
	rm "$dir/$name/$sessid"
	rmdir "$dir/$name"
fi
