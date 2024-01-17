#!/bin/sh
while sleep 2 ; do
    scripts/opensuserabbit.py | grep --line-buffered openSUSE:Factory | tee -a .dumprabbit.json | scripts/rabbithandle.py
done
