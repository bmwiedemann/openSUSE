#!/bin/sh

for i in gimp-gap*.tar.bz2 ; do
   case $i in *patched*) continue ;; esac
   test -f ${i//.tar./-patched.tar.} && continue
   bash gimp-gap-patch-source.sh $i
done
