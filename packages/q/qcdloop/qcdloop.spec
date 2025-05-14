#
# spec file for package qcdloop
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


%global shlib libqcdloop2
Name:           qcdloop
Version:        2.1.0
Release:        0
Summary:        An object-oriented one-loop scalar Feynman integrals framework
License:        GPL-3.0-only
URL:            https://qcdloop.web.cern.ch/qcdloop/
Source:         https://github.com/scarrazza/qcdloop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM qcdloop-soversion.patch badshah400@gmail.com -- Implement so versioning
Patch1:         qcdloop-soversion.patch
# PATCH-FIX-UPSTREAM qcdloop-fix-conflicting-types.patch badshah400@gmail.com -- Explicitly cast a variable type to ensure consistency across build archs; fixes build failures for i586
Patch2:         qcdloop-fix-conflicting-types.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkgconfig
ExcludeArch:    ppc %{power64}

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
%ifarch %{ix86} x86_64
  -DQUADMATH_LIBRARY=quadmath \
  -DENABLE_EXAMPLES:BOOL=ON \
%endif
  -DENABLE_FORTRAN_WRAPPER:BOOL=ON \
  %{nil}
%cmake_build

%install
%cmake_install

%ifarch %{ix86} x86_64
%check
pushd %__builddir
for exe in ./cache_test ./cmass_test ./trigger_test;
do
  exec ${exe}
done
popd
%endif

%ldconfig_scriptlets -n %{shlib}

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
