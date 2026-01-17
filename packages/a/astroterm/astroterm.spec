#
# spec file for package astroterm
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           astroterm
Version:        1.0.10
Release:        0
Summary:        Terminal-based planetarium
License:        MIT
URL:            https://github.com/da-luce/astroterm
Source:         https://github.com/da-luce/astroterm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        http://tdc-www.harvard.edu/catalogs/ybsc5.gz
BuildRequires:  meson >= 1.4.0
BuildRequires:  pkgconfig
BuildRequires:  xxd
BuildRequires:  pkgconfig(argtable2)
BuildRequires:  pkgconfig(ncursesw)

%description
A planetarium for your terminal! Explore stars, planets, constellations, and
more, all rendered right in the command line - no telescope required.

%prep
%autosetup -p1
gunzip -dc %{SOURCE2} > data/ybsc5

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/astroterm

%changelog
