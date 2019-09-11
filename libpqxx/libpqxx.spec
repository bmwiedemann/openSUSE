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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define abi_ver_major 5
%define abi_ver_minor 0

Name:           libpqxx
Version:        5.0.1
Release:        0
Summary:        C++ Client Library for PostgreSQL
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://pqxx.org/development/libpqxx/
Source:         https://github.com/jtv/libpqxx/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         libpqxx-sed-4.3.patch
Patch1:         libpqxx-add-python3-support.patch
Patch2:         libpqxx-add-pkg-config-support.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  postgresql-devel
# BuildRequires:  python
BuildRequires:  python3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains documentation needed for writing
C++ programs that connect to a PostgreSQL database.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
chmod 0644 COPYING
find . -name ".cvsignore" -delete

%build
autoreconf -fiv
%configure \
    --enable-shared \
    --disable-static \
    --disable-documentation
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/%{name}.la
pushd doc/html/Reference
    %fdupes -s .
popd

%post   %{abi_ver_major}_%{abi_ver_minor} -p /sbin/ldconfig
%postun %{abi_ver_major}_%{abi_ver_minor} -p /sbin/ldconfig

%files %{abi_ver_major}_%{abi_ver_minor}
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README.md README-UPGRADE
%{_libdir}/%{name}-%{abi_ver_major}.%{abi_ver_minor}.so

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/libpqxx.pc
%{_libdir}/%{name}.so
%{_includedir}/pqxx/
%{_bindir}/pqxx-config

%files doc
%defattr(-, root, root)
%doc doc/html

%changelog
