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


# upstream promises no ABI stability between releases (its CMake package
# version file is ExactVersion), so the soversion tracks major.minor
%define soversion 6.4
%define sover     6_4
Name:           re-flex
Version:        6.4.0
Release:        0
Summary:        C++ regex library and lexical analyzer generator with Unicode support
License:        BSD-3-Clause
URL:            https://www.genivia.com/doc/reflex/html/
Source:         %{name}-%{version}.tar.xz
# ship only the shared libreflex/libreflexmin and give them a soversion;
# upstream's CMake build sets none and also installs the static archives
Patch0:         reflex-shared-soversion.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig

%description
A high-performance C++ regex library and lexical analyzer generator with
Unicode support. Extends Flex++ with Unicode support, indent/dedent anchors,
lazy quantifiers, functions for lex and syntax error reporting and more.
Seamlessly integrates with Bison and other parsers.

%package -n libreflex%{sover}
Summary:        C++ regex library of RE-flex

%description -n libreflex%{sover}
The RE-flex regex matching/lexing runtime library (shared object).

%package -n libreflexmin%{sover}
Summary:        Minimal C++ regex library of RE-flex

%description -n libreflexmin%{sover}
The minimal RE-flex runtime library (shared object): the matcher engine
without the pattern converter, POSIX support and Unicode tables, for linking
generated scanners that do not need them.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       libreflex%{sover} = %{version}
Requires:       libreflexmin%{sover} = %{version}

%description devel
RE-flex is a high-performance C++ regex library and lexical analyzer generator
with Unicode support.

This package contains files required for building with re-flex (headers, the
shared-library symlinks, the pkg-config files and the CMake package config).

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
# the CMake build does not install the manpage; ship it like the autotools build did
install -D -m 0644 doc/man/reflex.1 %{buildroot}%{_mandir}/man1/reflex.1

%check
%ctest

%ldconfig_scriptlets -n libreflex%{sover}

%ldconfig_scriptlets -n libreflexmin%{sover}

%files
%license LICENSE.txt
%{_bindir}/reflex
%{_mandir}/man1/reflex.1%{?ext_man}

%files -n libreflex%{sover}
%license LICENSE.txt
%{_libdir}/libreflex.so.%{soversion}*

%files -n libreflexmin%{sover}
%license LICENSE.txt
%{_libdir}/libreflexmin.so.%{soversion}*

%files devel
%license LICENSE.txt
%{_includedir}/reflex
%{_libdir}/libreflex.so
%{_libdir}/libreflexmin.so
%{_libdir}/cmake/reflex/
%{_libdir}/pkgconfig/reflex.pc
%{_libdir}/pkgconfig/reflexmin.pc

%changelog
