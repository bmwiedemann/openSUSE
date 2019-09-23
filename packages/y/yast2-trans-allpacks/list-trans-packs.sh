#!/bin/bash

reqs=$(pdb query --filter \
  'yast2-trans-?? yast2-trans-??\_??,status:production' \
  | awk '{printf ("%s ", $1) }')
# echo $reqs

# for f in $(sed -n 's/^Conflicts: *\(.*\)/\1/gp' *.spec); do
#   [ -z "$f" ] && break
#   reqs=$(echo $reqs | sed "s/$f//")
# done
# # echo $reqs

# check whether all wanted packages are available in stable (noarch)
dist_dir=/mounts/dist/next-head-i586/suse/noarch
if [ -d $dist_dir ]; then
  for f in $reqs; do
    [ -f $dist_dir/$f.rpm ] || missing="$missing $f.rpm"
  done
else
  echo "warning: $dist_dir does not exist; skipping package check"
fi
# report result
if [ -n "$missing" ]; then
  echo "missing package in $dist_dir :"
  echo "        \"$missing\""
  exit 1
fi

sed -i.old "s/^Requires.*/Requires: $reqs/" yast2-trans-allpacks.spec
diff -u yast2-trans-allpacks.spec.old yast2-trans-allpacks.spec

exit 0

