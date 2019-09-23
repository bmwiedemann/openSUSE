#!/bin/sh
#
# Generate license file lists for each kernel-firmware topic
#
# usage: list-license.sh < licenses.list
#

for f in files-*; do
    echo '%license WHENCE' >> $f
done

while read first topic licenses; do
    case "$first" in
	\#*) continue;;
    esac
    test -z "$licenses" && continue
    for l in $licenses; do
	echo $l >> files-$topic.license
    done
done

for l in files-*.license; do
    f=${l%.license}
    sort $l | uniq | sed -e's/^\(.*\)$/%license \1/g' >> $f
    rm -f $l
done
