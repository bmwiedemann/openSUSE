#
# spec file for package xorg-x11-fonts
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "converted"
%define pkgflavor -converted
%else
%define pkgflavor %{nil}
%endif

Name:           xorg-x11-fonts%{pkgflavor}
BuildRequires:  pkgconfig
URL:            http://xorg.freedesktop.org/
Version:        7.6
Release:        0
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        X.Org fonts
License:        MIT
Group:          System/X11/Fonts
Source0:        http://xorg.freedesktop.org/archive/individual/font/font-adobe-100dpi-1.0.3.tar.bz2
Source1:        http://xorg.freedesktop.org/archive/individual/font/font-adobe-75dpi-1.0.3.tar.bz2
Source2:        http://xorg.freedesktop.org/archive/individual/font/font-arabic-misc-1.0.3.tar.bz2
Source3:        http://xorg.freedesktop.org/archive/individual/font/font-bh-100dpi-1.0.3.tar.bz2
Source4:        http://xorg.freedesktop.org/archive/individual/font/font-bh-75dpi-1.0.3.tar.bz2
Source5:        http://xorg.freedesktop.org/archive/individual/font/font-bh-lucidatypewriter-100dpi-1.0.3.tar.bz2
Source6:        http://xorg.freedesktop.org/archive/individual/font/font-bh-lucidatypewriter-75dpi-1.0.3.tar.bz2
Source7:        http://xorg.freedesktop.org/archive/individual/font/font-bh-ttf-1.0.3.tar.bz2
Source8:        http://xorg.freedesktop.org/archive/individual/font/font-bh-type1-1.0.3.tar.bz2
Source9:        http://xorg.freedesktop.org/archive/individual/font/font-bitstream-100dpi-1.0.3.tar.bz2
Source10:       http://xorg.freedesktop.org/archive/individual/font/font-bitstream-75dpi-1.0.3.tar.bz2
Source12:       http://xorg.freedesktop.org/archive/individual/font/font-bitstream-type1-1.0.3.tar.bz2
Source13:       http://xorg.freedesktop.org/archive/individual/font/font-cronyx-cyrillic-1.0.3.tar.bz2
Source14:       http://xorg.freedesktop.org/archive/individual/font/font-cursor-misc-1.0.3.tar.bz2
Source15:       http://xorg.freedesktop.org/archive/individual/font/font-daewoo-misc-1.0.3.tar.bz2
Source16:       http://xorg.freedesktop.org/archive/individual/font/font-dec-misc-1.0.3.tar.bz2
Source17:       http://xorg.freedesktop.org/archive/individual/font/font-ibm-type1-1.0.3.tar.bz2
Source18:       http://xorg.freedesktop.org/archive/individual/font/font-isas-misc-1.0.3.tar.bz2
Source19:       http://xorg.freedesktop.org/archive/individual/font/font-jis-misc-1.0.3.tar.bz2
Source20:       http://xorg.freedesktop.org/archive/individual/font/font-micro-misc-1.0.3.tar.bz2
Source21:       http://xorg.freedesktop.org/archive/individual/font/font-misc-cyrillic-1.0.3.tar.bz2
Source22:       http://xorg.freedesktop.org/archive/individual/font/font-misc-ethiopic-1.0.3.tar.bz2
Source23:       http://xorg.freedesktop.org/archive/individual/font/font-misc-meltho-1.0.3.tar.bz2
Source24:       http://xorg.freedesktop.org/archive/individual/font/font-misc-misc-1.1.2.tar.bz2
Source25:       http://xorg.freedesktop.org/archive/individual/font/font-mutt-misc-1.0.3.tar.bz2
Source26:       http://xorg.freedesktop.org/archive/individual/font/font-schumacher-misc-1.1.2.tar.bz2
Source27:       http://xorg.freedesktop.org/archive/individual/font/font-screen-cyrillic-1.0.4.tar.bz2
Source28:       http://xorg.freedesktop.org/archive/individual/font/font-sony-misc-1.0.3.tar.bz2
Source29:       http://xorg.freedesktop.org/archive/individual/font/font-sun-misc-1.0.3.tar.bz2
Source30:       http://xorg.freedesktop.org/archive/individual/font/font-winitzki-cyrillic-1.0.3.tar.bz2
Source31:       http://xorg.freedesktop.org/archive/individual/font/font-xfree86-type1-1.0.4.tar.bz2
Source32:       http://xorg.freedesktop.org/archive/individual/font/encodings-1.0.5.tar.bz2
Source33:       http://xorg.freedesktop.org/archive/individual/font/font-adobe-utopia-100dpi-1.0.4.tar.bz2
Source34:       http://xorg.freedesktop.org/archive/individual/font/font-adobe-utopia-75dpi-1.0.4.tar.bz2
Source35:       http://xorg.freedesktop.org/archive/individual/font/font-adobe-utopia-type1-1.0.4.tar.bz2
Source36:       http://xorg.freedesktop.org/archive/individual/font/font-alias-1.0.3.tar.bz2
Source100:      README.converted
%if "%{flavor}" == "converted"
Source1000:     https://pwu.fedorapeople.org/fonts/convertbitmap/convertfont.py
BuildRequires:  fontpackages-devel
BuildRequires:  fonttosfnt
BuildRequires:  ftdump
BuildRequires:  ttf-converter
BuildRequires:  xorg-x11-fonts-legacy
Requires(post): fonts-config
Requires(posttrans): fonts-config
Requires(postun): fonts-config
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
# In TW and SLE 15 SP2/Leap 15.2 we have pango >= 1.44.0 which
# doesn't support Type1 fonts (boo#1169444)
Supplements:    (xorg-x11-fonts and libpango-1_0-0)
%endif
%else
# "%%{flavor}" != "converted"
BuildRequires:  bdftopcf
BuildRequires:  fontpackages-devel
BuildRequires:  mkfontscale
# ucs2any
BuildRequires:  font-util
PreReq:         fonts-config
Requires:       %{name}-core
Recommends:     %{name}-converted
Recommends:     %{name}-legacy
Provides:       xorg-x11-fonts-cyrillic
Provides:       xorg-x11-fonts-scalable
Provides:       xorg-x11-fonts-syriac
Obsoletes:      xorg-x11-fonts-cyrillic
Obsoletes:      xorg-x11-fonts-scalable
Obsoletes:      xorg-x11-fonts-syriac
%endif

