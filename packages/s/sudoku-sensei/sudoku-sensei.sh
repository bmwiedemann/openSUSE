#!/bin/sh

GAME_LOCAL_DIR=$HOME/.sudoku-sensei
GAME_DATA_DIR=/usr/lib/sudoku-sensei
GAME_EXECUTABLE=$GAME_LOCAL_DIR/SudokuSensei

mkdir -p $GAME_LOCAL_DIR
cd $GAME_LOCAL_DIR

for dir in board doc images language ; do
    ln -snf  $GAME_DATA_DIR/$dir $dir
done

for dir in saves system ; do
    cp -a $GAME_DATA_DIR/$dir $dir
done

for file in SudokuSensei SudokuSensei.rc license.txt ; do
    cp -a $GAME_DATA_DIR/$file $GAME_LOCAL_DIR
done

exec $GAME_EXECUTABLE "${@}"
