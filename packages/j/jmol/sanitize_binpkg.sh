#!/bin/bash

v=16.1.13
if [ ! -e "Jmol-$v-binary.tar.gz" ]; then
	wget -c https://downloads.sf.net/jmol/Jmol-$v-binary.tar.gz
fi
rm -rf "jmol-$v"
tar -xf "Jmol-$v-binary.tar.gz"
# kill bundled software
rm "jmol-$v/jsmol.zip"
tar --use=xz -cf "jmol-$v.tar.xz" "jmol-$v"
