#!/usr/bin/bash

set -e

curVersion=$(grep Version: cockpit-subscriptions.spec | sed -e 's,^\(\s*Version:\s*\)\(.*\)\s*$,\2,')

if [[ ! "$curVersion" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
  echo "Error: curVersion is not a valid integer"
  exit 1
fi

###
### Fetch latest soruces
###

newVersion=$(git ls-remote --tags --refs "https://github.com/openSUSE/cockpit-subscriptions" | cut -d/ -f3- | sort -n | tail -n1)

echo "Current version: $curVersion"
echo "    New version: $newVersion"

if [[ ! "$newVersion" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
  echo "Error: newVersion cannot be determined"
  exit 1
fi

if [ "$(printf '%s\n' "$newVersion" "$curVersion" | sort -V | head -n1)" = "$newVersion" ]; then
	echo "Nothing to do."
	exit 0
fi

###
### UPDATE
###
curl -Lo cockpit-subscriptions-$newVersion.tar.xz https://github.com/openSUSE/cockpit-subscriptions/releases/download/$newVersion/cockpit-subscriptions-$newVersion.tar.xz
tar -xf cockpit-subscriptions-$newVersion.tar.xz
mv cockpit-subscriptions-$newVersion/package-lock.json package-lock.json
mv cockpit-subscriptions-$newVersion/cockpit-subscriptions.spec cockpit-subscriptions.spec

git rm cockpit-subscriptions-$curVersion.tar.xz
git add cockpit-subscriptions-$newVersion.tar.xz package-lock.json cockpit-subscriptions.spec
osc service mr
