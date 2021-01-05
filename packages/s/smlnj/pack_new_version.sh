#!/bin/sh
set -euo pipefail

#
# $ sh pack_new_version.sh [%version]
#
# See upstream: https://www.smlnj.org/dist/working/
#

if [ "${1+x}" = x ]; then
  version="$1"
else
  version=$(\grep Version: *.spec | cut -d: -f2 | xargs)
fi

files="$version-README.html doc.tgz asdl.tgz config.tgz \
       boot.ppc-unix.tgz boot.amd64-unix.tgz boot.x86-unix.tgz \
       cm.tgz compiler.tgz runtime.tgz system.tgz \
       MLRISC.tgz smlnj-lib.tgz old-basis.tgz \
       ckit.tgz nlffi.tgz \
       cml.tgz eXene.tgz \
       heap2asm.tgz \
       HISTORY.html install.html \
       ml-burg.tgz ml-lex.tgz ml-lpt.tgz ml-yacc.tgz \
       smlnj-c.tgz \
       pgraph.tgz trace-debug-profile.tgz"

PKG_NAME="smlnj-$version"
mkdir -p $PKG_NAME
cd $PKG_NAME

echo "Getting SMLNJ source tarballs for v$version"

for f in $files; do
  curl -s http://smlnj.cs.uchicago.edu/dist/working/$version/$f -C - -L -o $f &
done

echo -n "Waiting for downloads to complete... "
for job in `jobs -p`; do wait ${job}; done
echo "done"

cd ..
echo -n "Compressing archive... "
tar -cf - $PKG_NAME/ | xz -9 -c - > $PKG_NAME.tar.xz
echo "done"

echo "./smlnj-$version source updated"
