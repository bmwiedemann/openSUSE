#!/usr/bin/bash

set -e

curVersion=$(grep Version: cockpit-bootloader.spec | sed -e 's,^\(\s*Version:\s*\)\(.*\)\s*$,\2,')

if [[ ! "$curVersion" =~ ^[0-9]+(.[0-9]+)?$ ]]; then
  echo "Error: curVersion is not a valid integer"
  exit 1
fi

if [[ "$curVersion" =~ '.' ]]; then
    curMajor=$(echo ${curVersion} | cut -d'.' -f1)
    curMinor=$(echo ${curVersion} | cut -d'.' -f2)
else
    curMajor=$curVersion
    curMinor='0'
fi

###
### Fetch latest soruces
###

GitDir="cockpit-bootloader"
GWD="-C $GitDir"

# fetch latest cockpit-bootloader
if [ ! -d $GitDir ]; then
	git clone https://github.com/openSUSE/cockpit-bootloader $GitDir
else
    git $GWD checkout main
	git $GWD fetch
fi

newVersion=$(git $GWD tag | grep '^[0-9.]\+$' | sort -rn | head -1)

echo "Current version: $curVersion"
echo "    New version: $newVersion"

if [[ ! "$newVersion" =~ ^[0-9]+(.[0-9]+)?$ ]]; then
  echo "Error: newVersion cannot be determined"
  exit 1
fi

if [[ "$newVersion" =~ '.' ]]; then
    newMajor=$(echo ${newVersion} | cut -d'.' -f1)
    newMinor=$(echo ${newVersion} | cut -d'.' -f2)
else
    newMajor=$newVersion
    newMinor='0'
fi

if [ "$curMajor" -gt "$newMajor" ]; then
	echo "Nothing to do."
	exit 0
elif [[ "$curMajor" -eq "$newMajor"  && "$curMinor" -ge "$newMinor" ]]; then
	echo "Nothing to do."
	exit 0
fi

###
### UPDATE
###

# update node_modules
git $GWD checkout $newVersion
pushd $PWD
cd "$GitDir"
npm install --include optional
popd
cp "$GitDir/package-lock.json" .
osc service manualrun --verbose
rm --verbose *.tgz || true

# update package
curl -Lo cockpit-bootloader-$newVersion.tar.gz https://github.com/openSUSE/cockpit-bootloader/archive/$newVersion.tar.gz

# Updating version in spec file
sed -i -e "s,^\(\s*Version:\s*\)\(.*\)\s*$,\1${newVersion}," cockpit-bootloader.spec
git rm cockpit-bootloader-$curVersion.tar.gz
git add cockpit-bootloader-$newVersion.tar.gz
