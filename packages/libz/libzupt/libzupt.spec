#
# spec file for package libzupt
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2026 Alessandro de Oliveira Faria (A.K.A CABELO) <cabelo@opensuse.org>
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

Name:           libzupt
Version:        1.0.8
Release:        0
Summary:        Post-quantum hybrid cryptography library
License:        MIT
URL:            https://github.com/cabelo/libzupt
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
libzupt is a library that provides encryption and decryption of files and binary data in memory using post-quantum hybrid cryptography ML-KEM-768 + X25519 in various languages. The libzupt is an SDK designed to simplify the implementation of encryption and decryption for files and in-memory binary data, using a modern approach based on hybrid post-quantum cryptography ML-KEM-768 + X25519. 

%package -n libzupt1
Summary:        Post-quantum hybrid cryptography library

%description -n libzupt1
libzupt1 provides the shared runtime library for applications that use
libzupt for post-quantum hybrid cryptography based on ML-KEM-768 + X25519.

%package devel
Summary:        Development files for libzupt
Requires:       libzupt1 = %{version}-%{release}

%description devel
The %{name}-devel package contains library and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -ffat-lto-objects"
export CXXFLAGS="%{optflags} -ffat-lto-objects"

%cmake  \
	-DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_C_FLAGS_RELEASE:STRING="$CFLAGS" \
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="$CXXFLAGS" \
	-DLIBZUPT_BUILD_TESTS=ON \
	 %{nil}
%cmake_build 

%post -n libzupt1 -p /sbin/ldconfig
%postun -n libzupt1 -p /sbin/ldconfig

%check
ctest --output-on-failure

%install
%cmake_install
strip --strip-unneeded %{buildroot}%{_libdir}/libzupt.so.1.0.6 || :

%files -n libzupt1
%license LICENSE
%{_libdir}/libzupt.so.1*
%exclude %{_bindir}/*

%files devel
%dir %{_libdir}/cmake/libzupt
%{_includedir}/*
%{_libdir}/libzupt.so
%{_libdir}/libzupt_static.a
%{_libdir}/pkgconfig/libzupt.pc
%{_libdir}/cmake/libzupt/*.cmake

%changelog
