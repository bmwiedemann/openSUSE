#
# spec file for package baekmuk-bitmap-fonts
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


%define	bitmap_fontdir  %{_fontsdir}/baekmuk
Name:           baekmuk-bitmap-fonts
Version:        2.2
Release:        0
Summary:        Baekmuk Fonts, Bitmap Version
License:        HPND
Group:          System/X11/Fonts
URL:            https://kldp.net/baekmuk/
Source0:        http://kldp.net/baekmuk/release/865-baekmuk-bdf-%{version}.tar.gz
Source1:        http://kldp.net/baekmuk/release/865-baekmuk-ttf-%{version}.tar.gz
# fonts.scale.baekmuk is very bare bones and works with both, freetype and xtt
Source20:       fonts.scale.baekmuk
Patch0:         baekmuk-gulim-medium-18-pixel-bitmap.patch
Patch1:         baekmuk-gulim-bold-18-pixel-bitmap.patch
Patch2:         baekmuk-bdf-fonts-fix-fonts-alias.patch
BuildRequires:  fontpackages-devel
Provides:       baekmuk = %{version}
Provides:       locale(xorg-x11:ko)
Obsoletes:      baekmuk < 2.1
BuildArch:      noarch
%reconfigure_fonts_prereq
BuildRequires:  bdftopcf
BuildRequires:  mkfontdir

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
%setup -q -c -a 1
pushd baekmuk-bdf-%{version}
%patch0 -p0
%patch1 -p0
%patch2 -p1
popd

%build
pushd baekmuk-bdf-%{version}
for file in bdf/*.bdf; do
  bdftopcf $file | gzip -9 > ${file%.bdf}.pcf.gz
done

%install
pushd baekmuk-ttf-%{version}/ttf
mkdir -p %{buildroot}%{_ttfontsdir}
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}
install -c -m 644 %{SOURCE20} %{buildroot}%{_ttfontsdir}/fonts.scale.baekmuk
popd
pushd baekmuk-bdf-%{version}/bdf
mkdir -p %{buildroot}%{bitmap_fontdir}
install -c -m 644 *.pcf.gz %{buildroot}%{bitmap_fontdir}
install -c -m 644 fonts.alias %{buildroot}%{bitmap_fontdir}/fonts.alias
popd

mkfontdir %{buildroot}%{bitmap_fontdir}
%reconfigure_fonts_scriptlets -n baekmuk-bitmap-fonts
%reconfigure_fonts_scriptlets -c -n baekmuk-ttf-fonts

%files
%license baekmuk-bdf-%{version}/COPYRIGHT baekmuk-bdf-%{version}/COPYRIGHT.ks
%dir %{bitmap_fontdir}
%verify(not md5 size mtime) %{bitmap_fontdir}/fonts.dir
%{bitmap_fontdir}/fonts.alias
%{bitmap_fontdir}/*.pcf.gz

%files -n baekmuk-ttf-fonts
%license baekmuk-ttf-%{version}/COPYRIGHT
%dir %{_ttfontsdir}/
%{_ttfontsdir}/*.ttf
%config %{_ttfontsdir}/fonts.scale.baekmuk

%changelog
