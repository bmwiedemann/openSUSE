#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
Source22:       http://xorg.freedesktop.org/archive/individual/font/font-misc-ethiopic-1.0.4.tar.bz2
Source23:       http://xorg.freedesktop.org/archive/individual/font/font-misc-meltho-1.0.3.tar.bz2
Source24:       http://xorg.freedesktop.org/archive/individual/font/font-misc-misc-1.1.2.tar.bz2
Source25:       http://xorg.freedesktop.org/archive/individual/font/font-mutt-misc-1.0.3.tar.bz2
Source26:       http://xorg.freedesktop.org/archive/individual/font/font-schumacher-misc-1.1.2.tar.bz2
Source27:       http://xorg.freedesktop.org/archive/individual/font/font-screen-cyrillic-1.0.4.tar.bz2
Source28:       http://xorg.freedesktop.org/archive/individual/font/font-sony-misc-1.0.3.tar.bz2
Source29:       http://xorg.freedesktop.org/archive/individual/font/font-sun-misc-1.0.3.tar.bz2
Source30:       http://xorg.freedesktop.org/archive/individual/font/font-winitzki-cyrillic-1.0.3.tar.bz2
Source31:       http://xorg.freedesktop.org/archive/individual/font/font-xfree86-type1-1.0.4.tar.bz2
Source32:       http://xorg.freedesktop.org/archive/individual/font/encodings-1.0.6.tar.xz
Source33:       http://xorg.freedesktop.org/archive/individual/font/font-adobe-utopia-100dpi-1.0.4.tar.bz2
Source34:       http://xorg.freedesktop.org/archive/individual/font/font-adobe-utopia-75dpi-1.0.4.tar.bz2
Source35:       http://xorg.freedesktop.org/archive/individual/font/font-adobe-utopia-type1-1.0.4.tar.bz2
Source36:       http://xorg.freedesktop.org/archive/individual/font/font-alias-1.0.4.tar.bz2
Source100:      README.converted
%if "%{flavor}" == "converted"
Source1000:     https://pwu.fedorapeople.org/fonts/convertbitmap/convertfont.py
BuildRequires:  fontpackages-devel
BuildRequires:  fonttosfnt
BuildRequires:  ftdump
BuildRequires:  ttf-converter >= 1.0.6
BuildRequires:  xorg-x11-fonts-legacy
Requires(post): fonts-config
Requires(posttrans):fonts-config
Requires(postun):fonts-config
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
%setup -T -D -c
%if "%{flavor}" != "converted"
for i in $RPM_SOURCE_DIR/*.tar.{bz2,xz}; do tar xf $i; done
%else
cp %{SOURCE100} .
tar xjf %{SOURCE0}
tar xjf %{SOURCE1}
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
ttf-converter --bitmap-fonts /usr/share/fonts/misc/clB8x10.pcf.gz /usr/share/fonts/misc/clB8x12.pcf.gz /usr/share/fonts/misc/clB8x13.pcf.gz /usr/share/fonts/misc/clB8x14.pcf.gz /usr/share/fonts/misc/clB8x16.pcf.gz /usr/share/fonts/misc/clB9x15.pcf.gz /usr/share/fonts/misc/clI6x12.pcf.gz /usr/share/fonts/misc/clR6x12.pcf.gz  --output-dir generated/
ttf-converter --bitmap-fonts /usr/share/fonts/misc/clR8x8.pcf.gz /usr/share/fonts/misc/clB8x8.pcf.gz /usr/share/fonts/misc/clI8x8.pcf.gz --output-dir generated/
ttf-converter --bitmap-fonts /usr/share/fonts/75dpi/*.pcf.gz /usr/share/fonts/100dpi/*.pcf.gz /usr/share/fonts/misc/[dghjo]*.pcf.gz --output-dir generated/

# Special case for B&H LucidaBright Italic and Bold Italic
ttf-converter --bitmap-fonts --subfamily Italic /usr/share/fonts/75dpi/lubI08.pcf.gz /usr/share/fonts/75dpi/lubI10.pcf.gz /usr/share/fonts/75dpi/lubI12.pcf.gz /usr/share/fonts/75dpi/lubI14.pcf.gz /usr/share/fonts/75dpi/lubI18.pcf.gz /usr/share/fonts/75dpi/lubI19.pcf.gz /usr/share/fonts/75dpi/lubI24.pcf.gz /usr/share/fonts/100dpi/lubI08.pcf.gz /usr/share/fonts/100dpi/lubI10.pcf.gz /usr/share/fonts/100dpi/lubI12.pcf.gz /usr/share/fonts/100dpi/lubI14.pcf.gz /usr/share/fonts/100dpi/lubI18.pcf.gz /usr/share/fonts/100dpi/lubI19.pcf.gz /usr/share/fonts/100dpi/lubI24.pcf.gz --output-dir generated/
ttf-converter --bitmap-fonts --subfamily "Bold Italic" /usr/share/fonts/75dpi/lubBI08.pcf.gz /usr/share/fonts/75dpi/lubBI10.pcf.gz /usr/share/fonts/75dpi/lubBI12.pcf.gz /usr/share/fonts/75dpi/lubBI14.pcf.gz /usr/share/fonts/75dpi/lubBI18.pcf.gz /usr/share/fonts/75dpi/lubBI19.pcf.gz /usr/share/fonts/75dpi/lubBI24.pcf.gz /usr/share/fonts/100dpi/lubBI08.pcf.gz /usr/share/fonts/100dpi/lubBI10.pcf.gz /usr/share/fonts/100dpi/lubBI12.pcf.gz /usr/share/fonts/100dpi/lubBI14.pcf.gz /usr/share/fonts/100dpi/lubBI18.pcf.gz /usr/share/fonts/100dpi/lubBI19.pcf.gz /usr/share/fonts/100dpi/lubBI24.pcf.gz --output-dir generated/

ttf-converter --bitmap-fonts --subfamily Regular /usr/share/fonts/misc/cu12.pcf.gz /usr/share/fonts/misc/cu-alt12.pcf.gz --output-dir generated/
ttf-converter --bitmap-fonts --subfamily Italic --bitmapTransform skew,1,3 /usr/share/fonts/misc/cu12.pcf.gz --output-dir generated/
ttf-converter --bitmap-fonts --subfamily Regular --fix-glyph-unicode --replace-unicode-values 0x32AD,0x4EC --replace-unicode-values 0x32AE,0x4ED /usr/share/fonts/misc/cu-pua12.pcf.gz --output-dir generated/

# Move arabic characters to the right unicode block
ttf-converter --bitmap-fonts --subfamily Regular --shift-unicode-values 0,300,1530 /usr/share/fonts/misc/arabic24.pcf.gz --output-dir generated/
ttf-converter --bitmap-fonts --subfamily Regular --shift-unicode-values 0,300,1530 /usr/share/fonts/misc/cuarabic12.pcf.gz --output-dir generated/

# Move latin characters from fullwidth unicode block so they can be used.
#ttf-converter --bitmap-fonts --shift-unicode-values 0xff01,0xff5d,-65248  /usr/share/fonts/misc/hanglg16.pcf.gz --output-dir generated/
#ttf-converter --bitmap-fonts --shift-unicode-values 0xff01,0xff5d,-65248 --replace-unicode-values 0xffe0,0xa2 --replace-unicode-values 0xffe2,0xac --replace-unicode-values 0xffe1,0xa3 --replace-unicode-values 0xffe5,0xa5 /usr/share/fonts/misc/hanglm24.pcf.gz /usr/share/fonts/misc/hanglm16.pcf.gz --output-dir generated/
#ttf-converter --bitmap-fonts --shift-unicode-values 0xff01,0xff5d,-65248 /usr/share/fonts/misc/gb16fs.pcf.gz --output-dir generated/
sed -i -e 's/FAMILY_NAME "\(.*\)"/FAMILY_NAME "\1-converted"/' font-adobe*75dpi*/cour*[012][0248].bdf \
    font-adobe*75dpi*/helv*[012][0248].bdf
