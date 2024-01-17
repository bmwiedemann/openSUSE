#!/bin/bash

if [ -n "$1" ]; then
    rm -rf apache_rex
    git clone https://github.com/pgajdos/apache-rex __repo
    cd __repo
    git checkout -b $1
    git archive --format=tar --prefix="apache-rex/" $1 | bzip2 > ../apache-rex.tar.bz2
    cd ..
    rm -rf __repo
else
    echo "Usage: generate.tarball.sh COMMIT_ID"
fi