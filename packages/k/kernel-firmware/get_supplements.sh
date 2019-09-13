#!/bin/sh
#
# Generate modalias Supplements lines for the given kernel-firmware topic
#

target=$1
modules=""

sorted_modules () {
    for m in $*; do
	m=$(echo $m | sed -e's/-/_/g')
	echo $m
    done | sort | uniq
}

while read first topic mods; do
    if [ "$topic" = "$target" ]; then
	first=${first%:}
	if [ -z "$mods" ]; then
	    modules="$modules $first"
	else
	    modules="$modules $mods"
	fi
    fi
done < topics.list

smodules=$(sorted_modules $modules)

for m in $smodules; do
    grep '^'$m':' aliases.list | sed -e's/^.*: \(.*\)$/Supplements:    modalias(\1)/g'
done | sort | uniq

exit 0