sed -i -e 's/FAMILY_NAME "\(.*\)"/FAMILY_NAME "\1-converted"/' font-adobe*100dpi*/cour*[012][0248].bdf \
    font-adobe*100dpi*/helv*[012][0248].bdf

for name in font-adobe*/cour*.bdf font-adobe*/helv*.bdf; do
    fonttosfnt -b -c -g 2 -m 2 -o "${name%.bdf}.otb" "$name"
done

rm font-adobe*100*/cour*10.otb font-adobe*100*/helv*10.otb
for p in font-adobe*/cour*.otb font-adobe*/helv*.otb ; do
    realsize=`ftdump -p "$p" | grep size.*y_ppem | sed -e "s/.*size \([0-9]*\)\..*/\1/"`
    realsize=`printf %02d $realsize`
    dpi=`echo "$p" | sed -e "s/.*-\([0-9]*dpi\).*/\1/"`
    newname=`echo $p | sed -e "s/..\.otb$/-$dpi-$realsize.otb/"`
    if [ "$p" != "$newname" ]; then
        mv "$p" "$newname"
    fi
done
# Remove fonts of size 11 that are actually the same size as fonts of size 10
rm font-adobe*100*/cour*11.otb font-adobe*100*/helv*11.otb
# Remove fonts of size 20 that are actually the same size as fonts of size 18
rm font-adobe*100*/cour*20.otb font-adobe*100*/helv*20.otb
# Remove fonts of size 25 that are actually the same size as fonts of size 24
rm font-adobe*100*/cour*25.otb font-adobe*100*/helv*25.otb

cd generated

# Luxi Mono, Luxi Sans and Luxi Serif are already distributed in ttf format
rm Luxi*.ttf

