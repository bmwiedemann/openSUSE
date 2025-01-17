#
# spec file for package doxygen
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

Name:           doxygen
Version:        1.13.2
Release:        0
Summary:        Automated C, C++, and Java Documentation Generator
# qtools are used for building and they are GPL-3.0 licensed
License:        GPL-2.0-or-later
Group:          Development/Tools/Doc Generators
URL:            https://www.doxygen.nl/
Source0:        https://www.doxygen.nl/files/doxygen-%{version}.src.tar.gz
# suse specific
Patch1:         %{name}-no-lowercase-man-names.patch
Patch2:         reproducible.patch
BuildRequires:  bison
BuildRequires:  cmake >= 3.14
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  llvm-clang-devel
BuildRequires:  python3-base
BuildRequires:  python3-xml
# Do not bother building documentation with latex since it is present on the
# web trivialy for all versions of doxygen
Obsoletes:      doxygen-doc


%description
Doxygen is the de facto standard tool for generating documentation
from annotated C++ sources, but it also supports other popular
programming languages such as C, Objective-C, C-sharp, PHP, Java,
Python, IDL (Corba, Microsoft, and UNO/OpenOffice flavors), Fortran,
and to some extent D. Doxygen also supports the hardware description
language VHDL.

%prep
%setup -q
%autopatch -p1

%build
%cmake \
    -Dbuild_doc=OFF \
    -Dbuild_xmlparser=ON \
    -Dbuild_search=OFF \
    -Dbuild_wizard=OFF \
    -Duse_libclang=ON \
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
