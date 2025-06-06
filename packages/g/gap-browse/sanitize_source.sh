#!/bin/sh -ex
v="1.8.21"
wget -c "https://www.math.rwth-aachen.de/homes/Browse/Browse-$v.tar.bz2"
tar -xf "Browse-$v.tar.bz2"
# Delete CC-BY-NC files
rm -Rf "Browse-$v/bibl"
find "Browse-$v" -print0 | sort -z | tar --use=xz --null -T- -cf "Browse-$v.tar.xz" "Browse-$v/"