%description
This package contains fonts maintained and shipped with X.Org.

%if "%{flavor}" == "converted"
This package contains the Type1 (.pfb) fonts from xorg-x11-fonts,
converted to TrueType format, so they can be used by
applications that don't support Type1 fonts.
%endif

%package core
Summary:        Core Fonts for X.Org
Group:          System/X11/Fonts
PreReq:         fonts-config
Provides:       xorg-x11:/usr/X11R6/lib/X11/fonts/misc/cursor.pcf.gz

%description core
This package contains the 'fixed' and 'cursor' font required for any X
Server.

%package legacy
Summary:        Core Fonts for X.Org
Group:          System/X11/Fonts
PreReq:         fonts-config
Requires:       xorg-x11-fonts
Provides:       xorg-x11-fonts-100dpi
Provides:       xorg-x11-fonts-75dpi
Obsoletes:      xorg-x11-fonts-100dpi
Obsoletes:      xorg-x11-fonts-75dpi

%description legacy
This package contains the original Type1 and bitmap fonts that are converted
to truetype format in the xorg-x11-fonts-converted package

%prep
%setup -n . -T -D
%if "%{flavor}" != "converted"
rm -rf $RPM_BUILD_DIR/*
for i in $RPM_SOURCE_DIR/*.tar.bz2; do tar xjf $i; done
%else
cp %{SOURCE100} .
%endif

%build
%if "%{flavor}" != "converted"
echo -e '#!/bin/sh\nexec /usr/bin/gzip -n -9 "$@"' > ../gzip ; chmod a+x ../gzip ; PATH=`pwd`/..:$PATH
for dir in encodings-* $(ls | grep -v -e encodings -e alias) font-alias-* ; do
  pushd $dir
    case $dir in
     *alias-*)     option="--with-fontrootdir=/usr/share/fonts"            ;;
     *encodings-*) option="--with-encodingsdir=/usr/share/fonts/encodings" ;;
     *100dpi-*)    option="--with-fontdir=/usr/share/fonts/100dpi"         ;;
     *75dpi-*)     option="--with-fontdir=/usr/share/fonts/75dpi"          ;;
     *type1-*)     option="--with-fontdir=/usr/share/fonts/Type1"          ;;
     *ethiopic-*)  option="--with-ttf-fontdir= --with-otf-fontdir=/usr/share/fonts/truetype" ;;
     *meltho-*)    option="--with-fontdir=/usr/share/fonts/truetype"       ;;
     *misc-*)      option="--with-fontdir=/usr/share/fonts/misc"           ;;
     *ttf-*)       option="--with-fontdir=/usr/share/fonts/truetype"       ;;
     *cyrillic-*)  option="--with-fontdir=/usr/share/fonts/cyrillic"       ;;
     *)            option=""                                               ;;
    esac
    #autoreconf -fi
    ./configure CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
                --prefix=/usr --libdir=%{_libdir} \
                --mandir=%{_mandir} ${option}
  popd
done

%else
# "%%{flavor}" == "converted"
cp %{S:1000} .
ttf-converter --input-dir /usr/share/fonts/Type1/ --output-dir generated
cd generated
python3 ../convertfont.py /usr/share/fonts/75dpi/*.pcf.gz /usr/share/fonts/100dpi/*.pcf.gz
python3 ../convertfont.py /usr/share/fonts/misc/arabic24.pcf.gz /usr/share/fonts/misc/cu[^r]*.pcf.gz /usr/share/fonts/misc/cl*.pcf.gz /usr/share/fonts/misc/[dghjo]*.pcf.gz

# Luxi Mono, Luxi Sans and Luxi Serif are already distributed in ttf format
rm Luxi*.ttf

# Bitstream-Terminal and DEC-Terminal are not converted correctly so we better remove them
rm Bitstream-Terminal*.otb
rm DEC-Terminal*.otb
%endif

%install
%if "%{flavor}" != "converted"
for dir in encodings-* $(ls | grep -v -e encodings -e alias) font-alias-* ; do
    case $dir in
	*misc-cyrillic-*) option='FONT_FILES=koi12x24b koi12x24 koi6x13b koi7x14b koi8x16b koi8x16 koi9x15b koi9x18b';;
	*)                option='NOOPT=' ;;
    esac
    make -C $dir install DESTDIR=$RPM_BUILD_ROOT "${option}"
done
rm -f $RPM_BUILD_ROOT/usr/share/fonts/*/fonts.cache*
pushd $RPM_BUILD_ROOT
find usr/share/fonts/75dpi -type f -iname \*.pcf.gz | sed 's+^usr+/usr+g' | \
  grep -v -e ISO8859 >> $RPM_BUILD_DIR/files.%{name}-core
