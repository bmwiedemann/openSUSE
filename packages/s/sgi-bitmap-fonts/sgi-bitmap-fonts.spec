#
# spec file for package sgi-bitmap-fonts
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


%define upstream_name sgi-fonts
%define sgi_fontsdir  %{_miscfontsdir}/sgi

Name:           sgi-bitmap-fonts
Version:        1.0
Release:        0
# fonts gathered from
# ftp://patches-europe.sgi.com/pub/linux/ProPack1.4/SRPMS/sgi-fonts-1.0-1.src.rpm
# -> added COPYING file (MIT license), bug #752246
Summary:        Very Nice Bitmapped Fonts from SGI
License:        MIT
Group:          System/X11/Fonts
Source0:        %{upstream_name}.tar.bz2
Source1:        COPYING
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         %{name}-%{version}.patch
BuildRequires:  fontpackages-devel
BuildRequires:  freetype2
%if 0%{?suse_version} >= 1220
BuildRequires:  bdftopcf
BuildRequires:  fontconfig
BuildRequires:  imake
BuildRequires:  mkfontdir
BuildRequires:  xorg-cf-files
%else
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-devel
%endif
BuildRequires:  xorg-x11-fonts
Provides:       sgi-fonts = %{version}
# FIXME: This causes a rpmlint warning; change <= to < once here's a new upstream version
Obsoletes:      sgi-fonts <= %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
A few extra fonts from SGI, very readable.

%prep
%setup -q -n %{upstream_name}
%patch0 -p1

%build
xmkmf
make
cp %{SOURCE1} .

%install
make FONTINSTDIR=%{_miscfontsdir} DESTDIR=%{buildroot} install
pushd %{buildroot}%{sgi_fontsdir}
    gzip -n --best *.pcf
    fc-cache -f .
    mkfontscale .
    chmod u+w fonts.dir
    mkfontdir -e %{_fontsdir}/encodings
    touch .fonts-config-timestamp
popd
rm -f %{buildroot}%{sgi_fontsdir}/fonts.cache-?
rm -f %{buildroot}%{sgi_fontsdir}/.uuid

%reconfigure_fonts_scriptlets

%files
%defattr(644,root,root,755)
%doc COPYING
%dir %{sgi_fontsdir}
%verify(not md5 size mtime) %{sgi_fontsdir}/.fonts-config-timestamp
%verify(not md5 size mtime) %{sgi_fontsdir}/encodings.dir
%verify(not md5 size mtime) %{sgi_fontsdir}/fonts.dir
%verify(not md5 size mtime) %{sgi_fontsdir}/fonts.scale
%{sgi_fontsdir}/fonts.alias
%{sgi_fontsdir}/*.pcf.gz

%changelog
