#!/bin/sh
export ELECTRON_IS_DEV=0
cd XXXLIBDIRXXX/bitwarden
exec electron XXXLIBDIRXXX/bitwarden "$@"
