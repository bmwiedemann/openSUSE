#
# spec file for package edict
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           edict
Version:        20201102
Release:        0
Summary:        The Japanese Dictionary from the EDRDG project (EDICT format)
License:        CC-BY-SA-3.0 AND CC-BY-SA-4.0
Group:          System/I18n/Japanese
URL:            http://www.edrdg.org/jmdict/edict.html
# The files change daily, so we do not include their full URL here,
# but do see download_dicts.sh.
Source:         JMdict.gz
Source2:        edict.gz
Source3:        edict2u.gz
Source4:        enamdict.gz
Source6:        kanjidic2.xml.gz
Source7:        kanjidic.gz
Source8:        kanjd212.gz
Source9:        kradfile.gz
Source10:       radkfile.gz
Source11:       kanjd213u.gz
Source97:       download_dicts.sh
Source98:       http://www.edrdg.org/edrdg/licence.html
Source99:       http://www.kanji.org/kanji/dictionaries/skip_permission.htm
BuildArch:      noarch

%description
JMdict/EDICT is a machine-readable multilingual Japanese dictionary.
It contains Japanese–English translations for over 180000 entries,
representing more than 205000 unique headword–reading combinations.

The dictionary is made available in different formats. This package
contains the "edict" variant, a flat text file format, of:

* the JMdict project's word dictionary ("edict" file)
* the KANJIDIC project's JIS X 0208-1990 Kanji dictionary (6355 Kanji)
* KANJIDIC's JIS X 0212-1990 dictionary (an extra 5801 Kanji)
* KANJIDIC's JIS X 0213-2012 dictionary (an extra 952 Kanji)
* kanji-to-radical and radical-to-kanji indices
* ENAMDICT, a dictionary for proper names

Other formats are in the edict2 and jmdict packages.

%package -n edict2
Summary:        The Japanese Dictionary from the EDRDG project (edict2 format)
Group:          System/I18n/Japanese
Provides:       locale(ja)

%description -n edict2
JMdict/EDICT is a machine-readable multilingual Japanese dictionary.
It contains Japanese–English translations for over 180000 entries,
representing more than 205000 unique headword–reading combinations.

The dictionary is made available in different formats. This package
contains the "edict2" variant, an expanded version of the flat
"edict" text format but reflecting the structure of the XML entries,
of the JMdict word dictionary.

%package -n jmdict
Summary:        The Japanese Dictionary from the EDRDG project (JMdict format)
Group:          System/I18n/Japanese
Provides:       locale(ja)

%description -n jmdict
JMdict/EDICT is a machine-readable multilingual Japanese dictionary.
It contains Japanese–English translations for over 180000 entries,
representing more than 205000 unique headword–reading combinations.

The dictionary is made available in different formats. This package
contains the XML variant of:

* the JMdict project's word dictionary ("JMdict" file)
* the KANJIDIC project's Kanji dictionary (covering JIS 0208/0212/0213;
  "kanjidic2.xml" file)

%prep 
# Make %%doc work
cp "%_sourcedir"/*.htm* .

%build

%install
# Other packages look for files predominantly here, and expect files to be UTF-8.
d="%buildroot/%_datadir/edict"
mkdir -p "$d"
pushd "%_sourcedir/"
# files already in the right encoding
for i in JMdict.gz edict2u.gz kanjd213u.gz kanjidic2.xml.gz; do
	gzip -cd "$i" >"$d/${i%.gz}"
done
# transcode some files
for i in edict.gz enamdict.gz kanjd212.gz kanjidic.gz kradfile.gz radkfile.gz; do
	gzip -cd "$i" | iconv -f euc-jp -t utf-8 >"$d/${i%.gz}"
done
popd

%files
%license licence.html skip_permission.htm
%dir %_datadir/edict/
%_datadir/edict/edict
%_datadir/edict/enamdict
%_datadir/edict/kanjd212
%_datadir/edict/kanjd213u
%_datadir/edict/kanjidic
%_datadir/edict/kradfile
%_datadir/edict/radkfile

%files -n jmdict
%license licence.html
%dir %_datadir/edict/
%_datadir/edict/JMdict
%_datadir/edict/kanjidic2.xml

%files -n edict2
%license licence.html
%dir %_datadir/edict/
%_datadir/edict/edict2u

%changelog