# Bitstream-Charter-* is already converted to ttf format as CharterBT-*
rm Bitstream-Charter-*.otb

# Cursor.ttf just contains glyphs to be used as cursor, which isn't usable as ttf format
rm Cursor.ttf

# Bitstream-Terminal and DEC-Terminal are not converted correctly so we better remove them
rm Bitstream-Terminal*.otb
rm DEC-Terminal*.otb

# The Sun-OPEN-LOOK fonts just contains bitmap patterns without unicode values. They're hardly useful
rm Sun-OPEN-LOOK-cursor-Wide-Regular.otb
rm Sun-OPEN-LOOK-glyph-Wide-Regular.otb
rm Sun-OPEN-LOOK-glyph-Regular.otb
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
find $RPM_BUILD_ROOT/usr/share/fonts/75dpi -type f -iname \*.pcf.gz | sed -e "s+$RPM_BUILD_ROOT++g" -e 's+^usr+/usr+g' | \
  grep -v -e ISO8859 >> files.%{name}-core
rm -rf $RPM_BUILD_ROOT/usr/etc
rm -f $RPM_BUILD_ROOT/fonts.{dir,scale}
rm -f $RPM_BUILD_ROOT/usr/share/fonts/encodings/{,large}/encodings.dir

%else
# "%%{flavor}" == "converted"
cd generated
mkdir -p %{buildroot}/%{_datadir}/fonts/truetype
cp *.ttf %{buildroot}/%{_datadir}/fonts/truetype

for filename in Adobe-New-Century-Schoolbook*.otb \
   Adobe-Symbol-Regular.otb \
   Adobe-Times*.otb \
   Adobe-Utopia*.otb \
   B\&H-LucidaBright*.otb \
   B\&H-Lucida-Sans*.otb \
   B\&H-LucidaTypewriter-Sans*.otb \
   Arabic-Newspaper-Regular.otb \
   MUTT-ClearlyU-Alternate-Glyphs-Wide-Regular.otb \
   MUTT-ClearlyU-Arabic-Extra-Regular.otb \
   MUTT-ClearlyU-PUA-Regular.otb \
   MUTT-ClearlyU-Wide-Regular.otb \
   MUTT-ClearlyU-Wide-Italic.otb \
   Schumacher-Clean-Bold.otb \
   Schumacher-Clean-Wide-Bold.otb \
   Schumacher-Clean-Italic.otb \
   Schumacher-Clean-Wide-Italic.otb \
   Schumacher-Clean-Regular.otb \
   Schumacher-Clean-Wide-Regular.otb \
   ISAS-Fangsong-ti-Wide-Regular.otb \
   ISAS-Song-ti-Wide-Regular.otb \
   Daewoo-Gothic-Wide-Regular.otb \
   Daewoo-Mincho-Wide-Regular.otb \
   JIS-Fixed-Wide-Regular.otb \
   ; do
    cp "$filename"  %{buildroot}/%{_datadir}/fonts/truetype
done
cd ..
cp font-adobe*/*.otb %{buildroot}/%{_datadir}/fonts/truetype/

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
%{_datadir}/fonts/truetype/Utopia-*.ttf
%{_datadir}/fonts/truetype/B&H-LucidaTypewriter*.otb
%{_datadir}/fonts/truetype/Adobe-New-Century-Schoolbook*.otb
%{_datadir}/fonts/truetype/Adobe-Symbol-Regular.otb
%{_datadir}/fonts/truetype/Adobe-Times*.otb
%{_datadir}/fonts/truetype/Adobe-Utopia*.otb
%{_datadir}/fonts/truetype/B&H-LucidaBright*.otb
%{_datadir}/fonts/truetype/B&H-Lucida-Sans*.otb
%{_datadir}/fonts/truetype/B&H-LucidaTypewriter-Sans*.otb
%{_datadir}/fonts/truetype/Arabic-Newspaper-Regular.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Alternate-Glyphs-Wide-Regular.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Arabic-Extra-Regular.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-PUA-Regular.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Wide-Regular.otb
%{_datadir}/fonts/truetype/MUTT-ClearlyU-Wide-Italic.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Regular.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Bold.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Italic.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Wide-Regular.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Wide-Bold.otb
%{_datadir}/fonts/truetype/Schumacher-Clean-Wide-Italic.otb
%{_datadir}/fonts/truetype/ISAS-Fangsong-ti-Wide-Regular.otb
%{_datadir}/fonts/truetype/ISAS-Song-ti-Wide-Regular.otb
%{_datadir}/fonts/truetype/Daewoo-Gothic-Wide-Regular.otb
%{_datadir}/fonts/truetype/Daewoo-Mincho-Wide-Regular.otb
%{_datadir}/fonts/truetype/JIS-Fixed-Wide-Regular.otb
%{_datadir}/fonts/truetype/cour*.otb
%{_datadir}/fonts/truetype/helv*.otb
%endif

%changelog
