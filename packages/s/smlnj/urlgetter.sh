#!/bin/bash

# during build, it is invoked with:
# urlgetter.sh <source> <destination>
# ref: http://smlnj-gforge.cs.uchicago.edu/scm/viewvc.php/config/trunk/unpack?view=markup&root=smlnj

URL="$1"
DEST="$2"

FILE=$(basename $URL)
# remove version from filename
FILE=$(echo "$FILE" | sed -e "s/^[0-9.]*-//g")
# use expected file ext
FILE=$(echo "$FILE" | sed -e "s/.tz$/.tgz/g")

# point to local copy
FILENAME="$BUILDDIR/$FILE"

if [ ! -f "$FILENAME" ]; then
  echo "--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
  echo "ERROR: Could not find: $FILENAME"
  echo "The build wants: $1 -> $2"
  echo "Check pack_new_version.sh"
  echo "--*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
  exit 1
fi

# file ok
exit 0
