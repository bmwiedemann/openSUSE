#!/bin/sh

cp qemu.changes qemu-testsuite.changes

if [ "$1" != "-q" ]; then
  echo "Note that the patch queue needs to be regenerated via update_git.sh"
  echo "before running $0."
fi
