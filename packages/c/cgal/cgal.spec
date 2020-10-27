#
# spec file for package cgal
#
# Copyright (c) 2020 SUSE LLC
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


# Disable Qt5 for embedded platforms, QOpenGlFunctions_2_1 is not available with GLES
%ifarch %arm aarch64
%bcond_with qt5
%else
%bcond_without qt5
%endif

#@TODO : clarify and split licence correctly, GPL & LGPL 3+ version
#@TODO : split package in coherent parts
#@TODO : rename parts (inspirated by sfcgal packaging)
#@TODO : ask for rename and take into account the obsolete existant thing. like libcgal deps

# soversions, according to Installation/CMakeLists.txt
#   CGAL-4.14  : 14.0.0 , but only for CGAL_ImageIO (ABI broken in CGAL::Image_3.)
#                              and for CGAL_Qt5 (ABI broken in DemoMainWindow)
#   CGAL-4.14  : 13.0.3 , for other libraries
%define _sover 13
%define _sover_Core 13
%define _sover_ImageIO 14
%define _sover_Qt5 14

%define _sourcename CGAL
%define _libname() libCGAL%{?1}%{?2}%{expand:%{_sover%{?1}}}
Name:           cgal
Version:        5.1
Release:        0
Summary:        Computational Geometry Algorithms Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://www.cgal.org/
Source0:        https://github.com/CGAL/cgal/releases/download/v%{version}/CGAL-%{version}.tar.xz
Source1:        https://github.com/CGAL/cgal/releases/download/v%{version}/CGAL-%{version}-doc_html.tar.xz
Source2:        cgal-rpmlintrc
BuildRequires:  blas-devel
BuildRequires:  cmake >= 2.8.11
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glu-devel
BuildRequires:  gmp-devel
BuildRequires:  lapack-devel
BuildRequires:  libboost_atomic-devel >= 1.66.0
BuildRequires:  libboost_system-devel >= 1.66.0
BuildRequires:  libboost_thread-devel >= 1.66.0
%if %{with qt5}
BuildRequires:  cmake(Qt5) >= 5.3
BuildRequires:  cmake(Qt5OpenGL) >= 5.3
BuildRequires:  cmake(Qt5Svg) >= 5.3
BuildRequires:  cmake(Qt5Xml) >= 5.3
%endif
BuildRequires:  mpfr-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
Requires:       libcgal-devel = %{version}

%description
CGAL provides geometric algorithms in a C++ library.

The library offers data structures and algorithms like
triangulations, Voronoi diagrams, Boolean operations on polygons and
polyhedra, point set processing, arrangements of curves, surface and
volume mesh generation, geometry processing, alpha shapes, convex
hull algorithms, shape analysis, AABB and KD trees.

%package -n %{_libname}
Summary:        Computational Geometry Algorithms Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{_libname}
CGAL provides geometric algorithms in a C++ library.

The library offers data structures and algorithms like
triangulations, Voronoi diagrams, Boolean operations on polygons and
polyhedra, point set processing, arrangements of curves, surface and
volume mesh generation, geometry processing, alpha shapes, convex
hull algorithms, shape analysis, AABB and KD trees.

%package -n %{_libname _Core}
Summary:        Computational Geometry Algorithms Library
# Required after package split, remove on sover bump
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Libraries
Conflicts:      %{_libname} < %{version}

%description -n %{_libname _Core}
CGAL provides geometric algorithms in a C++ library.

The library offers data structures and algorithms like
triangulations, Voronoi diagrams, Boolean operations on polygons and
polyhedra, point set processing, arrangements of curves, surface and
volume mesh generation, geometry processing, alpha shapes, convex
hull algorithms, shape analysis, AABB and KD trees.

%package -n %{_libname _ImageIO}
Summary:        Computational Geometry Algorithms Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{_libname _ImageIO}
CGAL provides geometric algorithms in a C++ library.

The library offers data structures and algorithms like
triangulations, Voronoi diagrams, Boolean operations on polygons and
polyhedra, point set processing, arrangements of curves, surface and
volume mesh generation, geometry processing, alpha shapes, convex
hull algorithms, shape analysis, AABB and KD trees.

