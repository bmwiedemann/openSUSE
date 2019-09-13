#
# spec file for package ceres-solver
#
# Copyright (c) 2017-2018 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define sover 1

Name:           ceres-solver
Version:	1.14.0
Release:        0
License:	BSD-3-Clause
Summary:	C++ library for modeling and solving optimization problems
URL:		http://ceres-solver.org/
Group:		Development/Libraries/C and C++
Source:		http://ceres-solver.org/%{name}-%{version}.tar.gz
BuildRequires:	cmake >= 2.8.0
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(eigen3) >= 3.1.0
BuildRequires:	glog-devel >= 0.3.1
BuildRequires:	suitesparse-devel
BuildRequires:	libcxsparse3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Ceres Solver is a C++ library for modeling and solving large,
complicated optimization problems. It can be used to solve Non-linear Least
Squares problems with bounds constraints and general unconstrained optimization
problems.

This package is built with Eigen only.

%package -n libceres-devel
Summary:	Ceres Solver header files
Group:		Development/Libraries/C and C++
Requires:	libceres%{sover} = %{version}

%description -n libceres-devel
Ceres Solver is a C++ library for modeling and solving large,
complicated optimization problems. It can be used to solve Non-linear Least
Squares problems with bounds constraints and general unconstrained optimization
problems.

This package is built with Eigen only.


%package -n libceres%{sover}
Summary:	Ceres Solver shared library
Group:          System/Libraries
License:	LGPL-2.1

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
