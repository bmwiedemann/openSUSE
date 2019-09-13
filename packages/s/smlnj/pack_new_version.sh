#!/bin/sh
set -euo pipefail

version="110.81"
files="$version-README.html boot.ppc-unix.tgz boot.sparc-unix.tgz \
       boot.x86-unix.tgz boot.x86-win32.tgz ckit.tgz cml.tgz cm.tgz \
       compiler.tgz config.tgz CYGWININSTALL doc.tgz eXene.tgz heap2asm.tgz \
       HISTORY INSTALL MACOSXINSTALL ml-burg.tgz ml-lex.tgz ml-lpt.tgz \
       MLRISC.tgz ml-yacc.tgz nlffi.tgz old-basis.tgz pgraph.tgz \
       runtime.tgz smlnj-c.tgz smlnj-lib.tgz system.tgz \
       trace-debug-profile.tgz WININSTALL"

mkdir smlnj-$version
cd smlnj-$version

for f in $files; do
	curl -# http://smlnj.cs.uchicago.edu/dist/working/$version/$f -o $f
done

cd ..
tar cjf smlnj-$version.tar.bz2 smlnj-$version
rm -rf smlnj-$version
