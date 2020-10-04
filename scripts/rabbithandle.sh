#!/bin/sh
while sleep 2 ; do
    echo "starting $0"
    scripts/rabbithandle.py < /home/opensuserabbit/dumprabbit.json
done
