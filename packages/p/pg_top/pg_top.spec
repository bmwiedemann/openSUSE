#
# spec file for package pg_top
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


Name:           pg_top
Version:        4.1.1
Release:        0
Summary:        top for postgresql
License:        BSD-3-Clause
URL:            https://gitlab.com/pg_top/pg_top
Source:         pg_top-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  libbsd-devel
BuildRequires:  postgresql-server-devel

%description
pg_top is 'top' for PostgreSQL. It is derived from Unix Top. Similar to top, pg_top allows you to monitor PostgreSQL processes.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.rst
%{_bindir}/pg_top
%{_mandir}/man1/pg_top.1*

%changelog
