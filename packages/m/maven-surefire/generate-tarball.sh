#!/bin/bash
set -e

name=maven-surefire
version="$(sed -n 's/Version:\s*//p' ${name}.spec)"

# RETRIEVE
wget "https://archive.apache.org/dist/maven/surefire/surefire-${version}-source-release.zip" -O "${name}-${version}.orig.zip"

rm -rf tarball-tmp
mkdir tarball-tmp
cd tarball-tmp
unzip "../${name}-${version}.orig.zip"

# CLEAN TARBALL
find -name '*.jar' -delete
find -name '*.class' -delete

tar czf "../${name}-${version}.tar.gz" *
cd ..
rm -r tarball-tmp "${name}-${version}.orig.zip"
