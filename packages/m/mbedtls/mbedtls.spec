#
# spec file for package mbedtls
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


%define lib_tls     libmbedtls21
%define lib_crypto  libmbedcrypto16
%define lib_x509    libmbedx509-7
%define lib_everest libeverest
%define lib_p256m   libp256m
Name:           mbedtls
Version:        3.6.5
Release:        0
Summary:        Libraries for crypto and SSL/TLS protocols
License:        Apache-2.0 OR GPL-2.0-or-later
URL:            https://tls.mbed.org
Source:         %{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FEATURE-OPENSUSE - enable MBEDTLS_THREADING_PTHREAD and MBEDTLS_THREADING_C
Patch1:         mbedtls-enable-pthread.patch
# PATCH-FEATURE-OPENSUSE - enable MBEDTLS_SSL_DTLS_SRTP
Patch2:         mbedtls-enable-srtp.patch
BuildRequires:  cmake
BuildRequires:  ninja
%{?suse_build_hwcaps_libs}

%description
mbedtls implements the SSL3, TLS 1.0, 1.1 and 1.2 protocols. It
supports a number of extensions such as SSL Session Tickets (RFC
5077), Server Name Indication (SNI) (RFC 6066), Truncated HMAC (RFC
6066), Max Fragment Length (RFC 6066), Secure Renegotiation (RFC
5746) and Application Layer Protocol Negotiation (ALPN). It
understands the RSA, (EC)DH(E)-RSA, (EC)DH(E)-PSK and RSA-PSK key
exchanges.

%package -n %{lib_tls}
Summary:        Transport Layer Security protocol suite

%description -n %{lib_tls}
mbedtls implements the SSL 3.0, TLS 1.0, 1.1 and 1.2 protocols. It
supports a number of extensions such as SSL Session Tickets (RFC
5077), Server Name Indication (SNI) (RFC 6066), Truncated HMAC (RFC
6066), Max Fragment Length (RFC 6066), Secure Renegotiation (RFC
5746) and Application Layer Protocol Negotiation (ALPN). It
understands the RSA, (EC)DH(E)-RSA, (EC)DH(E)-PSK and RSA-PSK key
exchanges.

%package -n %{lib_crypto}
Summary:        Cryptographic base library for mbedtls

%description -n %{lib_crypto}
This subpackage of mbedtls contains a library that exposes
cryptographic ciphers, hashes, algorithms and format support such as
AES, MD5, SHA, Elliptic Curves, BigNum, PKCS, ASN.1, BASE64.

%package -n %{lib_x509}
Summary:        Library to work with X.509 certificates

%description -n %{lib_x509}
This subpackage of mbedtls contains a library that can read, verify
and write X.509 certificates, read/write Certificate Signing Requests
and read Certificate Revocation Lists.

%package -n %{lib_everest}
Summary:        Library libeverest

%description -n %{lib_everest}
This subpackage of mbedtls contains libeverest

%package -n %{lib_p256m}
Summary:        Library libp256m

%description -n %{lib_p256m}
This subpackage of mbedtls contains libp256m

%package devel
Summary:        Development files for mbedtls, a SSL/TLS library
Requires:       %{lib_crypto} = %{version}
Requires:       %{lib_everest} = %{version}
Requires:       %{lib_p256m} = %{version}
Requires:       %{lib_tls} = %{version}
Requires:       %{lib_x509} = %{version}

%description devel
This subpackage contains the development files for mbedtls,
a suite of libraries for cryptographic functions and the
SSL/TLS protocol suite.

%prep
%autosetup -p1

%build
%define __builder ninja
export CFLAGS="%{optflags} -Wno-stringop-overflow -Wno-maybe-uninitialized"
export CXXLAGS="%{optflags} -Wno-stringop-overflow -Wno-maybe-uninitialized"
%cmake \
  -DUNSAFE_BUILD=ON \
  -DLINK_WITH_PTHREAD=ON \
  -DINSTALL_MBEDTLS_HEADERS=ON \
  -DUSE_SHARED_MBEDTLS_LIBRARY=ON \
  -DUSE_STATIC_MBEDTLS_LIBRARY=OFF \
  -DENABLE_PROGRAMS=OFF \
  -DCMAKE_POLICY_DEFAULT_CMP0012=NEW
%cmake_build

%install
%cmake_install

%check
pushd build
LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
 %{_bindir}/ctest --output-on-failure --force-new-ctest-process

%ldconfig_scriptlets -n %{lib_tls}
%ldconfig_scriptlets -n %{lib_crypto}
%ldconfig_scriptlets -n %{lib_x509}
%ldconfig_scriptlets -n %{lib_everest}
%ldconfig_scriptlets -n %{lib_p256m}

%files devel
%license LICENSE
%doc ChangeLog README.md
%dir %{_includedir}/mbedtls
%dir %{_includedir}/psa
%dir %{_includedir}/everest
%dir %{_includedir}/everest/kremlin
%dir %{_includedir}/everest/kremlin/internal
%dir %{_includedir}/everest/kremlib
%dir %{_includedir}/everest/vs2013
%dir %{_libdir}/cmake/MbedTLS
%{_libdir}/cmake/MbedTLS/*
%{_includedir}/mbedtls/*.h
%{_includedir}/psa/*.h
%{_includedir}/everest/*.h
%{_includedir}/everest/kremlin/*.h
%{_includedir}/everest/kremlin/internal/*.h
%{_includedir}/everest/kremlib/*.h
%{_includedir}/everest/vs2013/*.h
%{_libdir}/libmbedtls.so
%{_libdir}/libmbedcrypto.so
%{_libdir}/libmbedx509.so
%{_libdir}/pkgconfig/*.pc

%files -n %{lib_tls}
%license LICENSE
%{_libdir}/libmbedtls.so.*

%files -n %{lib_crypto}
%license LICENSE
%{_libdir}/libmbedcrypto.so.*

%files -n %{lib_x509}
%license LICENSE
%{_libdir}/libmbedx509.so.*

%files -n %{lib_everest}
%license LICENSE
%{_libdir}/libeverest.so

%files -n %{lib_p256m}
%license LICENSE
%{_libdir}/libp256m.so

%changelog
