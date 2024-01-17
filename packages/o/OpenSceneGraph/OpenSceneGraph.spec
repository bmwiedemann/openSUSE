#
# spec file for package OpenSceneGraph
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


%define _osg_so_nr 161
%define _opt_so_nr 21
%if 0%{?is_opensuse}
%bcond_without gdal
%bcond_with    ffmpeg
%else
%bcond_with    gdal
%bcond_without ffmpeg
%endif

%bcond_without asio
%bcond_without dcmtk
%bcond_without fox
%bcond_without occt

%if 0%{?suse_version} >= 1550
%bcond_with    gtk2
%else
%bcond_without gtk2
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
# PATCH-FIX-OPENSUSE - fix build with asio >= 1.14.0, https://github.com/openscenegraph/OpenSceneGraph/issues/921
Patch0:         0001-Replace-boost-bind-usage-with-std-bind.patch
Patch1:         0002-Replace-obsoleted-asio-basic_stream_socket-get_io_se.patch
# PATCH-FIX-UPSTREAM - Fix build with OCCT 7.6
Patch2:         0001-Use-non-deprecated-methods-to-access-OpenCascade-Tri.patch
BuildRequires:  cmake
BuildRequires:  curl-devel
%if %{with ffmpeg}
BuildRequires:  ffmpeg-devel
%endif
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-fft-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
%if %{with gtk2}
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-1.0)
%endif
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.35
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libvncserver)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xrandr)
%if %{with dcmtk}
BuildRequires:  cmake(DCMTK)
BuildRequires:  pkgconfig(icu-uc)
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
Group:          System/Libraries
# try to cover up past mistakes
Conflicts:      libOpenSceneGraph100
Conflicts:      libOpenSceneGraph158

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
Requires:       libOpenSceneGraph%{_osg_so_nr} = %{version}-%{release}
Requires:       libOpenThreads-devel = %{version}
Requires:       libjpeg-devel
Requires:       libpng-devel
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libtiff-4)
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

%package plugin-ffmpeg
Summary:        FFmpeg plugin for OpenSceneGraph
Group:          Productivity/Graphics/Other
Provides:       OpenSceneGraphPlugin(ext:mov)
Provides:       OpenSceneGraphPlugin(ext:avi)
Provides:       %{name}-plugins:%{_libdir}/osgPlugins-%{version}/osgdb_ffmpeg.so
Conflicts:      %{name}-plugins < %{version}-%{release}

%description plugin-ffmpeg
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications.

This package contains the FFmpeg plugin for OpenSceneGraph.

%package plugin-gdal
Summary:        GDAL plugin for OpenSceneGraph
Group:          Productivity/Graphics/Other
Provides:       OpenSceneGraphPlugin(ext:gdal)
Provides:       %{name}-plugins:%{_libdir}/osgPlugins-%{version}/osgdb_gdal.so
Conflicts:      %{name}-plugins < %{version}-%{release}

%description plugin-gdal
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications.

This package contains the GDAL plugin for OpenSceneGraph.

%package plugin-gstreamer
Summary:        GStreamer plugin for OpenSceneGraph
Group:          Productivity/Graphics/Other
Provides:       OpenSceneGraphPlugin(ext:mov)
Provides:       OpenSceneGraphPlugin(ext:avi)
Provides:       %{name}-plugins:%{_libdir}/osgPlugins-%{version}/osgdb_gstreamer.so
Conflicts:      %{name}-plugins < %{version}-%{release}

%description plugin-gstreamer
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications.

This package contains the GStreamer plugin for OpenSceneGraph.

%package plugin-opencascade
Summary:        OpenCASCADE plugin for OpenSceneGraph
Group:          Productivity/Graphics/Other
Provides:       OpenSceneGraphPlugin(ext:step)
Provides:       OpenSceneGraphPlugin(ext:iges)
Provides:       %{name}-plugins:%{_libdir}/osgPlugins-%{version}/osgdb_opencascade.so
Conflicts:      %{name}-plugins < %{version}-%{release}

%description plugin-opencascade
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications.

This package contains the OpenCASCADE plugin for OpenSceneGraph.

%package plugin-pdf
Summary:        PDF plugin for OpenSceneGraph
Group:          Productivity/Graphics/Other
Provides:       OpenSceneGraphPlugin(ext:pdf)
Provides:       %{name}-plugins:%{_libdir}/osgPlugins-%{version}/osgdb_pdf.so
Conflicts:      %{name}-plugins < %{version}-%{release}

%description plugin-pdf
The OpenSceneGraph is a graphics toolkit for the development of
graphic applications.

This package contains the Poppler based PDF plugin for OpenSceneGraph.

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
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%patch0 -p1
%patch1 -p1
%endif
%patch2 -p1

for file in *.md *.txt; do
	sed -i "s/\r//g" "$file"
done
chmod 644 *.md *.txt

%build
%cmake \
  -DCMAKE_RELWITHDEBINFO_POSTFIX="" \
  -DBUILD_OSG_EXAMPLES=ON \
  -DBUILD_OSG_PLUGINS=ON \
  -DBUILD_DOCUMENTATION=OFF \
  -DBUILD_OSG_APPLICATIONS=ON \
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
%doc AUTHORS.txt NEWS.txt README.md
%{_bindir}/osg2cpp
%{_bindir}/osgarchive
%{_bindir}/osgconv
%{_bindir}/osgfilecache
%{_bindir}/osgversion
%{_bindir}/osgviewer
%{_bindir}/present3D
%{_bindir}/osgshaderpipeline

%files plugins
%{_libdir}/osgPlugins-%{version}/*.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_ffmpeg*.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_gdal*.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_gstreamer*.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_opencascade*.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_ogr*.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_pdf*.so

%if %{with ffmpeg}
%files plugin-ffmpeg
%{_libdir}/osgPlugins-%{version}/osgdb_ffmpeg*.so
%endif

%if %{with gdal}
%files plugin-gdal
%{_libdir}/osgPlugins-%{version}/osgdb_gdal*.so
%{_libdir}/osgPlugins-%{version}/osgdb_ogr*.so
%endif

%files plugin-gstreamer
%{_libdir}/osgPlugins-%{version}/osgdb_gstreamer*.so

%files plugin-opencascade
%{_libdir}/osgPlugins-%{version}/osgdb_opencascade*.so

%files plugin-pdf
%{_libdir}/osgPlugins-%{version}/osgdb_pdf*.so

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
%dir %{_libdir}/osgPlugins-%{version}/

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
