#!/usr/bin/bash

set -e

curVersion=$(grep Version: cockpit-machines.spec | sed -e 's,^\(\s*Version:\s*\)\(.*\)\s*$,\2,')

if [[ ! "$curVersion" =~ ^[0-9]+$ ]]; then
  echo "Error: curVersion is not a valid integer"
  exit 1
fi

###
### Fetch latest soruces
###

GWD="-C cockpit-machines"

# fetch latest cockpit-machines
if [ ! -d cockpit-machines ]; then
	git clone https://github.com/cockpit-project/cockpit-machines cockpit-machines
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
git $GWD checkout --quiet $newVersion
git $GWD submodule update --init --depth 1
diff cockpit-machines/node_modules/.package.json cockpit-machines/package.json
cp cockpit-machines/node_modules/.package-lock.json package-lock.json

# update node_modules
curl -Lo cockpit-machines-$newVersion.tar.gz https://github.com/cockpit-project/cockpit-machines/archive/refs/tags/$newVersion.tar.gz

# Updating version in spec file
sed -i -e "s,^\(\s*Version:\s*\)\(.*\)\s*$,\1${newVersion}," cockpit-machines.spec

# update modules
osc add cockpit-machines-$newVersion.tar.gz
osc rm  cockpit-machines-$curVersion.tar.gz
osc service mr

