#
# spec file for package aws-crt-cpp
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


%define library_version 1.0.0
%define library_soversion 1

Name:           aws-crt-cpp
Version:        0.26.11
Release:        0
Summary:        AWS C++ wrapper for AWS SDK C libraries
License:        Apache-2.0
Group:          Development/Languages/Other
URL:            https://aws.amazon.com/sdk-for-cpp/
Source0:        https://github.com/awslabs/aws-crt-cpp/archive/v%{version}.tar.gz
Patch0:         acc_fix-cmake-modules-path.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  cmake(aws-c-auth)
BuildRequires:  cmake(aws-c-cal)
BuildRequires:  cmake(aws-c-common)
BuildRequires:  cmake(aws-c-compression)
BuildRequires:  cmake(aws-c-event-stream)
BuildRequires:  cmake(aws-c-http)
BuildRequires:  cmake(aws-c-io)
BuildRequires:  cmake(aws-c-mqtt)
BuildRequires:  cmake(aws-c-s3)
BuildRequires:  cmake(aws-c-sdkutils)
BuildRequires:  cmake(aws-checksums)
BuildRequires:  cmake(s2n)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)

%description
The AWS SDK for C++ provides a modern C++ (version C++ 11 or later) interface for
Amazon Web Services (AWS). It is meant to be performant and fully functioning with
low- and high-level SDKs, while minimizing dependencies and providing platform
portability (Windows, OSX, Linux, and mobile).

%package bin
Summary:        AWS C++ wrapper for AWS SDK C libraries - application binaries
Group:          Development/Languages/Other

%description bin
AWS C++ wrapper for the following AWS SDK C libraries

 * aws-c-common: Cross-platform primitives and data structures.
 * aws-c-io: Cross-platform event-loops, non-blocking I/O, and TLS implementations.
 * aws-c-mqtt: MQTT client.
 * aws-c-auth: Auth signers such as Aws-auth sigv4
 * aws-c-http: HTTP 1.1 client, and websockets (H2 coming soon)
 * aws-checksums: Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations.
 * aws-c-event-stream: C99 implementation of the vnd.amazon.event-stream content-type.

This package contains application binaries.

%package -n lib%{name}%{library_soversion}
Summary:        AWS C++ wrapper for AWS SDK C libraries
Group:          Development/Languages/Other

%description -n lib%{name}%{library_soversion}
AWS C++ wrapper for the following AWS SDK C libraries

 * aws-c-common: Cross-platform primitives and data structures.
 * aws-c-io: Cross-platform event-loops, non-blocking I/O, and TLS implementations.
 * aws-c-mqtt: MQTT client.
 * aws-c-auth: Auth signers such as Aws-auth sigv4
 * aws-c-http: HTTP 1.1 client, and websockets (H2 coming soon)
 * aws-checksums: Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations.
 * aws-c-event-stream: C99 implementation of the vnd.amazon.event-stream content-type.

This package contains the shared libraries.

%package devel
Summary:        AWS C++ wrapper for AWS SDK C libraries - development files
Group:          Development/Languages/Other
Requires:       lib%{name}%{library_soversion} = %{version}

%description devel
AWS C++ wrapper for the following AWS SDK C libraries

 * aws-c-common: Cross-platform primitives and data structures.
 * aws-c-io: Cross-platform event-loops, non-blocking I/O, and TLS implementations.
 * aws-c-mqtt: MQTT client.
 * aws-c-auth: Auth signers such as Aws-auth sigv4
 * aws-c-http: HTTP 1.1 client, and websockets (H2 coming soon)
 * aws-checksums: Cross-Platform HW accelerated CRC32c and CRC32 with fallback to efficient SW implementations.
 * aws-c-event-stream: C99 implementation of the vnd.amazon.event-stream content-type.

This package contains development files.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DEPS=OFF \
    -DCMAKE_MODULE_PATH=%{_libdir}/cmake
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}%{_libdir}/cmake

# Testsuite requires network connection
#%%check
#%%ctest

%files bin
%{_bindir}/*

%files -n lib%{name}%{library_soversion}
%doc README.md
%{_libdir}/libaws*so

%files devel
%{_includedir}/aws
%{_libdir}/cmake

%changelog
