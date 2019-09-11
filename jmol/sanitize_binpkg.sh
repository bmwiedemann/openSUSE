#!/bin/bash

v=14.29.26
rm -rf "jmol-$v"
tar -xf "Jmol-$v-binary.tar.gz"
# kill bundled software
rm "jmol-$v/jsmol.zip"
tar -cf --use=xz "jmol-$v.tar.xz" "jmol-$v"
