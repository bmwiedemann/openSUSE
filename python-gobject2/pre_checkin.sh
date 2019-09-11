#!/bin/sh

sed 's,build_for_python3 0,build_for_python3 1,;s,^\(Name: *\)python-gobject,\1python3-gobject,' python-gobject2.spec > python3-gobject2.spec
cp python-gobject2.changes python3-gobject2.changes
