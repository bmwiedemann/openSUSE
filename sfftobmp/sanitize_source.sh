#!/bin/sh -ex

url=$(pcregrep -Po 'svn://\S+' sfftobmp.spec)
tail="${url##*/}"
svn co "$url"
rm -Rf "$tail/win32"