%package -n %{_libname _Qt5 - }
Summary:        Computational Geometry Algorithms Library
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
Group:          System/Libraries

%description -n %{_libname _Qt5 - }
CGAL provides geometric algorithms in a C++ library.

The library offers data structures and algorithms like
triangulations, Voronoi diagrams, Boolean operations on polygons and
polyhedra, point set processing, arrangements of curves, surface and
volume mesh generation, geometry processing, alpha shapes, convex
hull algorithms, shape analysis, AABB and KD trees.

%package devel
Summary:        Development files and tools for CGAL applications
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSL-1.0
Group:          Development/Libraries/C and C++
Requires:       %{_libname _Core} = %{version}
Requires:       %{_libname _ImageIO} = %{version}
Requires:       %{_libname} = %{version}
%if %{with qt5}
Requires:       %{_libname _Qt5 - } = %{version}
%endif
Requires:       blas
Requires:       cmake
Requires:       gmp-devel
Requires:       lapack
Requires:       libboost_atomic-devel
Requires:       libboost_system-devel
Requires:       libboost_thread-devel
Requires:       mpfr-devel
Requires:       zlib-devel
#For compatibility with package looking for our old name
Provides:       libcgal-devel = %{version}

%description devel
This package provides the headers files and tools you may need to
develop applications using CGAL.

%package demo-examples-devel
Summary:        Example & demo files for CGAL library usage
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND BSL-1.0 AND MIT
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
%cmake -DCGAL_HEADER_ONLY=OFF \
       -DCGAL_INSTALL_LIB_DIR=%{_lib}

make %{?_smp_mflags}

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

# Clean doc wrongly placed by make install
rm -rfv %{buildroot}/%{_datadir}/doc/CGAL

# no macos here.
rm %{buildroot}/%{_bindir}/cgal_make_macosx_app

install -d %{buildroot}/%{_docdir}/%{name}-doc/
cp -a doc_html %{buildroot}/%{_docdir}/%{name}-doc/
%fdupes %{buildroot}%{_docdir}/%{name}-doc/

%fdupes %{buildroot}/%{_datadir}

%post -n %{_libname} -p /sbin/ldconfig
%postun -n %{_libname} -p /sbin/ldconfig
%post -n %{_libname _Core} -p /sbin/ldconfig
%postun -n %{_libname _Core} -p /sbin/ldconfig
%post -n %{_libname _Qt5 - } -p /sbin/ldconfig
%postun -n %{_libname _Qt5 - } -p /sbin/ldconfig
%post -n %{_libname _ImageIO} -p /sbin/ldconfig
%postun -n %{_libname _ImageIO} -p /sbin/ldconfig

%files -n %{_libname}
%license LICENSE*
%{_libdir}/libCGAL.so.%{_sover}*

%files -n %{_libname _Core}
%{_libdir}/libCGAL_Core.so.%{_sover_Core}*

%files -n %{_libname _ImageIO}
%{_libdir}/libCGAL_ImageIO.so.%{_sover_ImageIO}*

%if %{with qt5}
%files -n %{_libname _Qt5 - }
%{_libdir}/libCGAL_Qt5.so.%{_sover_Qt5}*
%endif

%files devel
%license LICENSE*
%doc AUTHORS CHANGES.md
%{_includedir}/CGAL
%{_libdir}/libCGAL.so
%{_libdir}/libCGAL_Core.so
%{_libdir}/libCGAL_ImageIO.so
%if %{with qt5}
%{_libdir}/libCGAL_Qt5.so
%endif
%{_libdir}/cmake/CGAL
%{_bindir}/*
%{_mandir}/man1/cgal_create_cmake_script.1%{?ext_man}

%files demo-examples-devel
%license LICENSE*
%{_datadir}/CGAL

%files doc
%license LICENSE*
%doc AUTHORS CHANGES.md
%doc %{_docdir}/%{name}-doc/doc_html

%changelog
