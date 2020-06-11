#
# spec file for package ispc
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2020 LISA GmbH, Bingen, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           ispc
Version:        1.13.0
Release:        0
Summary:        C-based SPMD programming language compiler
Group:          Development/Languages/C and C++
License:        BSD-3-Clause
URL:            https://ispc.github.io/
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  cmake >= 3.13
BuildRequires:  clang-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  llvm-devel
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(python3)
ExclusiveArch:  %{arm} x86_64
%ifarch x86_64
# for some reason, ispc want to link to /usr/lib/crt1.o from glibc-devel-32bit for x86_64
BuildRequires:  glibc-devel-32bit
%endif

%description
A compiler for a variant of the C programming language, with extensions for
"single program, multiple data" (SPMD) programming.
 
%prep
%setup -q

# other distributions seem to provide curses compatibility links to ncurses
sed -i 's|${PROJECT_NAME} pthread z tinfo curses)|${PROJECT_NAME} pthread z tinfo ncurses)|' CMakeLists.txt

# fix clang library modules for new clang
%if 0%{?_llvm_sonum} >= 10
sed -i 's|set(CLANG_LIBRARY_LIST .*)|set(CLANG_LIBRARY_LIST clang-cpp)|' CMakeLists.txt
%endif

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
        -DISPC_INCLUDE_EXAMPLES=OFF \
        -DISPC_INCLUDE_TESTS=OFF \
        -DISPC_NO_DUMPS=ON

%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc *.md
%{_bindir}/%{name}
%{_bindir}/check_isa

%changelog
