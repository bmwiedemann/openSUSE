#
# spec file for package redis++
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


Name:           redis++
Version:        1.2.0
Release:        0
Summary:        C++ client for Redis
License:        Apache-2.0
URL:            https://github.com/sewenew/redis-plus-plus
Source0:        https://github.com/sewenew/redis-plus-plus/archive/%{version}.tar.gz
Patch0:         disable_static_lib.patch
Patch1:         use_shared_lib_for_test.patch
Patch2:         custom_install_locations.patch
BuildRequires:  c++_compiler
BuildRequires:  coreutils
BuildRequires:  hiredis-devel
BuildRequires:  libopenssl-devel
BuildRequires:  cmake

%description
Redis-plus-plus, a C++ client for Redis based on hiredis and written in C++11/C++17.

%package -n lib%{name}
Summary:        C++ client for Redis

%description -n lib%{name}
Redis-plus-plus, a C++ client for Redis based on hiredis and written in C++11/C++17.

%package devel
Summary:        Header files and libraries for %{name}
Requires:       lib%{name} = %{version}
Requires:       hiredis-devel

%description devel
The %{name}-devel package contains the header files and
libraries for redis-plus-plus.

%prep
%setup -q -n redis-plus-plus-%{version}
%patch0 -p1
%patch1
%patch2

%build
%cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DREDIS_PLUS_PLUS_USE_TLS=ON \
  -DREDIS_PLUS_PLUS_BUILD_STATIC=OFF \
  -DREDIS_LIBDIR=%{_lib} \
  -DREDIS_INCDIR=redis++ \
  -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags}"
%cmake_build

%install
%cmake_install

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%files -n lib%{name}
%license LICENSE
%doc README.md
%{_libdir}/libredis++.so

%files devel
%{_includedir}/redis++

%changelog
