#
# spec file for package mbedtls
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


%define lib_tls    libmbedtls12
%define lib_crypto libmbedcrypto3
%define lib_x509   libmbedx509-0
Name:           mbedtls
Version:        2.16.5
Release:        0
Summary:        Libraries for crypto and SSL/TLS protocols
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://tls.mbed.org
Source:         https://tls.mbed.org/download/%{name}-%{version}-apache.tgz
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpkcs11-helper-1)
BuildRequires:  pkgconfig(zlib)

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
Group:          System/Libraries

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
Group:          System/Libraries

%description -n %{lib_crypto}
This subpackage of mbedtls contains a library that exposes
cryptographic ciphers, hashes, algorithms and format support such as
AES, MD5, SHA, Elliptic Curves, BigNum, PKCS, ASN.1, BASE64.

%package -n %{lib_x509}
Summary:        Library to work with X.509 certificates
Group:          System/Libraries

%description -n %{lib_x509}
This subpackage of mbedtls contains a library that can read, verify
and write X.509 certificates, read/write Certificate Signing Requests
and read Certificate Revocation Lists.

%package devel
Summary:        Development files for mbedtls, a SSL/TLS library
Group:          Development/Libraries/C and C++
Requires:       %{lib_crypto} = %{version}
Requires:       %{lib_tls} = %{version}
Requires:       %{lib_x509} = %{version}

%description devel
This subpackage contains the development files for mbedtls,
a suite of libraries for cryptographic functions and the
SSL/TLS protocol suite.

%prep
%autosetup
sed -i 's|//\(#define MBEDTLS_ZLIB_SUPPORT\)|\1|' include/mbedtls/config.h
sed -i 's|//\(#define MBEDTLS_HAVEGE_C\)|\1|' include/mbedtls/config.h
sed -i 's|//\(#define MBEDTLS_THREADING_C\)|\1|' include/mbedtls/config.h
sed -i 's|//\(#define MBEDTLS_THREADING_PTHREAD\)|\1|' include/mbedtls/config.h

%build
%define __builder ninja
%cmake \
  -DLINK_WITH_PTHREAD=ON \
  -DUSE_PKCS11_HELPER_LIBRARY=ON \
  -DENABLE_ZLIB_SUPPORT=ON \
  -DINSTALL_MBEDTLS_HEADERS=ON \
  -DUSE_SHARED_MBEDTLS_LIBRARY=ON \
  -DUSE_STATIC_MBEDTLS_LIBRARY=OFF \
  -DENABLE_PROGRAMS=OFF
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{_builddir}/%{name}-%{version}/build/library
%ctest

%post -n %{lib_tls}      -p /sbin/ldconfig
%post -n %{lib_crypto}   -p /sbin/ldconfig
%post -n %{lib_x509}     -p /sbin/ldconfig
%postun -n %{lib_tls}    -p /sbin/ldconfig
%postun -n %{lib_crypto} -p /sbin/ldconfig
%postun -n %{lib_x509}   -p /sbin/ldconfig

%files devel
%license LICENSE
%doc ChangeLog README.md
%dir %{_includedir}/mbedtls
%{_includedir}/mbedtls/*.h
%{_libdir}/libmbedtls.so
%{_libdir}/libmbedcrypto.so
%{_libdir}/libmbedx509.so

%files -n %{lib_tls}
%license LICENSE
%{_libdir}/libmbedtls.so.*

%files -n %{lib_crypto}
%license LICENSE
%{_libdir}/libmbedcrypto.so.*

%files -n %{lib_x509}
%license LICENSE
%{_libdir}/libmbedx509.so.*

%changelog
