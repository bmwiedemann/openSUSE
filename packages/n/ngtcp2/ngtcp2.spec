#
# spec file for package ngtcp2
#
# Copyright (c) 2025 SUSE LLC
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


%global soname  libngtcp2
%global sover   16
%global gnutls_soname libngtcp2_crypto_gnutls
%global gnutls_sover 8
Name:           ngtcp2
Version:        1.12.0
Release:        0
Summary:        Implementation of the IETF QUIC protocol
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://nghttp2.org/ngtcp2
Source0:        https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
Source1:        https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz.asc
Source2:        ngtcp2.keyring
Source3:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gnutls) >= 3
BuildRequires:  pkgconfig(libnghttp3) >= 1.0.0

%description
ngtcp2 is an implementation of the QUIC protocol (RFC 9000)
with a C library API.

%package -n %{soname}-%{sover}
Summary:        Implementation of the IETF QUIC protocol
Group:          System/Libraries

%description -n %{soname}-%{sover}
ngtcp2 is an implementation of the QUIC protocol (RFC 9000)
with a C library API.

%package -n %{gnutls_soname}%{gnutls_sover}
Summary:        The ngtcp2 crypto API with GNUTLS as a backend
Group:          System/Libraries

%description -n %{gnutls_soname}%{gnutls_sover}
ngtcp2 is an implementation of the QUIC protocol (RFC 9000).
This package contains the crypto API of ngtcp2, which was built using
GNUTLS as the cryptographic provider.

%package -n python3-ngtcp2
Summary:        Python3 bindings for ngtcp2
Group:          Development/Libraries/Python

%description -n python3-ngtcp2
Python bindings for the ngtcp2 implementation of the QUIC protocol.

%package devel
Summary:        Development files for ngtcp2
Group:          Development/Languages/C and C++
Requires:       %{gnutls_soname}%{gnutls_sover} = %{version}
Requires:       %{soname}-%{sover} = %{version}
Provides:       libngtcp2-devel = %{version}-%{release}
Obsoletes:      libngtcp2-devel < %{version}-%{release}

%description devel
Development files for use with libngtcp2, which implements the
QUIC protocol.

%package doc
Summary:        Documentation for ngtcp2
Group:          Documentation/HTML

%description doc
Documentation for ngtcp2, which includes shared C libraries.

%prep
%autosetup -n ngtcp2-%{version} -p1

%build
%configure \
  --disable-static        \
  --disable-silent-rules  \
  --enable-lib-only       \
  --with-libnghttp3       \
  --with-gnutls           \
  --without-openssl       \
  --without-libev         \
  %{nil}
%make_build all

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

# Do not ship this
rm -rf %{buildroot}%{_datadir}/doc/ngtcp2

# None of applications using these man pages are built.
rm -rf %{buildroot}%{_mandir}/man1/* \
  doc/manual/html/.buildinfo

%check
%make_build check

%ldconfig_scriptlets -n %{soname}-%{sover}
%ldconfig_scriptlets -n %{gnutls_soname}%{gnutls_sover}

%files -n %{soname}-%{sover}
%license COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{gnutls_soname}%{gnutls_sover}
%license COPYING
%{_libdir}/%{gnutls_soname}.so.%{gnutls_sover}*

%files devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*.h
%{_libdir}/%{soname}.so
%{_libdir}/%{gnutls_soname}.so
%{_libdir}/pkgconfig/%{soname}.pc
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc

%changelog
