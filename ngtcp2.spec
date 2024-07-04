#
# spec file for package ngtcp2
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.6.0
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
ngtcp2 is an effort to implement RFC9000 QUIC protocol.

%package -n %{soname}-%{sover}
Summary:        Shared library for ngtcp2
Group:          System/Libraries

%description -n %{soname}-%{sover}
Shared C libraries for implementation of QUIC Protocol

%package -n %{gnutls_soname}%{gnutls_sover}
Summary:        Shared library for ngtcp2 - GNUTLS backend
Group:          System/Libraries

%description -n %{gnutls_soname}%{gnutls_sover}
Shared C libraries for implementation of QUIC Protocol - GNUTLS backend

%package -n python3-ngtcp2
Summary:        Python3 bindings for ngtcp2
Group:          Development/Libraries/Python

%description -n python3-ngtcp2
Python bindings for implementation of QUIC Protocol

%package -n %{soname}-devel
Summary:        Development files for ngtcp2
Group:          Development/Languages/C and C++
Requires:       %{gnutls_soname}%{gnutls_sover} = %{version}
Requires:       %{soname}-%{sover} = %{version}
Provides:       %{name}-devel

%description -n %{soname}-devel
Development files for usage with libngtcp2, which implements
QUIC Protocol.

%package doc
Summary:        Documentation for ngtcp2
Group:          Documentation/HTML

%description doc
Documentation for ngtcp2, which includes a shared C library

%prep
%setup -q -n ngtcp2-%{version}

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

%files -n %{soname}-devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/*.h
%{_libdir}/%{soname}.so
%{_libdir}/%{gnutls_soname}.so
%{_libdir}/pkgconfig/%{soname}.pc
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc

%changelog
