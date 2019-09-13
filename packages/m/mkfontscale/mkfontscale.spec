#
# spec file for package mkfontscale
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mkfontscale
Version:        1.2.1
Release:        0
Summary:        Utility to create index of scalable font files for X
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.25
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
Recommends:     xorg-x11-fonts-core
Provides:       mkfontdir = 1.0.7
Obsoletes:      mkfontdir <= 1.0.7
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%{_bindir}/mkfontdir
%{_bindir}/mkfontscale
%{_mandir}/man1/mkfontdir.1%{?ext_man}
%{_mandir}/man1/mkfontscale.1%{?ext_man}

%changelog
