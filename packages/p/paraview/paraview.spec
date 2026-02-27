#
# spec file for package paraview
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2026 SUSE LLC and contributors
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


%define major_ver 6
%define minor_ver 0
%define short_ver %{major_ver}.%{minor_ver}
%define shlib libparaview%{major_ver}_%{minor_ver}

Name:           paraview
Version:        %{short_ver}.1
Release:        0
Summary:        Data analysis and visualization application
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
URL:            https://www.paraview.org
Source0:        https://www.paraview.org/files/v%{short_ver}/ParaView-v%{version}.tar.xz
Source1:        %{name}-rpmlintrc
# CAUTION: GettingStarted may or may not be updated with each minor version
Source2:        https://www.paraview.org/files/v%{short_ver}/ParaViewGettingStarted-%{major_ver}.%{minor_ver}.1.pdf
# PATCH-FIX-UPSTREAM paraview-desktop-entry-fix.patch badshah400@gmail.com -- Fix desktop menu entry by inserting proper required categories
Patch0:         paraview-desktop-entry-fix.patch
# PATCH-FIX-OPENSUSE fix-libharu-missing-m.patch -- missing libraries for linking (gh#libharu/libharu#213)
Patch1:         fix-libharu-missing-m.patch
# We need to change the default soname for vtk modules.
Patch2:         fix-soversion-soname.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-Add-missing-libm-link-library-for-bundled-ExodusII.patch
BuildRequires:  Mesa-devel
BuildRequires:  cgns-devel
BuildRequires:  cmake >= 3.13
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gnuplot
BuildRequires:  graphviz
BuildRequires:  hdf5-devel
BuildRequires:  libboost_graph-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
%if 0%{?suse_version} <= 1500
BuildRequires:  protobuf-devel
%else
BuildRequires:  protobuf21-devel
%endif
BuildRequires:  python3-Sphinx
BuildRequires:  python3-Twisted
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-qt5-devel
BuildRequires:  readline-devel
BuildRequires:  sqlite3
BuildRequires:  utfcpp-devel
BuildRequires:  wget
BuildRequires:  cmake(vtk) >= 9.5.0
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(eigen3) >= 2.91.0
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblz4) >= 1.7.3
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
Requires:       gnuplot
Requires:       graphviz
Recommends:     %{name}-plugins
# Disable on aarch64 since GLES isn't supported for bundled vtk but is needed for paraview
ExcludeArch:    aarch64

%description
ParaView is a data analysis and visualization application for
visualizing large data sets.

ParaView runs on distributed and shared memory systems alike. It uses VTK
(the Visualization Toolkit) as the data processing and rendering engine.
Data exploration can be done interactively in 3D or programmatically using
batch processing.

NOTE: The version in this package has NOT been compiled with MPI support.

%package -n %{shlib}
Summary:        Shared libraries for Paraview
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package provides the shared libraries for paraview.

%package        devel
Summary:        Headers for building ParaView plugins or embedding Catalyst
Group:          Development/Libraries/Other
Requires:       %{shlib} = %{version}
Requires:       cmake >= 3.13
Requires:       glibc-devel
Requires:       libboost_thread-devel

%description    devel
This package contains headers and libraries required to build plugins
for ParaView or to embed ParaView Catalyst in a simulation program.

%package -n python3-paraview
Summary:        Python bindings for Paraview
Group:          Productivity/Scientific/Physics
Requires:       python3
Requires:       python3-Twisted
Requires:       python3-matplotlib
Requires:       python3-numpy
Requires:       python3-qt5

%package devel-static
Summary:        Static libraries for Paraview, needed to building plugins
Group:          Productivity/Scientific/Physics
Requires:       %{name}-devel = %{version}

%description devel-static
This package contains the static libraries for Paraview, needed, for
example, to build plugins for paraview.

%description -n python3-paraview
This package provides the python(3) bindings and modules for paraview.

%package plugins
Summary:        Plugins for paraview
Group:          Productivity/Scientific/Physics
Requires:       %{name} = %{version}

%description plugins
This package provides the paraview plugins bundled with the upstream release.

%prep
%autosetup -p1 -n ParaView-v%{version}

# FIX env BASED HASHBANG
sed -Ei "1{s|#!%{_bindir}/env python3|#!%{_bindir}/python3|}" Clients/CommandLineExecutables/paraview-config.in

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%global __builder ninja

%cmake -DPARAVIEW_BUILD_SHARED_LIBS:BOOL=ON \
%if 0%{?suse_version} <= 1500 && 0%{?is_opensuse}
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
%endif
       -DBUILD_EXAMPLES:BOOL=OFF \
       -DBUILD_TESTING:BOOL=OFF \
       -DCMAKE_CXX_EXTENSIONS:BOOL=OFF \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
       -DOpenGL_GL_PREFERENCE:STRING='GLVND' \
       -DPARAVIEW_BUILD_WITH_EXTERNAL:BOOL=ON \
       -DPARAVIEW_ENABLE_WEB:BOOL=ON \
       -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
       -DPARAVIEW_PYTHON_SITE_PACKAGES_SUFFIX=%{_lib}/python%{py3_ver}/site-packages \
       -DPARAVIEW_USE_EXTERNAL_VTK:BOOL=ON \
       -DPARAVIEW_USE_PYTHON:BOOL=ON \
       -DPARAVIEW_USE_QT:BOOL=ON \
       -DPARAVIEW_USE_VTKM:BOOL=OFF \
       -DQtTesting_INSTALL_NO_DEVELOPMENT:BOOL=ON \
       -DVTK_MODULE_ENABLE_ParaView_AdaptorsPython:STRING=NO \
       -DVTK_MODULE_ENABLE_ParaView_AdaptorsCamPython:STRING=NO \
       -Wno-dev \
       %{nil}

# ParaView >= 5.13.2 wrongly adds each option of CMAKE_SHARED_LINKER_FLAGS as a single
# option with multiple -Wl in betwen, this makes the build fail. Correct it manually
sed -i 's/,-Wl/ -Wl/g' ./build.ninja
sed -i 's/,-ffat-lto-objects/ -ffat-lto-objects/g' ./build.ninja

%cmake_build

%install
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -exec chmod -x "{}" +

%cmake_install

# INSTALL DOCUMENTATION USED BY THE HELP MENU IN MAIN APP
install -Dm0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}-%{short_ver}/doc/GettingStarted.pdf

%fdupes %{buildroot}/

%check

# Make sure the python library is at least importable
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitearch}
PYTHONDONTWRITEBYTECODE=1 python3 -c "from paraview.simple import *"

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files
%license %{_datadir}/licenses/ParaView/
%{_bindir}/*
# Part of paraview-devel-static
%exclude %{_bindir}/paraview-config
#
%exclude %{_bindir}/smTest*
%exclude %{_bindir}/vtk*
%{_datadir}/%{name}-%{short_ver}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_docdir}/paraview/
%{_libdir}/vtk/
%{_libdir}/vtk/hierarchy/
%{_libdir}/vtk/hierarchy/ParaView/

%files -n %{shlib}
%{_libdir}/*.so.*

%files plugins
%{_libdir}/%{name}-%{short_ver}/

%files devel
%{_libdir}/*.so
%{_libdir}/cmake/paraview-%{short_ver}/
%{_bindir}/smTest*
%{_includedir}/%{name}*

%files devel-static
%{_bindir}/paraview-config
%{_libdir}/*.a

%files -n python3-paraview
%{python3_sitearch}/%{name}/

%changelog
