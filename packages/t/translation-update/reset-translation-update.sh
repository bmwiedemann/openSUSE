#!/bin/bash
tar xvf *.bz2
find translation-update -type f -name '*.po' | xargs rm -v
tar cvjf translation-update.tar.bz2 translation-update
sed -i.bak 's|^\(%{_datadir}/locale-langpack\)|#\1|
s|^\(%dir %{_datadir}/locale-langpack\)|#\1|' *.spec
exit 0
