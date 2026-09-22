#!/usr/bin/bash
#
# sudo zypper in osc obs-service-cargo
#

f=android-tools-37.0.0

rm -rf ${f}
tar xf ${f}.tar.xz
patch -p1 -d ${f} -i ../fix-rust-based-mDNS-backend.patch
mv -v ${f}.tar.xz ${f}.tar.xz.org
tar cfJ ${f}.tar.xz ${f}
rm -rf ${f}
osc service manualrun cargo_vendor
rm -v ${f}.tar.xz
mv -v ${f}.tar.xz.org ${f}.tar.xz
