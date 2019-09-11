#
# spec file for package qore-pgsql-module
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define module_api %(qore --latest-module-api 2>/dev/null)
%define module_dir %{_libdir}/qore-modules

Name:           qore-pgsql-module
Version:        2.3
Release:        0
Summary:        PostgreSQL DBI module for Qore
License:        LGPL-2.0+ or GPL-2.0+ or MIT
Group:          Development/Languages/Other
Url:            http://qore.org
Source:         http://prdownloads.sourceforge.net/qore/%{name}-%{version}.tar.bz2
Patch0:         0001-Extend-64bit-architecure-list.patch
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
BuildRequires:  postgresql-devel
BuildRequires:  qore
BuildRequires:  qore-devel >= 0.8.5
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PostgreSQL DBI driver module for the Qore Programming Language. The PostgreSQL
driver is character set aware, supports multithreading, transaction management,
stored prodedure and function execution, etc.

%prep
%setup -q
%patch0 -p1
find test -type f|xargs chmod 644

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=/usr --disable-debug
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{module_dir}
mkdir -p %{buildroot}%{_datadir}/doc/qore-pgsql-module
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%fdupes -s docs

%files
%defattr(-,root,root,-)
%{module_dir}
%doc COPYING.LGPL COPYING.MIT README RELEASE-NOTES ChangeLog AUTHORS

%package doc
Summary:        PostgreSQL DBI module for Qore
Group:          Development/Languages

%description doc
PostgreSQL module for the Qore Programming Language.

This RPM provides API documentation, test and example programs

%files doc
%defattr(-,root,root,-)
%doc docs/pgsql/html test/db-test.q test/sql-stmt.q

%changelog
