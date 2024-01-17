#
# spec file for package qcdloop
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


%global shlib libqcdloop2
Name:           qcdloop
Version:        2.0.9
Release:        0
Summary:        An object-oriented one-loop scalar Feynman integrals framework
License:        GPL-3.0-only
URL:            https://qcdloop.web.cern.ch/qcdloop/
Source:         https://github.com/scarrazza/qcdloop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM qcdloop-math-linking.patch badshah400@gmail.com -- Explicitly link to math library to fix linking error when linking with --Wl,no-undefined
Patch0:         qcdloop-quadmath-linking.patch
# PATCH-FIX-UPSTREAM qcdloop-soversion.patch badshah400@gmail.com -- Implement so versioning
Patch1:         qcdloop-soversion.patch
# PATCH-FIX-UPSTREAM qcdloop-fix-conflicting-types.patch badshah400@gmail.com -- Explicitly cast a variable type to ensure consistency across build archs; fixes build failures for i586
Patch2:         qcdloop-fix-conflicting-types.patch
# PATCH-FEATURE-OPENSUSE qcdloop-remove-march-mtune-flags.patch badshah400@gmail.com -- Drop march and mtune flags being passed to the c++ compiler to enable building on multiple archs
Patch3:         qcdloop-remove-march-mtune-flags.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkgconfig
# Doesn't build on aarch64, ppc64* due to no quadmath
ExcludeArch:    aarch64 %power64

%description
QCDLoop is a library of one-loop scalar Feynman integrals, evaluated close to
four dimensions. QCDLoop can compute one-loop integrals for tadpole, bubble,
triangle and box topologies. See  arXiv:0712.1851 and arXiv:1605.03181 for
references.

%package -n %{shlib}
Summary:        Shared library for QCDLoop - a one-loop scalar Feynman integrals framework

%description -n %{shlib}
QCDLoop is a library of one-loop scalar Feynman integrals, evaluated close to
four dimensions. This package provides the shared library for QCDLoop.

%package devel
Summary:        Development headers and sources for QCDLoop
Requires:       %{shlib} = %{version}

%description devel
QCDLoop is a library of one-loop scalar Feynman integrals, evaluated close to
four dimensions. This package provides headers and sources for QCDLoop needed
for developing software against QCDLoop.

%prep
%autosetup -p1
sed -i "1{s|#! %{_bindir}/env bash|#! /bin/bash|}"  src/qcdloop-config.in

%build
%cmake \
  -DENABLE_EXAMPLES:BOOL=ON \
  -DENABLE_FORTRAN_WRAPPER:BOOL=ON

%cmake_build

%install
%cmake_install

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/libqcdloop.so.*

%files devel
%license LICENSE
%doc README.md
%{_bindir}/qcdloop-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}/

%changelog
