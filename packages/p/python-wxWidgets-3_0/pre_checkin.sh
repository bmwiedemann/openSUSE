#!/bin/sh

for i in wxPython-src-*.tar.bz2; do
	bash extract-source.sh "$i"
done
