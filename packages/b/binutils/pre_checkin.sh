#!/bin/bash

# the script takes binutils* and creates the cross-* packages

rm -f cross-*-binutils.spec cross-*-binutils.changes

# sh4 is stuck in the testsuite
for arch in aarch64 hppa hppa64 arm i386 x86_64 s390 s390x ppc ppc64 ppc64le ia64 sparc sparc64 spu avr mips m68k epiphany rx riscv64 xtensa; do

   echo -n "Building package for $arch --> cross-$arch-binutils ..."

   ln -f binutils.changes cross-$arch-binutils.changes
   targetarch=`echo $arch | sed -e "s/parisc/hppa/;s/i.86/i586/;s/ppc/powerpc/"`
   exclarch=`echo $arch | sed -e 's/parisc/hppa/;s/i.86/%ix86/;s/arm/%arm/'`
   sed -e "s/^Name:.*binutils\$/Name:         cross-$arch-binutils\nExcludeArch: $exclarch\n%define cross 1\n%define TARGET $targetarch/;" \
       < binutils.spec > cross-$arch-binutils.spec

   echo " done."
done

osc service localrun format_spec_file

