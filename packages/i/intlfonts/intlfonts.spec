#
# spec file for package intlfonts
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           intlfonts
Version:        1.2.1
Release:        0
Summary:        Documentation for the International Fonts
License:        HPND and SUSE-Redistributable-Content and SUSE-Public-Domain
Group:          System/X11/Fonts
Url:            ftp://ftp.gnu.org/gnu/intlfonts/
Source0:        intlfonts-1.2.1.tar.bz2
Source1:        gulim24.bdf.bz2
Source2:        fonts.scale.intlfonts-ttf
Source3:        efont-iso8859-15.tar.bz2
BuildRequires:  fontpackages-devel
Patch0:         intlfonts-1.2.dif
%if 0%{?suse_version} >= 1220
BuildRequires:  bdftopcf
%else
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-devel
%endif
BuildRequires:  freetype2
%define	type1_fontdir   %{_fontsdir}/Type1
%define bdf_fontdir     %{_fontsdir}/bdf
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       intlfnts = %{version}
Obsoletes:      intlfnts <= 1.2.1

%description
This package contains the READMEs for international fonts from the
following packages:

intlfonts-arabic-bitmap-fonts: Arab fonts for X11

intlfonts-asian-bitmap-fonts: Asian fonts for X11

intlfonts-chinese-bitmap-fonts: Chinese fonts for X11

intlfonts-chinese-big-bitmap-fonts: Big Chinese fonts for X11

intlfonts-ethiopic-bitmap-fonts: Ethiopic fonts for X11

intlfonts-euro-bitmap-fonts: European fonts for X11

intlfonts-japanese-bitmap-fonts: Japanese fonts for X11

intlfonts-japanese-big-bitmap-fonts: Big Japanese fonts for X11

intlfonts-phonetic-bitmap-fonts: IPA fonts for X11

intlfonts-ttf-fonts: TrueType fonts

intlfonts-type1-fonts: Type1 fonts

intlfonts-bdf-fonts: Bitmap fonts useful for printing exotic languages from
Emacs

%package     -n intlfonts-arabic-bitmap-fonts
Summary:        Arabic Fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntarab = %{version}
Provides:       locale(xorg-x11:ar)
Obsoletes:      ifntarab <= 1.2.1

%description -n intlfonts-arabic-bitmap-fonts
Arabic fonts for the X Window System.

%package     -n intlfonts-asian-bitmap-fonts
Summary:        Asian Fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntasia = %{version}
Provides:       locale(xorg-x11:km;th;vi)
Obsoletes:      ifntasia <= 1.2.1

%description -n intlfonts-asian-bitmap-fonts
Asian fonts for the X Window System.

%package     -n intlfonts-chinese-bitmap-fonts
Summary:        Chinese Fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntchia = %{version}
Provides:       locale(xorg-x11:zh)
Obsoletes:      ifntchia <= 1.2.1

%description -n intlfonts-chinese-bitmap-fonts
Chinese fonts for the X Window System.

%package     -n intlfonts-chinese-big-bitmap-fonts
Summary:        Big Chinese Fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntchib = %{version}
Provides:       locale(xorg-x11:zh)
Obsoletes:      ifntchib <= 1.2.1

%description -n intlfonts-chinese-big-bitmap-fonts
Big Chinese fonts for the X Window System.

%package     -n intlfonts-ethiopic-bitmap-fonts
Summary:        Ethiopic Fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntethi = %{version}
Provides:       locale(xorg-x11:am)
Obsoletes:      ifntethi <= 1.2.1

%description -n intlfonts-ethiopic-bitmap-fonts
Ethiopic fonts for the X Window System.

%package     -n intlfonts-euro-bitmap-fonts
Summary:        European fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifnteuro = %{version}
Provides:       locale(xorg-x11:cs;el)
Obsoletes:      ifnteuro <= 1.2.1

%description -n intlfonts-euro-bitmap-fonts
European fonts for the X Window System (ISO 8859-1, 8859-2, 8859-3,
8859-4, 8859-5/9, 8859-7, and 8859-8 together with
KOI8-1/GOST19768.74-1).

