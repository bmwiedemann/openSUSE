#!/bin/bash
# Run this script after updating the source tarball and changing the version
# number in the spec file. If you get errors about missing files in
# ./doc/librpmem/ and ./doc/rpmemd, you are probably missing libfabric.

TARBALL=$(rpmspec --parse pmdk.spec| grep "Source:" | awk '{ print $NF'} | xargs basename)
DIR=$(tar -tvf "$TARBALL" | head -n 1 | awk '{ print $NF}')

rm -Rf "$DIR"
tar -xf "$TARBALL"
cd "$DIR"
make -C doc all
FILES=$(find . -name "*\.[1357].md" | sed -e 's/\.md$//')
tar --use=xz -cf ../pregen-doc.tar.xz $FILES
