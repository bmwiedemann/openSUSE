#!/bin/sh

# cleanup everything first
rm -fr data2/voices-ogg
mkdir -p data2/voices-ogg
cd data2/voices-ogg

# Pick contents files for voices
curl -q https://gcompris.net/data2/voices-ogg/Contents -o Contents

for voice in $(awk '{print $2}' < Contents | grep ".rcc");
do 
	wget https://gcompris.net/data2/voices-ogg/$voice
done

md5sum -c Contents
if [ $? -ne 0 ];then
 echo "Contents is not valid, retry"
 exit 1
fi
cd ../../

tar -cvJf gcompris-qt-voices.tar.xz data2

# Reclean up before osc ci
rm -fr data2

wget -O LICENSE https://github.com/gcompris/GCompris-voices/raw/master/LICENSE
