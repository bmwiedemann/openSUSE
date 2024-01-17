#!/bin/sh

# This script helps to find important differences between
# wxWidgets/wxGTK and wxWidgets instance embedded in wxPython-src.

VER=2.9.4
PYREL=0
find wxWidgets-${VER} wxPython-src-${VER}.${PYREL} -type f | while read ; do tr -d '\r' <"$REPLY" >"$REPLY".new ; mv "$REPLY".new "$REPLY" ; done
find wxWidgets-${VER} wxPython-src-${VER}.${PYREL} -type f -exec sed -i /RCS-ID:/d {} \;
find wxWidgets-${VER} wxPython-src-${VER}.${PYREL} -type f -exec sed -i /\$Id/d {} \;
find wxWidgets-${VER} wxPython-src-${VER}.${PYREL} -name '*.wat' -exec rm {} \;
LANG=C diff -ur wxWidgets-${VER} wxPython-src-${VER}.${PYREL} | grep -v ^Only >wxWidgets-to-wxpython-${VER}.${PYREL}.patch
