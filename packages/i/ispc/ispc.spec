#
# spec file for package ispc
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2020-2026 LISA GmbH, Bingen, Germany.
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


%define libname libispcrt1

%define minimum_llvm_version 20

#if 0%{?suse_version} < 1699
#define force_llvm_version 21
#endif

# LLVM is build with OpenMP support only on 64bit archs and x86
%ifarch aarch64 ppc64 ppc64le %{ix86} x86_64
%bcond_without openmp_task_model
%else
%bcond_with openmp_task_model
%endif

Name:           ispc
Version:        1.31.0
Release:        0
Summary:        C-based SPMD programming language compiler
License:        BSD-3-Clause
Group:          Development/Languages/C and C++
URL:            https://ispc.github.io/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/v-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        series
Patch1:         skip-tests.patch
BuildRequires:  bison
BuildRequires:  clang%{?force_llvm_version}-devel >= %{minimum_llvm_version}
BuildRequires:  cmake >= 3.13
BuildRequires:  flex
BuildRequires:  llvm%{?force_llvm_version}-devel >= %{minimum_llvm_version}
%if %{with openmp_task_model}
BuildRequires:  libomp%{?force_llvm_version}-devel >= %{minimum_llvm_version}
%else
BuildRequires:  tbb-devel
%endif
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(level-zero)
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
%if 0%{?force_llvm_version}
perl -p -i -e "s:'clang':'clang-%{force_llvm_version}':g; s:'clang++':'clang++-%{force_llvm_version}':g" tests/lit-tests/lit.cfg
perl -p -i -e "s:llvm-dis:llvm-dis-%{force_llvm_version}:g" tests/lit-tests/avx10.2dmr-x8.ispc
%endif

%define _lto_cflags "-flto=thin"
echo "optflags: %{optflags}"
%cmake \
%if 0%{?force_llvm_version}
        -DCLANG_EXECUTABLE:STRING="clang-%{force_llvm_version}" \
        -DCLANGPP_EXECUTABLE:STRING="clang++-%{force_llvm_version}" \
        -DLLVM_AS_EXECUTABLE:STRING="llvm-as-%{force_llvm_version}" \
        -DCMAKE_C_COMPILER:STRING="clang-%{force_llvm_version}" \
        -DCMAKE_CXX_COMPILER:STRING="clang++-%{force_llvm_version}" \
%endif
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_C_FLAGS:STRING="$CFLAGS %{optflags} -fPIE" \
        -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS %{optflags} -fPIE" \
        -DCMAKE_EXE_LINKER_FLAGS="%{optflags} -pie" \
        -DCURSES_CURSES_LIBRARY=/usr/%_lib/libncurses.so \
        -DISPCRT_BUILD_TASK_MODEL=%{?with_openmp_task_model:OpenMP}%{!?with_openmp_task_model:TBB} \
        -DISPC_INCLUDE_EXAMPLES=OFF \
        -DISPCRT_BUILD_GPU:BOOL=ON \
        -DISPCRT_BUILD_TESTS:BOOL=OFF \
        -DISPC_INCLUDE_TESTS=ON \
        -DISPCRT_BUILD_STATIC=OFF \
        %{nil}
%cmake_build

%install
%cmake_install

%check
pushd %__builddir
%cmake_build check-all

%ldconfig_scriptlets -n %{libname}

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
%{_includedir}/ispc/
%{_includedir}/ispcrt/
%dir %{_includedir}/intrinsics/
%{_includedir}/intrinsics/emmintrin.isph
%{_includedir}/intrinsics/xmmintrin.isph
%dir %{_includedir}/stdlib/
%{_includedir}/stdlib/amx.isph
%{_includedir}/stdlib/short_vec.isph
%{_libdir}/*.so
%{_libdir}/cmake/ispc/
%{_libdir}/cmake/ispcrt-%{version}

%changelog
