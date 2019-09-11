#!/bin/bash

set -ex

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
    rm -f $PKG_DIR/ceph-csi-$VERSION.tar.xz
}
trap on_err ERR

ROOK_REPO="github.com/ceph/ceph-csi"
REV="release-v1.1.0"

GOPATH=$WORK_DIR
GOPATH_CEPHCSI="$GOPATH/src/github.com/ceph/ceph-csi"

# For dep to get dependencies correctly, git repos must be located in their upstream locations in
# the GOPATH. i.e., we have to clone SUSE/rook to github.com/rook/rook
mkdir --parents $GOPATH_CEPHCSI
git -C $GOPATH_CEPHCSI/.. clone https://$ROOK_REPO.git

cd "$GOPATH_CEPHCSI"
git checkout $REV

#get version from the tag in the repo
RELEASE="$(cut -d '-' -f1 <<< $(git describe --tags --long))"
GIT_COMMIT_NUM="$(cut -d '-' -f2 <<< $(git describe --tags --long))"
GIT_COMMIT="$(cut -d '-' -f3 <<< $(git describe --tags --long))"

VERSION="${RELEASE:1}+git$GIT_COMMIT_NUM.$GIT_COMMIT"


cd $PKG_DIR
tar -C "$GOPATH_CEPHCSI/.." -cJf ceph-csi-$VERSION.tar.xz ceph-csi/

# ceph/ceph-csi already has the vendor directory versioned, so no need to use dep

# update spec file versions
sed -i "s/^Version:.*/Version:       $VERSION/" ceph-csi.spec
