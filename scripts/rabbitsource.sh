#!/bin/sh
while sleep 2 ; do
    echo "starting $0"
    scripts/opensuserabbit.py | grep --line-buffered openSUSE:Factory >> ../dumprabbit.json
done
