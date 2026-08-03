#
# spec file for package ngtcp2
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%global gnutls_soname %{soname}_crypto_gnutls
%global gnutls_sover 8
%global openssl_soname %{soname}_crypto_ossl
%global openssl_sover 0
%if 0%{?suse_version} >= 1699
%bcond_without openssl
%else
# requires OpenSSL 3.x with QUIC support
%bcond_with openssl
%endif
%if 0%{?suse_version} && 0%{?suse_version} < 1600
%global force_gcc_version 14
%endif
Name:           ngtcp2
Version:        1.25.0
Release:        0
Summary:        Implementation of the IETF QUIC protocol
License:        MIT
URL:            https://nghttp2.org/ngtcp2
Source0:        https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz
Source1:        https://github.com/ngtcp2/ngtcp2/releases/download/v%{version}/ngtcp2-%{version}.tar.xz.asc
Source2:        ngtcp2.keyring
Source3:        baselibs.conf
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gnutls) >= 3.7.3
%if %{with openssl}
BuildRequires:  pkgconfig(openssl) >= 1.1.1
%endif

%description
ngtcp2 is an implementation of the QUIC protocol (RFC 9000)
with a C library API.

%package -n %{soname}-%{sover}
Summary:        Implementation of the IETF QUIC protocol

%description -n %{soname}-%{sover}
ngtcp2 is an implementation of the QUIC protocol (RFC 9000)
with a C library API.

%package -n %{gnutls_soname}%{gnutls_sover}
Summary:        The ngtcp2 crypto API with GNUTLS as a backend

%description -n %{gnutls_soname}%{gnutls_sover}
ngtcp2 is an implementation of the QUIC protocol (RFC 9000).
This package contains the crypto API of ngtcp2, which was built using
GNUTLS as the cryptographic provider.

%package -n %{openssl_soname}%{openssl_sover}
Summary:        The ngtcp2 crypto API with OpenSSL as a backend

%description -n %{openssl_soname}%{openssl_sover}
ngtcp2 is an implementation of the QUIC protocol (RFC 9000).
This package contains the crypto API of ngtcp2, which was built using
OpenSSL as the cryptographic provider.

%package -n python3-ngtcp2
Summary:        Python3 bindings for ngtcp2

%description -n python3-ngtcp2
Python bindings for the ngtcp2 implementation of the QUIC protocol.

%package devel
Summary:        Development files for ngtcp2
Requires:       %{soname}-%{sover} = %{version}
Provides:       libngtcp2-devel = %{version}-%{release}
Obsoletes:      libngtcp2-devel < %{version}-%{release}

%description devel
Development files for use with libngtcp2, which implements the
QUIC protocol.

%package -n libngtcp2_crypto_gnutls-devel
Summary:        GnuTLS Development files for ngtcp2
Requires:       %{gnutls_soname}%{gnutls_sover} = %{version}
Requires:       libngtcp2-devel = %{version}-%{release}

%description -n libngtcp2_crypto_gnutls-devel
GnuTLS as TLS backend development files for use with libngtcp2.

%package -n libngtcp2_crypto_ossl-devel
Summary:        OpenSSL Development files for ngtcp2
Requires:       %{openssl_soname}%{openssl_sover} = %{version}
Requires:       libngtcp2-devel = %{version}-%{release}

%description -n libngtcp2_crypto_ossl-devel
OpenSSL as TLS backend development files for use with libngtcp2.
QUIC protocol.

%prep
%autosetup -n ngtcp2-%{version} -p1

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
# --enable-lib-only skips the examples, so the example-only dependencies
# (libnghttp3, libev) are never probed and must not be requested here.
%configure \
  --disable-static        \
  --disable-silent-rules  \
  --enable-lib-only       \
  --with-gnutls           \
%if %{with openssl}
  --with-openssl          \
%else
  --without-openssl       \
%endif
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
%ldconfig_scriptlets -n %{openssl_soname}%{openssl_sover}

%files -n %{soname}-%{sover}
%license COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{gnutls_soname}%{gnutls_sover}
%license COPYING
%{_libdir}/%{gnutls_soname}.so.%{gnutls_sover}*

%if %{with openssl}
%files -n %{openssl_soname}%{openssl_sover}
%license COPYING
%{_libdir}/%{openssl_soname}.so.%{openssl_sover}*
%endif

%files devel
%dir %{_includedir}/%{name}/
%{_includedir}/%{name}/ngtcp2.h
%{_includedir}/%{name}/ngtcp2_crypto.h
%{_includedir}/%{name}/version.h
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{soname}.pc

%files -n libngtcp2_crypto_gnutls-devel
%{_includedir}/%{name}/ngtcp2_crypto_gnutls.h
%{_libdir}/%{gnutls_soname}.so
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc

%if %{with openssl}
%files -n libngtcp2_crypto_ossl-devel
%{_includedir}/%{name}/ngtcp2_crypto_ossl.h
%{_libdir}/%{openssl_soname}.so
%{_libdir}/pkgconfig/libngtcp2_crypto_ossl.pc
%endif

%changelog
