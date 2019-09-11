#!/bin/bash
# This script is called automatically during autobuild checkin.

ln -f timezone.changes timezone-java.changes

for spec in timezone-java.spec; do
{ sed -n -e '1,/COMMON-BEGIN/p' $spec.in
  sed -n -e '/COMMON-BEGIN/,/COMMON-END/p' timezone.spec
  sed -n -e '/COMMON-END/,/COMMON-PREP-BEGIN/p' $spec.in
  sed -n -e '/COMMON-PREP-BEGIN/,/COMMON-PREP-END/p' timezone.spec
  sed -n -e '/COMMON-PREP-END/,$p' $spec.in; } > $spec.tmp && mv $spec.tmp $spec
done
