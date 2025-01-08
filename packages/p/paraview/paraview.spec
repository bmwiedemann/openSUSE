#
# spec file for package paraview
#
# Copyright (c) 2025 SUSE LLC
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


%define major_ver 5
%define minor_ver 13
%define short_ver %{major_ver}.%{minor_ver}
%define shlib libparaview%{major_ver}_%{minor_ver}

%if 0%{?suse_version} <= 1500
%bcond_with    fast_float
%bcond_with    jsoncpp
%if 0%{?sle_version} <= 150400
%bcond_with    pugixml
%bcond_with    verdict
%else
%bcond_without pugixml
%bcond_without verdict
%endif

%if 0%{?sle_version} <= 150600
%bcond_with    jsoncpp
%bcond_with    fmt
%bcond_with    haru
%else
%bcond_without fmt
%bcond_without haru
%endif

%else
%bcond_without fast_float
%bcond_without fmt
%bcond_without haru
%bcond_without jsoncpp
%bcond_without pugixml
%bcond_without verdict
%endif

%bcond_without nlohmann
%bcond_without proj
%bcond_without gl2ps

Name:           paraview
Version:        %{short_ver}.2
Release:        0
Summary:        Data analysis and visualization application
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
URL:            https://www.paraview.org
Source0:        https://www.paraview.org/files/v%{short_ver}/ParaView-v%{version}.tar.xz
Source1:        %{name}-rpmlintrc
# CAUTION: GettingStarted may or may not be updated with each minor version
Source2:        https://www.paraview.org/files/v%{short_ver}/ParaViewGettingStarted-%{major_ver}.%{minor_ver}.2.pdf
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
BuildRequires:  protobuf21-devel
BuildRequires:  python3-Sphinx
BuildRequires:  python3-Twisted
BuildRequires:  python3-devel
BuildRequires:  python3-matplotlib
BuildRequires:  python3-qt5-devel
BuildRequires:  readline-devel
BuildRequires:  utfcpp-devel
BuildRequires:  wget
BuildRequires:  pkgconfig(CLI11)
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
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblz4) >= 1.7.3
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpqxx)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(proj) >= 5.0.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
%if %{with fmt}
BuildRequires:  fmt-10-devel
%endif
%if %{with gl2ps}
BuildRequires:  gl2ps-devel >= 1.4.1
%endif
%if %{with haru}
BuildRequires:  libharu-devel > 2.4.0
%endif
%if %{with fast_float}
BuildRequires:  cmake(FastFloat)
%endif
%if %{with jsoncpp}
BuildRequires:  pkgconfig(jsoncpp) >= 1.9.4
%endif
%if %{with nlohmann}
BuildRequires:  pkgconfig(nlohmann_json)
%endif
%if %{with pugixml}
BuildRequires:  pkgconfig(pugixml) >= 1.11
%endif
%if %{with verdict}
BuildRequires:  verdict-devel
%endif
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

# Fix erroneous dependency on sqlite3 binary
sed -i -e '/set(vtk_sqlite_build_binary 1)/ s/.*/#\0/' CMakeLists.txt

# Allow other versions for fast_float
sed -i -e '/VERSION .*/ d' VTK/ThirdParty/fast_float/CMakeLists.txt

%build
%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
%global __builder ninja

%cmake -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
       -DPARAVIEW_BUILD_SHARED_LIBS:BOOL=ON \
%if 0%{?suse_version} <= 1500 && 0%{?is_opensuse}
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
%endif
       -DBUILD_EXAMPLES:BOOL=OFF \
       -DBUILD_TESTING:BOOL=OFF \
       -DCMAKE_CXX_EXTENSIONS:BOOL=OFF \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
       -DPARAVIEW_BUILD_WITH_EXTERNAL:BOOL=ON \
       -DPARAVIEW_ENABLE_WEB:BOOL=ON \
       -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON \
       -DPARAVIEW_PYTHON_SITE_PACKAGES_SUFFIX=%{_lib}/python%{py3_ver}/site-packages/paraview \
       -DPARAVIEW_USE_PYTHON:BOOL=ON \
       -DPARAVIEW_USE_QT:BOOL=ON \
       -DPARAVIEW_USE_VTKM:BOOL=OFF \
       -DQtTesting_INSTALL_NO_DEVELOPMENT:BOOL=ON \
       -DVTK_BUILD_QT_DESIGNER_PLUGIN:BOOL=OFF \
       -DVTK_ENABLE_CATALYST:BOOL=ON \
       -DVTK_OPENGL_HAS_OSMESA:BOOL=OFF \
       -DVTK_PYTHON_OPTIONAL_LINK:BOOL=OFF \
       -DVTK_WRAP_PYTHON:BOOL=ON \
       -DVTK_MODULE_ENABLE_VTK_libharu:BOOL=YES \
       -DVTK_MODULE_ENABLE_VTK_pegtl:BOOL=YES \
       -DVTK_MODULE_ENABLE_VTK_zfp:BOOL=NO \
       -DVTK_MODULE_USE_EXTERNAL_VTK_exprtk:BOOL=OFF \
       -DVTK_MODULE_USE_EXTERNAL_VTK_fast_float:BOOL=%{?with_fast_float:ON}%{!?with_fast_float:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_fmt:BOOL=%{?with_fmt:ON}%{!?with_fmt:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps=%{?with_gl2ps:ON}%{!?with_gl2ps:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_ioss:BOOL=OFF \
       -DVTK_MODULE_USE_EXTERNAL_VTK_jsoncpp=%{?with_jsoncpp:ON}%{!?with_jsoncpp:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_libharu=%{?with_haru:ON}%{!?with_haru:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_libproj=%{?with_proj:ON}%{!?with_proj:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_nlohmannjson=%{?with_nlohmann:ON}%{!?with_nlohmann:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_pegtl=NO \
       -DVTK_MODULE_USE_EXTERNAL_VTK_pugixml=%{?with_pugixml:ON}%{!?with_pugixml:OFF} \
       -DVTK_MODULE_USE_EXTERNAL_VTK_token:BOOL=OFF \
       -DVTK_MODULE_USE_EXTERNAL_VTK_verdict=%{?with_verdict:ON}%{!?with_verdict:OFF} \
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

# Unnecessary hash-bang
sed -i "1{\@%{_bindir}/env@d}" %{buildroot}%{python3_sitearch}/paraview/vtkmodules/generate_pyi.py
sed -i "1{\@%{_bindir}/env@d}" %{buildroot}%{python3_sitearch}/paraview/vtkmodules/test/rtImageTest.py

# INSTALL DOCUMENTATION USED BY THE HELP MENU IN MAIN APP
install -Dm0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}-%{short_ver}/doc/GettingStarted.pdf

%fdupes %{buildroot}/

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
%dir %{_libdir}/vtk/
%dir %{_libdir}/vtk/hierarchy
%{_libdir}/vtk/hierarchy/ParaView/
%if %{without proj}
%{_datadir}/vtk-pv%{major_ver}.%{minor_ver}/
%endif

%files -n %{shlib}
%{_libdir}/*.so.*

%files plugins
%{_libdir}/%{name}-%{short_ver}/

%files devel
%{_libdir}/*.so
%{_libdir}/cmake/paraview-%{short_ver}/
%{_bindir}/smTest*
%{_bindir}/vtk*
%{_includedir}/%{name}*

%files devel-static
%{_bindir}/paraview-config
%{_libdir}/*.a

%files -n python3-paraview
%{python3_sitearch}/%{name}/

%changelog
