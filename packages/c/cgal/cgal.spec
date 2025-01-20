#
# spec file for package cgal
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2014 Ioda-Net Sàrl, Charmoille, Switzerland.
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


#@TODO : clarify and split licence correctly, GPL & LGPL 3+ version
#@TODO : split package in coherent parts
#@TODO : rename parts (inspirated by sfcgal packaging)
#@TODO : ask for rename and take into account the obsolete existant thing. like libcgal deps
%define _sourcename CGAL
Name:           cgal
Version:        6.0.1
Release:        0
Summary:        Computational Geometry Algorithms Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.cgal.org/
Source0:        https://github.com/CGAL/cgal/releases/download/v%{version}/CGAL-%{version}.tar.xz
Source1:        https://github.com/CGAL/cgal/releases/download/v%{version}/CGAL-%{version}-doc_html.tar.xz
Source2:        cgal-rpmlintrc
BuildRequires:  blas-devel
BuildRequires:  cmake >= 3.14
BuildRequires:  fdupes
BuildRequires:  glu-devel
BuildRequires:  gmp-devel
BuildRequires:  lapack-devel
BuildRequires:  libboost_atomic-devel >= 1.72
BuildRequires:  libboost_system-devel >= 1.72
BuildRequires:  libboost_thread-devel >= 1.72
BuildRequires:  mpfr-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
Requires:       libcgal-devel = %{version}
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif

%description
CGAL provides geometric algorithms in a C++ library.

The library offers data structures and algorithms like
triangulations, Voronoi diagrams, Boolean operations on polygons and
polyhedra, point set processing, arrangements of curves, surface and
volume mesh generation, geometry processing, alpha shapes, convex
hull algorithms, shape analysis, AABB and KD trees.

%package devel
Summary:        Development files and tools for CGAL applications
License:        BSL-1.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       blas
Requires:       cmake
Requires:       gmp-devel
Requires:       lapack
Requires:       libboost_atomic-devel >= 1.72
Requires:       libboost_system-devel >= 1.72
Requires:       libboost_thread-devel >= 1.72
Requires:       mpfr-devel
Requires:       zlib-devel
#For compatibility with package looking for our old name
Provides:       libcgal-devel = %{version}

%description devel
This package provides the headers files and tools you may need to
develop applications using CGAL.

%package demo-examples-devel
Summary:        Example & demo files for CGAL library usage
License:        BSL-1.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
BuildArch:      noarch

%description demo-examples-devel
This package provides the sources of examples and demos of
CGAL algorithms. You can study them, compile and test CGAL
library.

%package doc
Summary:        Documentation CGAL algorithms
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides the documentation for CGAL algorithms.

%prep
%setup -q -n CGAL-%{version} -a1

%build
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CXX="g++-13"
%endif

%cmake -DCGAL_INSTALL_LIB_DIR=%{_lib} \
       -DCGAL_INSTALL_DOC_DIR=%{_docdir}/%{name}-doc

%make_build

# Unfortunately take +6600sec locally.
# So we just deliver the source code in cgal package.
#  -DWITH_examples=true \
#  -DWITH_demos=true \

%install
%cmake_install

install -d %{buildroot}/%{_datadir}/CGAL/examples
install -d %{buildroot}/%{_datadir}/CGAL/demo
cp -a examples/* %{buildroot}/%{_datadir}/CGAL/examples
cp -a demo/* %{buildroot}/%{_datadir}/CGAL/demo

# no macos here.
#rm %{buildroot}/%{_bindir}/cgal_make_macosx_app

# installed as docs, but licenses are under %%{_datadir}/licenses/, remove duplicate
rm %{buildroot}%{_docdir}/%{name}-doc/LICENSE*

cp -a doc_html %{buildroot}/%{_docdir}/%{name}-doc/
%fdupes %{buildroot}%{_docdir}/%{name}-doc/

%fdupes %{buildroot}/%{_datadir}

%files devel
%license LICENSE*
%doc AUTHORS CHANGES.md
%{_includedir}/CGAL
%{_libdir}/cmake/CGAL
%{_bindir}/cgal_create_CMakeLists
%{_bindir}/cgal_create_cmake_script
%{_mandir}/man1/cgal_create_cmake_script.1%{?ext_man}

%files demo-examples-devel
%license LICENSE*
%{_datadir}/CGAL

%files doc
%license LICENSE*
%doc %dir %{_docdir}/%{name}-doc
%doc %{_docdir}/%{name}-doc/doc_html
%doc %{_docdir}/%{name}-doc/AUTHORS
%doc %{_docdir}/%{name}-doc/CHANGES.md

%changelog
