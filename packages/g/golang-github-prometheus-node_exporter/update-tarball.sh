#!/bin/bash

set -x

if ! command -V go;
then
    echo "ERROR: could not find go binary"
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
REPO_NAME="node_exporter"
REPO="https://github.com/prometheus/$REPO_NAME"
REV="v0.18.1"


cd $WORK_DIR
git clone "$REPO"
cd "$REPO_NAME"
git checkout $REV
VERSION="$(git describe)"
echo "Getting dependencies...might take a while"
go mod vendor
cd $PKG_DIR
tar -C "$WORK_DIR/$REPO_NAME/.." -cJf node_exporter-$VERSION.tar.xz \
    $REPO_NAME/node_exporter.go $REPO_NAME/go.mod $REPO_NAME/go.sum \
    $REPO_NAME/collector $REPO_NAME/vendor $REPO_NAME/Makefile \
    $REPO_NAME/Makefile.common $REPO_NAME/LICENSE $REPO_NAME/README.md \
    $REPO_NAME/ttar
# sed -i "s/^Version:.*/Version:       $VERSION/" golang-github-prometheus-node_exporter.spec
