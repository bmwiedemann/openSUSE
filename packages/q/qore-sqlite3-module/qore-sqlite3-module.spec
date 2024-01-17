#
# spec file for package qore-sqlite3-module
#
# Copyright (c) 2021 SUSE LLC
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


%define module_api %(qore --latest-module-api 2>/dev/null)
Name:           qore-sqlite3-module
Version:        1.0.2
Release:        0
Summary:        Sqlite3 DBI module for Qore
License:        LGPL-2.1-or-later
Group:          Development/Languages/Other
URL:            https://www.qore.org
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.7
BuildRequires:  sqlite3-devel
BuildRequires:  zstd
Requires:       qore-module(abi)%{?_isa} = %{module_api}

%description
Sqlite3 DBI driver module for the Qore Programming Language.

%package doc
Summary:        Documentation and examples for the Qore sqlute3 module
Group:          Development/Languages/Other
BuildArch:      noarch

%description doc
This package contains the HTML documentation and example programs for the Qore
xml module.

%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README RELEASE-NOTES AUTHORS
%dir %{_libdir}/qore-modules
%{_libdir}/qore-modules/*.qmod

%files doc
%doc test docs

%changelog
