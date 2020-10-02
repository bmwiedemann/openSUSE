#
# spec file for package spdlog
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


%define _sover  1
Name:           spdlog
Version:        1.8.1
Release:        0
Summary:        C++ logging library
License:        MIT
URL:            https://github.com/gabime/spdlog
Source0:        https://github.com/gabime/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  benchmark-devel >= 1.4.0
BuildRequires:  cmake >= 3.10
BuildRequires:  gcc
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++ >= 8
%else
BuildRequires:  gcc8-c++
%endif
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(libsystemd)

%description
This is a packaged version of the gabime/spdlog header-only C++
logging library available at Github.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{_sover} = %{version}
Requires:       libstdc++-devel
Requires:       pkgconfig(fmt)

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%package     -n lib%{name}%{_sover}
Summary:        C++ logging library

%description -n lib%{name}%{_sover}
This is a packaged version of the gabime/spdlog C++ logging library
available at Github.

%prep
%autosetup -p1
find . -name '.gitignore' -exec rm {} \;
sed -i -e "s,\r,," README.md LICENSE

%build
export CXX=g++
test -x "$(type -p g++-8)" && export CXX=g++-8
%cmake -G Ninja \
    -DSPDLOG_BUILD_TESTS=ON \
    -DSPDLOG_BUILD_BENCH=OFF \
    -DSPDLOG_FMT_EXTERNAL=ON \
    -DCMAKE_BUILD_TYPE=Release \
    -DSPDLOG_BUILD_EXAMPLES=OFF \
    -DSPDLOG_BUILD_SHARED=ON \
..
%ninja_build

%install
%ninja_install -C build

%check
export LD_LIBRARY_PATH="%{_builddir}/%{name}-%{version}/build"
%ctest

%post -n lib%{name}%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}%{_sover} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}%{_sover}
%{_libdir}/lib%{name}.so.%{_sover}*

%changelog
