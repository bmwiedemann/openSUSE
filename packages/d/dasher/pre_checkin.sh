#!/bin/sh

DEFAULT_LOCALES="en"
RECOMMENDED_LOCALES="de ru it pl es pt fr nl"
EXTRAS_LOCALES=
for locale in `grep -v ^# locale-map.txt | sed "s,.* ,,g" | sort -u`; do
  echo $DEFAULT_LOCALES $RECOMMENDED_LOCALES | grep -q $locale
  if test $? -ne 0; then
    EXTRAS_LOCALES="$EXTRAS_LOCALES $locale"
  fi
done

# Update the list of default/recommended locales in the script
sed -i "s,^DEFAULT_LOCALES=\".*$,DEFAULT_LOCALES=\"$DEFAULT_LOCALES\",;s,^RECOMMENDED_LOCALES=\".*$,RECOMMENDED_LOCALES=\"$RECOMMENDED_LOCALES\"," dasher-data-lang.sh

# Update the Provides locale(dasher:$locale) lines in spec file
RECOMMENDED_LOCALES=`echo $RECOMMENDED_LOCALES | sed "s, ,;,g"`
EXTRAS_LOCALES=`echo $EXTRAS_LOCALES | sed "s, ,;,g"`
sed "s,RECOMMENDED_LOCALES,$RECOMMENDED_LOCALES,;s,EXTRAS_LOCALES,$EXTRAS_LOCALES," dasher.spec.in > dasher.spec
