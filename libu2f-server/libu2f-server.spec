#
# spec file for package libu2f-server
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soname  0
Name:           libu2f-server
Version:        1.1.0
Release:        0
Summary:        Yubico Universal 2nd Factor (U2F) Server C Library
License:        BSD-2-Clause
Group:          Productivity/Networking/Security
Url:            https://developers.yubico.com/
Source0:        https://developers.yubico.com/libu2f-server/Releases/%{name}-%{version}.tar.xz
Source1:        https://developers.yubico.com/libu2f-server/Releases/%{name}-%{version}.tar.xz.sig
BuildRequires:  gengetopt
BuildRequires:  help2man
BuildRequires:  libhidapi-devel
BuildRequires:  libtool
BuildRequires:  libzip
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(json-c) >= 0.10
BuildRequires:  pkgconfig(openssl)

%description
This is a C library that implements the server-side of the U2F protocol.
More precisely, it provides an API for generating the JSON blobs required
by U2F devices to perform the U2F Registration and U2F Authentication
operations, and functionality for verifying the cryptographic operations.

%package     -n %{name}%{soname}
Summary:        Library for Universal 2nd Factor (U2F)
Group:          Productivity/Networking/Security

%description -n %{name}%{soname}
Libu2f-server provide a C library that implements
the server-side of the U2F protocol. There are APIs to talk to a U2F
device and perform the U2F Register and U2F Authenticate operations.

%package     -n %{name}-devel
Summary:        Development files for Universal 2nd Factor (U2F)
Group:          Development/Libraries/C and C++
Requires:       %{name}%{soname} = %{version}

%description -n %{name}-devel
This package contains the header file needed to develop applications that
use Universal 2nd Factor (U2F).

%package     -n u2f-server
Summary:        Tool to support Yubico's Universal 2nd Factor (U2F)
Group:          Productivity/Networking/Security
Requires:       %{name}%{soname} = %{version}

%description -n u2f-server

Command line tool that implements the server-side of the Universal 2nd Factor (U2F) protocol

%prep
%setup -q

%build
%configure --disable-static
make   %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{name}%{soname} -p /sbin/ldconfig
%postun -n %{name}%{soname} -p /sbin/ldconfig

%files -n %{name}%{soname}
%{_libdir}/%{name}.so.%{soname}
%{_libdir}/%{name}.so.%{soname}.1.0

%files -n %{name}-devel
%dir %{_includedir}/u2f-server
%{_includedir}/u2f-server/u2f-server.h
%{_includedir}/u2f-server/u2f-server-version.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*

%files -n u2f-server
%doc AUTHORS NEWS ChangeLog README
%license COPYING
%{_bindir}/u2f-server
%{_mandir}/man1/u2f-server.1%{ext_man}

%changelog
