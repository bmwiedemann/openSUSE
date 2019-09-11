#!bin/sh

ALL_MEDIUM_FONTS_FOR_ENITALIC="\
 batang10  batang12  batang14 batang16 batang18 batang20 batang24 \
 dotum10   dotum12   dotum14  dotum16  dotum18  dotum20  dotum24  \
 gulim10   gulim12   gulim14  gulim16  gulim18  gulim20  gulim24  \
 hline10   hline12   hline14  hline16  hline18  hline20  hline24  "            
ALL_MEDIUM_FONTS_FOR_ENBOLD="\
 dotum10 dotum12 dotum14 dotum16 dotum18 dotum20 dotum24 "
ALL_BOLD_FONTS_FOR_ENITALIC="\
 batang10b  batang12b batang14b batang16b batang18b batang20b batang24b \
 dotum10b   dotum12b  dotum14b  dotum16b  dotum18b  dotum20b  dotum24b  \
 gulim10b   gulim12b  gulim14b  gulim16b  gulim18b  gulim20b  gulim24b  "
for src in $ALL_MEDIUM_FONTS_FOR_ENITALIC ; do
 ./mkitalic ${src}.bdf > ${src}i.bdf 
done
for src in $ALL_MEDIUM_FONTS_FOR_ENBOLD ; do
  /usr/bin/perl ./mkbold ${src}.bdf > ${src}b.bdf
done
for src in $ALL_BOLD_FONTS_FOR_ENITALIC ; do
 ./mkitalic ${src}.bdf > ${src}i.bdf 
done
