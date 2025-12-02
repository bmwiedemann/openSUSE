#
# spec file for package dqlite
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lname libdqlite0
Name:           dqlite
Version:        1.18.3
Release:        0
Summary:        Distributed SQLite
License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
Group:          Development/Libraries/C and C++
URL:            https://github.com/canonical/dqlite
Source:         https://github.com/canonical/dqlite/archive/v%{version}-fixed.tar.gz#/%{name}-%{version}-fixed.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(liblz4) >= 1.7.1
BuildRequires:  pkgconfig(libuv) >= 1.8.0
BuildRequires:  pkgconfig(sqlite3) >= 3.22.0

%description
dqlite is a C library implementing an embeddable and replicated
SQL database engine with high-availability and automatic failover.

%package -n %{lname}
Summary:        Library implementing the distributed SQLite
Group:          System/Libraries

%description -n %{lname}
dqlite is a C library implementing an embeddable and replicated
SQL database engine with high-availability and automatic failover.

dqlite extends SQLite with a network protocol that can connect
together various instances of an application and have them act as a
highly-availablity cluster.

%package devel
Summary:        Development files for the distributed SQLite
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
dqlite is a C library implementing an embeddable and replicated
SQL database engine with high-availability and automatic failover.

This package contains the files necessary for developing and building
applications using the library.

%prep
%autosetup -p1 -n %{name}-%{version}-fixed

%build
autoreconf -fiv
%configure \
	--disable-static \
	--enable-build-raft \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{lname}

%check
make check %{?_smp_mflags}

%files devel
%license LICENSE
%doc AUTHORS README.md
%{_includedir}/dqlite.h
%{_libdir}/libdqlite.so
%{_libdir}/pkgconfig/dqlite.pc

%files -n %{lname}
%license LICENSE
%{_libdir}/libdqlite.so.*

%changelog
