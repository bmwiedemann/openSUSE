#
# spec file for package boringssl
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


%define sover 1
%define libname libboringssl%{sover}
%define src_install_dir /usr/src/%{name}
Name:           boringssl
Version:        20200122
Release:        0
Summary:        An SSL/TLS protocol implementation
License:        OpenSSL
Group:          Development/Sources
URL:            https://boringssl.googlesource.com/boringssl/
Source:         %{name}-%{version}.tar.xz
Patch0:         0002-crypto-Fix-aead_test-build-on-aarch64.patch
Patch1:         0003-enable-s390x-builds.patch
Patch2:         0004-fix-alignment-for-ppc64le.patch
Patch3:         0005-fix-alignment-for-arm.patch
BuildRequires:  cmake >= 3.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  go
BuildRequires:  libunwind-devel
BuildRequires:  ninja
BuildRequires:  patchelf
ExclusiveArch:  %{ix86} x86_64 aarch64 s390x ppc64le %arm

%description
BoringSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols, derived from OpenSSL.

%package -n %{libname}
Summary:        An SSL/TLS protocol implementation
Group:          System/Libraries
Recommends:     ca-certificates-mozilla

%description -n %{libname}
BoringSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols, derived from OpenSSL.

%package devel
Summary:        Development files for BoringSSL
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Development files for BoringSSL - an implementation of the Secure
Sockets Layer (SSL) and Transport Layer Security (TLS) protocols,
derived from OpenSSL.

%package source
Summary:        Source code of BoringSSL
Group:          Development/Sources
BuildArch:      noarch

%description source
Source files for BoringSSL implementation

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now"
%cmake_build

%install
# Install libraries
install -D -m0755 build/libcrypto.so %{buildroot}%{_libdir}/libboringssl_crypto.so.%{sover}
install -D -m0755 build/libssl.so %{buildroot}%{_libdir}/libboringssl_ssl.so.%{sover}
# Add SOVER to SONAME fields in libraries
patchelf --set-soname libboringssl_crypto.so.%{sover} %{buildroot}%{_libdir}/libboringssl_crypto.so.%{sover}
patchelf --set-soname libboringssl_ssl.so.%{sover} %{buildroot}%{_libdir}/libboringssl_ssl.so.%{sover}
# Create links from *.so to *.so.SOVER
ln -sf libboringssl_crypto.so.%{sover} %{buildroot}%{_libdir}/libboringssl_crypto.so
ln -sf libboringssl_ssl.so.%{sover} %{buildroot}%{_libdir}/libboringssl_ssl.so

# Install sources
rm -rf build/
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}
# Fix arch-independent-package-contains-binary-or-object
find %{buildroot}%{src_install_dir} -type f \( -name "*.a" -o -name "*.lib" -o -name "*.o" \) -exec rm -f "{}" +
# Fix non-executable-script warning.
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec chmod +x "{}" +
# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.pl" -exec sed -i 's|#!.*/usr/bin/env perl|#!/usr/bin/perl|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!.*/usr/bin/env python.*|#!/usr/bin/python3|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.sh" -exec sed -i 's|#!.*/usr/bin/env bash|#!/bin/bash|' "{}" +

# To avoid conflicts with openssl development files, change all includes from
# openssl to boringssl.
# BoringSSL headers provided by this pachage are installed in
# /usr/include/boringssl for the same reason.
find src/include/openssl -type f -exec sed -i 's/openssl/boringssl/' "{}" +

find src/include/openssl -type f -execdir install -D -m0644 "{}" "%{buildroot}%{_includedir}/boringssl/{}" \;

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc src/README.md
%license LICENSE
%{_libdir}/libboringssl_crypto.so.%{sover}
%{_libdir}/libboringssl_ssl.so.%{sover}

%files devel
%{_includedir}/boringssl
%{_libdir}/libboringssl_crypto.so
%{_libdir}/libboringssl_ssl.so

%files source
%{src_install_dir}

%changelog
