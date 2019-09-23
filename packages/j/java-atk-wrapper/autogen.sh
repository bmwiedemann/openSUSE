#!/bin/sh
# Run this to generate all the initial makefiles, etc.

test -n "$srcdir" || srcdir=`dirname "$0"`
test -n "$srcdir" || srcdir=.

olddir=`pwd`
cd "$srcdir"

mkdir -p m4

AUTORECONF=`which autoreconf`
if test -z ${AUTORECONF}; then
        echo "*** No autoreconf found, please intall it ***"
        exit 1
else
  autoreconf -vif || exit $?
fi

PKGCONFIG=`which pkg-config`
if test -z "$PKGCONFIG"; then
  echo "*** pkg-config not found, please install it ***"
  exit 1
fi

pkg-config --print-errors gobject-introspection-1.0
if [ "$?" != 0 ]; then
  echo "You probably need to install 'libgirepository1.0-dev'"
  exit 1
fi

# README and INSTALL are required by automake, but may be deleted by clean
# up rules. to get automake to work, simply touch these here, they will be
# regenerated from their corresponding *.in files by ./configure anyway.
touch README INSTALL

cd "$olddir"
test -n "$NOCONFIGURE" || "$srcdir/configure" "$@"
