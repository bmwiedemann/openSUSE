#!/bin/bash

rm -f cross*.spec cross*.changes

for arch in arm-none epiphany riscv64 rx; do
	pkgname=cross-$arch-newlib-devel
	outfile=$pkgname.spec
	echo "%define cross_arch $arch" > $outfile
	cat newlib.spec.in >> $outfile
	cp newlib.changes $pkgname.changes
done

osc service localrun format_spec_file
