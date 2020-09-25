#!/bin/bash

CLONE_NAME="SafeEyes"
LATEST_RELEASE="2.0.9"

if [ -d $CLONE_NAME/.git ]; then
	cd $CLONE_NAME
	git pull
	cd ..
else
	set -e
	git clone https://github.com/slgobinath/SafeEyes.git $CLONE_NAME
	set +e
fi

TOPDIR=$(pwd)
cd $CLONE_NAME
git config tar.tar.xz.command "xz -c"
LINE=$(git show --format=format:"%h %ai"|head -n 1)
set -- $LINE
REV=$1
DATE=$2
VER=${DATE//-/}
set -e
echo "Creating git archive ..."
git archive --format=tar.xz --prefix=$CLONE_NAME-${LATEST_RELEASE}+git${VER}/ -o $TOPDIR/$CLONE_NAME-${LATEST_RELEASE}+git${VER}.tar.xz master
cd $TOPDIR
echo $VER
echo $REV
#osc rm -f $CLONE_NAME-*.tar.xz || true
osc add $CLONE_NAME-${LATEST_RELEASE}+git${VER}.tar.xz
sed -i "s/^Version:.*/Version:        ${LATEST_RELEASE}+git${VER}/" $CLONE_NAME.spec
osc vc -m "Update to version $REV ($DATE):"
