#!/bin/sh
#
# Read WHENCE from stdin create files-xxx for each topic
#
# usage: make-files.sh [-v] topics.list DESTDIR < WHENCE
# 

verbose=:

if [ x"$1" = x"-v" ]; then
    verbose=echo
    shift
fi

topics="$1"
DESTDIR="$2"
fwdir=${3:-/lib/firmware}
dest=$DESTDIR/$fwdir

do_compress=1

if [ -n "$do_compress" ]; then
    cext=".xz"
else
    cext=""
fi

make_dirs () {
    local f="$1"
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

add_file () {
    local f="$1"
    make_dirs "$f"
    if [ -f "$dest/$f" ]; then
	echo "\"$fwdir/$f\"" >> files-$topic
    else
	echo "\"$fwdir/$f$cext\"" >> files-$topic
    fi
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
		    echo "%dir $fwdir" > files-$topic
		fi
	    fi
	    ;;
	File:*|RawFile:*)
	    test "$topic" = "SKIP" && continue
	    if [ -z "$topic" ]; then
		echo "ERROR: no topic found for $l"
		exit 1
	    fi
	    f=$(echo "$l" | sed -e's/^File: *//' -e's/^RawFile: *//' -e's/"//g' -e's/\\//g')
	    case "$f" in
		*/README*)
		    continue;;
	    esac
	    add_file "$f"
	    ;;
	Link:*)
	    test "$topic" = "SKIP" && continue
	    if [ -z "$topic" ]; then
		echo "ERROR: no topic found for $l"
		exit 1
	    fi
	    f=$(echo "$l" | sed -e's/^Link: *//' -e's/ *->.*$//' -es'/\\//g')
	    add_file "$f"
	    ;;
    esac
done

exit 0
