#!/usr/bin/bash

if [ -n "${WAYLAND_DISPLAY}" ]
then
  env -u WAYLAND_DISPLAY /usr/bin/lapce "$@"
else
  /usr/bin/lapce "$@"
fi
