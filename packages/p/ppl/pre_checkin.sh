#!/bin/bash
# This script is called automatically during autobuild checkin.
sed -e "s,^\(Name:.*ppl\),\1-testsuite," ppl.spec > ppl-testsuite.spec
