#
# spec file for package libnfs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Bjørn Lie, Bryne, Norway.
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


%define sover   13

Name:           libnfs
Version:        4.0.0
Release:        0
Summary:        Client library for accessing NFS shares over a network
License:        LGPL-2.1-or-later AND BSD-2-Clause AND GPL-3.0-or-later
Group:          Productivity/Networking/NFS
URL:            https://github.com/sahlberg/libnfs
Source0:        %{url}/archive/libnfs-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Package contains a library of functions for accessing NFSv2 and
NFSv3 servers from user space. It provides a low-level,
asynchronous RPC library for accessing NFS protocols, an
asynchronous library with POSIX-like VFS functions, and a
synchronous library with POSIX-like VFS functions.

%package -n libnfs%{sover}
Summary:        Client library for accessing NFS shares over a network
Group:          Productivity/Networking/NFS

%description -n libnfs%{sover}
Package contains a library of functions for accessing NFSv2 and
NFSv3 servers from user space. It provides a low-level,
asynchronous RPC library for accessing NFS protocols, an
asynchronous library with POSIX-like VFS functions, and a
synchronous library with POSIX-like VFS functions.

%package devel
Summary:        Development files for libnfs
Group:          Development/Languages/C and C++
Requires:       libnfs%{sover} = %{version}-%{release}

%description devel
The libnfs-devel package contains libraries and header files for
developing applications that use libnfs.

%package -n utils-libnfs
Summary:        Utilities for accessing NFS servers
# Handle libnfs from packman, which contained both binaries and lib
Group:          Productivity/Networking/NFS
Provides:       libnfs = %{version}-%{release}
Obsoletes:      libnfs < %{version}-%{release}

%description -n utils-libnfs
The utils-libnfs package contains simple client programs for
accessing NFS servers using libnfs.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

%build
autoreconf -fiv
%configure \
	--disable-static \
	--disable-examples \
	--enable-utils \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libnfs%{sover} -p /sbin/ldconfig
%postun -n libnfs%{sover} -p /sbin/ldconfig

%files -n libnfs%{sover}
%license COPYING LICENCE-LGPL-2.1.txt LICENCE-BSD.txt LICENCE-GPL-3.txt
%doc README
%{_libdir}/libnfs.so.*

%files devel
%{_libdir}/libnfs.so
%{_includedir}/nfsc/
%{_libdir}/pkgconfig/libnfs.pc

%files -n utils-libnfs
%{_bindir}/nfs-*
%{_mandir}/man1/nfs-*.1%{?ext_man}

%changelog
