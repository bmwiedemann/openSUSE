#!/bin/bash
set -e

name=relaxngcc
version="$(sed -n 's/Version:\s*//p' *.spec)"
pkgdir=`cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd`

tmpdir=`mktemp -d`
trap 'rm -r "$tmpdir"' EXIT
pushd "$tmpdir" >/dev/null

# RETRIEVE
wget "https://prdownloads.sourceforge.net/${name}/${name}-20031218.zip"

treeroot="$tmpdir/tree"
mkdir "$tmpdir/tree"
pushd "$treeroot" >/dev/null

unzip "../${name}-20031218.zip"

# CLEAN TARBALL
# Remove all the binary files:
find . -name '*.class' -delete
find . -name '*.jar' -delete

# Remove the sources that will be generated with JavaCC:
rm */src/relaxngcc/javabody/*.java

mv ${name}-20031218 ${name}-${version}

tar cJf "$pkgdir/${name}-${version}.tar.xz" *
