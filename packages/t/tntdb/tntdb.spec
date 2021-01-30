#
# spec file for package tntdb
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


%define sover   5
Name:           tntdb
Version:        1.4
Release:        0
Summary:        Library for simple database access
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.tntnet.org/index.html
Source0:        http://www.tntnet.org/download/tntdb-%{version}.tar.gz
Patch0:         tntdb-1.4-avoid-version.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  findutils
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig(cxxtools)
BuildRequires:  pkgconfig(libmariadb)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  postgresql-server-devel
%endif

%description
Tntdb is a library for simple database access.

The database independent layer offers easy to use methods for working with the database and also greatly simplifies resource-management. The classes hold reference-counted pointers to the actual implementation. They are copyable and assignable. The user can use the classes just like simple values. The resources they reference are freed, when the last reference is deleted. This happens normally just by leaving the scope. There is normally no reason to instantiate them dynamically on the heap.

The driver-layer contains the actual implementation, which does the work. These classes are database-dependent. The user normally doesn't need to deal with this.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Tntdb is a library for simple database access.

The database independent layer offers easy to use methods for working with the database and also greatly simplifies resource-management. The classes hold reference-counted pointers to the actual implementation. They are copyable and assignable. The user can use the classes just like simple values. The resources they reference are freed, when the last reference is deleted. This happens normally just by leaving the scope. There is normally no reason to instantiate them dynamically on the heap.

This package contains documentation

%package -n libtntdb%{sover}
Summary:        Library for simple database access
Group:          Development/Libraries/C and C++
Provides:       tntdb

%description -n libtntdb%{sover}
Tntdb is a library for simple database access.

The database independent layer offers easy to use methods for working with the database and also greatly simplifies resource-management. The classes hold reference-counted pointers to the actual implementation. They are copyable and assignable. The user can use the classes just like simple values. The resources they reference are freed, when the last reference is deleted. This happens normally just by leaving the scope. There is normally no reason to instantiate them dynamically on the heap.

The driver-layer contains the actual implementation, which does the work. These classes are database-dependent. The user normally doesn't need to deal with this.

%package -n libtntdb-devel
Summary:        Development files for tntdb
Group:          Development/Libraries/C and C++
Requires:       libtntdb%{sover} = %{version}

%description -n libtntdb-devel
Headers and so links for tntdb library.

%package -n tntdb-mysql
Summary:        MySQL plugin for tntdb
Group:          Development/Libraries/C and C++

%description -n tntdb-mysql
MySQL plugin for tntdb abstraction library.

%package -n tntdb-postgresql
Summary:        PostgreSQL plugin for tntdb
Group:          Development/Libraries/C and C++

%description -n tntdb-postgresql
PostgreSQL plugin for tntdb abstraction library.

%package -n tntdb-sqlite
Summary:        SQLite plugin for tntdb
Group:          Development/Libraries/C and C++

%description -n tntdb-sqlite
SQLite plugin for tntdb abstraction library.

%package -n tntdb-replicate
Summary:        SQLite plugin for tntdb
Group:          Development/Libraries/C and C++

%description -n tntdb-replicate
Replication plugin for tntdb abstraction library.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure \
	--with-postgresql \
	--with-replicate \
	--with-mysql \
	--with-sqlite \
	--with-doxygen
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -name '*.a' -delete

%post -n libtntdb%{sover} -p /sbin/ldconfig
%postun -n libtntdb%{sover} -p /sbin/ldconfig

%files doc
%doc %{_datadir}/doc/%{name}

%files -n libtntdb%{sover}
%license COPYING
%{_libdir}/libtntdb.so.*

%files -n libtntdb-devel
%doc AUTHORS ChangeLog README
%{_includedir}/tntdb
%{_includedir}/tntdb.h
%{_libdir}/libtntdb.so
%{_libdir}/pkgconfig/tntdb.pc

%files -n tntdb-mysql
%dir %{_libdir}/tntdb
%{_libdir}/tntdb/tntdb*mysql.so

%files -n tntdb-postgresql
%dir %{_libdir}/tntdb
%{_libdir}/tntdb/tntdb*postgresql.so

%files -n tntdb-sqlite
%dir %{_libdir}/tntdb
%{_libdir}/tntdb/tntdb*sqlite.so

%files -n tntdb-replicate
%dir %{_libdir}/tntdb
%{_libdir}/tntdb/tntdb*replicate.so

%changelog
