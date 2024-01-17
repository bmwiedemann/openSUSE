#!/bin/bash

. /usr/share/opengl-games-utils/opengl-game-functions.sh

GAME=`basename $0 | sed 's/-wrapper.*//'`

checkDriOK $GAME

exec $GAME "$@"
