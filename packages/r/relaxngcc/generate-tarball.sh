#!/bin/bash
set -e

name=relaxngcc
version="$(sed -n 's/Version:\s*//p' *.spec)"

# RETRIEVE
wget "http://prdownloads.sourceforge.net/${name}/${name}-20031218.zip"

rm -rf tarball-tmp
mkdir -p tarball-tmp
cd tarball-tmp
unzip "../${name}-20031218.zip"

# CLEAN TARBALL
# Remove all the binary files:
find . -name '*.class' -delete
find . -name '*.jar' -delete

# Remove the sources that will be generated with JavaCC:
rm */src/relaxngcc/javabody/*.java

mv ${name}-20031218 ${name}-${version}

tar cJf "../${name}-${version}.tar.xz" *
cd ..
rm -r tarball-tmp "${name}-20031218.zip"
