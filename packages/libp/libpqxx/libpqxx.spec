#
# spec file for package libpqxx
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


%define abi_ver_major 6
%define abi_ver_minor 4
Name:           libpqxx
Version:        6.4.5
Release:        0
Summary:        C++ Client Library for PostgreSQL
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://pqxx.org/development/libpqxx/
Source:         https://github.com/jtv/libpqxx/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  postgresql-server-devel
BuildRequires:  python3
BuildRequires:  pkgconfig(libpq)

%description
This is the official C++ client API for postgres.  What libpqxx brings you is
effective use of templates to reduce the inconvenience of dealing with type
conversions; of standard C++ strings to keep you from having to worry about
buffer allocation and overflow attacks; of exceptions to take the tedious and
error-prone plumbing around error handling out of your hands; of constructors
and destructors to bring resource management under control; and even basic
object-orientation to give you some extra reliability features that would be
hard to get with most other database interfaces.

%package %{abi_ver_major}_%{abi_ver_minor}
Summary:        C++ Client Library for PostgreSQL
Group:          System/Libraries

%description %{abi_ver_major}_%{abi_ver_minor}
This is the official C++ client API for postgres.  What libpqxx brings you is
effective use of templates to reduce the inconvenience of dealing with type
conversions; of standard C++ strings to keep you from having to worry about
buffer allocation and overflow attacks; of exceptions to take the tedious and
error-prone plumbing around error handling out of your hands; of constructors
and destructors to bring resource management under control; and even basic
object-orientation to give you some extra reliability features that would be
hard to get with most other database interfaces.

%package devel
Summary:        C++ Client Library for PostgreSQL
Group:          Development/Libraries/C and C++
Requires:       %{name}-%{abi_ver_major}_%{abi_ver_minor} = %{version}

%description devel
This package contains header files needed for writing
C++ programs that connect to a PostgreSQL database.

%prep
%autosetup

%build
chmod 0644 COPYING
sed -i "s|env python|python3|g" tools/splitconfig
sed -i "s|env python|python3|g" tools/template2mak.py
%configure \
  --enable-shared \
  --disable-static \
  --disable-documentation
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la

%post   %{abi_ver_major}_%{abi_ver_minor} -p /sbin/ldconfig
%postun %{abi_ver_major}_%{abi_ver_minor} -p /sbin/ldconfig

%files %{abi_ver_major}_%{abi_ver_minor}
%license COPYING
%doc AUTHORS NEWS README.md README-UPGRADE
%{_libdir}/%{name}-%{abi_ver_major}.%{abi_ver_minor}.so

%files devel
%{_libdir}/pkgconfig/libpqxx.pc
%{_libdir}/%{name}.so
%{_includedir}/pqxx/

%changelog