popd
rm -rf $RPM_BUILD_ROOT/usr/etc
rm -f $RPM_BUILD_ROOT/fonts.{dir,scale}
rm -f $RPM_BUILD_ROOT/usr/share/fonts/encodings/{,large}/encodings.dir

%else
# "%%{flavor}" == "converted"
cd generated
mkdir -p %{buildroot}/%{_datadir}/fonts/truetype
cp *.ttf %{buildroot}/%{_datadir}/fonts/truetype

for filename in Adobe-Courier*.otb \
   Adobe-Helvetica*.otb \
   Adobe-New-Century-Schoolbook*.otb \
   Adobe-Symbol.otb \
   Adobe-Times*.otb \
   Adobe-Utopia*.otb \
   B\&H-LucidaBright*.otb \
   B\&H-Lucida-Sans*.otb \
   B\&H-LucidaTypewriter-Sans*.otb \
   Bitstream-Charter*.otb \
   Arabic-Newspaper.otb \
   MUTT-ClearlyU-Alternate-Glyphs-Wide.otb \
   MUTT-ClearlyU-Arabic-Extra.otb \
   MUTT-ClearlyU-Devangari-Extra.otb \
   MUTT-ClearlyU-Ligature-Wide.otb \
   MUTT-ClearlyU-PUA.otb \
   MUTT-ClearlyU-Wide.otb \
   MUTT-ClearlyU-Devanagari.otb \
   Schumacher-Clean-Bold.otb \
   Schumacher-Clean-Wide-Bold.otb \
   Schumacher-Clean-Italic.otb \
   Schumacher-Clean-Wide-Italic.otb \
   Schumacher-Clean.otb \
   Schumacher-Clean-Wide.otb \
   ISAS-Fangsong-ti-Wide.otb \
   ISAS-Song-ti-Wide.otb \
   Daewoo-Gothic-Wide.otb \
   Daewoo-Mincho-Wide.otb \
   JIS-Fixed-Wide.otb \
   Sun-OPEN-LOOK-cursor-Wide.otb \
   Sun-OPEN-LOOK-glyph-Wide.otb \
   Sun-OPEN-LOOK-glyph.otb ; do
    cp "$filename"  %{buildroot}/%{_datadir}/fonts/truetype
