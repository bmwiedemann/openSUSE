#
# spec file for package qore-pgsql-module
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


%define module_api   %(qore --latest-module-api 2>/dev/null)
%define src_name     module-psql-%{version}
Name:           qore-pgsql-module
Version:        3.2.0
Release:        0
Summary:        PostgreSQL DBI module for Qore
License:        GPL-2.0-or-later OR LGPL-2.0-or-later OR MIT
Group:          Development/Languages/Other
URL:            http://qore.org
Source:         https://github.com/qorelanguage/module-pgsql/releases/download/v%{version}/qore-pgsql-module-%{version}.tar.bz2#/%{src_name}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  cmake >= 3.5
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
BuildRequires:  (qore-stdlib if qore >= 2.0)
Requires:       qore-module(abi)%{?_isa} = %{module_api}
Requires:       /usr/bin/env

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
%setup -q -n qore-pgsql-module-%{version}

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5
export CXXFLAGS="%{?optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DCMAKE_SKIP_RPATH=1 -DCMAKE_SKIP_INSTALL_RPATH=1 -DCMAKE_SKIP_BUILD_RPATH=1 -DCMAKE_PREFIX_PATH=${_prefix}/lib64/cmake/Qore .
make %{?_smp_mflags}
make %{?_smp_mflags} docs
sed -i 's/#!\/usr\/bin\/env qore/#!\/usr\/bin\/qore/' test/*.qtest

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes -s %{__builddir}/html


%files
%defattr(-,root,root,-)
%{_libdir}/qore-modules
%license COPYING.LGPL COPYING.MIT
%doc README RELEASE-NOTES AUTHORS


%files doc
%defattr(-,root,root,-)
%doc docs/pgsql/html test/pgsql.qtest test/sql-stmt.q

%changelog
