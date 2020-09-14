#
# spec file for package raft
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without libuv
Name:           raft
Version:        0.9.25
Release:        0
Summary:        Fully asynchronous C implementation of the Raft consensus protocol
License:        LGPL-3.0-only WITH linking-exception-lgpl-3.0
URL:            https://github.com/canonical/raft
Source:         https://github.com/canonical/raft/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
%if !%{without libuv}
BuildRequires:  pkgconfig(libuv) >= 1.8.0
%endif

%description
This library is a fully asynchronous C implementation of the Raft consensus protocol.

It implements the core Raft algorithm logic and a pluggable interface defining I/O for
networking and persistent storage. The algorithm supports leadership election,
log replication, log compaction, and  membership changes.

%if %{with libuv}
A stock implementation of the I/O interface based on libuv is included.
%endif

%package -n libraft0
Summary:        Library implementing the Raft consensus protocol

%description -n libraft0
This library is a fully asynchronous C implementation of the Raft consensus protocol.

It implements the core Raft algorithm logic and a pluggable interface defining I/O for
networking and persistent storage. The algorithm supports leadership election,
log replication, log compaction, and  membership changes.

%if %{with libuv}
A stock implementation of the I/O interface based on libuv is included.
%endif

%package devel
Summary:        Development files for the Raft library implementation of the consensus protocol
Requires:       libraft0 = %{version}
%if !%{without libuv}
Requires:       pkgconfig(libuv) >= 1.8.0
%endif

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
	--disable-static \
%if %{without libuv}
	--disable-uv \
%endif

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libraft0 -p /sbin/ldconfig
%postun -n libraft0 -p /sbin/ldconfig

%files devel
%license LICENSE
%doc AUTHORS README.md
%{_includedir}/raft.h
%dir %{_includedir}/raft
%{_includedir}/raft/fixture.h
%if !%{without libuv}
%{_includedir}/raft/uv.h
%endif
%{_libdir}/libraft.so
%{_libdir}/pkgconfig/raft.pc

%files -n libraft0
%license LICENSE
%{_libdir}/libraft.so.0
%{_libdir}/libraft.so.0.0.7

%changelog
