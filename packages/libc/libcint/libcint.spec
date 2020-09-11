#
# spec file for package libcint
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


%define major 3
%define minor 1
%define libname %{name}%{major}
%define develname   cint
Name:           libcint
Version:        %{major}.%{minor}.1
Release:        0
Summary:        General Gaussian-type orbitals integrals for quantum chemistry
License:        BSD-2-Clause
URL:            https://github.com/sunqm/libcint
Source:         https://github.com/sunqm/libcint/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-fortran
BuildRequires:  openblas-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
# qcint is a drop-in replacement of the same library with architecture dependent optimizations
Conflicts:      qcint

%description
libcint is an open source library for analytical Gaussian integrals.
It provides C/Fortran API to evaluate one-electron / two-electron
integrals for Cartesian / real-spherical / spinor Gaussian type functions.

%package -n    %{libname}
Summary:        General Gaussian-type orbitals integrals for quantum chemistry

%description -n    %{libname}
libcint is an open source library for analytical Gaussian integrals.
It provides C/Fortran API to evaluate one-electron / two-electron
integrals for Cartesian / real-spherical / spinor Gaussian type functions.

%package -n     %{develname}-devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}
Conflicts:      qcint-devel

%description -n %{develname}-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DENABLE_EXAMPLE:BOOL=ON \
       -DWITH_F12:BOOL=ON \
       -DWITH_COULOMB_ERF:BOOL=ON \
       -DWITH_RANGE_COULOMB:BOOL=ON \
       -DENABLE_TEST:BOOL=ON \
       -DQUICK_TEST:BOOL=ON

%cmake_build

%install
%cmake_install

%check
%ctest

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libcint.so.%{major}
%{_libdir}/libcint.so.%{version}

%files -n %{develname}-devel
%license LICENSE
%doc README doc/program_ref.pdf
%{_includedir}/cint.h
%{_includedir}/cint_funcs.h
%{_libdir}/libcint.so

%changelog
