#
# spec file for package spdlog
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


Name:           spdlog
%define lname	libspdlog1_14
%define sover	1.14
Version:        1.14.1
Release:        0
Summary:        C++ logging library
License:        MIT
URL:            https://github.com/gabime/spdlog
Source0:        https://github.com/gabime/%{name}/archive/refs/tags/v%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM 2827.patch -- Added missing square bracket to fix the level_to_string_view
#Patch0:         https://patch-diff.githubusercontent.com/raw/gabime/spdlog/pull/2827.patch
BuildRequires:  cmake >= 3.10
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++ >= 13
%else
BuildRequires:  gcc13-c++
%endif
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  (pkgconfig(catch2) >= 3)
BuildRequires:  (pkgconfig(fmt) >= 10.0.0)
BuildRequires:  pkgconfig(libsystemd)

%description
A header-only/compiled, C++ logging library.

* Asynchronous mode (optional)
* Multi/Single threaded loggers.
* Various log targets (rotating/daily files, console, with colors,
  syslog, custom target)

%package devel
Summary:        Header files for spdlog
Requires:       %{lname} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig(fmt)

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%package     -n %{lname}
Summary:        C++ logging library

%description -n %{lname}
A header-only/compiled, C++ logging library.

* Asynchronous mode (optional)
* Multi/Single threaded loggers.
* Various log targets (rotating/daily files, console, with colors,
  syslog, custom target)

%prep
%autosetup -p1
find . -name .gitignore -delete
sed -i -e "s,\r,," README.md LICENSE

%build
export CXX=g++
test -x "$(type -p g++-13)" && export CXX=g++-13

# spdlog embodies fmt ABI; add some symvers so both ld.so and rpm notice the change.
v=v$(rpm -q --qf="%%{VERSION}" --whatprovides "pkgconfig(fmt)" | sed -e 's/\..*//')
echo "FMT_$v { global: _ZN6spdlog*N3fmt${#v}${v}*; };" >spdlog.sym
v="$PWD/spdlog.sym"

%cmake -G Ninja \
    -DSPDLOG_BUILD_TESTS=ON \
    -DSPDLOG_BUILD_BENCH=OFF \
    -DSPDLOG_FMT_EXTERNAL=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DSPDLOG_BUILD_EXAMPLES=OFF \
    -DSPDLOG_BUILD_SHARED=ON \
    -DCMAKE_SHARED_LINKER_FLAGS="%{?build_ldflags} -Wl,--as-needed -Wl,-z,now  -Wl,--version-script=$v" \
..
%ninja_build

%install
%ninja_install -C build

%check
export LD_LIBRARY_PATH="$PWD/build"
%ctest

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md
%{_includedir}/spdlog/
%{_libdir}/libspdlog.so
%{_libdir}/cmake/spdlog/
%{_libdir}/pkgconfig/spdlog.pc
%{_libdir}/cmake

%files -n %{lname}
%{_libdir}/libspdlog.so.*

%changelog
