#!/bin/sh

sed 's,build_for_python3 0,build_for_python3 1,;s,^\(Name: *\)python-,\1python3-,' python-virtkey.spec > python3-virtkey.spec
cp python-virtkey.changes python3-virtkey.changes
