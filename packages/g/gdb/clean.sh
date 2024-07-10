#!/bin/sh

dryrun=false
while [ $# -gt 0 ]; do
    case $1 in
	-dryrun|--dryrun|-dry-run|--dry-run)
	    dryrun=true
	    ;;
	*)
	    echo "Don't know how to handle arg: $1"
	    exit 1
    esac
    shift
done
	 
first=true
for f in *.patch; do
    if grep -q "^Patch.*[ \t]$f" gdb.spec; then
	continue
    fi

    if $dryrun; then
	if $first; then
	    echo "Patches not mentioned in gdb.spec:"
	fi
	first=false

	echo "$f"

	continue
    fi

    ( set -x; osc remove -f "$f" )
done

files=$(echo ./*~)
if [ "$files" != "./*~" ]; then
    if $dryrun; then
	echo "Backup files:"
	echo "$files"
    else
	for f in $files; do
	    ( set -x; rm -f "$f" )
	done
    fi
fi
