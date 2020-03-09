#!/bin/sh

rm -rf kube-prometheus
osc service ra
cd kube-prometheus
go get github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb
~/go/bin/jb update
cd vendor
rm kube-prometheus
ln -sf ../jsonnet/kube-prometheus .
cd ..
tar --owner root --group root -cJf ../vendor.tar.xz jsonnetfile.lock.json vendor
cd ..
