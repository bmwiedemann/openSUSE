#
# spec file for package ispc
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2023 LISA GmbH, Bingen, Germany.
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


%global min_llvm_version 16
%global max_llvm_version 19.9
%define libname libispcrt1

# LLVM is build with OpenMP support only on 64bit archs and x86
%ifarch aarch64 ppc64 ppc64le %{ix86} x86_64
%bcond_without openmp_task_model
%else
%bcond_with openmp_task_model
%endif

Name:           ispc
Version:        1.25.3
Release:        0
Summary:        C-based SPMD programming language compiler
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            https://ispc.github.io/
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/v-%{version}.tar.gz#/%{name}-%{version}.tar.gz
#!BuildIgnore:  clang15
BuildRequires:  bison
BuildRequires:  cmake >= 3.13
BuildRequires:  flex
%if %{suse_version} < 1550
# Leap/SLE 15 does not understand boolean requires
BuildRequires:  cmake(Clang) >= 19
#!BuildConflicts: cmake(Clang) >= 20
%endif
BuildRequires:  (cmake(Clang) >= %{min_llvm_version} with cmake(Clang) =< %{max_llvm_version})
BuildRequires:  (cmake(LLVM)  >= %{min_llvm_version} with cmake(LLVM)  =< %{max_llvm_version})
%if %{with openmp_task_model}
BuildRequires:  (libomp-devel-provider >= %{min_llvm_version} with libomp-devel-provider  =< %{max_llvm_version})
%else
BuildRequires:  tbb-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(python3)
%ifarch x86_64
# x86_64 always includes x86 target support: https://github.com/ispc/ispc/issues/1865
BuildRequires:  glibc-devel-32bit
%endif
# aarch32 requires LLVM with aarch64 target support, likewise for ix86
ExclusiveArch:  x86_64 aarch64
# require devel for now for backwards compatibility (until now, packages just BuildRequire: ispc)
Requires:       %{name}-devel

%description
A compiler for a variant of the C programming language, with extensions for
"single program, multiple data" (SPMD) programming.

%package -n %{libname}
Summary:        C-based SPMD programming language compiler library
Group:          System/Libraries
# Old library name violating SLPP, only dash or <none> allowed as separator
Conflicts:      libispcrt_1 <= 1.18.0

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
%autosetup -p1

# fix clang library modules for our clang 10 and above
sed -i 's|set(CLANG_LIBRARY_LIST .*)|set(CLANG_LIBRARY_LIST clang-cpp)|' CMakeLists.txt

# disable build of static library, https://github.com/ispc/ispc/issues/2385
sed -i -e '/build_ispcrt(STATIC/ s@.*@#\0@' ispcrt/CMakeLists.txt

%build
%define _lto_cflags "-flto=thin"
echo "optflags: %{optflags}"
%cmake \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIE" \
        -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIE" \
        -DCMAKE_EXE_LINKER_FLAGS="%{optflags} -pie" \
        -DCURSES_CURSES_LIBRARY=/usr/%_lib/libncurses.so \
        -DISPCRT_BUILD_TASK_MODEL=%{?with_openmp_task_model:OpenMP}%{!?with_openmp_task_model:TBB} \
        -DISPC_INCLUDE_EXAMPLES=OFF \
        -DISPC_INCLUDE_TESTS=ON \
        -DISPCRT_BUILD_STATIC=OFF \
        %{nil}
%cmake_build

%install
%cmake_install

%check
pushd %__builddir
%cmake_build check-all

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
