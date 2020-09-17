#
# spec file for package ceres-solver
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


%define sover 1

Name:           ceres-solver
Version:        1.14.0
Release:        0
Summary:        C++ library for modeling and solving optimization problems
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://ceres-solver.org/
Source:         http://ceres-solver.org/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.0
BuildRequires:  gcc-c++
BuildRequires:  glog-devel >= 0.3.1
BuildRequires:  libcxsparse3
BuildRequires:  suitesparse-devel
BuildRequires:  pkgconfig(eigen3) >= 3.1.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ceres Solver is a C++ library for modeling and solving large,
complicated optimization problems. It can be used to solve Non-linear Least
Squares problems with bounds constraints and general unconstrained optimization
problems.

This package is built with Eigen only.

%package -n libceres-devel
Summary:        Ceres Solver header files
License:        BSD-3-Clause
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
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n libceres%{sover}
Ceres Solver is a C++ library for modeling and solving large,
complicated optimization problems. It can be used to solve Non-linear Least
Squares problems with bounds constraints and general unconstrained optimization
problems.

This package is built with Eigen only.


%prep
%setup -q

%build
%cmake -DCXSPARSE=ON -DSUITESPARSE=ON -DEIGENSPARSE=ON -DOPENMP=ON -DCXX11=ON -DCMAKE_INSTALL_PREFIX=/usr -DEIGEN_INCLUDE_DIR_HINTS=/usr/include/eigen3 -DGFLAGS=OFF -DMINIGLOG=OFF -DBUILD_SHARED_LIBS=ON
make

%install
%cmake_install

%post -n libceres%{sover} -p /sbin/ldconfig

%postun -n libceres%{sover} -p /sbin/ldconfig

%files -n libceres-devel
%defattr(-,root,root)
%{_includedir}/ceres/
%{_libdir}/cmake/Ceres/
%{_libdir}/libceres.so

%files -n libceres%{sover}
%defattr(-,root,root)
%{_libdir}/libceres.so.*

%changelog
