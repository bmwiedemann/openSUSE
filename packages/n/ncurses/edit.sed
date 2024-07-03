#!/usr/bin/bash

while test "${1::2}" = "--" ; do
    case "$1" in
    --cflags=*)
	cflags="${cflags:+$cflags }${1#*=}"
	shift
	;;
    --cflags)
	cflags="${cflags:+$cflags }$2"
	shift 2
	;;
    --libs=*)
	libs="${libs:+$libs }${1#*=}"
	shift
	;;
    --libs)
	libs="${libs:+$libs }$2"
	shift 2
	;;
    esac
done

sed -ri -e "
/^[[:blank:]]*--cflags.*\)/,/;;/ {
    s|for opt in .*|for opt in ${cflags}|
}
/^[[:blank:]]*--libs.*\)/,/;;/ {
    s|for opt in .*|for opt in ${libs}|
}" ${1+"$@"}
