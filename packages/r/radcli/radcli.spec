#
# spec file for package radcli
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2024, Martin Hauke <mardnh@gmx.de>
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


%define sover 6
Name:           radcli
Version:        1.4.0
Release:        0
Summary:        A RADIUS client library
License:        BSD-2-Clause AND MIT
Group:          Development/Languages/C and C++
URL:            https://radcli.github.io/radcli/
Source:         https://github.com/radcli/radcli/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(nettle)

%description
The radcli library is a library for writing RADIUS Clients. The library's
approach is to allow writing RADIUS-aware application in less than 50 lines
of C code. It was based originally on freeradius-client and is source compatible
with it.

%package -n libradcli%{sover}
Summary:        A RADIUS client library
Group:          System/Libraries

%description -n libradcli%{sover}
The radcli library is a library for writing RADIUS Clients. The library's
approach is to allow writing RADIUS-aware application in less than 50 lines
of C code. It was based originally on freeradius-client and is source compatible
with it.

%package devel
Summary:        Header files for libradcli
Group:          Development/Libraries/C and C++
Requires:       libradcli%{sover} = %{version}

%description devel
This package contains libraries and header files for developing applications
that use libradcli.

%package compat-devel
Summary:        Development files for compatibility with radiusclient-ng and freeradius-client
Group:          Development/Libraries/C and C++
Requires:       libradcli%{sover} = %{version}
Requires:       radcli-devel = %{version}
Conflicts:      freeradius-client-devel
Conflicts:      radiusclient-ng-devel
Provides:       freeradius-client-devel

%description compat-devel
This package contains the compatibility headers and libraries for freeradius-client and radiusclient-ng.

%prep
%setup -q

%build
touch config.rpath
autoreconf -fiv
%configure \
    --disable-static \
    --disable-rpath \
    --with-nettle \
    --with-tls \
    --enable-legacy-compat
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post   -n libradcli%{sover} -p /sbin/ldconfig
%postun -n libradcli%{sover} -p /sbin/ldconfig

%files
%license COPYRIGHT
%doc AUTHORS NEWS README.md
%dir %{_sysconfdir}/radcli
%config(noreplace) %{_sysconfdir}/radcli/radiusclient-tls.conf
%config(noreplace) %{_sysconfdir}/radcli/radiusclient.conf
%config(noreplace) %{_sysconfdir}/radcli/servers
%config(noreplace) %{_sysconfdir}/radcli/servers-tls
%{_datadir}/radcli

%files -n libradcli%{sover}
%{_libdir}/libradcli.so.%{sover}*

%files devel
%dir %{_includedir}/radcli
%{_includedir}/radcli/radcli.h
%{_includedir}/radcli/version.h
%{_libdir}/libradcli.so
%{_libdir}/pkgconfig/radcli.pc
%{_mandir}/man3/*.3%{?ext_man}

%files compat-devel
%{_includedir}/freeradius-client.h
%{_includedir}/radiusclient-ng.h
%{_libdir}/libfreeradius-client.so
%{_libdir}/libradiusclient-ng.so

%changelog
