#!/bin/sh

GAME_LOCAL_DIR=$HOME/.twind
GAME_DATA_DIR=/usr/lib/twind
GAME_EXECUTABLE=/usr/lib/twind/twind

mkdir -p $GAME_LOCAL_DIR
cd $GAME_LOCAL_DIR

for dir in graphics music sound ; do
    ln -snf $GAME_DATA_DIR/$dir $dir
done

exec $GAME_EXECUTABLE "${@}"
