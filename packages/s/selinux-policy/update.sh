#!/bin/sh

date=$(date '+%Y%m%d')
base_name_pattern='selinux-policy-*.tar.xz'

echo Update to $date

old_tar_file=$(ls -1 $base_name_pattern)

osc service manualrun

rm -rf container-selinux
git clone --depth 1 https://github.com/containers/container-selinux.git
rm -f container.*
mv container-selinux/container.* .
rm -rf container-selinux

# delete old files. Might need a better sanity check
tar_cnt=$(ls -1 $base_name_pattern  | wc -l)
if [ $tar_cnt -gt 1 ]; then
  echo delte old file $old_tar_file
  rm "$old_tar_file"
  osc addremove
fi

osc status

