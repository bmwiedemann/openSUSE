#
# spec file for package luabind
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


%define sover   0_9_1
Name:           luabind
Version:        0.9.1+git20150408.a0edf58
Release:        0
Summary:        Lua C++ bindings
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/rpavlik/luabind
Source:         %{name}-%{version}.tar.xz
Patch0:         fix-cmake-lib-version.patch
Patch1:         install-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  lua53-devel
BuildRequires:  pkgconfig
BuildRequires:  procps
Requires:       lua53
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%package devel
Summary:        Luabind headers
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       lua53-devel

%package -n lib%{name}%{sover}
Summary:        Luabind Library
Group:          Development/Libraries/C and C++

%description
Luabind is a library that helps you create bindings between C++ and Lua.
It has the ability to expose functions and classes, written in C++, to Lua.

%description devel
Luabind is a library that helps you create bindings between C++ and Lua.
It has the ability to expose functions and classes, written in C++, to Lua.
This package contains needed development files like headers.

%description -n lib%{name}%{sover}
Luabind is a library that helps you create bindings between C++ and Lua.
It has the ability to expose functions and classes, written in C++, to Lua.
This package contains the library.

%prep
%autosetup -p1

%build
# Parallel build settings ...
limit_jobs="%{?jobs:%{jobs}}"
# do not eat all memory
echo "Available memory:"
free
echo "System limits:"
ulimit -a
if test -n "$limit_jobs" -a "$limit_jobs" -gt 1 ; then
%ifarch ppc64le
    # tuned arbitrarily to avoid oom
    mem_per_process=1500
%else
    mem_per_process=350
%endif
    max_mem=`LANG=C free -t -m | sed -n "s|^Mem: *\([0-9]*\).*$|\1|p"`
    max_jobs="$(($max_mem / $mem_per_process))"
    test "$limit_jobs" -gt "$max_jobs" && limit_jobs="$max_jobs" echo "Warning: Reducing number of jobs to $max_jobs because of memory limits"
fi
test "$limit_jobs" -le 0 && limit_jobs=1 && echo "Warning: Do not use the parallel build at all becuse of memory limits"

%cmake \
    -DLUA_INCLUDE_DIR=%{lua_incdir} \
    -DBUILD_SHARED_LUABIND=ON \
    -DLIB_DIR="%{_lib}"
make -j$limit_jobs

%install
%cmake_install

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files devel
%{_includedir}/luabind
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}.so

%files -n lib%{name}%{sover}
%license LICENSE
%{_libdir}/lib%{name}.so.*

%changelog
