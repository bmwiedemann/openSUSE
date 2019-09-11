#!/bin/bash

set -ex

if ! command -V go;
then
    echo "ERROR: could not find go binary"
    exit 1
fi

if ! command -V dep;
then
    echo "ERROR: could not find dep binary"
    exit 1
fi

if ! command -V git;
then
    echo "ERROR: could not find git binary"
    exit 1
fi

WORK_DIR=$(mktemp -d -t)
function clean_up {
    echo "cleaning up..."
    rm -rf $WORK_DIR
}
trap clean_up EXIT SIGINT SIGTERM

PKG_DIR=$(pwd)
function on_err {
    echo "ERROR: previous command has failed"
    echo "Removing archive."
    rm -f $PKG_DIR/rook-$VERSION.tar.xz
    rm -f $PKG_DIR/rook-$VERSION-vendor.tar.xz
}
trap on_err ERR

ROOK_REPO="github.com/SUSE/rook"
REV="suse-master"

GOPATH=$WORK_DIR
GOPATH_ROOK="$GOPATH/src/github.com/rook/rook"

# For dep to get dependencies correctly, git repos must be located in their upstream locations in
# the GOPATH. i.e., we have to clone SUSE/rook to github.com/rook/rook
mkdir --parents $GOPATH_ROOK
git -C $GOPATH_ROOK/.. clone https://$ROOK_REPO.git

cd "$GOPATH_ROOK"
git checkout $REV

#RELEASE should be from git describe when history would be correct
RELEASE="$(cut -d '-' -f1 <<< $(git describe --long))"
RELEASE="v1.0.0"
GIT_COMMIT_NUM="$(cut -d '-' -f2 <<< $(git describe --long))"
GIT_COMMIT="$(cut -d '-' -f3 <<< $(git describe --long))"

VERSION="${RELEASE:1}+git$GIT_COMMIT_NUM.$GIT_COMMIT"

# make primary source tarball before changing anything in the repo
cd $PKG_DIR
tar -C "$GOPATH_ROOK/.." -cJf rook-$VERSION.tar.xz rook/

# make vendor tarball
cd "$GOPATH_ROOK"

echo "Getting dependencies...might take a while"
GOPATH=$WORK_DIR make vendor

cd $PKG_DIR
tar -C "$GOPATH_ROOK/.." -cJf rook-$VERSION-vendor.tar.xz rook/vendor


# update spec file versions
sed -i "s/^Version:.*/Version:       $VERSION/" rook.spec
sed -i "s/^rook_container_version=.*/rook_container_version='${RELEASE:1}.$GIT_COMMIT_NUM'  # this is udpated by update-tarball.sh/" rook.spec
