#!/bin/sh
while sleep 2 ; do
    echo "starting $0"
    tail -f /home/opensuserabbit/dumprabbit.json | scripts/rabbithandle.py
done
