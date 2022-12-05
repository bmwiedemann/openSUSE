#
# spec file for package raft
#
# Copyright (c) 2022 SUSE LLC
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


%define raft_sover 2
Name:           raft
Version:        0.16.0
Release:        0
Summary:        Fully asynchronous C implementation of the Raft consensus protocol
License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/canonical/raft
Source:         https://github.com/canonical/raft/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  pkgconfig(liblz4) >= 1.7.1
BuildRequires:  pkgconfig(libuv) >= 1.18.0

%description
This library is a fully asynchronous C implementation of the Raft consensus protocol.

It implements the core Raft algorithm logic and a pluggable interface defining I/O for
networking and persistent storage. The algorithm supports leadership election,
log replication, log compaction, and  membership changes.

A stock implementation of the I/O interface based on libuv is included.

%package -n libraft%{raft_sover}
Summary:        Library implementing the Raft consensus protocol

%description -n libraft%{raft_sover}
This library is a fully asynchronous C implementation of the Raft consensus protocol.

It implements the core Raft algorithm logic and a pluggable interface defining I/O for
networking and persistent storage. The algorithm supports leadership election,
log replication, log compaction, and  membership changes.

A stock implementation of the I/O interface based on libuv is included.

%package devel
Summary:        Development files for the Raft library implementation of the consensus protocol
Requires:       libraft%{raft_sover} = %{version}
Requires:       pkgconfig(libuv) >= 1.18.0

%description devel
This library is a fully asynchronous C implementation of the Raft consensus protocol.

It implements the core Raft algorithm logic and a pluggable interface defining I/O for
networking and persistent storage. The algorithm supports leadership election,
log replication, log compaction, and  membership changes.

This package contains the files necessary for developing and building applications
using the library.

%prep
%setup -q

%build
autoreconf -iv
%configure \
	--disable-static

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libraft%{raft_sover} -p /sbin/ldconfig
%postun -n libraft%{raft_sover} -p /sbin/ldconfig

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
