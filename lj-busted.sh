#!/bin/sh
set -xeu

/usr/bin/luajit /usr/bin/busted "$@"