%package     -n intlfonts-japanese-bitmap-fonts
Summary:        Japanese Fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntjapa = %{version}
Provides:       locale(xorg-x11:ja)
Obsoletes:      ifntjapa <= 1.2.1

%description -n intlfonts-japanese-bitmap-fonts
Japanese fonts for the X Window System.

%package     -n intlfonts-japanese-big-bitmap-fonts
Summary:        Big Japanese Fonts for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntjapb = %{version}
Provides:       locale(xorg-x11:ja)
Obsoletes:      ifntjapb <= 1.2.1

%description -n intlfonts-japanese-big-bitmap-fonts
Big Japanese fonts for the X Window System.

%package     -n intlfonts-phonetic-bitmap-fonts
Summary:        IPA font for the X Window System
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       ifntphon = %{version}
Obsoletes:      ifntphon <= 1.2.1

%description -n intlfonts-phonetic-bitmap-fonts
The International Phonetic Alphabet font for the X Window System.

%package     -n intlfonts-ttf-fonts
Summary:        TrueType Fonts from the GNU Intlfonts Package
Group:          System/X11/Fonts
%reconfigure_fonts_prereq
Provides:       intlfonts-ttf = %{version}
Obsoletes:      intlfonts-ttf <= 1.2.1

%description  -n intlfonts-ttf-fonts
TrueType fonts from the GNU intlfonts package.

%package     -n intlfonts-bdf-fonts
Summary:        Fonts from the GNU Intlfonts Package in BDF Format
Group:          System/X11/Fonts
Provides:       intlfonts-bdf = %{version}
Obsoletes:      intlfonts-bdf <= 1.2.1

%description  -n intlfonts-bdf-fonts
Fonts from the GNU intlfonts package in the BDF format.

These fonts are useful for printing exotic languages such as Thai,
Tibetan, Vietnamese, Arabic, and more from within Emacs.

%package     -n intlfonts-type1-fonts
Summary:        Type1 Fonts from the GNU Intlfonts Package
Group:          System/X11/Fonts
%reconfigure_fonts_prereq

%description  -n intlfonts-type1-fonts
Type1 fonts from the GNU intlfonts package.

%prep
%setup -n intlfonts-1.2.1 -b 0 -a 3
%patch0
bunzip2 -c $RPM_SOURCE_DIR/gulim24.bdf.bz2 > gulim24.bdf

#
# Legal issue
#

test ! -e Asian/tib16-mule.bdf   || exit 1
test ! -e Asian/tib1c16-mule.bdf || exit 1
test ! -e Asian/tib1c24-mule.bdf || exit 1
test ! -e Asian/tib24-mule.bdf   || exit 1

%build
  set +o posix
  SUBDIRS="European Asian Chinese Japanese Ethiopic Misc"
  SUBDIRS_X="Chinese-X Japanese-X Korean-X"
  SUBDIRS_BIG="European.BIG  Chinese.BIG Japanese.BIG"
  SUBDIRS_EFONT="efont-iso8859-15"
  dirs="$SUBDIRS $SUBDIRS_BIG $SUBDIRS_EFONT"
  for b in $(find $dirs -name '*.bdf') ; do
      p=${b%%.bdf}.pcf
      test -s ${p}.gz || { bdftopcf -o ${p} $b && gzip -n -9f ${p}; }
  done

