#! /bin/bash

. $(pwd)/tycho-scripts.sh

projLoc=$1
zipLoc=$projLoc/target/*.zip
mfLoc=$2

zipDir=`dirname ${zipLoc}`
zipFile=`basename ${zipLoc}`
tmpDir=${zipDir}/tmp
[ -z "$mfLoc" ] && mfLoc=/dev/null

mkdir -p ${tmpDir}
unzip -d ${tmpDir} ${zipLoc}
wantedBundles=`sed 's/ fragment=\"true\"//' ${projLoc}/*.product | sed -n 's/.*<plugin id=\"\(.*\)\"\/>.*/\1/ p'`
pushd ${tmpDir}
pluginsDir=`find . -type d -name plugins`
pushd ${pluginsDir} && rm -rf *
symlinkBundles "${wantedBundles}"
for b in *; do readlink $b; done >$mfLoc
popd
zip -ry ${zipFile} *
popd
mv ${tmpDir}/${zipFile} ${zipLoc}
