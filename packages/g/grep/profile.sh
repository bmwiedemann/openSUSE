#!/bin/sh
# profiling script for profile-guided-optimizations (PGO)
# must be fully deterministic in what it does for reproducible builds
# should cover most code for good PGO optimization benefit
# See https://github.com/bmwiedemann/theunreproduciblepackage/tree/master/pgo
# for background information on PGO reproducibility

grep=src/grep
t=COPYING
exec > /dev/null
for param in "" -v -i -h -H -l -L -q -n -Z -E -F -P -e -w -c -o; do
  $grep $param "GNU" $t
  $grep $param "G.*U" $t
done
