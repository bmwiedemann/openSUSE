#
# spec file for package spglib
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


%if 0%{?suse_version} >= 1600
%bcond_without tests
%else
%bcond_with    tests
%endif

%define shlib libsymspg2
Name:           spglib
Version:        2.2.0
Release:        0
Summary:        Find and handle crystal symmetries
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
URL:            https://spglib.github.io/spglib/
Source0:        https://github.com/spglib/spglib/archive/v%{version}.tar.gz#/spglib-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  c++_compiler
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-PyYAML
BuildRequires:  pkgconfig(gtest)
%endif

%description
Spglib is a C library to find and handle crystal symmetries.

Features:
 * Find symmetry operations
 * Identify space-group type
 * Wyckoff position assignment
 * Refine crystal structure
 * Search irreducible k-points
 * Find a primitive cell

%package -n %{shlib}
Summary:        The shared library for SPGLIB
Group:          System/Libraries

%description -n %{shlib}
Spglib is a C library to find and handle crystal symmetries.

%package devel
Summary:        Development files for spglib/libsymspg
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}

%description devel
Spglib is a C library to find and handle crystal symmetries.

%package -n python3-spglib
Summary:        Python bindings for spglib/libsymspg
Group:          Development/Languages/Python
Requires:       python3-numpy

%description -n python3-spglib
Spglib is a C library to find and handle crystal symmetries.

%prep
%setup -q
%autopatch -p1

%build
%cmake \
  -DSPGLIB_WITH_Python:BOOL=ON \
  -DSPGLIB_WITH_TESTS:BOOL=%{?with_tests:ON}%{!?with_tests:OFF} \
  %{nil}
%cmake_build

%install
%cmake_install

# Fix "env-script-interpreter" rpmlint warning
chmod 644 ruby/*.rb

# Remove shared library and header copies from python directory
rm -Rf %{python3_sitearch}/spglib/include
rm -Rf %{python3_sitearch}/spglib/libsymspg.so*

%check
%if %{with tests}
export PYTHONPATH=%{buildroot}%{python_sitearch} 
export PYTHONDONTWRITEBYTECODE=1
%ctest
%endif

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license COPYING
%{_libdir}/libsymspg.so.*

%files devel
%doc example ruby
%{_includedir}/spglib.h
%{_libdir}/libsymspg.so
%{_libdir}/cmake/Spglib
%{_libdir}/pkgconfig/spglib.pc

%files -n python3-spglib
%{python3_sitearch}/spglib

%changelog
