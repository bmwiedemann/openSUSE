#
# spec file for package qore-mysql-module
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           qore-mysql-module
Version:        2.0.2.1
Release:        0
Summary:        MySQL DBI module for Qore
License:        LGPL-2.1-or-later OR GPL-2.0-or-later
Group:          Development/Languages/Other
Url:            http://qore.org
Source:         https://github.com/qorelanguage/module-mysql/releases/download/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libmysqlclient-devel
BuildRequires:  qore
BuildRequires:  qore-devel
Requires:       %{_bindir}/env
Requires:       qore-module-api-%{module_api}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MySQL DBI driver module for the Qore Programming Language. The MySQL driver is
character set aware and supports multithreading, transaction management, and
stored procedure execution.

%prep
%setup -q

%build
%ifarch x86_64 aarch64 ppc64 ppc64le x390x
c64=--enable-64bit
%endif
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" ./configure RPM_OPT_FLAGS="%{optflags}" --prefix=/usr --disable-debug $c64
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{module_dir}
mkdir -p %{buildroot}%{_datadir}/doc/qore-mysql-module
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find test -type f|xargs chmod 644
%fdupes -s docs

%files
%defattr(-,root,root,-)
%{module_dir}
%doc README RELEASE-NOTES ChangeLog AUTHORS
%license COPYING.GPL COPYING.LGPL

%package doc
Summary:        MySQL DBI module for Qore
Group:          Development/Languages/Other

%description doc
MySQL module for the Qore Programming Language.

This RPM provides API documentation, test and example programs

%files doc
%defattr(-,root,root,-)
%doc docs/mysql/html test/db-test.q test/sql-stmt.q

%changelog
