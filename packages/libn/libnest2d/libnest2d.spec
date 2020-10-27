#
# spec file for package libnest2d
#
# Copyright (c) 2020 SUSE LLC
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

Name:           libnest2d
Version:        0.4+git.20200805
Release:        0
Summary:        Library for the 2D bin packaging problem
License:        LGPL-3.0-only
URL:            https://github.com/tamasmeszaros/libnest2d
Source:         libnest2d-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://github.com/tamasmeszaros/libnest2d/pull/18
Patch0:         Add-disallowed-areas.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libpolyclipping-devel
BuildRequires:  pkgconfig(nlopt)

%description
A library and framework for the 2D bin packaging problem.

%package devel
Summary:        Library for the 2D bin packaging problem
Requires:       libboost_headers-devel
Requires:       libpolyclipping-devel
Requires:       pkgconfig(nlopt)

%description devel
A library and framework for the 2D bin packaging problem.

%prep
%autosetup -p1
sed -i -e "s/ lib\([^n]\)/ "%{_lib}"\1/" CMakeLists.txt

%build
%cmake \
  -DLIBNEST2D_HEADER_ONLY=ON
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/libnest2d
%{_libdir}/cmake/Libnest2D

%changelog
