#
# spec file for package ceres-solver
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


%define sover 2
Name:           ceres-solver
Version:        2.0.0
Release:        0
Summary:        C++ library for modeling and solving optimization problems
License:        Apache-2.0 AND BSD-3-Clause AND MIT
Group:          Development/Libraries/C and C++
URL:            http://ceres-solver.org/
Source:         http://ceres-solver.org/%{name}-%{version}.tar.gz
Patch0:         https://github.com/ceres-solver/ceres-solver/commit/941ea13475913ef8322584f7401633de9967ccc8.patch#/fix-tbb-2021.1-detection.patch
BuildRequires:  cmake >= 3.5.0
BuildRequires:  gcc-c++
BuildRequires:  glog-devel >= 0.3.1
BuildRequires:  suitesparse-devel
BuildRequires:  pkgconfig(eigen3) >= 3.3.0

%description
Ceres Solver is a C++ library for modeling and solving large,
complicated optimization problems. It can be used to solve Non-linear Least
Squares problems with bounds constraints and general unconstrained optimization
problems.

This package is built with Eigen only.

%package -n libceres-devel
Summary:        Ceres Solver header files
License:        Apache-2.0 AND BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       glog-devel >= 0.3.1
Requires:       libceres%{sover} = %{version}

%description -n libceres-devel
Ceres Solver is a C++ library for modeling and solving large,
complicated optimization problems. It can be used to solve Non-linear Least
Squares problems with bounds constraints and general unconstrained optimization
problems.

This package is built with Eigen only.

%package -n libceres%{sover}
Summary:        Ceres Solver shared library
License:        Apache-2.0 AND BSD-3-Clause
Group:          System/Libraries

%description -n libceres%{sover}
Ceres Solver is a C++ library for modeling and solving large,
complicated optimization problems. It can be used to solve Non-linear Least
Squares problems with bounds constraints and general unconstrained optimization
problems.

This package is built with Eigen only.

%prep
%autosetup -p1

%build
%cmake \
  -DCXSPARSE=ON \
  -DSUITESPARSE=ON \
  -DEIGENSPARSE=ON \
  -DGFLAGS=OFF \
  -DMINIGLOG=OFF \
  %{nil}
%cmake_build

%install
%cmake_install

%post -n libceres%{sover} -p /sbin/ldconfig

%postun -n libceres%{sover} -p /sbin/ldconfig

%files -n libceres-devel
%{_includedir}/ceres/
%{_libdir}/cmake/Ceres/
%{_libdir}/libceres.so

%files -n libceres%{sover}
%{_libdir}/libceres.so.%{sover}*

%changelog
