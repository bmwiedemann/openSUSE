#!/usr/bin/bash
#
# Script to update the vendor tarball
# Author: Elisei Roca
#------------------------------------

# set -x

NAME=etcd
STACK=("server" "etcdctl" "etcdutl")
VERSION=$(grep -oP '(?<=Version:)(.*)' etcd.spec | xargs)

[ ! -f "$NAME-$VERSION".tar.gz ] && echo "$NAME-$VERSION.tar.gz does not exist" && exit 1 

echo "Updating vendor file..."

rm -rf /tmp/"$NAME" ||:
mkdir -p /tmp/"$NAME"/vendor

tar --strip-components=1 -xvf "$NAME-$VERSION".tar.gz -C /tmp/"$NAME" &> /dev/null

dir=$(pwd)
for item in ${STACK[*]}; do
	mkdir /tmp/"$NAME"/vendor/"$item"
	cd /tmp/"$NAME/$item"
	go mod vendor
	mv vendor/ ../vendor/"$item"
done
cd "$dir"

fdupes -r -1 /tmp/"$NAME"/vendor/ |
  while read line; do 
    target="";
    for file in ${line[*]}; do
      if [ "x${target}" == "x" ]; then
        target=$file;
      else
        ln -f "${target}" "${file}";
      fi; 
    done;
  done

tar -czvf vendor.tar.gz -C /tmp/"$NAME" vendor &> /dev/null
rm -rf /tmp/"$NAME"  ||:

echo "Repacked to vendor.tar.gz"
