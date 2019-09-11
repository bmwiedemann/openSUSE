#
# spec file for package boringssl
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 0
%define libname libboringssl%{sover}

Name:           boringssl
Version:        20181228
Release:        0
Summary:        An SSL/TLS protocol implementation
License:        OpenSSL
Group:          Development/Libraries/C and C++
Url:            https://boringssl.googlesource.com/boringssl/
Source:         %{name}-%{version}.tar.xz
Patch0:         add-soversion-option.patch
Patch1:         0001-crypto-Fix-aead_test-build-on-aarch64.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  go

%description
BoringSSL is an implementation of the Secure Sockets Layer (SSL) and
Transport Layer Security (TLS) protocols, derived from OpenSSL.

%package -n %{libname}
Summary:        An SSL/TLS protocol implementation
Group:          Productivity/Networking/Security
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake \
    -DCMAKE_C_FLAGS="%{optflags} -pthread" \
    -DCMAKE_CXX_FLAGS="%{optflags} -pthread" \
    -DSOVERSION=1
%make_jobs

%install
install -D -m0755 build/crypto/libcrypto.so.%{sover} %{buildroot}%{_libdir}/libboringssl_crypto.so.%{sover}
install -D -m0755 build/crypto/libcrypto.so %{buildroot}%{_libdir}/libboringssl_crypto.so
install -D -m0755 build/ssl/libssl.so.%{sover} %{buildroot}%{_libdir}/libboringssl_ssl.so.%{sover}
install -D -m0755 build/ssl/libssl.so %{buildroot}%{_libdir}/libboringssl_ssl.so
install -D -m0755 build/decrepit/libdecrepit.so.%{sover} %{buildroot}%{_libdir}/libboringssl_decrepit.so.%{sover}
install -D -m0755 build/decrepit/libdecrepit.so %{buildroot}%{_libdir}/libboringssl_decrepit.so
install -D -m0755 build/libboringssl_gtest.so.%{sover} %{buildroot}%{_libdir}/libboringssl_gtest.so.%{sover}
install -D -m0755 build/libboringssl_gtest.so %{buildroot}%{_libdir}/libboringssl_gtest.so

# To avoid conflicts with openssl development files, change all includes from
# openssl to boringssl.
# BoringSSL headers provided by this pachage are installed in
# /usr/include/boringssl for the same reason.
find include/openssl -type f -exec sed -i 's/openssl/boringssl/' "{}" +

find include/openssl -type f -execdir install -D -m0644 "{}" "%{buildroot}%{_includedir}/boringssl/{}" \;

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README.md
%license LICENSE
%{_libdir}/libboringssl_crypto.so.%{sover}
%{_libdir}/libboringssl_ssl.so.%{sover}
%{_libdir}/libboringssl_decrepit.so.%{sover}
%{_libdir}/libboringssl_gtest.so.%{sover}

%files devel
%{_includedir}/boringssl
%{_libdir}/libboringssl_crypto.so
%{_libdir}/libboringssl_ssl.so
%{_libdir}/libboringssl_decrepit.so
%{_libdir}/libboringssl_gtest.so

%changelog
