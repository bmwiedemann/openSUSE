#!/bin/sh

if [ -w /sysroot/etc/udev/rules.d ]; then
  # chzdev generated device activation starts with 41 ...
  cp -p /etc/udev/rules.d/41-* /sysroot/etc/udev/rules.d
fi
