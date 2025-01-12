#
# spec file for package re-flex
#
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


Name:           re-flex
Version:        5.1.1
Release:        0
Summary:        C++ regex library and lexical analyzer generator with Unicode support
License:        BSD-3-Clause
URL:            https://www.genivia.com/doc/reflex/html/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  c++_compiler
BuildRequires:  pkgconfig
# make sure SIMD optimizations are used and package build reprodicbly
%ifarch x86_64
#!BuildConstraint: hardware:cpu:flag x86-64-v3
%endif

%description
A high-performance C++ regex library and lexical analyzer generator with
Unicode support. Extends Flex++ with Unicode support, indent/dedent anchors,
lazy quantifiers, functions for lex and syntax error reporting and more.
Seamlessly integrates with Bison and other parsers.

%package devel
Summary:        Development files for %{name}

%description devel
Unicode support. Extends Flex++ with Unicode support, indent/dedent anchors,
lazy quantifiers, functions for lex and syntax error reporting and more.
Seamlessly integrates with Bison and other parsers.

This package contains files requires for building with re-flex.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot}%{_libdir}/ -type f -name "*.a" -print -delete

%check
%make_build check

%files
%license LICENSE.txt
%{_bindir}/reflex
%{_mandir}/man1/reflex.1%{?ext_man}

%files devel
%license LICENSE.txt
%{_includedir}/reflex
%{_libdir}/pkgconfig/reflex.pc
%{_libdir}/pkgconfig/reflexmin.pc

%changelog
