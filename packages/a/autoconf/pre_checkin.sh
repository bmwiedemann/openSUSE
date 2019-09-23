#!/bin/bash
# This script is called automatically during autobuild checkin.
sed -i "s/^Version:.*/$(grep ^Version: autoconf.spec)/" autoconf-el.spec
ln -f autoconf.changes autoconf-el.changes
sed -e "s,^\(Name:.*autoconf\),\1-testsuite," autoconf.spec > autoconf-testsuite.spec
ln -f autoconf.changes autoconf-testsuite.changes
