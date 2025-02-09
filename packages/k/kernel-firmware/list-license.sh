#!/bin/sh
#
# Generate license file lists for each kernel-firmware topic
#
# usage: list-license.sh [-c] < licenses.list
#

if [ x"$1" = x"-c" ]; then
    docopy=1
    shift
fi

while read first topic licenses; do
    case "$first" in
	\#*) continue;;
    esac
    test -z "$licenses" && continue
    for l in $licenses; do
	case "$l" in
	    *:*)
		src="${l%:*}"
		dst="${l#*:}"
		test -n "$docopy" && cp "$src" "$dst"
		l="$dst"
		;;
	esac
	echo $l >> files-$topic.license
    done
done

for l in files-*.license; do
    f=${l%.license}
    sort -u $l | uniq | sed -e's/^\(.*\)$/%license \1/g' >> $f
    rm -f $l
done
