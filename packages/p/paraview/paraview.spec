#
# spec file for package paraview
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define major_ver 5.6

Name:           paraview
Version:        5.6.2
Release:        0
Summary:        Data analysis and visualization application
License:        BSD-3-Clause
Group:          Productivity/Scientific/Physics
Url:            https://www.paraview.org
Source0:        https://www.paraview.org/files/v%{major_ver}/ParaView-v%{version}.tar.xz
Source1:        %{name}-rpmlintrc
# CAUTION: GettingStarted may or may not be updated with each minor version
Source2:        https://www.paraview.org/files/v%{major_ver}/ParaViewGettingStarted-%{major_ver}.0.pdf
Source3:        https://www.paraview.org/files/v%{major_ver}/ParaViewGuide-%{version}.pdf
# PATCH-FIX-UPSTREAM paraview-desktop-entry-fix.patch badshah400@gmail.com -- Fix desktop menu entry by inserting proper required categories
Patch1:         paraview-desktop-entry-fix.patch
# PATCH-FIX-UPSTREAM paraview-fix-file-contains-date-time.patch badshah400@gmail.com -- Remove reference to __DATE__ and __TIME__ from source
Patch2:         paraview-fix-file-contains-date-time.patch
# PATCH-FIX-UPSTREAM paraview-do-not-install-missing-vtk-doxygen-dir.patch foss@grueninger.de -- Remove install of nonexistent doxygen/html dir
Patch3:         paraview-do-not-install-missing-vtk-doxygen-dir.patch
# PATCH-FIX-UPSTREAM paraview-find-qhelpgenerator-qt5.patch badshah400@gmail.com -- Help find qhelpgenerator-qt5 instead of qhelpgenerator when Qt5 is used
Patch4:         paraview-find-qhelpgenerator-qt5.patch
# PATCH-FIX-OPENSUSE fix-libharu-missing-m.patch -- missing libraries for linking
Patch8:         fix-libharu-missing-m.patch
# PATCH-FIX-OPENSUSE fix-libhdf5-missing-m.patch -- missing libraries for linking
Patch9:         fix-libhdf5-missing-m.patch
BuildRequires:  Mesa-devel
BuildRequires:  boost-devel
BuildRequires:  cmake >= 3.3
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gnuplot
BuildRequires:  graphviz
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpqxx-devel
BuildRequires:  libtiff-devel
BuildRequires:  openssl-devel
BuildRequires:  python-Sphinx
BuildRequires:  python-devel
BuildRequires:  python-matplotlib
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xt)
%py_requires
BuildRequires:  fdupes
BuildRequires:  python-qt5-devel
BuildRequires:  python-twisted
BuildRequires:  python-zope.interface
BuildRequires:  readline-devel
BuildRequires:  wget
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
Requires:       gnuplot
Requires:       graphviz
Requires:       python
Requires:       python-base
Requires:       python-twisted
Requires:       python-zope.interface
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
# FIXME: Remove when builds for 32-bit are fixed; they currently fail due to offt definition issues in ThirdParty/cgns/vtkcgns/src/adf/ADF_internals.c
ExcludeArch:    %ix86
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ParaView is a data analysis and visualization application for
visualizing large data sets.

ParaView runs on distributed and shared memory systems alike. It uses VTK
(the Visualization Toolkit) as the data processing and rendering engine.
Data exploration can be done interactively in 3D or programmatically using
batch processing.

NOTE: The version in this package has NOT been compiled with MPI support.

%package        devel
Summary:        Headers for building ParaView plugins or embedding Catalyst
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description    devel
This package contains headers and libraries required to build plugins
for ParaView or to embed ParaView Catalyst in a simulation program.

%prep
%setup -q -n ParaView-v%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch8 -p1
%patch9 -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

# Prepare for gcc 4.9.0: work around gcc 4.9.0 regression
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=61294
sed -i -e 's/-Wl,--fatal-warnings//' VTK/CMake/vtkCompilerExtraFlags.cmake

export CC='gcc'
export CXX='g++'

