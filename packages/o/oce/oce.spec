#
# spec file for package oce
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


# Whether clang should be used instead of gcc
%bcond_with scanbuild
%if %{with scanbuild}
%bcond_without clang
%else
%bcond_with clang
%endif

# Whether DRAWEXE should be built
%bcond_without build_draw

# disable vtk atm, oce code needs some older version
%if 0%{?suse_version} > 91310
%bcond_without build_vtk
%else
%bcond_with build_vtk
%endif

# Define openCASCADE version
%define ocversion 6.9.1

Name:           oce
Version:        0.18.3
Release:        0
Summary:        OpenCASCADE Community Edition
License:        LGPL-2.1-only WITH OCCT-exception-1.0
Group:          Productivity/Graphics/CAD

URL:            https://github.com/tpaviot/oce
Source0:        oce-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  cmake
BuildRequires:  fdupes
%if %{with clang}
BuildRequires:  libstdc++-devel
BuildRequires:  llvm-clang
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  ftgl-devel
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
%if %{with build_draw}
%if 0%{?suse_version} > 1230
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(tk)
%else
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
%endif
%endif
BuildRequires:  xz
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
%if %{with build_vtk}
BuildRequires:  vtk-devel
%ifarch x86_64

%else
%if 0%{?suse_version} > 1310
BuildRequires:  -libjawt.so
%else
BuildRequires:  -libjawt.so()
%endif
BuildRequires:  -libjawt.so(SUNWprivate_1.1)
%endif
%endif
BuildRequires:  java-devel
Provides:       OCE = %{version}
Provides:       OpenCASCADE = %{ocversion}
Obsoletes:      OCE < %{version}
Obsoletes:      OpenCASCADE < %{ocversion}
Conflicts:      otherproviders(OpenCASCADE)

%description
OpenCASCADE is a suite for 3D surface and solid modeling, visualization, data
exchange and rapid application development. It is a platform for
development of numerical simulation software including CAD/CAM/CAE, AEC and
GIS, as well as PDM applications.

%package vtk
Summary:        VTK libraries
Group:          System/Libraries

%description vtk
This package includes OpenCASCADE VTK libraries.

%package DRAWEXE
Summary:        Scripting interface to the OpenCASCADE libraries
Group:          Productivity/Graphics/Visualization/Other

%description DRAWEXE
This program provides a kind of scripting interface to the OpenCASCADE
libraries. You can perform a simple test by starting it and entering at the
command line: "pload ALL" then "source /usr/share/oce/src/DrawResources/VisualizationDemo.tcl".

%package devel
Summary:        Development files for openCASCADE
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
%if %{with build_vtk}
Requires:       %{name}-vtk = %{version}
%endif
Provides:       OCE-devel = %{version}
Provides:       OpenCASCADE-devel = %{ocversion}
Obsoletes:      OCE-devel < %{version}
Obsoletes:      OpenCASCADE-devel < %{ocversion}
Conflicts:      otherproviders(OpenCASCADE-devel)

%description devel
This package contains the files needed for development with OpenCASCADE.

%prep
%setup -q

%build
mkdir build
cd build
  CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
  CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing" \
%if %{with clang}
%if %{with scanbuild}
  CC=/usr/share/clang/scan-build/ccc-analyzer CXX=/usr/share/clang/scan-build/c++-analyzer CCC_CXX=clang++ \
%else
  CC=clang CXX=clang++ \
%endif
%endif
  cmake \
    -DOCE_USE_BUNDLE=OFF \
    -DOCE_USE_PCH=OFF \
    -DOCE_BUILD_SHARED_LIB=ON \
    -DOCE_DISABLE_X11=OFF \
    -DOCE_MODEL=ON \
    -DOCE_OCAF=ON \
    -DOCE_DATAEXCHANGE=ON \
%if %{with build_vtk}
    -DOCE_WITH_VTK=ON \
%else
    -DOCE_WITH_VTK=OFF \
%endif
%if %{with build_draw}
    -DOCE_DRAW=ON \
%else
    -DOCE_DRAW=OFF \
%endif
    -DOCE_VISUALISATION=ON -DOCE_DISABLE_TKSERVICE_FONT=OFF \
    -DOCE_WITH_GL2PS=ON \
    -DOCE_WITH_FREEIMAGE=ON \
    -DOCE_EXTRA_WARNINGS=OFF \
    -DOCE_TESTING=OFF \
    -DOCE_ADD_HEADERS=OFF \
    -DOCE_RPATH_FILTER_SYSTEM_PATHS=ON \
    -DOCE_ENABLE_DEB_FLAG=ON \
    -DOCE_COVERAGE=OFF \
    -DOCE_MULTITHREAD_LIBRARY=OPENMP -DOCE_TBB_MALLOC_SUPPORT=OFF \
    -DOCE_INSTALL_PREFIX=%_prefix \
    -DOCE_INSTALL_BIN_DIR=%_bindir \
    -DOCE_INSTALL_LIB_DIR=%_libdir \
    -DOCE_INSTALL_PACKAGE_LIB_DIR=%_libdir \
    -DOCE_INSTALL_INCLUDE_DIR=%_includedir/oce \
    -DOCE_INSTALL_DATA_DIR=%_datadir/oce \
    -DOCE_INSTALL_CMAKE_DATA_DIR=%_datadir/oce \
    ..
%if %{with scanbuild}
  /usr/share/clang/scan-build/scan-build --use-analyzer %_bindir/clang -analyze-headers \
%endif
  make %{?_smp_mflags} VERBOSE=1
cd ..

%install
cd build
  make install DESTDIR=%buildroot
cd ..

%fdupes -s %buildroot/%_includedir

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post vtk -p /sbin/ldconfig

%postun vtk -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%_libdir/libFW*
%_libdir/libPT*
%_libdir/libTK*
%if %{with build_vtk}
%exclude %_libdir/*Vtk*.so.*
%endif
%exclude %_libdir/*.so
%_datadir/oce
%if %{with build_draw}
%exclude %_datadir/oce/src/DrawResources
%exclude %_datadir/oce/*.cmake

%files DRAWEXE
%defattr(-,root,root,-)
%_bindir/DRAWEXE
%_datadir/oce/src/DrawResources
%endif

%if %{with build_vtk}
%files vtk
%defattr(-,root,root,-)
%_libdir/*Vtk*.so.*
%endif

%files devel
%defattr(-,root,root,-)
%doc NEWS.md
%_datadir/oce/*.cmake
%_includedir/oce
%_libdir/*.so

%changelog