%install
  mkdir -p %{buildroot}%{_miscfontsdir}/
  set +o posix
  for f in $(find ./ -name '*.pcf.gz') ; do
      install -m 0444 $f %{buildroot}%{_miscfontsdir}/
  done
  mkdir -p %{buildroot}%{_ttfontsdir}/
  install -m 0444 TrueType/*.ttf %{buildroot}%{_ttfontsdir}/
  install -m 0444 $RPM_SOURCE_DIR/fonts.scale.intlfonts-ttf %{buildroot}%{_ttfontsdir}/
  mkdir -p %{buildroot}%{type1_fontdir}/
  install -m 0444 Type1/*.[ap]f? %{buildroot}%{type1_fontdir}/
  mkdir -p %{buildroot}%{bdf_fontdir}/
  for f in \
	lt1-24-etl lt1-16b-etl lt1-16i-etl lt1-16bi-etl lt1-24-etl lt1-16b-etl \
	lt1-16i-etl lt1-16bi-etl lt2-24-etl lt3-24-etl lt4-24-etl thai24 \
	grk24-etl heb24-etl 12x24rk 12x24rk cyr24-etl lt5-24-etl jiskan24 \
	gb24st jiskan24 gulim24 jksp40 cns1-40 cns2-40 taipei24 taipei24 \
	sish24-etl ipa24-etl visc24-etl visc24-etl arab24-0-etl arab24-1-etl \
	lao24-mule arab24-2-etl ind1c24-mule \
	ethio24f-uni cns3-40 cns4-40 cns5-40 cns6-40 cns7-40 ind24-mule
  do
      install -m 0444 `find . -name $f.bdf` %{buildroot}%{bdf_fontdir}
  done
  # install documents
  mkdir   -m 0755 -p %{buildroot}%{_defaultdocdir}/intlfonts
  find . -name 'README*' | while read i; do
    mkdir -p %{buildroot}%{_defaultdocdir}/intlfonts/${i%/*}
    install -m 0444 $i %{buildroot}%{_defaultdocdir}/intlfonts/${i%/*}
  done
  cp -a %{buildroot}%{_defaultdocdir}/intlfonts/Misc \
        %{buildroot}%{_defaultdocdir}/intlfonts/Arabic

%reconfigure_fonts_scriptlets -n intlfonts-arabic-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-asian-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-chinese-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-chinese-big-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-ethiopic-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-euro-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-japanese-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-japanese-big-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-phonetic-bitmap-fonts

%reconfigure_fonts_scriptlets -n intlfonts-ttf-fonts -c

%reconfigure_fonts_scriptlets -n intlfonts-type1-fonts -c

%files
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/README*

%files -n intlfonts-arabic-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Arabic
%dir %{_miscfontsdir}/
%{_miscfontsdir}/arab16-0-etl.pcf.gz
%{_miscfontsdir}/arab16-1-etl.pcf.gz
%{_miscfontsdir}/arab16-2-etl.pcf.gz
%{_miscfontsdir}/arab24-0-etl.pcf.gz
%{_miscfontsdir}/arab24-1-etl.pcf.gz
%{_miscfontsdir}/arab24-2-etl.pcf.gz

%files -n intlfonts-asian-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Asian
%dir %{_miscfontsdir}/
%{_miscfontsdir}/ind16-mule.pcf.gz
%{_miscfontsdir}/ind16-uni.pcf.gz
%{_miscfontsdir}/ind1c16-mule.pcf.gz
%{_miscfontsdir}/ind1c24-mule.pcf.gz
%{_miscfontsdir}/ind24-mule.pcf.gz
%{_miscfontsdir}/ind24-uni.pcf.gz
%{_miscfontsdir}/isci16-mule.pcf.gz
%{_miscfontsdir}/isci24-mule.pcf.gz
%{_miscfontsdir}/lao14-mule.pcf.gz
%{_miscfontsdir}/lao16-mule.pcf.gz
%{_miscfontsdir}/lao18-mule.pcf.gz
%{_miscfontsdir}/lao18b-mule.pcf.gz
%{_miscfontsdir}/lao18i-mule.pcf.gz
%{_miscfontsdir}/lao24-mule.pcf.gz
%{_miscfontsdir}/thai14.pcf.gz
%{_miscfontsdir}/thai16.pcf.gz
%{_miscfontsdir}/thai18.pcf.gz
%{_miscfontsdir}/thai18b.pcf.gz
%{_miscfontsdir}/thai18bi.pcf.gz
%{_miscfontsdir}/thai18i.pcf.gz
%{_miscfontsdir}/thai24.pcf.gz
%{_miscfontsdir}/visc16-etl.pcf.gz
%{_miscfontsdir}/visc18-etl.pcf.gz
%{_miscfontsdir}/visc18b-etl.pcf.gz
%{_miscfontsdir}/visc18bi-etl.pcf.gz
%{_miscfontsdir}/visc18i-etl.pcf.gz
%{_miscfontsdir}/visc24-etl.pcf.gz
%{_miscfontsdir}/xtis18.pcf.gz
%{_miscfontsdir}/xtis24.pcf.gz

%files -n intlfonts-chinese-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Chinese
%dir %{_miscfontsdir}/
%{_miscfontsdir}/cns1-16.pcf.gz
%{_miscfontsdir}/cns1-24.pcf.gz
%{_miscfontsdir}/cns2-16.pcf.gz
%{_miscfontsdir}/cns2-24.pcf.gz
%{_miscfontsdir}/cns3-16.pcf.gz
%{_miscfontsdir}/cns3-24.pcf.gz
%{_miscfontsdir}/cns4-16.pcf.gz
%{_miscfontsdir}/cns4-24.pcf.gz
%{_miscfontsdir}/cns5-16.pcf.gz
%{_miscfontsdir}/cns5-24.pcf.gz
%{_miscfontsdir}/cns6-16.pcf.gz
%{_miscfontsdir}/cns6-24.pcf.gz
%{_miscfontsdir}/cns7-16.pcf.gz
%{_miscfontsdir}/cns7-24.pcf.gz
%{_miscfontsdir}/guob16.pcf.gz
%{_miscfontsdir}/sish14-etl.pcf.gz
%{_miscfontsdir}/sish16-etl.pcf.gz
%{_miscfontsdir}/sish24-etl.pcf.gz
%{_miscfontsdir}/taipei16.pcf.gz
%{_miscfontsdir}/taipei24.pcf.gz

%files -n intlfonts-chinese-big-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Chinese.BIG
%dir %{_miscfontsdir}/
%{_miscfontsdir}/cc40s.pcf.gz
%{_miscfontsdir}/cc48s.pcf.gz
%{_miscfontsdir}/cns1-40.pcf.gz
%{_miscfontsdir}/cns2-40.pcf.gz
%{_miscfontsdir}/cns3-40.pcf.gz
%{_miscfontsdir}/cns4-40.pcf.gz
%{_miscfontsdir}/cns5-40.pcf.gz
%{_miscfontsdir}/cns6-40.pcf.gz
%{_miscfontsdir}/cns7-40.pcf.gz

%files -n intlfonts-ethiopic-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Ethiopic
%dir %{_miscfontsdir}/
%{_miscfontsdir}/ethio16f-uni.pcf.gz
%{_miscfontsdir}/ethio24f-uni.pcf.gz

%files -n intlfonts-euro-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/European
%doc %{_defaultdocdir}/intlfonts/European.BIG
%doc %{_defaultdocdir}/intlfonts/efont*
%dir %{_miscfontsdir}/
%{_miscfontsdir}/cyr14-etl.pcf.gz
%{_miscfontsdir}/cyr16-etl.pcf.gz
%{_miscfontsdir}/cyr24-etl.pcf.gz
%{_miscfontsdir}/grk14-etl.pcf.gz
%{_miscfontsdir}/grk16-etl.pcf.gz
%{_miscfontsdir}/grk24-etl.pcf.gz
%{_miscfontsdir}/koi14-etl.pcf.gz
%{_miscfontsdir}/koi16-etl.pcf.gz
%{_miscfontsdir}/koi24-etl.pcf.gz
%{_miscfontsdir}/lt1-14-etl.pcf.gz
%{_miscfontsdir}/lt1-16-etl.pcf.gz
%{_miscfontsdir}/lt1-16b-etl.pcf.gz
%{_miscfontsdir}/lt1-16bi-etl.pcf.gz
%{_miscfontsdir}/lt1-16i-etl.pcf.gz
%{_miscfontsdir}/lt1-18-etl.pcf.gz
%{_miscfontsdir}/lt1-18.pcf.gz
%{_miscfontsdir}/lt1-18b-etl.pcf.gz
%{_miscfontsdir}/lt1-18bi-etl.pcf.gz
%{_miscfontsdir}/lt1-18i-etl.pcf.gz
%{_miscfontsdir}/lt1-24-etl.pcf.gz
%{_miscfontsdir}/lt1-24b-etl.pcf.gz
%{_miscfontsdir}/lt1-24bi-etl.pcf.gz
%{_miscfontsdir}/lt1-24i-etl.pcf.gz
%{_miscfontsdir}/lt2-14-etl.pcf.gz
%{_miscfontsdir}/lt2-16-etl.pcf.gz
%{_miscfontsdir}/lt2-24-etl.pcf.gz
%{_miscfontsdir}/lt3-14-etl.pcf.gz
%{_miscfontsdir}/lt3-16-etl.pcf.gz
%{_miscfontsdir}/lt3-24-etl.pcf.gz
%{_miscfontsdir}/lt4-14-etl.pcf.gz
%{_miscfontsdir}/lt4-16-etl.pcf.gz
%{_miscfontsdir}/lt4-24-etl.pcf.gz
%{_miscfontsdir}/lt5-14-etl.pcf.gz
%{_miscfontsdir}/lt5-16-etl.pcf.gz
%{_miscfontsdir}/lt5-24-etl.pcf.gz
%{_miscfontsdir}/heb14-etl.pcf.gz
%{_miscfontsdir}/heb16-etl.pcf.gz
%{_miscfontsdir}/heb24-etl.pcf.gz
%{_miscfontsdir}/bmp16-etl.pcf.gz
%{_miscfontsdir}/lt1-40-etl.pcf.gz
%{_miscfontsdir}/h16-iso8859-15.pcf.gz
%{_miscfontsdir}/h16_b-iso8859-15.pcf.gz
%{_miscfontsdir}/h16_bi-iso8859-15.pcf.gz
%{_miscfontsdir}/h16_i-iso8859-15.pcf.gz
%{_miscfontsdir}/h24-iso8859-15.pcf.gz
%{_miscfontsdir}/h24_b-iso8859-15.pcf.gz
%{_miscfontsdir}/h24_bi-iso8859-15.pcf.gz
%{_miscfontsdir}/h24_i-iso8859-15.pcf.gz

%files -n intlfonts-japanese-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Japanese
%dir %{_miscfontsdir}/
%{_miscfontsdir}/a18rk.pcf.gz
%{_miscfontsdir}/a18rkb.pcf.gz
%{_miscfontsdir}/a18rki.pcf.gz
%{_miscfontsdir}/j78-16.pcf.gz
%{_miscfontsdir}/j83-18.pcf.gz
%{_miscfontsdir}/j83-18b.pcf.gz
%{_miscfontsdir}/j83-18i.pcf.gz
%{_miscfontsdir}/j90-16.pcf.gz
%{_miscfontsdir}/jksp16.pcf.gz
%{_miscfontsdir}/jksp24.pcf.gz

%files -n intlfonts-japanese-big-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Japanese.BIG
%dir %{_miscfontsdir}/
%{_miscfontsdir}/jiskan32.pcf.gz
%{_miscfontsdir}/jiskan48.pcf.gz
%{_miscfontsdir}/jksp40.pcf.gz

%files -n intlfonts-phonetic-bitmap-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Misc
%dir %{_miscfontsdir}/
%{_miscfontsdir}/ipa14-etl.pcf.gz
%{_miscfontsdir}/ipa16-etl.pcf.gz
%{_miscfontsdir}/ipa24-etl.pcf.gz

%files -n intlfonts-ttf-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/TrueType
%dir %{_ttfontsdir}/
%config %{_ttfontsdir}/fonts.scale.intlfonts-ttf
%{_ttfontsdir}/*.ttf

%files -n intlfonts-type1-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/Type1
%{type1_fontdir}

%files -n intlfonts-bdf-fonts
%defattr(-,root,root)
%dir %{_defaultdocdir}/intlfonts
%doc %{_defaultdocdir}/intlfonts/*.X
%{bdf_fontdir}

%changelog
