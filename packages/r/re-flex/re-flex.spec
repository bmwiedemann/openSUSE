#
# spec file for package re-flex
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define sover 6
Name:           re-flex
Version:        6.3.0
Release:        0
Summary:        C++ regex library and lexical analyzer generator with Unicode support
License:        BSD-3-Clause
URL:            https://www.genivia.com/doc/reflex/html/
Source:         %{name}-%{version}.tar.xz
# build the shared library (libreflex.so) the upstream CMake build supports and
# give it a soversion; the autotools build only produced static archives
Patch0:         reflex-shared-soversion.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
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

%package -n libreflex%{sover}
Summary:        C++ regex library of RE-flex

%description -n libreflex%{sover}
The RE-flex regex matching/lexing runtime library (shared object).

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       libreflex%{sover} = %{version}

%description devel
Unicode support. Extends Flex++ with Unicode support, indent/dedent anchors,
lazy quantifiers, functions for lex and syntax error reporting and more.
Seamlessly integrates with Bison and other parsers.

This package contains files required for building with re-flex (headers, the
shared-library symlink and the CMake package config).

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# the CMake build does not install the manpage; ship it like the autotools build did
install -D -m 0644 doc/man/reflex.1 %{buildroot}%{_mandir}/man1/reflex.1

%ldconfig_scriptlets -n libreflex%{sover}

%files
%license LICENSE.txt
%{_bindir}/reflex
%{_mandir}/man1/reflex.1%{?ext_man}

%files -n libreflex%{sover}
%license LICENSE.txt
%{_libdir}/libreflex.so.%{sover}*

%files devel
%license LICENSE.txt
%{_includedir}/reflex
%{_libdir}/libreflex.so
%{_libdir}/cmake/reflex/

%changelog
