#!/bin/bash

v=14.30.1
if [ ! -e "Jmol-$v-binary.tar.gz" ]; then
	wget -c http://downloads.sf.net/jmol/Jmol-$v-binary.tar.gz
fi
rm -rf "jmol-$v"
tar -xf "Jmol-$v-binary.tar.gz"
# kill bundled software
rm "jmol-$v/jsmol.zip"
tar --use=xz -cf "jmol-$v.tar.xz" "jmol-$v"
