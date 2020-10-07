#
# spec file for package OpenSceneGraph34
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


%define _osg_so_nr	131
%define _opt_so_nr	20
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?is_opensuse})
%bcond_without gdal
%else
%bcond_with gdal
%endif
%define sname OpenSceneGraph
Name:           OpenSceneGraph34
Version:        3.4.1
Release:        0
Summary:        3D graphics toolkit
# Actually they call it OpenSceneGraph Public License, Version 0.0, which is
# "LGPL-2.1-only AND WXwindows" (https://spdx.org/licenses/WXwindows)
# "LGPL-2.1-only WITH WxWindows-exception-3.1" would be valid (https://spdx.org/licenses/WxWindows-exception-3.1.html)
# Contrary to that most sources state "GPL-2.0-only"
# Ticket opened to clear license situation: https://github.com/openscenegraph/OpenSceneGraph/issues/552
License:        LGPL-2.1-only WITH WxWindows-exception-3.1
Group:          Productivity/Graphics/Other
URL:            http://openscenegraph.org/projects/osg
Source0:        https://github.com/openscenegraph/%{sname}/archive/%{sname}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM 8e26ebd23ef9_Fixed_coverity_detected_defect_OOB_read.patch -- Fix out-of-bound-read, also required for the next patch to apply
Patch0:         8e26ebd23ef9_Fixed_coverity_detected_defect_OOB_read.patch
# PATCH-FIX-UPSTREAM 01c712e85195_Explicit_signed_char_declarations.patch -- compilation fix for e.g. ARM, PPC
Patch1:         01c712e85195_Explicit_signed_char_declarations.patch
# PATCH-FIX-UPSTREAM https://github.com/openscenegraph/OpenSceneGraph/issues/779
Patch2:         fix_deprecated_FIND_PACKAGE_wxWidgets_usage.patch
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel < 3.1
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-fft-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-1.0)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.35
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xrandr)
%if %{with gdal}
BuildRequires:  pkgconfig(gdal)
%endif
Conflicts:      OpenSceneGraph

%description
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL, freeing the developer from implementing and optimizing low
level graphics calls, and provides many additional utilities for
development of graphics applications.

%package -n libOpenSceneGraph%{_osg_so_nr}
Summary:        Shared libraries for OpenSceneGraph
Group:          System/Libraries
%if "%{_osg_so_nr}" >= "130"
# try to cover up past mistakes
Obsoletes:      libOpenSceneGraph100
%endif

%description -n libOpenSceneGraph%{_osg_so_nr}
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains the shared libraries for OpenSceneGraph.

%package -n libOpenSceneGraph%{_osg_so_nr}-devel
Summary:        OpenSceneGraph development files
Group:          Development/Libraries/C and C++
Requires:       curl-devel
Requires:       freeglut-devel
Requires:       giflib-devel
Requires:       libOpenSceneGraph%{_osg_so_nr} = %{version}
Requires:       libOpenThreads%{_opt_so_nr}-devel = %{version}
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libtiff-4)
Requires:       pkgconfig(openal)
Requires:       pkgconfig(poppler-glib)
Requires:       pkgconfig(sdl2)
Requires:       pkgconfig(xrandr)
Conflicts:      libOpenSceneGraph1-devel
Provides:       libOpenSceneGraph-devel = %{version}
# library is versioned, but headers conflict
Conflicts:      libOpenSceneGraph-devel

%description -n libOpenSceneGraph%{_osg_so_nr}-devel
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains the header and development files for
OpenSceneGraph.

%package -n libOpenThreads%{_opt_so_nr}
Summary:        Shared libraries for OpenSceneGraph
Group:          System/Libraries

%description -n libOpenThreads%{_opt_so_nr}
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains the shared libraries for OpenSceneGraph.

%package -n libOpenThreads%{_opt_so_nr}-devel
Summary:        OpenSceneGraph development files
Group:          Development/Libraries/C and C++
Requires:       libOpenThreads%{_opt_so_nr} = %{version}
Provides:       libOpenThreads-devel = %{version}
# library is versioned, but headers conflict
Conflicts:      libOpenThreads-devel

%description -n libOpenThreads%{_opt_so_nr}-devel
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains the header and development files for
OpenSceneGraph.

%package plugins
Summary:        Plugins for OpenSceneGraph
Group:          Productivity/Graphics/Other
Provides:       OpenSceneGraph-plugins = %{version}

%description plugins
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains some plugins for OpenSceneGraph.

%package examples
Summary:        OpenSceneGraph example applications
Group:          Productivity/Graphics/Other
Conflicts:      OpenSceneGraph-examples

%description examples
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains some example applications built with OpenSceneGraph

