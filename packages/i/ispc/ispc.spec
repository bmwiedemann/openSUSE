#
# spec file for package ispc
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020-2022 LISA GmbH, Bingen, Germany.
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


%define llvm_ver 14
%define libname libispcrt_1

Name:           ispc
Version:        1.18.0
Release:        0
Summary:        C-based SPMD programming language compiler
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            https://ispc.github.io/
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/v-%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!BuildIgnore:  clang15
BuildRequires:  bison
BuildRequires:  clang%llvm_ver-devel
BuildRequires:  cmake >= 3.13
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  libomp-devel
BuildRequires:  llvm%llvm_ver-devel
BuildRequires:  llvm%llvm_ver-gold
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(python3)
ExclusiveArch:  %{arm} x86_64
%ifarch x86_64
# for some reason, ispc want to link to /usr/lib/crt1.o from glibc-devel-32bit for x86_64
BuildRequires:  glibc-devel-32bit
%endif
# require devel for now for backwards compatibility (until now, packages just BuildRequire: ispc)
Requires:       %{name}-devel

%description
A compiler for a variant of the C programming language, with extensions for
"single program, multiple data" (SPMD) programming.

%package -n %{libname}
Summary:        C-based SPMD programming language compiler library
Group:          System/Libraries

%description -n %{libname}
Libary for a variant of the C programming language, with extensions for
"single program, multiple data" (SPMD) programming.

%package devel
Summary:        Development files for ispc
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}

%description    devel
This package contains the C++ header, symbolic links to the shared
libraries and cmake files for %{name}.  If you would like to develop
programs using %{name}, you will need to install %{name}-devel.

%prep
%setup -q

# fix clang library modules for our clang 10 and above
sed -i 's|set(CLANG_LIBRARY_LIST .*)|set(CLANG_LIBRARY_LIST clang-cpp)|' CMakeLists.txt

%build
%define _lto_cflags "-flto=thin"
echo "optflags: %{optflags}"
# our llvm is built without assertions, which is required for DUMPS to be operational
%cmake \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIE" \
        -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIE" \
        -DCMAKE_EXE_LINKER_FLAGS="%{optflags} -pie" \
        -DCURSES_CURSES_LIBRARY=/usr/%_lib/libncurses.so \
        -DISPC_INCLUDE_EXAMPLES=OFF \
        -DISPC_INCLUDE_TESTS=OFF \
        -DISPC_NO_DUMPS=ON

%cmake_build

%install
%cmake_install
# remove static lib
rm %{buildroot}%{_libdir}/libispcrt_static.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE.txt
%doc *.md
%{_libdir}/*.so.*

%files
%license LICENSE.txt
%doc *.md
%{_bindir}/%{name}
%{_bindir}/check_isa

%files devel
%license LICENSE.txt
%{_includedir}/ispcrt
%{_libdir}/*.so
%{_libdir}/cmake/ispcrt-%{version}

%changelog
