#!/bin/sh
# download dictionaries du jour
for i in JMdict edict edict2u enamdict kanjidic2.xml kanjidic \
    kanjd212 kanjd213u kradfile radkfile; do
	wget -O "$i.gz" "http://ftp.edrdg.org/pub/Nihongo/$i.gz"
done
