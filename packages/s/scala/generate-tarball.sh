#!/bin/bash
set -e

name=scala
version="$(sed -n 's/Version:\s*//p' *.spec)"

# RETRIEVE
wget "https://github.com/scala/scala/archive/v${version}.tar.gz" -O "${name}-${version}.orig.tar.gz"

rm -rf tarball-tmp
mkdir tarball-tmp
cd tarball-tmp
tar xf "../${name}-${version}.orig.tar.gz"

# CLEAN TARBALL
find -name '*.jar' -delete
find -name '*.class' -delete
# Possibly proprietary code
find -name '*.dll' -delete
find -name '*.so' -delete
# Contains minified js of uncertain origin
rm -r */src/compiler/scala/tools/nsc/doc/html/resource/lib

tar czf "../${name}-${version}.tar.gz" *
cd ..
rm -r tarball-tmp "${name}-${version}.orig.tar.gz"