%cmake  -DPV_INSTALL_LIB_DIR:PATH=%{_lib}/%{name} \
        -DVTK_INSTALL_ARCHIVE_DIR:PATH=%{_lib}/%{name} \
        -DVTK_INSTALL_LIBRARY_DIR:PATH=%{_lib}/%{name} \
        -DVTK_INSTALL_PACKAGE_DIR:PATH=%{_lib}/cmake/%{name}-%{major_ver} \
        -DVTK_INSTALL_DATA_DIR=share/%{name} \
        -DVTK_INSTALL_DOC_DIR=share/doc/packages/%{name} \
        -DCMAKE_CXX_COMPILER:FILEPATH=$CXX \
        -DCMAKE_C_COMPILER:FILEPATH=$CC \
        -DCMAKE_SKIP_RPATH:BOOL=OFF \
        -DPARAVIEW_USE_VTKM:BOOL=OFF \
        -DPARAVIEW_BUILD_QT_GUI:BOOL=ON \
        -DPARAVIEW_BUILD_PLUGIN_SLACTools:BOOL=ON \
        -DPARAVIEW_ENABLE_PYTHON:BOOL=ON \
        -DVTK_WRAP_PYTHON:BOOL=ON \
        -DVTK_WRAP_PYTHON_SIP:BOOL=ON \
        -DVTK_OPENGL_HAS_OSMESA:BOOL=OFF \
        -DVTK_USE_SYSTEM_EXPAT:BOOL=ON \
        -DVTK_USE_SYSTEM_FREETYPE:BOOL=ON \
        -DVTK_USE_SYSTEM_JPEG:BOOL=ON \
        -DVTK_USE_SYSTEM_PNG:BOOL=ON \
        -DVTK_USE_SYSTEM_TIFF:BOOL=ON \
        -DVTK_USE_SYSTEM_LZMA:BOOL=ON \
        -DVTK_USE_SYSTEM_ZLIB:BOOL=ON \
        -DVTK_USE_SYSTEM_ZOPE:BOOL=ON \
        -DVTK_USE_SYSTEM_TWISTED:BOOL=ON \
        -DVTK_USE_SYSTEM_GL2PS:BOOL=OFF \
        -DBUILD_DOCUMENTATION:BOOL=ON \
        -DBUILD_EXAMPLES:BOOL=OFF \
        -DBUILD_TESTING:BOOL=OFF \
        -DQtTesting_INSTALL_NO_DEVELOPMENT:BOOL=ON \
        -DPARAVIEW_INSTALL_DEVELOPMENT_FILES:BOOL=ON

# FIXME: TURN ON WHEN UPDATED GL2PS > 1.3.9 IS RELEASED
#       -DVTK_USE_SYSTEM_GL2PS:BOOL=ON \

# FIXME: CAUSES ERRORS WITH THE IN-APP PYTHON SHELL WHICH STILL LOOKS FOR PY MODULES IN THE DEFAULT DIR %%{_libdir}/%%{name}/site-packages
#       -DVTK_INSTALL_PYTHON_MODULE_DIR:PATH="%%{python_sitearch}/%%{name}" \

# FIXME: CAUSES PYTHON BYTECODE TIMESTAMP WARNINGS
#       -G"Unix Makefiles" \

# https://gitlab.kitware.com/paraview/paraview/issues/17049 from
#       -DCMAKE_SKIP_RPATH:BOOL=ON

%make_jobs

%install
find . \( -name \*.txt -o -name \*.xml -o -name '*.[ch]' -o -name '*.[ch][px][px]' \) -exec chmod -x "{}" +

%cmake_install

# UNNECESSARY STATIC LIB
rm -fr %{buildroot}%{_libexecdir}/libFmmMesh.a

# INSTALL DOCUMENTATION USED BY THE HELP MENU IN MAIN APP
install -Dm0644 %{S:2} %{buildroot}%{_datadir}/%{name}-%{major_ver}/doc/GettingStarted.pdf
install -Dm0644 %{S:3} %{buildroot}%{_datadir}/%{name}-%{major_ver}/doc/Guide.pdf

%fdupes %{buildroot}/

%post
/sbin/ldconfig
%icon_theme_cache_post
%desktop_database_post

%postun
/sbin/ldconfig
%icon_theme_cache_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc License_v1.2.txt

%exclude %{_bindir}/smTest*
%exclude %{_bindir}/vtk*
%exclude %{_includedir}/
%exclude %{_libdir}/cmake/

%{_libdir}/%{name}/
%{_bindir}/*
%{_docdir}/%{name}/
%{_datadir}/%{name}-%{major_ver}/
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files devel
%defattr(-,root,root)
%{_bindir}/smTest*
%{_bindir}/vtk*
%{_includedir}/%{name}*
%{_libdir}/cmake/%{name}-%{major_ver}/

%changelog
