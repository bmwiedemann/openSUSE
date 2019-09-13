#!/bin/sh
set -x

VER="$(sed -n 's/Version:\s*//p' *.spec)"

FNS=scala-$VER

rm -rf $FNS/
git clone git://github.com/scala/scala.git $FNS
cd $FNS
git checkout v$VER
git log --pretty=format:"%H%n%ci" v$VER | head -n 2 | \
   sed -e 's/\-//g' -e 's/\s\+.*//g' >../scala.gitinfo
cd ..
tar -zcf $FNS.tgz --exclude $FNS/.git $FNS/
cd $FNS
./pull-binary-libs.sh
rm -rf lib/jline.jar
tar -zcf ../$FNS-bootstrap.tgz --exclude .git lib/*.jar
cd ..
rm -rf $FNS/
