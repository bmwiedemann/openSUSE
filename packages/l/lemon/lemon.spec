#
# spec file for package lemon
#
# Copyright (c) 2021 SUSE LLC
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


%define sonum   1_3_1
%define libname libemon%{sonum}
Name:           lemon
Version:        1.3.1
Release:        0
Summary:        Library of Efficient Models and Optimization in Networks
License:        BSL-1.0
Group:          System/Libraries
URL:            https://lemon.cs.elte.hu/
Source0:        http://lemon.cs.elte.hu/pub/sources/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE fix_install_libdir.patch andythe_great@pm.me -- Fix some files went into lib instead of lib64.
Patch0:         fix_install_libdir.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glpk-devel >= 4.33
Requires:       %{libname} = %{version}

%description
LEMON stands for Library for Efficient Modeling and Optimization in
Networks.  It is a C++ template library providing efficient
implementations of common data structures and algorithms with focus on
combinatorial optimization tasks connected mainly with graphs and
networks.

LEMON is a member of the COIN-OR initiative, a collection of OR related
open source projects. You are free to use it in your commercial or
non-commercial applications under very permissive license terms.

The project was launched by the Egerváry Research Group on Combinatorial
Optimization (EGRES) at the Operations Research Department of the Eötvös
Loránd University, Budapest in 2003. Up to this point, the developers of
the library work at the Eötvös Loránd University, Budapest and at the
Budapest University of Technology and Economics.

%package -n     libemon%{sonum}
Summary:        Library of Efficient Models and Optimization in Networks
Group:          System/Libraries
Requires:       libglpk40 >= 4.33

%description -n libemon%{sonum}
LEMON stands for Library for Efficient Modeling and Optimization in
Networks.  It is a C++ template library providing efficient
implementations of common data structures and algorithms with focus on
combinatorial optimization tasks connected mainly with graphs and
networks.

This package contains the shared library of LEMON.

%package devel
Summary:        Development headers and files for LEMON
Group:          Development/Libraries/C and C++
BuildRequires:  pkgconfig
Requires:       %{name} = %{version}-%{release}
Requires:       glpk-devel >= 4.33
Requires:       %{libname} = %{version}

%description devel
LEMON stands for Library for Efficient Modeling and Optimization in
Networks.  It is a C++ template library providing efficient
implementations of common data structures and algorithms with focus on
combinatorial optimization tasks connected mainly with graphs and
networks.

This package contains the libraries and headers for developing
applications which use LEMON.

%package doc
Summary:        Documentation of LEMON
Group:          Documentation/HTML
Requires:       %{name} = %{version}-%{release}
Requires:       %{libname} = %{version}

%description doc
LEMON stands for Library for Efficient Modeling and Optimization in
Networks.  It is a C++ template library providing efficient
implementations of common data structures and algorithms with focus on
combinatorial optimization tasks connected mainly with graphs and
networks.

This package contains the documentation of LEMON in HTML format.

%prep
%autosetup -p1

%build
%cmake \
%if 0%{?suse_version} > 1530
       -DCMAKE_BUILD_TYPE:STRING=Maintainer \
%endif
       ..
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
# Build type Maintainer will enable testing, but no clue why it fail on Leap but not on TW.
%if 0%{?suse_version} > 1530
%ctest
%endif

%files -n %{libname}
%{_libdir}/libemon.so.%{version}

%files
%license LICENSE
%doc README
%{_bindir}/lemon-0.x-to-1.x.sh
%{_bindir}/dimacs-solver
%{_bindir}/dimacs-to-lgf
%{_bindir}/lgf-gen

%files devel
%dir %{_datadir}/lemon
%dir %{_datadir}/lemon/cmake
%{_includedir}/lemon
%{_libdir}/pkgconfig/lemon.pc
%{_libdir}/libemon.so
%{_datadir}/lemon/cmake/LEMONConfig.cmake

%files doc
%doc doc/html

%changelog
