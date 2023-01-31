#
# spec file for package redis++
#
# Copyright (c) 2023 SUSE LLC
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
Name:           redis++
Version:        1.3.7
Release:        0
Summary:        C++ client for Redis
License:        Apache-2.0
URL:            https://github.com/sewenew/redis-plus-plus
Source0:        https://github.com/sewenew/redis-plus-plus/archive/%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(hiredis_ssl)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(openssl)

%description
Redis-plus-plus, a C++ client for Redis based on hiredis and written in C++11/C++17.

%package -n lib%{name}%{sover}
Summary:        C++ client for Redis

%description -n lib%{name}%{sover}
Redis-plus-plus, a C++ client for Redis based on hiredis and written in C++11/C++17.

%package devel
Summary:        Header files and libraries for %{name}
Requires:       lib%{name}%{sover} = %{version}
# With version 1.3, proper so-versioning was added, which made the .so a pure devel symlink
# For this reason though we conflict with older, unversioned libraries
Conflicts:      lib%{name} < 1.3

%description devel
The %{name}-devel package contains the header files and
libraries for redis-plus-plus.

%prep
%autosetup -n redis-plus-plus-%{version}

%build
sed -i -e '/DESTINATION.*/s/lib/%{_lib}/' CMakeLists.txt
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags}" \
  -DREDIS_PLUS_PLUS_BUILD_STATIC=OFF \
  -DREDIS_PLUS_PLUS_USE_TLS=ON \
  -DREDIS_PLUS_PLUS_BUILD_TEST=OFF \
  -DREDIS_PLUS_PLUS_BUILD_ASYNC="libuv"
%cmake_build

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libredis++.so.%{sover}{,.*}

%files devel
%license LICENSE
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libredis++.so
%{_datadir}/cmake/redis++
%{_includedir}/sw

%changelog
