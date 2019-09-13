#!/bin/bash
# This script is called automatically during autobuild checkin.
sed -e "s,^\(Name:.*libtool\),\1-testsuite," \
    -e "s,^\(#\ spec\ file\ for.*libtool\),\1-testsuite," libtool.spec > libtool-testsuite.spec
cp libtool.changes libtool-testsuite.changes
