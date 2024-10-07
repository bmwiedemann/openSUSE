#!/usr/bin/bash
#
# Script to update the vendor tarball
# Author: Elisei Roca
#------------------------------------

set -eo pipefail
# set -x

NAME=etcd
STACK=("server" "etcdctl" "etcdutl")
VERSION=$(grep -oP '(?<=Version:)(.*)' etcd.spec | xargs)

[ ! -f "$NAME-$VERSION".tar.gz ] && echo "$NAME-$VERSION.tar.gz does not exist" && exit 1 

echo "Updating vendor file..."

tempdir="$(mktemp -d --suffix=.etcd)"
function cleanup() {
  rm -rf "${tempdir}"
}
trap cleanup EXIT

mkdir -p "${tempdir}/vendor"

tar --strip-components=1 -xvf "$NAME-$VERSION".tar.gz -C "${tempdir}" &> /dev/null

dir=$(pwd)
for item in ${STACK[*]}; do
	mkdir "${tempdir}/vendor/${item}"
	cd "${tempdir}/${item}"
	go mod vendor
	mv vendor/ ../vendor/"$item"
done
cd "$dir"

fdupes -r -1 "${tempdir}/vendor/" |
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

tar -czvf vendor.tar.gz -C "${tempdir}" vendor &> /dev/null

echo "Repacked to vendor.tar.gz"
