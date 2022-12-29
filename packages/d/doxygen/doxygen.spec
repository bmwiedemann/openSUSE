#
# spec file for package doxygen
#
# Copyright (c) 2022 SUSE LLC
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


%if 0%{?sle_version} >= 150100
# build with "--with libclang" to enable libclang support
%bcond_with libclang
%endif

Name:           doxygen
Version:        1.9.6
Release:        0
Summary:        Automated C, C++, and Java Documentation Generator
# qtools are used for building and they are GPL-3.0 licensed
License:        GPL-2.0-or-later AND GPL-3.0-only
Group:          Development/Tools/Doc Generators
URL:            https://www.doxygen.nl/
Source0:        https://www.doxygen.nl/files/doxygen-%{version}.src.tar.gz
# suse specific
Patch1:         %{name}-no-lowercase-man-names.patch
# The unified libclang-cpp library doesn't exist on older Leap / SLE
Patch10:        doxygen-no-libclang-cpp.patch
BuildRequires:  bison
BuildRequires:  cmake >= 2.8.12
BuildRequires:  flex
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  python3-base
BuildRequires:  python3-xml
# Do not bother building documentation with latex since it is present on the
# web trivialy for all versions of doxygen
Obsoletes:      doxygen-doc
%if %{with libclang}
BuildRequires:  llvm-clang-devel
%endif

%description
Doxygen is a documentation system for C, C++, Java, and IDL. It can
generate an online class browser (in HTML) and an offline reference
manual (in LaTeX) from a set of documented source files. The
documentation is extracted directly from the sources. Doxygen is
developed on a Linux platform, but it runs on most other UNIX flavors
as well.

%prep
%setup -q
# Leap 15 and SLE don't accept '%%autopatch -M'
%patch1 -p1
%if %{with libclang}
%if 0%{?sle_version} == 150100 || (0%{?sle_version} == 150200 && !0%{?is_opensuse})
%patch10 -p1
%endif
%endif

%build
%cmake \
    -Dbuild_doc=OFF \
    -Dbuild_xmlparser=ON \
    -Dbuild_search=OFF \
    -Dbuild_wizard=OFF \
%if %{with libclang}
    -Duse_libclang=ON \
%endif
%if 0%{?suse_version} <= 1500
    -DCMAKE_C_COMPILER=gcc-9 \
    -DCMAKE_CXX_COMPILER=g++-9 \
%endif
    -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_MODULE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,relro,-z,now" \
    -DBUILD_SHARED_LIBS=OFF \
    -DBUILD_STATIC_LIBS=ON
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 doc/doxygen.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%attr(644,root,root) %{_mandir}/man1/doxygen.1%{?ext_man}
%attr(755,root,root) %{_bindir}/*

%changelog
