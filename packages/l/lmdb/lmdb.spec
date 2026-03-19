#
# spec file for package lmdb
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname liblmdb-0_9_35
Name:           lmdb
Version:        0.9.35
Release:        0
Summary:        Lightning Memory-Mapped Database Manager
License:        OLDAP-2.8
URL:            https://symas.com/mdb/
Source:         https://git.openldap.org/openldap/openldap/-/archive/LMDB_%{version}/openldap-LMDB_%{version}.tar.gz
Source1:        lmdb.pc.in
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE - Build and link to shared library
Patch1:         0001-Makefile-use-shared-library.patch
# PATCH-FIX-UPSTREAM - debugging tools (https://github.com/kacfengine/lmdb)
Patch2:         0002-Add-extra-tools-and-CFEngine-modifications-for-LMDB.patch
%if 0%{?rhel_version} == 700
BuildRequires:  perl-Exporter
%endif

%description
LMDB is a Btree-based database management library with an API similar
to BerkeleyDB. The library is thread-aware and supports concurrent
read/write access from multiple processes and threads. The DB
structure is multi-versioned, and data pages use a copy-on-write
strategy, which also provides resistance to corruption and eliminates
the need for any recovery procedures. The database is exposed in a
memory map, requiring no page cache layer of its own.

%package -n %{lname}
Summary:        Shared library for Lightning Memory-Mapped Database (LMDB)

%description -n %{lname}
LMDB is a Btree-based database management library with an API similar
to BerkeleyDB. The library is thread-aware and supports concurrent
read/write access from multiple processes and threads. The DB
structure is multi-versioned, and data pages use a copy-on-write
strategy, which also provides resistance to corruption and eliminates
the need for any recovery procedures. The database is exposed in a
memory map, requiring no page cache layer of its own.

This package contains the shared library.

%package devel
Summary:        Development package for lmdb
Requires:       %{lname} = %{version}

%description devel
LMDB is a Btree-based database management library with an API similar
to BerkeleyDB. The library is thread-aware and supports concurrent
read/write access from multiple processes and threads. The DB
structure is multi-versioned, and data pages use a copy-on-write
strategy, which also provides resistance to corruption and eliminates
the need for any recovery procedures. The database is exposed in a
memory map, requiring no page cache layer of its own.

This package contains the files needed to compile programs that use
the liblmdb library.

%prep
%autosetup -p1 -n openldap-LMDB_%{version}

%build
cd libraries/liblmdb
%make_build SOVERSION=%{version} CFLAGS="%{optflags}"

%install
cd libraries/liblmdb
make install DESTDIR=%{buildroot} SOVERSION=%{version} \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    mandir=%{_mandir} \
    includedir=%{_includedir} \
    datarootdir=%{_datadir}
ln -s %{_libdir}/liblmdb-%{version}.so %{buildroot}%{_libdir}/liblmdb.so

# Install pkgconfig file
sed -e 's:@PREFIX@:%{_prefix}:g' \
    -e 's:@EXEC_PREFIX@:%{_exec_prefix}:g' \
    -e 's:@LIBDIR@:%{_libdir}:g' \
    -e 's:@INCLUDEDIR@:%{_includedir}:g' \
    -e 's:@PACKAGE_VERSION@:%{version}:g' \
    %{SOURCE1} >lmdb.pc
install -Dpm 0644 -t %{buildroot}%{_libdir}/pkgconfig lmdb.pc

%check
cd libraries/liblmdb
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{make_build} test

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc libraries/liblmdb/CHANGES
%doc libraries/liblmdb/COPYRIGHT
%license libraries/liblmdb/LICENSE
%{_bindir}/lm*
%{_bindir}/mdb_*
%{_mandir}/man1/*.1%{?ext_man}

%files -n %{lname}
%{_libdir}/liblmdb-%{version}.so

%files devel
%{_includedir}/lmdb.h
%{_libdir}/liblmdb.so
%{_libdir}/pkgconfig/lmdb.pc

%changelog
