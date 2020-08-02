#!/bin/bash

TARBALL=$(rpmspec --parse pmdk.spec| grep "Source:" | awk '{ print $NF'} | xargs basename)
DIR=$(tar tvf $TARBALL  | head -n 1 | awk '{ print $NF}')

rm -Rf $DIR
tar xf $TARBALL
cd $DIR
make -C doc all
FILES=$(find . -name "*\.[1357].md" | sed -e 's/\.md$//')
tar czf ../pregen-doc.tgz $FILES
