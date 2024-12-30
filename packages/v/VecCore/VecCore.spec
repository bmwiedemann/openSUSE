#
# spec file for package VecCore
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


Name:           VecCore
Version:        0.8.2
Release:        0
Summary:        C++ Library for Portable SIMD Vectorization
License:        Apache-2.0
URL:            https://root-project.github.io/veccore
Source:         https://github.com/root-project/veccore/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  cmake(Vc) >= 1.3.3
BuildRequires:  pkgconfig(gtest) >= 1.11.0

%description
VecCore is a simple abstraction layer on top of other vectorization libraries.
It provides an architecture-independent API for expressing vector operations on
data. Code written with this API can then be dispatched to one of several
backends like Vc, UME::SIMD, or a scalar implementation.

%package devel
Summary:        Headers and cmake modules for VecCore

%description devel
VecCore is a simple abstraction layer on top of other vectorization libraries.

This package provides the headers and cmake modules for %{name}.

%prep
%autosetup -p1 -n veccore-%{version}
# make sure to build with system libraries
rm -rf builtins/*

%build
# The SKIP_RPATH fix is needed for Leap 15.2, but doesn't hurt generally
%cmake -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DCMAKE_CXX_STANDARD=14 \
       -DVC:BOOL=ON \
       -DUMESIMD:BOOL=OFF \
       -DUSE_EXTERNAL_GTEST:BOOL=ON \
       -DBUILD_TESTING:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/

%changelog
