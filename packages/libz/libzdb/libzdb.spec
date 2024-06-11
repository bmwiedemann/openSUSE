#
# spec file for package libzdb
#
# Copyright (c) 2024 SUSE LLC
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


%define         libsoname       %{name}13
Name:           libzdb
Version:        3.2.3
Release:        0
Summary:        Zild Database Library
License:        GPL-3.0-or-later
Group:          System/Libraries
URL:            https://www.tildeslash.com/libzdb/
Source0:        http://www.tildeslash.com/%{name}/dist/%{name}-%{version}.tar.gz
BuildRequires:  flex
BuildRequires:  mysql-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
BuildRequires:  re2c
BuildRequires:  sqlite3-devel

%description
The Zild Database Library implements a small, fast, and easy to use
database API with thread-safe connection pooling. The library can connect
transparently to multiple database systems, has zero configuration and
connections are specified via a standard URL scheme.

%package -n %{libsoname}
Summary:        Shared library for libzdb
Group:          System/Libraries
Provides:       libzdb

%description -n %{libsoname}
Zild Database Library

This package contains the shared libzdb library

%package devel
Summary:        Development files for libzdb
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}

%description devel
The libraries and header files for developing applications that use libzdb

%prep
%setup -q

%build
%configure \
  --disable-static \
  --enable-openssl \
  --enable-sqliteunlock \
  --enable-protected
%make_build

%install
%make_install
# remove static libs
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%license COPYING
%doc AUTHORS CHANGES README
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/zdb.pc
%{_includedir}/*

%changelog
