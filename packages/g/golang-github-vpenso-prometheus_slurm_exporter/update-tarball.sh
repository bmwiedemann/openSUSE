#!/bin/bash

set -x

PKG_DIR=$(pwd)
REPO_NAME="prometheus-slurm-exporter"
GIT_REPO="https://github.com/vpenso/prometheus-slurm-exporter"
REV="0.8"
DIR_NAME="$REPO_NAME"-"$REV"

command -v go >/dev/null 2>&1 || { echo >&2 "The script requires 'go' but it's not installed.  Aborting."; exit 1; }
command -v git >/dev/null 2>&1 || { echo >&2 "The script requires 'git' but it's not installed.  Aborting."; exit 1; }

WORK_DIR=$(mktemp -d -t)

cd $WORK_DIR
git clone "$GIT_REPO"  "$DIR_NAME"
cd "$DIR_NAME"
git checkout "$REV"
rm -rf .git
cp $PKG_DIR/go.mod "$WORK_DIR"/"$DIR_NAME"

##echo "Getting dependencies...might take a while"
##go mod vendor

cd $PKG_DIR
tar -C "$WORK_DIR/$DIR_NAME/.." -czf "$DIR_NAME".tar.gz \
    "$DIR_NAME"

