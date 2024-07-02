#
# spec file for package turbo
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


Name:           turbo
Release:        0
Version:        1715766145.697580e
Summary:        Text editor based on Scintilla and Turbo Vision
License:        MIT
URL:            https://github.com/magiblot/turbo
Source:         %{name}-%{version}.tar.xz
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  gtest
BuildRequires:  libmagic1
BuildRequires:  gpm
BuildRequires:  tvision-devel-static
Suggests:       (xclip or xset)
Patch1:         Use-GNUInstallDirs.patch

%description
Turbo is an experimental text editor for the terminal,
based on the Scintilla code editing component by Neil
Hodgson and the Turbo Vision application framework.

%package devel
Summary:        Development files for the Turbo text editor

%description devel
Contains the headers and CMake files for the Turbo text
editor, based on the Scintilla code editing component
and the Turbo Vision 2.0 application framework.

%prep
%autosetup -p1

%build
# Disable LTO due to an lto-no-text-in-archive problem with libtvision.a in tvision-devel
%global _lto_cflags %nil

%cmake \
    -DTURBO_USE_SYSTEM_TVISION=YES \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build

%install
%cmake_install

%files
%license COPYRIGHT
%doc README.md
%{_bindir}/turbo
%{_prefix}/%{_lib}/libturbo-core.so
%{_mandir}/man1/turbo.1.gz

%files devel
%{_includedir}/*
%{_libdir}/cmake/

%changelog
