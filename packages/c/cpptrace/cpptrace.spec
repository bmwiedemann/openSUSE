#
# spec file for package cpptrace
#
# Copyright (c) 2026 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

%define         __builder ninja
%define sover   1
%define libname libcpptrace%{sover}

Name:           cpptrace
Version:        1.0.4
Release:        0
Summary:        Portable C++ stacktrace library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/jeremy-rifkin/cpptrace
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  cmake >= 3.14
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  zstd
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libdwarf) >= 0.8
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libzstd)

%description
cpptrace is a library for obtaining stack traces in C++.
It uses DWARF debug information to resolve symbols,
file names, line numbers, and inlined calls.
It also offers a std::stacktrace like API.

%package -n %{libname}
Summary:        Portable C++ stacktrace library
Group:          System/Libraries

%description -n %{libname}
cpptrace is a library for obtaining stack traces in C++.
It uses DWARF debug information to resolve symbols,
file names, line numbers, and inlined calls.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
# cpptrace's installed CMake config files depend on libdwarf and libunwind
Requires:       pkgconfig(libdwarf)
Requires:       pkgconfig(libunwind)

%description devel
Headers, pkg-config data, and CMake config files needed to build
applications that link against cpptrace.

%prep
%autosetup -p1

%build
%cmake \
    -DBUILD_SHARED_LIBS=ON \
    -DCPPTRACE_USE_EXTERNAL_LIBDWARF=ON \
    -DCPPTRACE_FIND_LIBDWARF_WITH_PKGCONFIG=ON \
    -DCPPTRACE_GET_SYMBOLS_WITH_LIBDWARF=ON \
    -DCPPTRACE_UNWIND_WITH_LIBUNWIND=ON \
    %{nil}
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}%{_includedir}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE
%{_libdir}/libcpptrace.so.%{sover}
%{_libdir}/libcpptrace.so.%{sover}.*

%files devel
%doc README.md
%{_includedir}/cpptrace/
%{_includedir}/ctrace/
%{_libdir}/libcpptrace.so
%{_libdir}/cmake/cpptrace/

%changelog
