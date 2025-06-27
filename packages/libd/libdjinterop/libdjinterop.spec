#
# spec file for package libdjinterop
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


%define libname libdjinterop0
Name:           libdjinterop
Version:        0.26.1
Release:        0
Summary:        Access library for DJ record databases
License:        LGPL-3.0-only
URL:            https://github.com/xsco/libdjinterop
Source:         https://github.com/xsco/libdjinterop/archive/refs/tags/%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)

%description
libdjinterop is a C++ library for accessing database formats used to
store information about DJ record libraries.

%package -n %{libname}
Summary:        Access library for DJ record databases

%description -n %{libname}
libdjinterop is a C++ library for accessing database formats used to
store information about DJ record libraries.

This library currently supports:
 * Engine Library, as used on "Prime"-series DJ equipment.

%package devel
Summary:        Headers for libdjinterop, a DJ record database library
Requires:       %{libname} = %{version}

%description devel
libdjinterop is a C++ library for accessing database formats used to
store information about DJ record libraries.

%prep
%autosetup -p1

%build
# ABI break between 0.24.3->0.26.0 (and possibly others).
# Add marker to ensure RPM lockstepupdates consumers with the library.
sv="$PWD/djio.ver"
ver=$(echo "%version" | cut -d+ -f1)
echo "DJIO_$ver { global: *; };" >"$sv"
%cmake -DCMAKE_SHARED_LINKER_FLAGS:STRING="-Wl,--version-script=$sv"
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%{_libdir}/libdjinterop.so.*
%license LICENSE

%files devel
%doc README.md
%{_libdir}/libdjinterop.so
%{_includedir}/djinterop/
%{_libdir}/pkgconfig/djinterop.pc
%{_prefix}/lib/cmake/

%changelog
