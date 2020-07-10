#!/bin/bash

# written by cunix in 2019
#
# Installs or links previously found licenses.
#
# $1 should be the soure directory, prepared with script "find_licenses.sh"
# $2 should be the (already created) destination directory

vendor_licenses_dir=$1
install_licenses_dir=$2
licenses_files=/tmp/real_license_files.txt
licenses_links=/tmp/link_license_files.txt

rm $licenses_files
rm $licenses_links

find -P $vendor_licenses_dir -type f -fprintf $licenses_files "%f\n"
find -P $vendor_licenses_dir -type l -fprintf $licenses_links "%f %l\n"

while read line
  do
    install -D -m 0644 $vendor_licenses_dir/$line $install_licenses_dir/$line
  done < $licenses_files

cd $install_licenses_dir
while read line
  do
    combo=($line)
    ln -s ${combo[1]} ${combo[0]}
  done < $licenses_links
