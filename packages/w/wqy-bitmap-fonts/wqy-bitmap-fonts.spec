#
# spec file for package wqy-bitmap-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           wqy-bitmap-fonts
Version:        0.9.9_0
Release:        0
%define fontdir     %{_fontsdir}/Chinese/wqy-bitmapfont
Summary:        Wen Quan Yi Bitmap Song CJK Fonts
License:        GPL-2.0-with-font-exception
Group:          System/X11/Fonts
Url:            http://wenq.org/
Source0:        wqy-bitmapfont-pcf-0.9.9-0.tar.gz
# silents "Having multiple values in <test> isn't supported and may not works as expected"
Patch0:         wqy-bitmap-fonts-conf.patch
BuildRequires:  fontpackages-devel
Requires(pre):  fontconfig
%reconfigure_fonts_prereq
Provides:       wqy-bitmapfont = %{version}
Obsoletes:      wqy-bitmapfont < 0.9.9_0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Wen Quan Yi bitmap font includes complete CJK Unified
Ideograph (U4E00 - U9FA5) glyphs at four different sizes
(9pt-12X12 pixel, 10pt-13X13 pixel, 11pt-15X15 pixel,
12pt-16x16 pixel) and two weights (medium and bold).

%prep
%setup -n wqy-bitmapfont
sed -i "s/equal/qual/" 85-wqy-bitmapsong.conf
%patch0 -p1

%build

%install
mkdir -p %{buildroot}%{fontdir}
install -m 644 *.pcf %{buildroot}%{fontdir}
gzip -n -9 %{buildroot}%{fontdir}/*.pcf
install -c -m 644 fonts.alias %{buildroot}%{fontdir}/fonts.scale
mkdir -p %{buildroot}%{_datadir}/icons/
cp LOGO.png %{buildroot}%{_datadir}/icons/wqy-bitmapsong.png
%install_fontsconf 85-wqy-bitmapsong.conf

%reconfigure_fonts_scriptlets -c

%files
%defattr(-, root,root)
%doc AUTHORS README COPYING ChangeLog
%{_fontsdir}/Chinese
%files_fontsconf_availdir
%files_fontsconf_file -l 85-wqy-bitmapsong.conf
%{_datadir}/icons/wqy-bitmapsong.png

%changelog
