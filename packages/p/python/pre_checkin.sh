#!/bin/bash
# This script is called automatically during autobuild checkin.

for spec in python-doc.spec python.spec; do
{ sed -n -e '1,/COMMON-PATCH-BEGIN/p' $spec
  sed -n -e '/COMMON-PATCH-BEGIN/,/COMMON-PATCH-END/p' python-base.spec
  sed -n -e '/COMMON-PATCH-END/,/COMMON-PREP-BEGIN/p' $spec
  sed -n -e '/COMMON-PREP-BEGIN/,/COMMON-PREP-END/p' python-base.spec
  sed -n -e '/COMMON-PREP-END/,$p' $spec;
 } | uniq > $spec.tmp && mv $spec.tmp $spec
done
