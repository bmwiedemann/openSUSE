#
# spec file for package google-or-tools
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


%define sonum 9
%bcond_without tests

Name:           google-or-tools
Version:        9.3
Release:        0
License:        Apache-2.0
Summary:        Suite for solving combinatorial optimization problems
URL:            https://developers.google.com/optimization/
Group:          Development/Languages/C++
Source:         https://github.com/google/or-tools/archive/refs/tags/v9.3.tar.gz#/google-or-tools-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - fix incompatibility with re2, abseil and C++17
Patch0:         https://github.com/google/or-tools/commit/0d3572bda874ce30b35af161a713ecd1793cd296.patch#/fix_re2_string_view.patch
# PATCH-FIX-UPSTREAM - fix build with -Wl,--no-undefined
Patch1:         0001-Build-Python-modules-as-CMake-MODULEs.patch
# PATCH-FIX-OPENSUSE
Patch2:         0001-Do-not-try-to-download-ortools-wheel.patch
# PATCH-FIX-UPSTREAM - fix malformed C++
Patch3:         https://github.com/google/or-tools/commit/672303cc2f2396c4bd5fbed8430208308815bd54.patch#/fix_malformed_Cpp.patch
# PATCH-FIX-UPSTREAM - allow build on i586/armv7
Patch4:         0001-Set-SWIGWORDSIZE-dependent-on-architecture-bitness.patch
# PATCH-FIX-UPSTREAM - remove bad entries from RUNPATHs
Patch5:         0001-Only-add-relevant-directories-to-sample-RUNPATHs.patch
Patch6:         0002-Only-add-relevant-directories-to-flatzinc-library-ex.patch
BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake >= 3.18
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 7
BuildRequires:  python3-absl-py
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-mypy-protobuf
BuildRequires:  python3-numpy >= 1.13.1
BuildRequires:  python3-pandas
BuildRequires:  python3-pybind11-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-virtualenv
BuildRequires:  python3-wheel
BuildRequires:  swig
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)

%description
OR-Tools is an open source software suite for optimization, tuned for
tackling the world's toughest problems in vehicle routing, flows,
integer and linear programming, and constraint programming.

%package -n python3-ortools
Summary:        Suite for solving combinatorial optimization problems
Group:          Development/Languages/Python

%description -n python3-ortools
Python3 bindings for the OR-Tools suite, for solving combinatorial
optimization problems.

%package minizinc
Summary:        OR-Tools minizinc solver
Group:          Productivity/Scientific/Math
Requires:       minizinc

%description minizinc
Minizinc solver using the OR-Tools suite.

%package -n libortools%{sonum}
Summary:        Suite for solving combinatorial optimization problems
Group:          System/Libraries

%description -n libortools%{sonum}
OR-Tools is an open source software suite for optimization.

%package -n libflatzinc%{sonum}
Summary:        Suite for solving combinatorial optimization problems
Group:          System/Libraries

%description -n libflatzinc%{sonum}
OR-Tools is an open source software suite for optimization.

%package devel
Summary:        Suite for solving combinatorial optimization problems
Group:          Development/Languages/C++
Requires:       libflatzinc%{sonum} = %{version}
Requires:       libortools%{sonum} = %{version}

%description devel
Development files (C/C++) for the OR-Tools suite.

%prep
%autosetup -p1 -n or-tools-%{version}

%build
%global optflags %{optflags} -Wno-error=return-type
%cmake \
  -DBUILD_DEPS:BOOL=OFF \
  -DBUILD_pybind11:BOOL=OFF \
  -DBUILD_PYTHON:BOOL=ON \
  -DVENV_USE_SYSTEM_SITE_PACKAGES:BOOL=ON \
  -DUSE_SCIP:BOOL=OFF \
  -DUSE_COINOR:BOOL=OFF \
  %{nil}
%cmake_build

%install
%cmake_install
# Remove duplicate library
rm %{buildroot}/%{python3_sitearch}/ortools/.libs/libortools.so.9
rmdir %{buildroot}/%{python3_sitearch}/ortools/.libs

%post -n libortools%{sonum} -p /sbin/ldconfig
%postun -n libortools%{sonum} -p /sbin/ldconfig
%post -n libflatzinc%{sonum} -p /sbin/ldconfig
%postun -n libflatzinc%{sonum} -p /sbin/ldconfig

%check
# Test using e.g. SCIP are not skipped, exclude
%if %{with tests}
%define known_fail 'python.*mip|python_contrib.*|python_linear_solver_integer_programming_example|python_python_appointments|python_python_steel_mill_slab_sat|cxx_tests_issue173|python_tests_dual_loading|python_tests_pywraplp_test'
%if %{__isa_bits} == 32
%ctest --exclude-regex %{known_fail} || true
%else
%ctest --exclude-regex %{known_fail}
%endif
%endif

%files
%doc CONTRIBUTING.md README.md
%license LICENSE
%{_bindir}/*
%exclude %{_bindir}/fz

%files -n python3-ortools
%{python3_sitearch}/ortools
%{python3_sitearch}/ortools-%{version}*info

%files minizinc
%{_bindir}/fz
%{_datadir}/minizinc

%files -n libortools%{sonum}
%{_libdir}/libor*.so.%{sonum}*

%files -n libflatzinc%{sonum}
%{_libdir}/libflatzinc*.so.%{sonum}*

%files devel
%{_libdir}/lib*.so
%{_libdir}/cmake/ortools
%{_includedir}/ortools
%{_includedir}/ortools_export.h

%changelog
