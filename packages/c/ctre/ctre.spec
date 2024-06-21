#
# spec file for package ctre
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


%if 0%{?suse_version} <= 1550
%define gcc_ver 11
%endif
Name:           ctre
Version:        3.9.0
Release:        0
Summary:        Compile time regular expressions library
License:        Apache-2.0
URL:            https://compile-time.re
Source:         https://github.com/hanickadot/compile-time-regular-expressions/archive/refs/tags/v%{version}.tar.gz#/%{name}-%version.tar.gz
# https://github.com/hanickadot/compile-time-regular-expressions/issues/253
Patch1:         unsigned-char.patch
BuildRequires:  cmake
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
A compile-time regular expressions with support for
matching/searching/capturing during compile-time or runtime.

%package devel
Summary:        Header and cmake files for ctre, a regular expressions library
BuildArch:      noarch

%description devel
This package provides the header files and other development files needed for
developing applications against ctre.

%prep
%autosetup -p1 -n compile-time-regular-expressions-%{version}

%build
%cmake \
  -DCMAKE_CXX_COMPILER=g++%{?gcc_ver:-%{gcc_ver}} \
  -DCTRE_MODULE:BOOL=OFF \
	-DCTRE_BUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
CXX=g++%{?gcc_ver:-%{gcc_ver}} %make_build

%files devel
%license LICENSE
%doc README.md
%{_includedir}/*
%{_datadir}/cmake/ctre/
%{_datadir}/pkgconfig/*.pc

%changelog
