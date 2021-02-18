#!/bin/bash
set -e

name=plexus-languages
version="$(sed -n 's/Version:\s*//p' *.spec)"
pkgdir=`cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd`

tmpdir=`mktemp -d`
echo $tmpdir
trap 'rm -r "$tmpdir"' EXIT
pushd "$tmpdir" >/dev/null

# RETRIEVE
wget "https://github.com/codehaus-plexus/plexus-languages/archive/plexus-languages-${version}.tar.gz" -O "${name}-${version}.orig.tar.gz"

treeroot="$tmpdir/tree"
mkdir "$tmpdir/tree"
pushd "$treeroot" >/dev/null

tar xf "../${name}-${version}.orig.tar.gz"

# CLEAN TARBALL
find -name '*.jar' -delete
find -name '*.class' -delete

tar cJf "$pkgdir/${name}-${version}.tar.xz" *
