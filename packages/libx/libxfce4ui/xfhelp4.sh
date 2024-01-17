#!/bin/sh
#
#  xfce
#
#  Copyright (C) 1999 Olivier Fourdan (fourdan@xfce.org)
#  Copyright (C) 2003 Jasper Huijsmans (jasper@xfce.org)
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#

HELP_DIR="/usr/share/xfce4"

if [ -n "$1" ]; then
    HELP_FILE=
    MODULE="${1%.html}"
    case $1 in
        *.html)
            HELP_FILE="$1"
            ;;
    esac
else
    exit 1
fi

# Check for translated documentation
if [ -n "$LC_ALL" ] ; then
  LC=$LC_ALL
elif [ -n "$LANG" ] ; then
  LC=$LANG
else
  LC="C"
fi

LC_CLEAN="${LC%_*}"

if [ -r "$HELP_DIR/$MODULE/html/$LC/index.html" ]
then
  URL="$HELP_DIR/$MODULE/html/$LC/index.html"
elif [ -r "$HELP_DIR/$MODULE/html/$LC_CLEAN/index.html" ]
then
  URL="$HELP_DIR/$MODULE/html/$LC_CLEAN/index.html"
elif [ -r "$HELP_DIR/$MODULE/html/C/index.html" ]
then
  URL="$HELP_DIR/$MODULE/html/C/index.html"
elif [ -n "$HELP_FILE" ]
then
  if [ -r "$HELP_DIR/$MODULE/html/$LC/$HELP_FILE" ]
  then
    URL="$HELP_DIR/$MODULE/html/$LC/$HELP_FILE"
  elif [ -r "$HELP_DIR/$MODULE/html/$LC_CLEAN/$HELP_FILE" ]
  then
    URL="$HELP_DIR/$MODULE/html/$LC_CLEAN/$HELP_FILE"
  elif [ -r "$HELP_DIR/$MODULE/html/C/$HELP_FILE" ]
  then
    URL="$HELP_DIR/$MODULE/html/C/$HELP_FILE"
  else
    URL="$HELP_DIR/xfce-utils/html/C/index.html"
  fi
else
  URL="$HELP_DIR/xfce-utils/html/C/index.html"
fi

exo-open "${URL}"
