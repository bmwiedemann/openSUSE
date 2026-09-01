#!/usr/bin/bash

set -e

curVersion=$(grep Version: cockpit-files.spec | sed -e 's,^\(\s*Version:\s*\)\(.*\)\s*$,\2,')

if [[ ! "$curVersion" =~ ^[0-9]+$ ]]; then
  echo "Error: curVersion is not a valid integer"
  exit 1
fi

###
### Fetch latest soruces
###

GWD="-C cockpit-files"

# fetch latest cockpit-files
if [ ! -d cockpit-files ]; then
	git clone https://github.com/cockpit-project/cockpit-files cockpit-files
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
diff cockpit-files/node_modules/.package.json cockpit-files/package.json
cp cockpit-files/node_modules/.package-lock.json package-lock.json

# update node_modules
curl -Lo cockpit-files-$newVersion.tar.gz https://github.com/cockpit-project/cockpit-files/archive/refs/tags/$newVersion.tar.gz

# Updating version in spec file
sed -i -e "s,^\(\s*Version:\s*\)\(.*\)\s*$,\1${newVersion}," cockpit-files.spec

# update modules
osc add cockpit-files-$newVersion.tar.gz
osc rm  cockpit-files-$curVersion.tar.gz
osc service mr

