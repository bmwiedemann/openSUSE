#!/usr/bin/bash

set -e

curVersion=$(grep Version: cockpit-podman.spec | sed -e 's,^\(\s*Version:\s*\)\(.*\)\s*$,\2,')

if [[ ! "$curVersion" =~ ^[0-9]+$ ]]; then
  echo "Error: curVersion is not a valid integer"
  exit 1
fi

###
### Fetch latest soruces
###

GitDir="cockpit-podman"
GWD="-C $GitDir"

# fetch latest cockpit-podman
if [ ! -d $GitDir ]; then
	git clone https://github.com/cockpit-project/cockpit-podman $GitDir
else
    git $GWD checkout main
	git $GWD fetch
fi

newVersion=$(git $GWD tag | grep '^[0-9.]\+$' | sort -rn | head -1)

echo "Current version: $curVersion"
echo "    New version: $newVersion"

if [[ ! "$newVersion" =~ ^[0-9]+$ ]]; then
  echo "Error: newVersion cannot be determined"
  exit 1
fi

if [ "$curVersion" -ge "$newVersion" ]; then
	echo "Nothing to do."
	exit 0
fi

###
### UPDATE
###
# # initialize all submodules
git $GWD checkout $newVersion
git $GWD submodule update --init --depth 1
diff $GitDir/node_modules/.package.json $GitDir/package.json
cp $GitDir/node_modules/.package-lock.json package-lock.json

# update node_modules
curl -Lo cockpit-podman-$newVersion.tar.gz https://github.com/cockpit-project/cockpit-podman/archive/$newVersion.tar.gz

# Updating version in spec file
sed -i -e "s,^\(\s*Version:\s*\)\(.*\)\s*$,\1${newVersion}," cockpit-podman.spec
osc rm cockpit-podman-$curVersion.tar.gz
osc add cockpit-podman-$newVersion.tar.gz
osc service mr

