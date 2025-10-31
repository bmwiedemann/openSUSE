#
# spec file for package libformfactor
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


%define sover 0_3_2
Name:           libformfactor
Version:        0.3.2
Release:        0
Summary:        Efficient computation of scattering form factors of arbitrary polyhedra
License:        GPL-3.0-or-later
URL:            https://jugit.fz-juelich.de/mlz/libformfactor
Source:         https://jugit.fz-juelich.de/mlz/libformfactor/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
# taken from Fedora
Patch0:         libformfactor-fix-cmake.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  cmake(LibHeinz)
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
Efficient computation of scattering form factors (Fourier shape transforms) of
arbitrary polyhedra according to Wuttke, J Appl Cryst 54, 580-587 (2021).

%package -n %{name}%{sover}
Summary:        Efficient computation of scattering form factors of arbitrary polyhedra

%description -n %{name}%{sover}
Efficient computation of scattering form factors (Fourier shape transforms) of
arbitrary polyhedra according to Wuttke, J Appl Cryst 54, 580-587 (2021).

This package contains the share library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{sover} = %{version}

%description devel
Efficient computation of scattering form factors (Fourier shape transforms) of
arbitrary polyhedra according to Wuttke, J Appl Cryst 54, 580-587 (2021).

This package contains the files needed to build with %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license LICENSE
%{_libdir}/libformfactor.so.*

%files devel
%license LICENSE
%{_includedir}/ff
%{_libdir}/cmake/formfactor
%{_libdir}/libformfactor.so

%changelog
