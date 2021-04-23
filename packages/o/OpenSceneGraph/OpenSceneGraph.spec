#
# spec file for package OpenSceneGraph
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


%define _osg_so_nr	158
%define _opt_so_nr	21
%if 0%{?is_opensuse}
%bcond_without gdal
%else
%bcond_with gdal
%endif
# asio is not available in Leap < 15.2 and SLE15SP1
# dcmtk is not available in SLE15SP1 and causes a build issue in Leap 15.1
%if 0%{?sle_version} < 150200 && 0%{?suse_version} == 1500
%bcond_with asio
%bcond_with dcmtk
%else
%bcond_without asio
%bcond_without dcmtk
%endif
# occt and fox are not available in SLE15SP1
%if 0%{?is_opensuse} || 0%{?sle_version} >= 150200
%bcond_without fox
%bcond_without occt
%else
%bcond_with fox
%bcond_with occt
%endif
Name:           OpenSceneGraph
Version:        3.6.5
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
Source0:        https://github.com/openscenegraph/%{name}/archive/%{name}-%{version}.tar.gz
Source99:       %{name}-rpmlintrc
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(IlmBase)
BuildRequires:  pkgconfig(OpenEXR)
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
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xrandr)
%if %{with dcmtk}
BuildRequires:  cmake(DCMTK)
%endif
%if %{with fox}
BuildRequires:  pkgconfig(fox)
%endif
%if %{with occt}
BuildRequires:  occt-devel
%endif
%if %{with asio}
BuildRequires:  asio-devel
%endif
%if %{with gdal}
BuildRequires:  pkgconfig(gdal)
%endif

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
# try to cover up past mistakes
Group:          System/Libraries
Obsoletes:      libOpenSceneGraph100

%description -n libOpenSceneGraph%{_osg_so_nr}
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains the shared libraries for OpenSceneGraph.

%package -n libOpenSceneGraph-devel
Summary:        OpenSceneGraph development files
Group:          Development/Libraries/C and C++
Requires:       curl-devel
Requires:       freeglut-devel
Requires:       giflib-devel
Requires:       libOpenSceneGraph%{_osg_so_nr} = %{version}
Requires:       libOpenThreads-devel = %{version}
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

%description -n libOpenSceneGraph-devel
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

%package -n libOpenThreads-devel
Summary:        OpenSceneGraph development files
Group:          Development/Libraries/C and C++
Requires:       libOpenThreads%{_opt_so_nr} = %{version}
Conflicts:      libOpenThreads1-devel

%description -n libOpenThreads-devel
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

%description examples
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications such as flight simulators, games, virtual
reality and scientific visualization. Based around the concept of a
scene graph, it provides an object-oriented framework on top of
OpenGL.

This package contains some example applications built with OpenSceneGraph

%prep
%setup -q -n %{name}-%{name}-%{version}

for file in *.md *.txt ChangeLog; do
	sed -i "s/\r//g" "$file"
done
chmod 644 *.md *.txt ChangeLog

%build
%cmake \
  -DBUILD_OSG_EXAMPLES=ON \
  -DBUILD_OSG_PLUGINS=ON \
  -DBUILD_DOCUMENTATION=OFF \
  -DBUILD_OSG_APPLICATIONS=ON \
  -DCMAKE_BUILD_TYPE=Release \
  -DDYNAMIC_OPENSCENEGRAPH=ON \
  -DDYNAMIC_OPENTHREADS=ON \
%if "%{_lib}" == "lib64"
  -DLIB_POSTFIX=64
%endif

%cmake_build

%install
%cmake_install
# example bins installed in share dir, not acceptable. Note, this will break
# when %%{_datadir}/OpenSceneGraph is also used for other stuff
mv %{buildroot}%{_datadir}/OpenSceneGraph \
   %{buildroot}%{_libdir}

%post -n libOpenSceneGraph%{_osg_so_nr} -p /sbin/ldconfig
%post -n libOpenThreads%{_opt_so_nr} -p /sbin/ldconfig
%postun -n libOpenSceneGraph%{_osg_so_nr} -p /sbin/ldconfig
%postun -n libOpenThreads%{_opt_so_nr} -p /sbin/ldconfig

%files
%license LICENSE.txt
%doc AUTHORS.txt NEWS.txt README.md ChangeLog
%{_bindir}/osg2cpp
%{_bindir}/osgarchive
%{_bindir}/osgconv
%{_bindir}/osgfilecache
%{_bindir}/osgversion
%{_bindir}/osgviewer
%{_bindir}/present3D
%{_bindir}/osgshaderpipeline

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

%files -n libOpenSceneGraph-devel
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
%{_libdir}/pkgconfig/openscenegraph.pc
%{_libdir}/pkgconfig/openscenegraph-osg*.pc

%files examples
%{_libdir}/OpenSceneGraph

%files -n libOpenThreads%{_opt_so_nr}
%{_libdir}/libOpenThreads.so.*

%files -n libOpenThreads-devel
%{_includedir}/OpenThreads/
%{_libdir}/libOpenThreads.so
%{_libdir}/pkgconfig/openthreads.pc

%changelog
