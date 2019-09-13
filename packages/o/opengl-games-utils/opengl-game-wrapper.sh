#!/bin/sh -e

. /usr/share/opengl-games-utils/opengl-game-functions.sh

game=$(basename $0)
game="${game%%-wrapper*}"

checkDriOK "$game"

exec "$game" "$@"
