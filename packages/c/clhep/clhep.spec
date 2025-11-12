#
# spec file for package clhep
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define tagname 2_4_7_2
%define shlib libCLHEP-%{tagname}
# clhep requires a buildir which is not a subdirectory of the sourcedir
%global __builddir %{_builddir}/%{name}_build

Name:           clhep
Version:        2.4.7.2
Release:        0
Summary:        A class library for high energy physics
License:        GPL-3.0-only OR LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://proj-clhep.web.cern.ch/proj-clhep/
Source0:        https://gitlab.cern.ch/CLHEP/CLHEP/-/archive/CLHEP_%{tagname}/CLHEP-CLHEP_%{tagname}.tar.bz2#/clhep-%{tagname}.tar.bz2
Source99:       clhep.macros
# PATCH-FIX-UPSTREAM clhep-docdir.patch badshah400@gmail.com -- Allow configuring docdir from cmake command
Patch2:         clhep-docdir.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# Section Docs
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  texlive-latex-bin
# /Section
%include %SOURCE99

%description
CLHEP is intended to be a set of high energy physics specific
foundation and utility classes such as random generators, physics
vectors, geometry and linear algebra. CLHEP is structured in a set of
packages independent of any external package (interdependencies within
CLHEP are allowed under certain conditions).

%package -n %{shlib}
Summary:        A class library for high energy physics
Group:          Productivity/Scientific/Physics
Provides:       clhep = %{version}
Obsoletes:      clhep < %{version}

%description -n %{shlib}
CLHEP is intended to be a set of high energy physics specific
foundation and utility classes such as random generators, physics
vectors, geometry and linear algebra. CLHEP is structured in a set of
packages independent of any external package (interdependencies within
CLHEP are allowed under certain conditions).

This package provides the shared libraries for CLHEP.

%package devel
Summary:        A class library for high energy physics
Group:          Development/Libraries/C and C++
Requires:       %{name}-Units-devel = %{version}
Requires:       %{name}-Utility-devel = %{version}
Requires:       %{shlib} = %{version}
Requires:       pkgconfig(clhep-cast) = %{version}
Requires:       pkgconfig(clhep-evaluator) = %{version}
Requires:       pkgconfig(clhep-exceptions) = %{version}
Requires:       pkgconfig(clhep-genericfunctions) = %{version}
Requires:       pkgconfig(clhep-geometry) = %{version}
Requires:       pkgconfig(clhep-matrix) = %{version}
Requires:       pkgconfig(clhep-random) = %{version}
Requires:       pkgconfig(clhep-randomobjects) = %{version}
Requires:       pkgconfig(clhep-refcount) = %{version}
Requires:       pkgconfig(clhep-vector) = %{version}
Recommends:     %{name}-doc = %{version}

%description devel
CLHEP is intended to be a set of high energy physics specific
foundation and utility classes such as random generators, physics
vectors, geometry and linear algebra. CLHEP is structured in a set of
packages independent of any external package (interdependencies within
CLHEP are allowed under certain conditions).

This package provides the header files and libraries for development
of applications using CLHEP.

%package doc
Summary:        Documentation for CLHEP
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package provides documentation for the CLHEP library.

# Section CLHEP library subpackages

%package Units-devel
Summary:        The Units library from CLHEP
BuildArch:      noarch

%description Units-devel
This package provides the header-only Units library from CLHEP

%package Utility-devel
Summary:        CLHEP Utility library
BuildArch:      noarch

%description Utility-devel
This package provides the header-only Utility library from CLHEP.

%clhep_subpkg_lib -n Cast
%clhep_subpkg_lib -n Evaluator
%clhep_subpkg_lib -n Exceptions
%clhep_subpkg_lib -n GenericFunctions
%clhep_subpkg_lib -n Geometry
%clhep_subpkg_lib -n Matrix
%clhep_subpkg_lib -n Random
%clhep_subpkg_lib -n RandomObjects
%clhep_subpkg_lib -n RefCount
%clhep_subpkg_lib -n Vector

# Note pkgconfig based requires are automatically determined
%clhep_subpkg_devel -n Cast
%clhep_subpkg_devel -n Evaluator
%clhep_subpkg_devel -n Exceptions
%clhep_subpkg_devel -n GenericFunctions
%clhep_subpkg_devel -n Geometry
%clhep_subpkg_devel -n Matrix clhep-Units-devel clhep-Utility-devel
%clhep_subpkg_devel -n Random clhep-Units-devel clhep-Utility-devel
%clhep_subpkg_devel -n RandomObjects clhep-Units-devel clhep-Utility-devel
%clhep_subpkg_devel -n RefCount
%clhep_subpkg_devel -n Vector clhep-Units-devel

# /Section

%prep
%autosetup -n CLHEP-CLHEP_%{tagname} -p1
chmod -x README.md ChangeLog

%build
# remove nonworking check for LIB_SUFFIX, gives wrong result for PPC64
sed -i "/_clhep_lib_suffix_64()/d" cmake/Modules/ClhepVariables.cmake

%cmake \
  -DCLHEP_BUILD_DOCS:BOOL=ON \
  -DCLHEP_BUILD_STATIC_LIBS:BOOL=OFF \
  -DCLHEP_DOCDIR:PATH=%{_docdir}/%{name}/ \
%ifarch x86_64 ppc64 ppc64le aarch64 riscv64
  -DLIB_SUFFIX=64 \
%endif
%{nil}

%cmake_build

%install
%cmake_install

# testThreaded fails on 32-bit
%ifnarch %{ix86}
%check
%ctest
%endif

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%license COPYING COPYING.LESSER
%doc ChangeLog README.md
%{_libdir}/libCLHEP-%{version}.so

%files devel
%{_bindir}/clhep-config
%{_includedir}/CLHEP/*.h
%{_includedir}/clhep.modulemap
%{_libdir}/libCLHEP.so
%{_libdir}/CLHEP-%{version}/
%{_libdir}/pkgconfig/clhep.pc

%files doc
%{_docdir}/%{name}/

%files Units-devel
%{_bindir}/Units-config
%{_includedir}/CLHEP/Units/

%files Utility-devel
%{_bindir}/Utility-config
%{_includedir}/CLHEP/Utility/

%changelog
