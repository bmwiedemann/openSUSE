#!/usr/bin/bash

set -e

curVersion=$(grep Version: cockpit-repos.spec | sed -e 's,^\(\s*Version:\s*\)\(.*\)\s*$,\2,')

if [[ ! "$curVersion" =~ ^[0-9]+$ ]]; then
  echo "Error: curVersion is not a valid integer"
  exit 1
fi

###
### Fetch latest soruces
###

newVersion=$(git ls-remote --tags --refs "https://github.com/openSUSE/cockpit-repos" | cut -d/ -f3- | tail -n1)

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
curl -Lo cockpit-repos-$newVersion.tar.xz https://github.com/openSUSE/cockpit-repos/releases/download/$newVersion/cockpit-repos-$newVersion.tar.xz
tar -xf cockpit-repos-$newVersion.tar.xz
mv cockpit-repos-$newVersion/package-lock.json package-lock.json
mv cockpit-repos-$newVersion/cockpit-repos.spec cockpit-repos.spec

git rm cockpit-repos-$curVersion.tar.xz
git add cockpit-repos-$newVersion.tar.xz package-lock.json cockpit-repos.spec
osc service mr

