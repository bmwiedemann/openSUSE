#!/bin/bash
#
XY=$(xdpyinfo |awk '/dimensions:/{print $2;exit}')
CACHEFILE=${HOME}/.cache/xlock-sim/lock-$XY.png
ICON=/usr/share/i3lock-xlock-compat/i3lock-icon.png
if ! test -e $CACHEFILE || test $ICON -nt $CACHEFILE; then
	install -d ${HOME}/.cache/xlock-sim
	convert $ICON -background none -gravity center -extent $XY $CACHEFILE
fi
# not totally black, so that we can see something is happening even if convert failed
exec /usr/bin/i3lock -n -c 444444 -i $CACHEFILE
