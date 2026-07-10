#
# spec file for package libnfs
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2015 Bjørn Lie, Bryne, Norway.
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover   16
Name:           libnfs
Version:        6.0.2
Release:        0
Summary:        Client library for accessing NFS shares over a network
License:        BSD-2-Clause AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Productivity/Networking/NFS
URL:            https://github.com/sahlberg/libnfs
Source0:        %{url}/archive/libnfs-%{version}.tar.gz
Patch0:         libnfs-5.0.3-glibc-2_43.patch
# PATCH-FIX-UPSTREAM libnfs-CVE-2026-53689.patch bsc#1268135 mgorse@suse.com -- ZDR: check the string size for sanity.
Patch1:         libnfs-CVE-2026-53689.patch
# PATCH-FIX-UPSTReAM libnfs-CVE-2026-57918.patch mgorse@suse.com -- socket: prevent an underflow in xid.
Patch2:         libnfs-CVE-2026-57918.patch
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(krb5-gssapi)

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

%ldconfig_scriptlets -n libnfs%{sover}

%files -n libnfs%{sover}
%license COPYING LICENCE-LGPL-2.1.txt LICENCE-BSD.txt LICENCE-GPL-3.txt
%doc README
%{_libdir}/libnfs.so.%{sover}{,.*}

%files devel
%license COPYING LICENCE-LGPL-2.1.txt LICENCE-BSD.txt LICENCE-GPL-3.txt
%{_libdir}/libnfs.so
%{_includedir}/nfsc/
%{_libdir}/pkgconfig/libnfs.pc

%files -n utils-libnfs
%license COPYING LICENCE-LGPL-2.1.txt LICENCE-BSD.txt LICENCE-GPL-3.txt
%{_bindir}/nfs-*
%{_mandir}/man1/nfs-*.1%{?ext_man}

%changelog
