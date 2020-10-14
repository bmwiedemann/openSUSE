#!/bin/sh
#
# Read WHENCE from stdin and install the compressed firmware files into DESTDIR.
# The file list for each topic is created as files-xxx under the current dir.
#
# usage: install-split.sh [-v] topics.list DESTDIR < WHENCE
# 

verbose=:

if [ x"$1" = x"-v" ]; then
    verbose=echo
    shift
fi

topics="$1"
DESTDIR="$2"
fwdir=/lib/firmware
dest=$DESTDIR/$fwdir

do_compress=1

if [ -n "$do_compress" ]; then
    cext=".xz"
else
    cext=""
fi

make_dirs () {
    local f="$1"
    mkdir -p $(dirname "$dest/$f")
    local d=$(dirname "$f")
    if [ "$d" != "." ]; then
	while true; do
	    if ! grep -q '%dir '"$fwdir/$d"'$' files-$topic; then
		echo "%dir $fwdir/$d" >> files-$topic
	    fi
	    case "$d" in
		*/*) d=${d%/*};;
		*) break;;
	    esac
	done
    fi
}

copy_link () {
    local f="$1"
    local lf="$2"
    test -f "$dest/$f$cext" && return
    test -z "$lf" && lf=$(readlink "$f")
    make_dirs "$f"
    ln -sf "$lf$cext" "$dest/$f$cext"
    echo "\"$fwdir/$f$cext\"" >> files-$topic
    $verbose "Link: $lf$cext -> $f$cext for topic $topic"
}

copy_file () {
    local f="$1"
    test -f "$dest/$f$cext" && return
    make_dirs "$f"
    install -c -m 0644 "$f" $(dirname "$dest/$f")
    test -n "$do_compress" && xz -f -C crc32 "$dest/$f"
    echo "\"$fwdir/$f$cext\"" >> files-$topic
    $verbose "Copy: $f$cext for topic $topic"
}

sub="xxx"
while read l; do
    test -z "$l" && continue
    case "$l" in
	----*)
	    sub=""
	    topic=""
	    ;;
	Driver:*)
	    test -n "$sub" && continue
	    sub=$(echo "$l" | sed -e's/Driver: *//' -e's/[ :].*$//')
	    m=$(grep -m1 "^$sub": "$topics" | sed -e's/^.*:[[:space:]]*//')
	    test -z "$m" && continue
	    set -- $m
	    topic="$1"
	    if [ "$topic" = "SKIP" ]; then
		continue
	    fi
	    $verbose "Switching to topic $topic"
	    if [ -n "$topic" ]; then
		if [ ! -s files-$topic ]; then
		    echo "%dir /lib/firmware" > files-$topic
		fi
	    fi
	    ;;
	File:*)
	    test "$topic" = "SKIP" && continue
	    if [ -z "$topic" ]; then
		echo "ERROR: no topic found for $l"
		exit 1
	    fi
	    f=$(echo "$l" | sed -e's/^File: *//' -e's/"//g')
	    if [ -L "$f" ]; then
		copy_link "$f"
	    else
		copy_file "$f"
	    fi
	    ;;
	Link:*)
	    test "$topic" = "SKIP" && continue
	    if [ -z "$topic" ]; then
		echo "ERROR: no topic found for $l"
		exit 1
	    fi
	    echo "$l" | sed -e's/^Link: *//g' -e's/-> //g' | while read f d; do
		copy_link "$f" "$d"
	    done
	    ;;
    esac
done

exit 0
