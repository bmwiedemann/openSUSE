#
# spec file for package Clipper2
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_with clipper2_testing
%global sh_lib libClipper2-2
%global sh_z_lib libClipper2Z2
%global broken_sh_lib libClipper2_1
%global broken_sh_z_lib libClipper2Z_1

%if 0%{?suse_version} < 1600
%global force_gcc_version 14
%endif

Name:           Clipper2
Version:        2.0.1
Release:        0
Summary:        Polygon Clipping and Offsetting
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        BSL-1.0
URL:            https://github.com/AngusJohnson/Clipper2/tree/main?tab=BSL-1.0-1-ov-file#readme
Source0:        https://github.com/AngusJohnson/Clipper2/archive/refs/tags/Clipper2_%{version}.tar.gz#/Clipper2-Clipper2_%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  gtest

%description
The Clipper2 library performs intersection, union, difference and XOR boolean
operations on both simple and complex polygons. It also performs polygon
offsetting. This is a major update of my original Clipper library that was
written over 10 years ago. That library I'm now calling Clipper1, and while it
still works very well, Clipper2 is better in just about every way.

%package -n %{sh_lib}
Summary:        Shared library for Clipper2
Obsoletes:      %{broken_sh_lib} < %{version}-%{release}

%description -n %{sh_lib}
The Clipper2 library performs intersection, union, difference and XOR boolean
operations on both simple and complex polygons. It also performs polygon
offsetting. This is a major update of my original Clipper library that was
written over 10 years ago. That library I'm now calling Clipper1, and while it
still works very well, Clipper2 is better in just about every way.

%package -n %{sh_z_lib}
Summary:        Shared library for Clipper2
Obsoletes:      %{broken_sh_z_lib} < %{version}-%{release}

%description -n %{sh_z_lib}
The Clipper2 library performs intersection, union, difference and XOR boolean
operations on both simple and complex polygons. It also performs polygon
offsetting. This is a major update of my original Clipper library that was
written over 10 years ago. That library I'm now calling Clipper1, and while it
still works very well, Clipper2 is better in just about every way.

%package devel
Summary:        Development files for Clipper2
Requires:       %{sh_lib} = %{version}
Requires:       %{sh_z_lib} = %{version}

%description devel
The Clipper2 library performs intersection, union, difference and XOR boolean
operations on both simple and complex polygons. It also performs polygon
offsetting. This is a major update of my original Clipper library that was
written over 10 years ago. That library I'm now calling Clipper1, and while it
still works very well, Clipper2 is better in just about every way.

%prep
%autosetup -p1 -n %{name}-%{name}_%{version}

%build
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
cd CPP
%cmake -DUSE_EXTERNAL_GTEST=ON -DCLIPPER2_HI_PRECISION:BOOL=ON
%cmake_build

%install
cd CPP
%cmake_install

%if %{with clipper2_testing}
%check
cd CPP
%ctest
%endif

%ldconfig_scriptlets -n %{sh_lib}
%ldconfig_scriptlets -n %{sh_z_lib}

%files -n %{sh_lib}
%license LICENSE
%{_libdir}/libClipper2.so.*

%files -n %{sh_z_lib}
%license LICENSE
%{_libdir}/libClipper2Z.so.*

%files devel
%license LICENSE
%doc README.md
%{_libdir}/libClipper2.so
%{_libdir}/libClipper2Z.so
%{_libdir}/pkgconfig/Clipper2.pc
%{_libdir}/pkgconfig/Clipper2Z.pc
%{_includedir}/clipper2/
%{_libdir}/cmake/clipper2/

%changelog
