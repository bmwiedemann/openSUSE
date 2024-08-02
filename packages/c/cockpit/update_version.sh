#!/usr/bin/bash

set -e

curVersion=$(grep Version: cockpit.spec | sed -e 's,^\(\s*Version:\s*\)\(.*\)\s*$,\2,')

if [[ ! "$curVersion" =~ ^[0-9]+$ ]]; then
  echo "Error: curVersion is not a valid integer"
  exit 1
fi

###
### Fetch latest soruces
###

# fetch latest theme
if [ ! -d cockpit-suse-theme ]; then
    git clone https://github.com/dgdavid/cockpit-suse-theme.git
else
	git -C cockpit-suse-theme pull --ff-only
fi
git -C cockpit-suse-theme archive --format=tar --prefix=cockpit-suse-theme/ -o ../cockpit-suse-theme.tar HEAD

# fetch latest cockpit
if [ ! -d cockpit ]; then
	git clone https://github.com/cockpit-project/cockpit.git cockpit
else
    git -C cockpit checkout main
	git -C cockpit fetch
fi

newVersion=$(git -C cockpit tag | grep '^[0-9.]\+$' | sort -rn | head -1)

echo "Current version: $curVersion"
echo "    New version: $newVersion"

if [ "$curVersion" -ge "$newVersion" ]; then
	echo "Nothing to do."
	exit 0
fi

###
### UPDATE
###
# # initialize all submodules
git -C cockpit checkout $newVersion
git -C cockpit submodule update --init --depth 1
diff cockpit/node_modules/.package.json cockpit/package.json
cp cockpit/node_modules/.package-lock.json package-lock.json

# update node_modules
osc service mr

# remove node_modules and tests
git -C cockpit submodule deinit node_modules test/reference

# update tarballs
CockpitPath="cockpit-$newVersion/"
MainTarball="cockpit.tar"
D=$PWD

git -C cockpit archive --format=tar --prefix=$CockpitPath -o "$D/$MainTarball" $newVersion

# append each initialized submodule
git -C cockpit submodule foreach "n=\$(basename \$sm_path)
git archive --format=tar --prefix=${CockpitPath}\${sm_path}/ -o \"$D/\$n.tar\" HEAD
"
SubmoduleTarballs=$(git -C cockpit submodule foreach --quiet "echo \$(basename \$sm_path.tar)")

# need to unpack and pack again, because OBS can't deal with concatenated tarballs :(
rm -f "cockpit-$newVersion.tar"
rm -rf cockpit-$newVersion/
for i in $MainTarball $SubmoduleTarballs; do
	tar xf $i
done
rm $MainTarball $SubmoduleTarballs
tar zcf cockpit-$newVersion.tar.gz cockpit-$newVersion/

echo "Archive created: cockpit-$newVersion.tar"

# Update spec file
git -C cockpit remote show suse || git -C cockpit remote add suse git@github.com:openSUSE/cockpit.git
git -C cockpit fetch suse opensuse-$curVersion
git -C cockpit checkout -b opensuse-$newVersion suse/opensuse-$curVersion
git -C cockpit rebase -i $newVersion

echo "Don't forget to:"
echo "  1. finish rebase"
echo "  2. push new branch"
echo "  3. update cockpit.spec, and"
echo "  4. set new default branch on GitHub"

# Updating version in spec file
sed -i -e "s,^\(\s*Version:\s*\)\(.*\)\s*$,\1${newVersion}," cockpit/tools/cockpit.spec

