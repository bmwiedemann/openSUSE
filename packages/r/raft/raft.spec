#
# spec file for package raft
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de
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


%define raft_sover 0
Name:           raft
Version:        0.22.0
Release:        0
Summary:        Asynchronous C implementation of the Raft consensus protocol
License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/cowsql/raft
Source:         https://github.com/cowsql/raft/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(liblz4) >= 1.7.1
BuildRequires:  pkgconfig(libuv) >= 1.18.0

%description
This library is a asynchronous C implementation of the Raft consensus protocol.
It implements the core Raft algorithm logic, and various drivers are provided
that implement actual network communication and persistent data storage.

The library supports asynchronous or non-blocking I/O engines (such as libuv and
io_uring), although it can be used in threaded or blocking contexts as well.

%package -n libraft%{raft_sover}
Summary:        Asynchronous C implementation of the Raft consensus protocol

%description -n libraft%{raft_sover}
This library is a asynchronous C implementation of the Raft consensus protocol.
It implements the core Raft algorithm logic, and various drivers are provided
that implement actual network communication and persistent data storage.

The library supports asynchronous or non-blocking I/O engines (such as libuv and
io_uring), although it can be used in threaded or blocking contexts as well.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       libraft%{raft_sover} = %{version}

%description devel
This library is a asynchronous C implementation of the Raft consensus protocol.
It implements the core Raft algorithm logic, and various drivers are provided
that implement actual network communication and persistent data storage.

The library supports asynchronous or non-blocking I/O engines (such as libuv and
io_uring), although it can be used in threaded or blocking contexts as well.
This library is a fully asynchronous C implementation of the Raft consensus protocol.

This package contains the files necessary for developing and building applications
using the library.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n libraft%{raft_sover}

%files devel
%license LICENSE
%doc AUTHORS README.md
%{_includedir}/raft.h
%dir %{_includedir}/raft
%{_includedir}/raft/fixture.h
%{_includedir}/raft/uv.h
%{_libdir}/libraft.so
%{_libdir}/pkgconfig/raft.pc

%files -n libraft%{raft_sover}
%license LICENSE
%{_libdir}/libraft.so.%{raft_sover}
%{_libdir}/libraft.so.%{raft_sover}.*

%changelog
