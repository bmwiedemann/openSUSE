#
# spec file for package spglib
#
# Copyright (c) 2022 SUSE LLC
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


%define shlib libsymspg1
Name:           spglib
Version:        2.0.2
Release:        0
Summary:        Find and handle crystal symmetries
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
URL:            https://spglib.github.io/spglib/
Source0:        https://github.com/spglib/spglib/archive/v%{version}.tar.gz#/spglib-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-setuptools

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
pushd .
%cmake
%cmake_build
popd

pushd python
%python3_build
popd

%install
pushd .
%cmake_install
rm %{buildroot}%{_libdir}/lib*.a
popd

# Fix "env-script-interpreter" rpmlint warning
chmod 644 ruby/*.rb

pushd python
%python3_install
popd

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license COPYING
%{_libdir}/libsymspg.so.*

%files devel
%doc example ruby
%{_includedir}/spglib.h
%{_includedir}/spglib_f08.f90
%{_libdir}/libsymspg.so
%{_libdir}/pkgconfig/spglib.pc

%files -n python3-spglib
%{python3_sitearch}/spglib
%{python3_sitearch}/spglib*.egg-info

%changelog
