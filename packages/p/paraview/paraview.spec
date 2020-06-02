#
# spec file for package paraview
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


%define major_ver 5.8
%define shlib libparaview5_8

%if 0%{?suse_version} <= 1500
%bcond_with    pugixml
%else
%bcond_without pugixml
%endif
# Need unrelased version > 1.4.0 with e.g. gl2psTextOptColorBL
%bcond_with    gl2ps
# Need patched version with HPDF_SHADING
%bcond_with    haru

%define __builder ninja

Name:           paraview
Version:        5.8.0
Release:        0
Summary:        Data analysis and visualization application
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
URL:            https://www.paraview.org
Source0:        https://www.paraview.org/files/v%{major_ver}/ParaView-v%{version}.tar.xz
Source1:        %{name}-rpmlintrc
# CAUTION: GettingStarted may or may not be updated with each minor version
Source2:        https://www.paraview.org/files/v%{major_ver}/ParaViewGettingStarted-%{major_ver}.0.pdf
Source3:        https://www.paraview.org/files/v%{major_ver}/ParaViewGuide-%{version}.pdf
# PATCH-FIX-UPSTREAM paraview-desktop-entry-fix.patch badshah400@gmail.com -- Fix desktop menu entry by inserting proper required categories
Patch1:         paraview-desktop-entry-fix.patch
# PATCH-FIX-UPSTREAM fix-3d48a287-support-new-api-cgio_read_data_type.patch -- Add support for new API cgio_read_***data***_type
Patch2:         fix-3d48a287-support-new-api-cgio_read_data_type.patch
# PATCH-FIX-OPENSUSE fix-libharu-missing-m.patch -- missing libraries for linking (gh#libharu/libharu#213)
Patch8:         fix-libharu-missing-m.patch
# PATCH-FIX-OPENSUSE bundled_exodusii_add_missing_libpthread.patch stefan.bruens@rwth-aachen.de -- Add missing libm for linking (updated to upstream patch, see https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6865)
Patch10:        bundled_exodusii_add_missing_libpthread.patch
BuildRequires:  Mesa-devel
BuildRequires:  cgns-devel
BuildRequires:  cmake >= 3.13
BuildRequires:  desktop-file-utils
BuildRequires:  double-conversion-devel
BuildRequires:  doxygen
BuildRequires:  exodusii-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gnuplot
BuildRequires:  graphviz
BuildRequires:  hdf5-devel
BuildRequires:  libboost_graph-devel
BuildRequires:  libboost_headers-devel
%if %{with gl2ps}
BuildRequires:  gl2ps-devel
%endif
%if %{with haru}
BuildRequires:  libharu-devel > 2.3.0
%endif
BuildRequires:  libnetcdf_c++-devel
BuildRequires:  ninja
BuildRequires:  python3-Sphinx
BuildRequires:  python3-Twisted
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-qt5-devel
BuildRequires:  readline-devel
BuildRequires:  utfcpp-devel
BuildRequires:  wget
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(eigen3) >= 2.91.0
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(jsoncpp) >= 0.7.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblz4) >= 1.7.3
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpqxx)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf) >= 2.6.0
%if %{with pugixml}
BuildRequires:  pkgconfig(pugixml)
%endif
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-plugins
Requires:       gnuplot
Requires:       graphviz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       cmake >= 3.3
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
sed -Ei "1{s|#!/usr/bin/env python3|#!/usr/bin/python3|}" Clients/CommandLineExecutables/paraview-config

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
       -DPARAVIEW_BUILD_SHARED_LIBS:BOOL=ON \
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DPARAVIEW_USE_VTKM:BOOL=OFF \
       -DPARAVIEW_USE_QT:BOOL=ON \
       -DPARAVIEW_USE_PYTHON:BOOL=ON \
       -DPARAVIEW_PYTHON_SITE_PACKAGES_SUFFIX=%{_lib}/python%{py3_ver}/site-packages/paraview \
       -DVTK_PYTHON_OPTIONAL_LINK:BOOL=OFF \
       -DPARAVIEW_ENABLE_WEB:BOOL=ON \
       -DVTK_WRAP_PYTHON:BOOL=ON \
       -DVTK_OPENGL_HAS_OSMESA:BOOL=OFF \
       -DBUILD_EXAMPLES:BOOL=OFF \
       -DBUILD_TESTING:BOOL=OFF \
       -DQtTesting_INSTALL_NO_DEVELOPMENT:BOOL=ON \
       -DVTK_BUILD_QT_DESIGNER_PLUGIN:BOOL=OFF \
       -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
       -DPARAVIEW_BUILD_WITH_EXTERNAL:BOOL=ON \
       -DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps=%{?with_gl2ps:ON}%{!?with_gl2ps:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_libharu=%{?with_haru:ON}%{!?with_haru:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_pugixml=%{?with_pugixml:ON}%{!?with_pugixml:OFF}

%cmake_build

%install
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -exec chmod -x "{}" +

%cmake_install

# INSTALL DOCUMENTATION USED BY THE HELP MENU IN MAIN APP
install -Dm0644 %{S:2} %{buildroot}%{_datadir}/%{name}-%{major_ver}/doc/GettingStarted.pdf
install -Dm0644 %{S:3} %{buildroot}%{_datadir}/%{name}-%{major_ver}/doc/Guide.pdf

# REMOVE paraview-config: DOESN'T WORK WITHOUT STATIC LIBS ANYWAY
rm %{buildroot}%{_bindir}/paraview-config

%fdupes %{buildroot}/

%post -n %{shlib} -p /sbin/ldconfig

%postun -n %{shlib} -p /sbin/ldconfig

%files
%license %{_datadir}/licenses/ParaView/
%{_bindir}/*
%exclude %{_bindir}/smTest*
%exclude %{_bindir}/vtk*
%{_datadir}/%{name}-%{major_ver}/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_docdir}/paraview/
%dir %{_libdir}/vtk/
%dir %{_libdir}/vtk/hierarchy
%{_libdir}/vtk/hierarchy/ParaView/

%files -n %{shlib}
%{_libdir}/*.so.*

%files plugins
%{_libdir}/%{name}-%{major_ver}/

%files devel
%{_libdir}/*.so
%{_libdir}/cmake/paraview-%{major_ver}/
%{_bindir}/smTest*
%{_bindir}/vtk*
%{_includedir}/%{name}*

%files devel-static
%{_libdir}/*.a

%files -n python3-paraview
%{python3_sitearch}/%{name}/

%changelog
