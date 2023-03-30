#!/bin/bash

# This script reads filenames from STDIN and outputs any relevant provides
# information that needs to be included in the package.
target="mingw32"
host="i686-w64-mingw32"

if [ -n "$1" ]; then
   package_name="$1"
fi

[ -z "$OBJDUMP" ] && OBJDUMP="$host-objdump"

filelist=`sed "s/['\"]/\\\&/g"`

dlls=$(echo "$filelist" | grep '\.dll$')
pcs=$(echo "$filelist" | grep '\.pc$')
libs=$(echo "$filelist" | grep '\.a$')

for f in $dlls; do
    [ ! -f "$f" ] && continue
    basename=`basename "$f" | tr "[:upper:]" "[:lower:]"`
    echo "$target($basename)"
done

for g in $pcs; do
    [ ! -f "$g" ] && continue
	PKG_CONFIG_PATH="${g%/*}" "$host-pkgconf" --print-errors --print-provides "$g" | awk '{ print "'"$target"'(pkg:"$1")", $2, $3 }'
done | sort -u

for h in $libs; do
    [ ! -f "$h" ] && continue
    libname=`basename "$h" | sed 's#^lib##g' | sed 's#\.dll\.#\.#g' | sed 's#\.a##g'`
	echo "$target(lib:$libname)"
done