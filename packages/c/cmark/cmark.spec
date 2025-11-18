#
# spec file for package cmark
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define libname libcmark0_31_1
Name:           cmark
Version:        0.31.1
Release:        0
Summary:        CommonMark parsing and rendering library and program in C
License:        BSD-2-Clause AND MIT AND CC-BY-SA-4.0
Group:          Productivity/Text/Utilities
URL:            https://github.com/jgm/cmark
Source:         https://github.com/jgm/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.7
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
`cmark` is the C reference implementation of CommonMark,
a rationalized version of Markdown syntax with a spec.

It provides a shared library (`libcmark`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark`) for parsing and rendering CommonMark
documents.

%package -n %{libname}
Summary:        CmmonMark parsing and rendering library
Group:          System/Libraries

%description -n %{libname}
It provides a shared library (`libcmark`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark`) for parsing and rendering CommonMark
documents.

%package devel
Summary:        Development files for cmark library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}
# The CMake config files define a target for the executable.
Requires:       %{name} = %{version}

%description devel
This package provides the development files for cmark.

%prep
%autosetup -p1

%build
%cmake -DCMARK_TESTS=OFF -DCMARK_STATIC=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libname}

%files
%license COPYING
%{_bindir}/cmark
%{_mandir}/man1/cmark.1%{?ext_man}

%files -n %{libname}
%license COPYING
%{_libdir}/libcmark.so.%{version}

%files devel
%license COPYING
%{_includedir}/cmark.h
%{_includedir}/cmark_export.h
%{_includedir}/cmark_version.h
%{_libdir}/libcmark.so
%{_libdir}/pkgconfig/libcmark.pc
%{_mandir}/man3/cmark.3%{?ext_man}
%dir %{_libdir}/cmake/cmark
%{_libdir}/cmake/cmark/cmark*.cmake
%doc README.md

%changelog
