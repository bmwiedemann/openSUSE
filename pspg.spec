#
# spec file for package pspg
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


Name:           pspg
Version:        1.9.0
Release:        0
Summary:        Pager for PostgreSQL, MariaDB, Percona, and MySQL
License:        BSD-2-Clause
Group:          Productivity/Text/Utilities
URL:            https://github.com/okbob/pspg
Source:         https://github.com/okbob/pspg/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(ncurses)

%description
Advanced pager for PostgreSQL and MySQL databases.
Everybody who uses psql uses less pager. It is working well, but there is
not any special support for tabular data. Tabular data related features
are core functionality of this pager.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_bindir}/pspg

%changelog
