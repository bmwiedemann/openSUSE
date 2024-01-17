#
# spec file for package qore-pgsql-module
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


%define module_api   %(qore --latest-module-api 2>/dev/null)
%define src_name     module-pgsql-%{version}
Name:           qore-pgsql-module
Version:        3.2.0
Release:        0
Summary:        PostgreSQL DBI module for Qore
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
URL:            http://qore.org
Source:         https://github.com/qorelanguage/module-pgsql/archive/refs/tags/v%{version}.tar.gz#/%{src_name}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  openssl-devel
%if 0%{?sle_version} == 150300 || 0%{?sle_version} == 150200
BuildRequires:  postgresql10-devel
%else
BuildRequires:  postgresql-devel
%endif
BuildRequires:  qore
BuildRequires:  qore-devel >= 1.0.0
BuildRequires:  qore-stdlib >= 1.0.0
Requires:       qore-module(abi)%{?_isa} = %{module_api}

%description
PostgreSQL DBI driver module for the Qore Programming Language. The PostgreSQL
driver is character set aware, supports multithreading, transaction management,
stored prodedure and function execution, etc.

%package doc
Summary:        PostgreSQL DBI module for Qore
Group:          Development/Languages

%description doc
PostgreSQL module for the Qore Programming Language.

This package provides API documentation, test and example programs

%prep
%setup -q -n %{src_name}

%build
%cmake -Denable-scu=OFF
%cmake_build docs

%install
%cmake_install
%fdupes -s %{__builddir}/html

%files
%license COPYING.LGPL COPYING.MIT
%doc README RELEASE-NOTES AUTHORS
%{_libdir}/qore-modules

%files doc
%doc %{__builddir}/docs/pgsql/html

%changelog
