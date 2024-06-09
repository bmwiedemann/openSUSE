#
# spec file for package tvision
#
# Copyright (c) 2024 SUSE LLC
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


Name:           tvision
Release:        0
Version:        0~git631
Summary:        Modern port of Turbo Vision 2.0
Group:          Development/Languages/C and C++
License:        MIT
URL:            https://github.com/magiblot/tvision
Source:         %{name}-%{version}.tar.xz

%description
A modern port of Turbo Vision 2.0, the classical
framework for text-based user interfaces, but
with Unicode support.

Turbo Vision lets application developers avoid
writing platform-specific workarounds for TUI apps.
It attempts to reproduce consistent results everywhere,
without developers worrying about terminal capabilities,
direct I/O, ifdefs, and other platform quirks.

Turbo Vision provides many widget classes (also known
as views), including resizable, overlapping windows,
pull-down menus, dialog boxes, buttons, scroll bars,
input boxes, check boxes and radio buttons. You may
use and extend these; but even if you prefer creating
your own, Turbo Vision already handles event dispatching,
display of fullwidth Unicode characters, etc.

%package devel-static
Summary:        Static library for Turbo Vision 2.0
Group:          Development/Languages/C and C++
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  gtest
BuildRequires:  gpm
Suggests:       (xclip or xset)

%description devel-static
This package contains the static library, headers,
and help file compiler from the modernised Turbo
Vision 2.0 port.

A modern port of Turbo Vision 2.0, the classical
framework for text-based user interfaces, but with
Unicode and cross=platform support.


%package demos
Summary:        Demo programs of Turbo Vision 2.0
Group:          Development/Languages/C and C++
Suggests:       (xclip or xset)

%description demos
This package contains demo programs showing off the
modernised Turbo Vision 2.0 port.

A modern port of Turbo Vision 2.0, the classical
framework for text-based user interfaces, but
with Unicode and cross-platform support.

%prep
%autosetup -p1

%build
# Disable LTO due to a lto-no-text-in-archive problem with libtvision.a
%global _lto_cflags %nil

# Add CMake flag to let libtvision.a be used properly as a system lib
%cmake -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build

%install
%cmake_install

%check
pushd test/
%cmake
%cmake_build
popd

%files devel-static
%license COPYRIGHT
%doc README.md
%{_bindir}/tvhc
%{_includedir}/*
%{_libdir}/*
%{_libdir}/cmake/

%files demos
%{_bindir}/tvdemo
%{_bindir}/tvedit

%changelog
