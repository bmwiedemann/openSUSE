#
# spec file for package libretls
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 28
Name:           libretls
Version:        3.8.1
Release:        0
Summary:        Libtls for OpenSSL
License:        ISC AND BSD-3-Clause
URL:            https://git.causal.agency/libretls/about/
Source:         https://causal.agency/libretls/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libssl)

%description
LibreTLS is a port of libtls from LibreSSL to OpenSSL. libtls is “a new TLS
library, designed to make it easier to write foolproof applications”.

LibreTLS aims to make the libtls API more easily and widely available for
OpenSSL based systems. Specifically it uses the default CA locations of
OpenSSL.

# libressl also builds a libtls package, avoid clashes in case of identical shared library versions
%package libtls%{sover}
Summary:        Libtls for OpenSSL
Conflicts:      libtls%{sover}

%description libtls%{sover}
LibreTLS is a port of libtls from LibreSSL to OpenSSL. libtls is “a new TLS
library, designed to make it easier to write foolproof applications”.

LibreTLS aims to make the libtls API more easily and widely available for
OpenSSL based systems. Specifically it uses the default CA locations of
OpenSSL.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}-libtls%{sover} = %{version}
Conflicts:      libressl-devel

%description devel
LibreTLS is a port of libtls from LibreSSL to OpenSSL. libtls is “a new TLS
library, designed to make it easier to write foolproof applications”.

LibreTLS aims to make the libtls API more easily and widely available for
OpenSSL based systems. Specifically it uses the default CA locations of
OpenSSL.

This package contains the files needed to build with %{name}.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets libtls%{sover}

%files libtls%{sover}
%{_libdir}/libtls.so.%{sover}{,.*}

%files devel
%{_includedir}/tls.h
%{_libdir}/libtls.so
%{_mandir}/man3/*.3%{?ext_man}
%{_libdir}/pkgconfig/libtls.pc

%changelog
