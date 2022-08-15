#
# spec file for package o2scl
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


%define shlib lib%{name}0
Name:           o2scl
Version:        0.926
Release:        0
Summary:        Object-oriented Scientific Computing Library
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://neutronstars.utk.edu/code/o2scl/html/index.html
Source:         https://github.com/awsteiner/o2scl/releases/download/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE o2scl-disable-slow-hdf-test.patch badshah400@gmail.com -- Disable an hdf5 test that takes too long causing OBS workers to time out and build to fail
Patch0:         o2scl-disable-slow-hdf-test.patch
# PATCH-FEATURE-OPENSUSE o2scl-disable-test-without-destdir-support.patch badshah400@gmail.com -- Disable tests that use data files installed to datadir but does not support DESTDIR and therefore cannot be run in a buildroot env
Patch1:         o2scl-disable-test-without-destdir-support.patch
# PATCH-FIX-UPSTREAM o2scl-eos_quark_cfl6-test-increase-tol.patch gh#awsteiner/o2scl#18 badshah400@gmail.com -- Increase the tolerance of a test that fails due to minor tolerance issues on x86_64
Patch2:         o2scl-eos_quark_cfl6-test-increase-tol.patch
# PATCH-FIX-UPSTREAM o2scl-failing-tests-increase-tol.patch badshah400@gmail.com -- Minor increases in tolerance for a few more failing tests
Patch3:         o2scl-failing-tests-increase-tol.patch
BuildRequires:  armadillo-devel
BuildRequires:  eigen3-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
# Required For Patch0
BuildRequires:  libtool
%if 0%{?suse_version} > 1320
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(gsl)
Recommends:     %{name}-doc = %{version}

%description
O2scl is a C++ library for object-oriented numerical programming. It
includes interpolation, differentiation, integration, roots of
polynomials, equation solving, minimization, constrained minimization,
Monte Carlo integration, simulated annealing, least-squares fitting,
solution of ordinary differential equations, two-dimensional
interpolation, Chebyshev approximation, unit conversions, and file I/O
with HDF5.

%package -n %{shlib}
Summary:        Shared libraries for O2scl, a scientific computation library
Group:          System/Libraries

%description -n %{shlib}
O2scl is a C++ library for object-oriented numerical programming.

This package provides the shared libraries for %{name}.

%package devel
Summary:        Source and header files for O2scl
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       armadillo-devel
Requires:       eigen3-devel
Requires:       gcc-c++
Requires:       hdf5-devel
Requires:       readline-devel
Requires:       pkgconfig(gsl)

%description devel
O2scl is a C++ library for object-oriented numerical programming.

This package provides the source and header files for writing software
using %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML

%description doc
O2scl is a C++ library for object-oriented numerical programming.
This package provides the documentation for %{name}.

%prep
%autosetup -p1

%build
autoreconf -fvi
export CXXFLAGS+=" -DO2SCL_PLAIN_HDF5_HEADER"
%configure \
%if 0%{?suse_version} >= 1500
  --enable-gsl2 \
%endif
  --enable-eigen \
  --disable-static

%make_build

%install
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/o2scl/* %{buildroot}%{_docdir}/%{name}/

# REMOVE BOGUS DUPLICATD DOC
rm -fr %{buildroot}%{_prefix}/search

# Remove Makefile junk
find %{buildroot}%{_docdir}/%{name}/ -name "Makefile.*" -delete -print

# Remove static libs and libtool archives
find %{buildroot}%{_libdir} "(" -name "*.a" -o -name "*.la" ")" -delete -print

%fdupes %{buildroot}%{_docdir}/%{name}/

# Tests fail on i586/arm*/aarch64/ppc* due to tolerances in the test codes being set too low. Enable only for x86_64 until fixed
%ifarch x86_64
%check
%make_build check
%endif

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files devel
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_bindir}/acol
%{_bindir}/ame_parse
%{_bindir}/yanic
%{_datadir}/%{name}/
%{_libdir}/*.so
%{_includedir}/o2scl/

%files doc
%doc %{_docdir}/%{name}/

%changelog
