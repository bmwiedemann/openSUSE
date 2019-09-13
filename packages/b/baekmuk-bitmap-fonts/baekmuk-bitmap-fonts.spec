#
# spec file for package baekmuk-bitmap-fonts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define	bitmap_fontdir  %{_fontsdir}/baekmuk

Name:           baekmuk-bitmap-fonts
BuildRequires:  gawk
BuildRequires:  perl
%if 0%{?suse_version} >= 1220
BuildRequires:  bdftopcf
BuildRequires:  mkfontdir
%else
BuildRequires:  xorg-x11
%endif
%if 0%{?suse_version} < 1130
BuildRequires:  freetype2
%endif
Version:        2.1
Release:        0
Summary:        Baekmuk Fonts, Bitmap Version
License:        HPND
Group:          System/X11/Fonts
Source0:        baekmuk-2.1.tar.bz2
Source1:        baekmuk-doc-2.1.tar.gz
Source2:        baekmuk-ttf-2.1.tar.bz2
Source17:       fonts.alias
Source18:       mkitalic
Source19:       mkbold
# truetype-ko-fonts.dir is nice, but in xtt syntax, which does not work with freetype
Source20:       truetype-ko-fonts.dir
# fonts.scale.baekmuk is very bare bones and works with both, freetype and xtt
Source21:       fonts.scale.baekmuk
Source22:       prepare-bitmap-fonts.sh
Source30:       baekmuk-bitmap-fonts-prepared.tar.bz2
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         baekmuk-gulim-medium-18-pixel-bitmap.patch
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         baekmuk-gulim-bold-18-pixel-bitmap.patch
%reconfigure_fonts_prereq
BuildRequires:  fontpackages-devel
Provides:       baekmuk = %{version}
Provides:       locale(xorg-x11:ko)
Obsoletes:      baekmuk < 2.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Baekmuk Fonts (Korean fonts for the X Window System, bitmap version).

%package -n   baekmuk-ttf-fonts
Summary:        Baekmuk Fonts, TrueType Version
Group:          System/X11/Fonts
Provides:       baekmuk-ttf = %{version}
Provides:       scalable-font-ko
Provides:       locale(ko)
Obsoletes:      baekmuk-ttf < 2.1

%description -n baekmuk-ttf-fonts
Baekmuk Fonts (Korean fonts for the X Window System, True Type
version).

%prep
%setup -q -c -a 0 -a 1 -a 2
%patch0 -p0 -b .baekmuk-gulim-medium-18-pixel-bitmap
%patch1 -p0 -b .baekmuk-gulim-bold-18-pixel-bitmap

%build
install -m 755 $RPM_SOURCE_DIR/mkitalic .
install -m 755 $RPM_SOURCE_DIR/mkbold .
# Prepare a tar ball containing a complete set of all baekmuk bitmap fonts.
# If the tar ball is already available and up to date,  just unpack the prepared
# tar ball.
# Generating the bold and especially the italic fonts takes a HUGE amount of time
# (8 hours on a 500 Mhz Pentium III). And although this is a noarch package,
# autobuild tries to build it an all architectures. This causes big problems when
# we don't have lots of build power for an architecture, for example for sparc and ppc.
# cp $RPM_SOURCE_DIR/prepare-bitmap-fonts.sh .
# source ./prepare-bitmap-fonts.sh
# tar jcvf baekmuk-bitmap-fonts-prepared.tar.bz2 *.bdf
cp $RPM_SOURCE_DIR/baekmuk-bitmap-fonts-prepared.tar.bz2 .
tar jxvf baekmuk-bitmap-fonts-prepared.tar.bz2        # already prepared tarball
for src in *.bdf ; do
 bdftopcf $src | gzip -n -9 > ${src%.bdf}.pcf.gz
done

%install
mkdir -p %{buildroot}%{bitmap_fontdir}
mkdir -p %{buildroot}%{_ttfontsdir}
install -c -m 644 *.pcf.gz %{buildroot}%{bitmap_fontdir}
install -c -m 644 %{SOURCE17} %{buildroot}%{bitmap_fontdir}/fonts.alias
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}
install -c -m 644 $RPM_SOURCE_DIR/fonts.scale.baekmuk %{buildroot}%{_ttfontsdir}/fonts.scale.baekmuk
mkfontdir %{buildroot}%{bitmap_fontdir}

%reconfigure_fonts_scriptlets -n baekmuk-bitmap-fonts

%reconfigure_fonts_scriptlets -c -n baekmuk-ttf-fonts

%files
%defattr(-, root,root)
%doc COPYRIGHT COPYRIGHT.ks
%dir %{bitmap_fontdir}
%verify(not md5 size mtime) %{bitmap_fontdir}/fonts.dir
%{bitmap_fontdir}/fonts.alias
%{bitmap_fontdir}/*.pcf.gz

%files -n baekmuk-ttf-fonts
%defattr(-, root,root)
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*.ttf
%config %{_ttfontsdir}/fonts.scale.baekmuk

%changelog
