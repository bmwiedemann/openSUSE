#
# spec file for package font-util
#
# Copyright (c) 2023 SUSE LLC
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


Name:           font-util
Version:        1.4.0
Release:        0
Summary:        X.Org font package creation/installation utilities
License:        MIT
Group:          System/X11/Fonts
URL:            https://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/archive/individual/font/%{name}-%{version}.tar.xz
Source1:        http://xorg.freedesktop.org/archive/individual/font/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        http://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WINDOWS/CP932.TXT
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
# Package was named xorg-x11-fonts-devel until 12.2
# We use 7.7 for Provides/Obsoletes, since we're renaming the packages when
# X11R7.7 is in RC1, and xorg-x11-fonts-devel was version 7.6
Provides:       xorg-x11-fonts-devel = 7.7
Obsoletes:      xorg-x11-fonts-devel < 7.7

%description
This package provides utilities for X.Org font package
creation/installation.

%prep
%setup -q
# see Bug 194720 for details
cp %{SOURCE3} map-JISX0201.1976-0

%build
%configure --with-mapdir=%{_datadir}/fonts/util --with-fontrootdir=%{_datadir}/fonts

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/bdftruncate
%{_bindir}/ucs2any
%{_mandir}/man1/bdftruncate.1%{?ext_man}
%{_mandir}/man1/ucs2any.1%{?ext_man}
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/fontutil.m4
%{_datadir}/fonts/util/
%{_libdir}/pkgconfig/fontutil.pc

%changelog
