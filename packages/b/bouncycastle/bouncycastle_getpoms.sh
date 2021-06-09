#!/bin/sh

if [ -z "$1" ]
then
    echo "Usage: $0 <version>"
    exit 1
fi

for b in bcprov bcpkix bcpg bcmail bctls ; do
    wget https://repo1.maven.org/maven2/org/bouncycastle/${b}-jdk15on/${1}/${b}-jdk15on-${1}.pom
done
