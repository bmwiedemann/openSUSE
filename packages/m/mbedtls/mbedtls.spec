#
# spec file for package mbedtls
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


%define lib_tls     libmbedtls23
%define lib_x509    libmbedx509-9
%define lib_tfpsa   libtfpsacrypto2
Name:           mbedtls
Version:        4.1.0
Release:        0
Summary:        Libraries for crypto and SSL/TLS protocols
License:        Apache-2.0 OR GPL-2.0-or-later
URL:            https://www.trustedfirmware.org/projects/mbed-tls/
Source:         https://github.com/Mbed-TLS/mbedtls/releases/download/mbedtls-%{version}/mbedtls-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM mbedtls-fix-libmbedcrypto-compat-install.patch gh#Mbed-TLS/mbedtls#10777 -- install the libmbedcrypto compat library with executable permissions
Patch0:         mbedtls-fix-libmbedcrypto-compat-install.patch
BuildRequires:  cmake
BuildRequires:  ninja
BuildRequires:  python3
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

%package -n %{lib_x509}
Summary:        Library to work with X.509 certificates

%description -n %{lib_x509}
This subpackage of mbedtls contains a library that can read, verify
and write X.509 certificates, read/write Certificate Signing Requests
and read Certificate Revocation Lists.

%package -n %{lib_tfpsa}
Summary:        Trusted Firmware PSA cryptography library

%description -n %{lib_tfpsa}
TF-PSA-Crypto is the reference implementation of the PSA cryptography
API. It provides the cryptographic primitives used by Mbed TLS 4.x.

This package also ships the libmbedcrypto backward-compatibility
library, which has the same SONAME (libtfpsacrypto.so.2).

%package devel
Summary:        Development files for mbedtls, a SSL/TLS library
Requires:       %{lib_tfpsa} = %{version}
Requires:       %{lib_tls} = %{version}
Requires:       %{lib_x509} = %{version}

%description devel
This subpackage contains the development files for mbedtls,
a suite of libraries for cryptographic functions and the
SSL/TLS protocol suite.

%prep
%autosetup -p1
# Enable threading and DTLS-SRTP support (previously carried as
# the mbedtls-enable-pthread.patch / mbedtls-enable-srtp.patch
# downstream patches, now set via the upstream config tool).
python3 scripts/config.py set MBEDTLS_THREADING_C
python3 scripts/config.py set MBEDTLS_THREADING_PTHREAD
python3 scripts/config.py set MBEDTLS_SSL_DTLS_SRTP

%build
%define __builder ninja
%cmake \
  -DUSE_SHARED_MBEDTLS_LIBRARY=ON \
  -DUSE_STATIC_MBEDTLS_LIBRARY=OFF \
  -DUSE_SHARED_TF_PSA_CRYPTO_LIBRARY=ON \
  -DUSE_STATIC_TF_PSA_CRYPTO_LIBRARY=OFF \
  -DENABLE_PROGRAMS=OFF \
  -DMBEDTLS_FATAL_WARNINGS=OFF \
  -DTF_PSA_CRYPTO_FATAL_WARNINGS=OFF \
  -DLINK_WITH_PTHREAD=ON
%cmake_build

%install
%cmake_install
# Create the libmbedcrypto compatibility symlinks. Upstream creates these
# via an install(CODE) rule that does not reach the staged (DESTDIR) tree.
ln -sf libmbedcrypto.so.%{version} %{buildroot}%{_libdir}/libmbedcrypto.so.18
ln -sf libmbedcrypto.so.18 %{buildroot}%{_libdir}/libmbedcrypto.so

%check
pushd build
LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
 %{_bindir}/ctest --output-on-failure --force-new-ctest-process
popd

%ldconfig_scriptlets -n %{lib_tls}
%ldconfig_scriptlets -n %{lib_x509}
%ldconfig_scriptlets -n %{lib_tfpsa}

%files devel
%license LICENSE
%doc ChangeLog README.md
%{_includedir}/mbedtls/
%{_includedir}/psa/
%{_includedir}/tf-psa-crypto/
%{_libdir}/libmbedtls.so
%{_libdir}/libmbedcrypto.so
%{_libdir}/libmbedx509.so
%{_libdir}/libtfpsacrypto.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/

%files -n %{lib_tls}
%license LICENSE
%{_libdir}/libmbedtls.so.*

%files -n %{lib_x509}
%license LICENSE
%{_libdir}/libmbedx509.so.*

%files -n %{lib_tfpsa}
%license LICENSE
%{_libdir}/libtfpsacrypto.so.*
# libmbedcrypto backward-compatibility library (SONAME libtfpsacrypto.so.2)
%{_libdir}/libmbedcrypto.so.18
%{_libdir}/libmbedcrypto.so.%{version}

%changelog
