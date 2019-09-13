#!/bin/bash

# $1 - revision number to checkout.
: ${1?"You must either provide desired revision number \"X\" to checkout: `basename $0` X
                                or fetch the latest revision by: `basename $0` HEAD"}

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
name=non-ntk
version=1.3.0

pushd "$tmp" >/dev/null
echo "Fetching git revision: $1"
git clone git://git.tuxfamily.org/gitroot/non/fltk.git $name-$version |tee $name.stdout
cd $name-$version
git reset $1
rm -rf .git* .waf*
cd ..
rm -rf $name.stdout
tar jcf "$pwd"/$name-$version-git$1.tar.bz2 $name-$version
echo "Written: $name-$version-git$1.tar.bz2"
popd >/dev/null