done

%endif

%clean
rm -rf "$RPM_BUILD_ROOT"

# %%post scriptlets
%reconfigure_fonts_scriptlets

%if "%{flavor}" != "converted"
%reconfigure_fonts_scriptlets -n xorg-x11-fonts-core
%reconfigure_fonts_scriptlets -n xorg-x11-fonts-legacy

%files
%defattr(-,root,root)
%dir /usr/share/fonts/Type1
%dir /usr/share/fonts/cyrillic
%dir /usr/share/fonts/truetype
%ghost /usr/share/fonts/Type1/encodings.dir
%ghost /usr/share/fonts/Type1/fonts.dir
%ghost /usr/share/fonts/Type1/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/Type1/.fonts-config-timestamp
%ghost /usr/share/fonts/cyrillic/encodings.dir
%ghost /usr/share/fonts/cyrillic/fonts.dir
%ghost /usr/share/fonts/cyrillic/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/cyrillic/.fonts-config-timestamp
/usr/share/fonts/cyrillic/fonts.alias
/usr/share/fonts/cyrillic/*.pcf.gz
%ghost /usr/share/fonts/truetype/encodings.dir
%ghost /usr/share/fonts/truetype/fonts.dir
%ghost /usr/share/fonts/truetype/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/truetype/.fonts-config-timestamp
/usr/share/fonts/truetype/*.otf
/usr/share/fonts/truetype/*.ttf

%files core
%defattr(-,root,root)
%dir /usr/share/fonts/misc
%dir /usr/share/fonts/encodings
%dir /usr/share/fonts/encodings/large
/usr/share/fonts/encodings/*.enc.gz
/usr/share/fonts/encodings/large/*.enc.gz
%ghost /usr/share/fonts/misc/encodings.dir
%ghost /usr/share/fonts/misc/fonts.dir
%ghost /usr/share/fonts/misc/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/misc/.fonts-config-timestamp
/usr/share/fonts/misc/fonts.alias
/usr/share/fonts/misc/[1-9k]*.pcf.gz
/usr/share/fonts/misc/cursor.pcf.gz
/usr/share/fonts/misc/micro.pcf.gz
/usr/share/fonts/misc/nil2.pcf.gz

%files legacy -f files.%{name}-core
%dir /usr/share/fonts/75dpi
%ghost /usr/share/fonts/75dpi/encodings.dir
%ghost /usr/share/fonts/75dpi/fonts.dir
%ghost /usr/share/fonts/75dpi/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/75dpi/.fonts-config-timestamp
%dir /usr/share/fonts/100dpi
%ghost /usr/share/fonts/100dpi/encodings.dir
%ghost /usr/share/fonts/100dpi/fonts.dir
%ghost /usr/share/fonts/100dpi/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/100dpi/.fonts-config-timestamp
/usr/share/fonts/75dpi/fonts.alias
/usr/share/fonts/75dpi/*-ISO8859-*.pcf.gz
/usr/share/fonts/100dpi/fonts.alias
/usr/share/fonts/100dpi/*.pcf.gz
/usr/share/fonts/misc/arabic24.pcf.gz
/usr/share/fonts/misc/cu[^r]*.pcf.gz
/usr/share/fonts/misc/cl*.pcf.gz
/usr/share/fonts/misc/[dghjo]*.pcf.gz
/usr/share/fonts/Type1/*.afm
/usr/share/fonts/Type1/*.pfa
/usr/share/fonts/Type1/*.pfb

%else
# "%%{flavor}" == "converted"
%files
%defattr(-,root,root)
%doc README.converted
%dir %{_datadir}/fonts/truetype
%{_datadir}/fonts/truetype/CharterBT-*.ttf
%{_datadir}/fonts/truetype/Courier10PitchBT-*.ttf
%{_datadir}/fonts/truetype/Courier-*.ttf
%{_datadir}/fonts/truetype/Courier.ttf
%{_datadir}/fonts/truetype/Cursor.ttf
%{_datadir}/fonts/truetype/Utopia-*.ttf
%{_datadir}/fonts/truetype/B&H-LucidaTypewriter*.otb
%{_datadir}/fonts/truetype/Adobe-Courier*.otb
%{_datadir}/fonts/truetype/Adobe-Helvetica*.otb
%{_datadir}/fonts/truetype/Adobe-New-Century-Schoolbook*.otb
%{_datadir}/fonts/truetype/Adobe-Symbol.otb
%{_datadir}/fonts/truetype/Adobe-Times*.otb
%{_datadir}/fonts/truetype/Adobe-Utopia*.otb
%{_datadir}/fonts/truetype/B&H-LucidaBright*.otb
%{_datadir}/fonts/truetype/B&H-Lucida-Sans*.otb
%{_datadir}/fonts/truetype/B&H-LucidaTypewriter-Sans*.otb
%{_datadir}/fonts/truetype/Bitstream-Charter*.otb
%{_datadir}/fonts/truetype/Arabic-Newspaper.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Alternate-Glyphs-Wide.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Arabic-Extra.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Devangari-Extra.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Ligature-Wide.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-PUA.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Wide.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Devanagari.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Bold.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Wide-Bold.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Italic.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Wide-Italic.otb
%{_datadir}/fonts/truetype/Schumacher-Clean.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Wide.otb
%{_datadir}/fonts/truetype/ISAS-Fangsong-ti-Wide.otb
%{_datadir}/fonts/truetype/ISAS-Song-ti-Wide.otb
%{_datadir}/fonts/truetype/Daewoo-Gothic-Wide.otb
%{_datadir}/fonts/truetype/Daewoo-Mincho-Wide.otb
%{_datadir}/fonts/truetype/JIS-Fixed-Wide.otb
%{_datadir}/fonts/truetype/Sun-OPEN-LOOK-cursor-Wide.otb
%{_datadir}/fonts/truetype/Sun-OPEN-LOOK-glyph-Wide.otb
%{_datadir}/fonts/truetype/Sun-OPEN-LOOK-glyph.otb
%endif

%changelog
