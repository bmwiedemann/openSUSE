#!/bin/sh

if [ "$USER" = "root" ]
then
  HELIX_RUNTIME=/usr/lib64/helix/runtime exec /usr/lib64/helix/hx "$@"
else
  mkdir -p "$HOME/.config/helix/runtime"
  exec /usr/lib64/helix/hx "$@"
fi
