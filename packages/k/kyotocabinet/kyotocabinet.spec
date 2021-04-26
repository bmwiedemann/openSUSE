#
# spec file for package kyotocabinet
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


%define soname 16
Name:           kyotocabinet
Version:        1.2.77
Release:        0
Summary:        A straightforward implementation of DBM
License:        SUSE-GPL-3.0-with-FLOSS-exception
Group:          Productivity/Databases/Tools
URL:            https://fallabs.com/kyotocabinet/
Source:         https://fallabs.com/kyotocabinet/pkg/kyotocabinet-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-MISSING-TAG -- See http://wiki.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch1:         %{name}-fix_rpath.patch
Patch2:         configure-8-byte-atomics.patch
Patch3:         %{name}-pie.patch
Patch4:         %{name}-fix-debuginfo.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libbz2-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if "%{_target_cpu}" == "i386"
# kyotocabinet uses __sync_* primitives and requires at least 586
ExclusiveArch:  i586
%endif

%description
Kyoto Cabinet is a library of routines for managing a database. The database
is a simple data file containing records, each is a pair of a key and a
value. Every key and value is serial bytes with variable length. Both binary
data and character string can be used as a key and a value. Each key
must be unique within a database. There is neither concept of data tables
nor data types. Records are organized in hash table or B+ tree.

Kyoto Cabinet runs very fast. For example, elapsed time to store one
million records is 0.9 seconds for hash database, and 1.1 seconds for B+ tree
database. Moreover, the size of database is very small. For example, overhead
for a record is 16 bytes for hash database, and 4 bytes for B+ tree database.
Furthermore, scalability of Kyoto Cabinet is great. The database size can be
up to 8EB (9.22e18 bytes).

Kyoto Cabinet is written in the C++ language, and provided as API of C++, C,
Java, Python, Ruby, Perl, and Lua. Kyoto Cabinet is available on platforms
which have API conforming to C++03 with the TR1 library extensions.
Kyoto Cabinet is a free software licensed under the GNU General Public License.
On the other hand, a commercial license is also provided. If you use
Kyoto Cabinet within a proprietary software, the commercial license is required.

This package contains the command-line utilities to manage KyotoCabinet
database files.

%package -n libkyotocabinet-devel
Summary:        Development Environment for the kyotocabinet Library
Group:          Development/Languages/C and C++
Requires:       libkyotocabinet%{soname} = %{version}
Provides:       libkyotocabinet%{soname}-devel = %{version}

%description -n libkyotocabinet-devel
This package contains the development environment (headers, shared
library symlink, pkg-config file, ...) for libkyotocabinet%{soname}

%package -n libkyotocabinet%{soname}
Summary:        Modern Implementation of DBM - Shared Library
Group:          System/Libraries
Provides:       libkyotocabinet = %{version}

%description -n libkyotocabinet%{soname}
Kyoto Cabinet is a library of routines for managing a database. The database
is a simple data file containing records, each is a pair of a key and a
value. Every key and value is serial bytes with variable length. Both binary
data and character string can be used as a key and a value. Each key
must be unique within a database. There is neither concept of data tables
nor data types. Records are organized in hash table or B+ tree.

Kyoto Cabinet runs very fast. For example, elapsed time to store one
million records is 0.9 seconds for hash database, and 1.1 seconds for B+ tree
database. Moreover, the size of database is very small. For example, overhead
for a record is 16 bytes for hash database, and 4 bytes for B+ tree database.
Furthermore, scalability of Kyoto Cabinet is great. The database size can be
up to 8EB (9.22e18 bytes).

Kyoto Cabinet is written in the C++ language, and provided as API of C++, C,
Java, Python, Ruby, Perl, and Lua. Kyoto Cabinet is available on platforms
which have API conforming to C++03 with the TR1 library extensions.
Kyoto Cabinet is a free software licensed under the GNU General Public License.
On the other hand, a commercial license is also provided. If you use
Kyoto Cabinet within a proprietary software, the commercial license is required.

%prep
%autosetup -p1

%build
sed -ie "/ldconfig/d" Makefile.in
sed -ie "/DOCDIR/d" Makefile.in
sed -ri 's/-march=native/-O2 -g3/g' configure.in
autoreconf -fiv
%configure
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/kyotocabinet
rm -rf %{buildroot}%{_libdir}/libkyotocabinet.a

%check
# make check

%post   -n libkyotocabinet%{soname} -p /sbin/ldconfig
%postun -n libkyotocabinet%{soname} -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog
%doc doc/*
%doc *.idl
%{_bindir}/*
%{_mandir}/man1/*

%files -n libkyotocabinet-devel
%{_includedir}/*.h
%{_libdir}/libkyotocabinet.so
%{_libdir}/pkgconfig/kyotocabinet.pc

%files -n libkyotocabinet%{soname}
%license COPYING
%doc ChangeLog
%{_libdir}/libkyotocabinet.so.%{soname}*

%changelog
