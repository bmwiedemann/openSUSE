#!/bin/sh
p="assimp-3.3.1"
wget -c "https://github.com/assimp/assimp/archive/v3.3.1/$p.tar.gz"
rm -Rf "$p"
tar -xf "$p.tar.gz"
rm -Rf "$p/test/models-nonbsd"
tar --owner=root --group=root -czf "$p-suse.tar.gz" "$p"
