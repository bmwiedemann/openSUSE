#
# spec file for package xfishtank
#
# Copyright (c) 2025 SUSE LLC
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


Name:           xfishtank
Version:        3.3.2
Release:        0
Summary:        An aquarium in the root window
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Background
URL:            https://ratrabbit.nl/ratrabbit/software/xfishtank/index.html
Source:         https://ratrabbit.nl/downloads/xfishtank/%{name}-%{version}.tar.gz
Patch0:         reproducible.patch
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtst)
Requires:       gnome-icon-theme

%description
A nice little aquarium with funny fish -- yet another background screen.

%prep
%autosetup -p1

%build
%configure
%make_build CCOPTIONS="%{optflags}"

%install
%make_install

%check
%make_build check

%files
%doc README
%license COPYING
%{_bindir}/xfishtank
%{_mandir}/man1/xfishtank.1%{?ext_man}
%{_datadir}/applications/xfishtank.desktop
%{_datadir}/pixmaps/xfishtank.png

%changelog
