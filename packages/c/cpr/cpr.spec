#
# spec file for package cpr
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2024 munix9@googlemail.com
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
%define mongv 7.7

%if "%{_vendor}" == "openEuler"
%bcond_with    tests
%else
%ifarch %{ix86}
%bcond_with    tests
%else
%bcond_without tests
%endif
%endif

Name:           cpr
Version:        1.14.2
Release:        0
Summary:        libcurl wrapper with a python-requests inspired API
License:        MIT
URL:            https://github.com/libcpr/cpr
Source0:        https://github.com/libcpr/cpr/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source10:       https://github.com/cesanta/mongoose/archive/%{mongv}.tar.gz#/mongoose-%{mongv}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  (ninja or ninja-build)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)

%if "%{?_vendor}" == "openEuler"
%define cmake_opts -S . -B $PWD/build
%define cmake_build cmake --build $PWD/build -j `nproc`
%define cmake_install DESTDIR="%{buildroot}" cmake --install $PWD/build
%endif

%description
C++ Requests is a wrapper around libcurl inspired by python-requests.

%package -n lib%{name}%{sover}
Summary:        libcurl wrapper with a python-requests inspired API

%description -n lib%{name}%{sover}
C++ Requests is a wrapper around libcurl inspired by python-requests.
Wrapped features include e.g. custom headers, various POST uploads,
various authentication methods, support for timeouts, cookie support,
and asynchronous requests.

%package devel
Summary:        The development files for libcpr
Requires:       lib%{name}%{sover} = %{version}

Requires:       libunistring-devel
Requires:       pkgconfig(libcurl)
Requires:       pkgconfig(libssl)
Requires:       pkgconfig(zlib)

%description devel
This package contains libraries and header files for developing
applications that use libcpr.

%prep
%autosetup -p1

# get mongoose src from local file
sed -e 's|URL .* https.*/cesanta/mongoose/.*\.tar\.gz$|URL file://%{SOURCE10}|' \
    -i CMakeLists.txt

%build
%define __builder ninja
%set_build_flags
export CFLAGS="$CFLAGS -Wno-error=deprecated-declarations"
%if 0%{?suse_version} <= 1500
export CFLAGS="$CFLAGS -pthread"
%endif
export CXXFLAGS="$CFLAGS"
export TEST=OFF
%if %{with tests}
export TEST=ON
%endif

%cmake -DCPR_BUILD_TESTS=$TEST -DCPR_BUILD_TESTS_PROXY=OFF -DCPR_BUILD_TESTS_SSL=$TEST \
  -DCPR_ENABLE_CURL_HTTP_ONLY=ON -DCPR_DEBUG_SANITIZER_FLAG_ALL=OFF \
  -DCPR_USE_SYSTEM_CURL=ON -DCPR_USE_SYSTEM_GTEST=ON %{?cmake_opts}

%cmake_build

%install
%cmake_install
rm %{buildroot}/usr/lib64/cmake/GTest/GTestTargets.cmake ||:

%check
%if %{with tests}
%ctest --parallel 1 --timeout 60 --verbose
%endif

%if 0%{?suse_version} >= 1500
%ldconfig_scriptlets -n lib%{name}%{sover}
%else
%post   -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig
%endif

%files -n lib%{name}%{sover}
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/lib%{name}.so

%changelog
