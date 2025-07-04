#
# spec file for package aws-lc
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


%define         sover 1_54_0
%define         __builder ninja
Name:           aws-lc
Version:        1.54.0
Release:        0
Summary:        Checksums package for AWS SDK for C
License:        Apache-2.0
URL:            https://github.com/aws/aws-lc
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# integration test needs internet
Patch0:         disable-integrationtest.patch
Patch1:         vendor-fix.patch
Patch2:         soname.patch
BuildRequires:  clang
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
BuildRequires:  go
BuildRequires:  libstdc++-devel
BuildRequires:  llvm-gold
BuildRequires:  ninja
BuildRequires:  cmake(aws-c-common)
BuildRequires:  pkgconfig(libunwind)
Conflicts:      libressl
Conflicts:      openssl
ExcludeArch:    %{arm}

%description
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.

%package devel
Summary:        AWS-LC development headers
Requires:       libssl%{sover} = %{version}
Conflicts:      libopenssl-3-devel
Conflicts:      libressl-devel

%description devel
AWS-LC is a general-purpose cryptographic library maintained by the AWS
Cryptography team for AWS and their customers. It іs based on code from the
Google BoringSSL project and the OpenSSL project.

%package -n libssl%{sover}
Summary:        Library file for %{name}

%description -n libssl%{sover}
%{summary}.

%package -n libcrypto%{sover}
Summary:        Crypto library for %{name}

%description -n libcrypto%{sover}
%{summary}.

%package benchmark
Summary:        Benchmarktool for %{name}

%description benchmark
%{summary}.

%prep
%autosetup -a1 -p1
sed -i 's|project(AWSLC VERSION @@VERSION@@)|project(AWSLC VERSION %{version})|g' CMakeLists.txt

%build
%cmake -DCMAKE_C_FLAGS="-Wno-error=unused-variable -Wno-error=stringop-overflow="
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}
# fix shebang
sed -i 's|/usr/bin/env bash|/usr/bin/bash|g' %{buildroot}%{_bindir}/c_rehash

%ldconfig_scriptlets -n libssl%{sover}
%ldconfig_scriptlets -n libcrypto%{sover}

%check
%ninja_build -C build run_tests

%files
%{_bindir}/openssl
%{_bindir}/c_rehash

%files benchmark
%{_bindir}/bssl

%files devel
%dir %{_libdir}/crypto
%dir %{_libdir}/ssl
%{_includedir}/openssl
%{_libdir}/crypto/cmake
%{_libdir}/libcrypto.so
%{_libdir}/libssl.so
%{_libdir}/pkgconfig/libcrypto.pc
%{_libdir}/pkgconfig/libssl.pc
%{_libdir}/pkgconfig/openssl.pc
%{_libdir}/ssl/cmake/

%files -n libssl%{sover}
%{_libdir}/libssl.so.%{version}

%files -n libcrypto%{sover}
%{_libdir}/libcrypto.so.%{version}

%changelog