%prep
%setup -q -n %{sname}-%{sname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
for file in *.txt ChangeLog; do
	sed -i "s/\r//g" "$file"
done
chmod 644 *.txt ChangeLog

%build
%cmake \
	-DBUILD_OSG_EXAMPLES=ON \
	-DBUILD_OSG_PLUGINS=ON \
	-DBUILD_DOCUMENTATION=OFF \
	-DBUILD_OSG_WRAPPER=ON \
	-DBUILD_OSG_APPLICATIONS=ON \
	-DCMAKE_BUILD_TYPE=Release \
	-DDYNAMIC_OPENSCENEGRAPH=ON \
	-DDYNAMIC_OPENTHREADS=ON \
	-DDESIRED_QT_VERSION=5
make %{?_smp_mflags}

%install
%cmake_install
# example bins installed in share dir, not acceptable. Note, this will break
# when %%{_datadir}/OpenSceneGraph is also used for other stuff
mv %{buildroot}%{_datadir}/OpenSceneGraph \
   %{buildroot}%{_libdir}/%{name}

%post -n libOpenSceneGraph%{_osg_so_nr} -p /sbin/ldconfig
%post -n libOpenThreads%{_opt_so_nr} -p /sbin/ldconfig
%postun -n libOpenSceneGraph%{_osg_so_nr} -p /sbin/ldconfig
%postun -n libOpenThreads%{_opt_so_nr} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc AUTHORS.txt NEWS.txt README.txt ChangeLog
%{_bindir}/osg2cpp
%{_bindir}/osgarchive
%{_bindir}/osgconv
%{_bindir}/osgfilecache
%{_bindir}/osgversion
%{_bindir}/osgviewer
%{_bindir}/present3D

%files plugins
%{_libdir}/osgPlugins-%{version}/

%files -n libOpenSceneGraph%{_osg_so_nr}
%{_libdir}/libosg.so.*
%{_libdir}/libosgAnimation.so.*
%{_libdir}/libosgDB.so.*
%{_libdir}/libosgFX.so.*
%{_libdir}/libosgGA.so.*
%{_libdir}/libosgManipulator.so.*
%{_libdir}/libosgParticle.so.*
%{_libdir}/libosgShadow.so.*
%{_libdir}/libosgSim.so.*
%{_libdir}/libosgTerrain.so.*
%{_libdir}/libosgText.so.*
%{_libdir}/libosgUtil.so.*
%{_libdir}/libosgUI.so.*
%{_libdir}/libosgVolume.so.*
%{_libdir}/libosgViewer.so.*
%{_libdir}/libosgWidget.so.*
%{_libdir}/libosgPresentation.so.*
%{_libdir}/libosgQt.so.*

%files -n libOpenSceneGraph%{_osg_so_nr}-devel
%{_includedir}/osg/
%{_includedir}/osgAnimation/
%{_includedir}/osgDB/
%{_includedir}/osgFX/
%{_includedir}/osgGA/
%{_includedir}/osgManipulator/
%{_includedir}/osgParticle/
%{_includedir}/osgShadow/
%{_includedir}/osgSim/
%{_includedir}/osgTerrain/
%{_includedir}/osgText/
%{_includedir}/osgUI/
%{_includedir}/osgUtil/
%{_includedir}/osgViewer/
%{_includedir}/osgVolume/
%{_includedir}/osgWidget/
%{_includedir}/osgQt/
%{_includedir}/osgPresentation/
%{_libdir}/libosg.so
%{_libdir}/libosgAnimation.so
%{_libdir}/libosgDB.so
%{_libdir}/libosgFX.so
%{_libdir}/libosgGA.so
%{_libdir}/libosgManipulator.so
%{_libdir}/libosgParticle.so
%{_libdir}/libosgShadow.so
%{_libdir}/libosgSim.so
%{_libdir}/libosgTerrain.so
%{_libdir}/libosgText.so
%{_libdir}/libosgUI.so
%{_libdir}/libosgUtil.so
%{_libdir}/libosgViewer.so
%{_libdir}/libosgVolume.so
%{_libdir}/libosgWidget.so
%{_libdir}/libosgPresentation.so
%{_libdir}/libosgQt.so
%{_libdir}/pkgconfig/openscenegraph.pc
%{_libdir}/pkgconfig/openscenegraph-osg*.pc

%files examples
%{_libdir}/%{name}

%files -n libOpenThreads%{_opt_so_nr}
%{_libdir}/libOpenThreads.so.*

%files -n libOpenThreads%{_opt_so_nr}-devel
%{_includedir}/OpenThreads/
%{_libdir}/libOpenThreads.so
%{_libdir}/pkgconfig/openthreads.pc

%changelog
