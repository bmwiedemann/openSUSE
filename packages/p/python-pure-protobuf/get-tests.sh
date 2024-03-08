#!/usr/bin/sh

set -e

if [ -z $1 ]; then
echo "Please input a version for which we should download the tests for"
else
VERSION=$1
curl -LO https://github.com/eigenein/protobuf/archive/refs/tags/$VERSION.tar.gz
mkdir -p tmp
tar xf $VERSION.tar.gz -C tmp
cd tmp/protobuf-$VERSION
tar cf python-pure-protobuf-tests-$VERSION.tar.gz tests
mv python-pure-protobuf-tests-$VERSION.tar.gz ../..
cd ../..
rm -rf tmp $VERSION.tar.gz
fi
