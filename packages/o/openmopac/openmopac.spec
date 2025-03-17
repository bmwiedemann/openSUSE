#
# spec file for package openmopac
#
# Copyright (c) 2025 SUSE LLC
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

%define         libname  libmopac2
Name:           openmopac
Version:        23.1.2
Release:        0
Summary:        Molecular Orbital PACkage
License:        Apache-2.0
URL:            https://openmopac.github.io
Source0:        mopac-%{version}.tar.gz
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRequires:  python3-numpy-devel
# mopac7 is obsolete version of same software
Provides:       mopac7 = %{version}
Obsoletes:      mopac7 < %{version}

%description
MOPAC is a computational chemistry software package that implements a
variety of semi-empirical quantum chemistry methods based on the neglect of
diatomic differential overlap (NDDO) approximation and fit primarily for
gas-phase thermochemistry

%package -n	%{libname}
Summary:        Dynamic libraries from %{name}

%description -n	%{libname}
MOPAC is a computational chemistry software package that implements a
variety of semi-empirical quantum chemistry methods based on the neglect of
diatomic differential overlap (NDDO) approximation and fit primarily for
gas-phase thermochemistry

This package contains dynamic libraries.

%package    -n mopac-devel
Summary:        Header files for %{name}
Requires:       %{libname} = %{version}
Provides:       libmopac7-1-devel

%description -n mopac-devel
MOPAC is a computational chemistry software package that implements a
variety of semi-empirical quantum chemistry methods based on the neglect of
diatomic differential overlap (NDDO) approximation and fit primarily for
gas-phase thermochemistry

This package contains development files.

%prep
%autosetup -n mopac-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSE
%doc README.md
%{_bindir}/mopac
%{_bindir}/mopac-makpol
%{_bindir}/mopac-param

%files -n %{libname}
%license LICENSE
%{_libdir}/libmopac.so.2

%files -n mopac-devel
%license LICENSE
%{_includedir}/mopac.h
%{_libdir}/libmopac.so

%changelog
