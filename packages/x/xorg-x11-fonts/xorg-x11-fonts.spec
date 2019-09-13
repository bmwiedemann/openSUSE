#
# spec file for package xorg-x11-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xorg-x11-fonts
BuildRequires:  bdftopcf
BuildRequires:  fontpackages-devel
BuildRequires:  mkfontscale
# ucs2any
BuildRequires:  font-util
BuildRequires:  pkgconfig
Url:            http://xorg.freedesktop.org/
Version:        7.6
Release:        0
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         fonts-config
Requires:       %{name}-core
Provides:       xorg-x11-fonts-100dpi
Provides:       xorg-x11-fonts-75dpi
Provides:       xorg-x11-fonts-cyrillic
Provides:       xorg-x11-fonts-scalable
Provides:       xorg-x11-fonts-syriac
Obsoletes:      xorg-x11-fonts-100dpi
Obsoletes:      xorg-x11-fonts-75dpi
Obsoletes:      xorg-x11-fonts-cyrillic
Obsoletes:      xorg-x11-fonts-scalable
Obsoletes:      xorg-x11-fonts-syriac
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

%description
This package contains fonts maintained and shipped with X.Org.



%package core
Summary:        Core Fonts for X.Org
Group:          System/X11/Fonts
PreReq:         fonts-config
Provides:       xorg-x11:/usr/X11R6/lib/X11/fonts/misc/cursor.pcf.gz

%description core 
This package contains the 'fixed' and 'cursor' font required for any X
Server.



%prep
%setup -n . -T -D
rm -rf $RPM_BUILD_DIR/*
for i in $RPM_SOURCE_DIR/*.tar.bz2; do tar xjf $i; done

%build
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

%install
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

%clean
rm -rf "$RPM_BUILD_ROOT"

# %%post scriptlets
%reconfigure_fonts_scriptlets

%reconfigure_fonts_scriptlets -n xorg-x11-fonts-core

%files 
%defattr(-,root,root)
%dir /usr/share/fonts/100dpi
%dir /usr/share/fonts/Type1
%dir /usr/share/fonts/cyrillic
%dir /usr/share/fonts/truetype
%ghost /usr/share/fonts/100dpi/encodings.dir
%ghost /usr/share/fonts/100dpi/fonts.dir
%ghost /usr/share/fonts/100dpi/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/100dpi/.fonts-config-timestamp
/usr/share/fonts/100dpi/fonts.alias
/usr/share/fonts/100dpi/*.pcf.gz
/usr/share/fonts/75dpi/fonts.alias
/usr/share/fonts/75dpi/*-ISO8859-*.pcf.gz
%ghost /usr/share/fonts/Type1/encodings.dir
%ghost /usr/share/fonts/Type1/fonts.dir
%ghost /usr/share/fonts/Type1/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/Type1/.fonts-config-timestamp
/usr/share/fonts/Type1/*.afm
/usr/share/fonts/Type1/*.pfa
/usr/share/fonts/Type1/*.pfb
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

%files core -f files.%{name}-core
%defattr(-,root,root)
%dir /usr/share/fonts/misc
%dir /usr/share/fonts/75dpi
%ghost /usr/share/fonts/75dpi/encodings.dir
%ghost /usr/share/fonts/75dpi/fonts.dir
%ghost /usr/share/fonts/75dpi/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/75dpi/.fonts-config-timestamp
%dir /usr/share/fonts/encodings
%dir /usr/share/fonts/encodings/large
/usr/share/fonts/encodings/*.enc.gz
/usr/share/fonts/encodings/large/*.enc.gz
%ghost /usr/share/fonts/misc/encodings.dir
%ghost /usr/share/fonts/misc/fonts.dir
%ghost /usr/share/fonts/misc/fonts.scale
%ghost %verify(not mode) /usr/share/fonts/misc/.fonts-config-timestamp
/usr/share/fonts/misc/fonts.alias
/usr/share/fonts/misc/*.pcf.gz

%changelog
