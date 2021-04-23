#!/bin/sh

if [ -z $1 ]; then
    echo Usage: download-dic.sh YYYYMMDD
    exit 1;
fi

dest=skkdic-$1
rm -r $dest
# wget -c -r -np -k -L -p http://openlab.ring.gr.jp/skk/skk/dic/
mkdir -p $dest
find openlab.ring.gr.jp/skk/skk/dic -name "SKK-JISYO.*" -exec cp {} $dest \;

# remove dictionaries that cannot be packaged
rm -f $dest/dic/SKK-JISYO.edict

mkdir -p $dest/READMEs
cp openlab.ring.gr.jp/skk/skk/dic/READMEs/committers.txt $dest/READMEs
cp openlab.ring.gr.jp/skk/skk/dic/ChangeLog* $dest

tar cvJf skkdic-$1.tar.xz $dest
