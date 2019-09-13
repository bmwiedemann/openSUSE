#
# spec file for package x11-japanese-bitmap-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define fontdir   %{_fontsdir}/japanese

Name:           x11-japanese-bitmap-fonts
Summary:        Japanese Fixed Fonts for the X Window System
License:        SUSE-Public-Domain and HPND
Group:          System/X11/Fonts
BuildRequires:  fdupes
%if 0%{?suse_version} >= 1220
BuildRequires:  bdftopcf
BuildRequires:  mkfontdir
%else
BuildRequires:  xorg-x11
%endif
%if 0%{?suse_version} < 1130
BuildRequires:  freetype2
%endif
Version:        20020904
Release:        0
Url:            http://openlab.ring.gr.jp/efont/japanese/
Source0:        http://openlab.ring.gr.jp/efont/dist/japanese/japanese-bitmap-fonts-0.4.5.tar.bz2
Source1:        mkbold
Source2:        mkitalic
Source4:        xfonts_jp.tar.bz2
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       xfntjp = %{version}
Provides:       locale(xorg-x11:ja)
Obsoletes:      xfntjp <= 20020904
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This Package contains Japanese fixed-width fonts for X11.

It contains the fonts knj10, kaname-alter, shinonome12, shinonome16,
k14goth, Kappa20, kanji32, and marumoji.

On top of that, it also contains bold, italic, and bold-italic versions
of the popular Japanese fonts usually found in the
/usr/lib/X11/fonts/misc directory of the standard X11 distribution and
bold, italic, and bold-italic versions of iso-8859-1 fonts which fit
nicely in style and width to the Japanese fonts.

%prep
%setup -q -n japanese-bitmap-fonts-0.4.5
mkdir -p extra
pushd extra
    tar xvf $RPM_SOURCE_DIR/xfonts_jp.tar.bz2
popd

%build
mkdir build
./configure --with-pcf=yes --with-fontdir=`pwd`/build
make pcf
rm build/fonts.dir
gzip -n -9 build/*.pcf
pushd extra
    for i in 7x14 7x14rk k14 8x16 8x16rk jiskan16 ; do
      /usr/bin/perl $RPM_SOURCE_DIR/mkbold ${i}.bdf > ${i}b.bdf
      /usr/bin/perl $RPM_SOURCE_DIR/mkitalic  ${i}.bdf > ${i}i.bdf
      /usr/bin/perl $RPM_SOURCE_DIR/mkbold ${i}i.bdf > ${i}bi.bdf
        # the non-(bold/italic) versions of the 14 and 16 pixel fonts
	# are already in xf86.rpm, include only the bold/italic ones here:
	for j in ${i}b.bdf ${i}i.bdf ${i}bi.bdf ; do
	    bdftopcf $j | gzip -n -9  > `basename $j .bdf`.pcf.gz
	done
    done
popd

%install
mkdir -p %{buildroot}%{fontdir}
cp -p build/* %{buildroot}%{fontdir}
cp -p extra/*.pcf* %{buildroot}%{fontdir}
%fdupes %{buildroot}%{fontdir}

%clean

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc README* ChangeLog
%{fontdir}

%changelog
