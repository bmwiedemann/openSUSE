#
# spec file for package ogre
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _version 1-9-0
%define soname 1_9_0
%bcond_with cg
Name:           ogre
Version:        1.9.0
Release:        0
Summary:        Object-Oriented Graphics Rendering Engine
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            http://www.ogre3d.org/
Source0:        https://bitbucket.org/sinbad/ogre/get/v%{_version}.tar.bz2
# PATCH-FIX-UPSTREAM ogre1.9.0-browser-cmake.patch
Patch0:         ogre1.9.0-browser-cmake.patch
# PATCH-FIX-SLE ogre-1.9.0-fixsled.patch
Patch1:         ogre-1.9.0-fixsled.patch
# PATCH-FIX-SLE ogre-1.9.0-texturearray-ambig-uint.patch
Patch2:         ogre-1.9.0-texturearray-ambig-uint.patch
# PATCH-FIX-SLE ogre-1.9.0-longlongconstants.patch
Patch3:         ogre-1.9.0-longlongconstants.patch
# PATCH-FIX-UPSTREAM resolve link errors due to incorrect template creation
Patch4:         fix-template-function.patch
# Patch-FIX-UPSTREAM fix-aarch64-detection.patch
Patch5:         fix-aarch64-detection.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
# TODO remove 6 months after Leap:15.0 release
BuildRequires:  boost-devel
%endif
BuildRequires:  libcppunit-devel
BuildRequires:  pkgconfig
BuildRequires:  strace
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zziplib)
Obsoletes:      libOgreMain <= %{version}
%if %{with cg}
BuildRequires:  cg-devel
%endif

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreMain%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Recommends:     libOgreMain%{soname}-plugins
Provides:       libOgreMain = %{version}

%description -n libOgreMain%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreMain%{soname}-plugins
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreMain-plugins = %{version}

%description -n libOgreMain%{soname}-plugins
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%if %{with cg}
%package -n libOgreMain%{soname}-plugin-Cg
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreMain-plugin-Cg = %{version}

%description -n libOgreMain%{soname}-plugin-Cg
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the Cg plugin.
%endif

%package -n libOgrePaging%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgrePaging = %{version}

%description -n libOgrePaging%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

The Paging Scene Manager allows scenes to be split into a set of pages. Only
those pages that are being used need be loaded at any given time, allowing
arbitrarily large scenes. Each page has its own heightmap, to which several
textures can be applied by height.

%package -n libOgreProperty%{soname}
Summary:        Ogre 3D: an open source graphics engine
Group:          System/Libraries
Provides:       libOgreProperty = %{version}

%description -n libOgreProperty%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

OGRE's property system allows you to associate values of arbitrary type with
names, and have those values exposed via a self-describing interface.

%package -n libOgreOverlay%{soname}
Summary:        Ogre Overlay library
Group:          System/Libraries
Provides:       libOgreOverlay = %{version}

%description -n libOgreOverlay%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

An overlay is an additional plane that is layed over the finished render of a
scene. Commonly, scores or interaction menus for the player are positioned
there. In the Ogre demos, overlays are used to display the Ogre logo as well as
current information about the scene, such as polygon count or current frames
per second.

%package -n libOgreVolume%{soname}
Summary:        Ogre Volume component
Group:          System/Libraries
Provides:       libOgreVolume = %{version}

%description -n libOgreVolume%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains a component to render volumes. It can handle any volume
data, but featurewise has a tedency towards terrains. The terrain aspect means
that it is all about huge meshes being displayed with a level of detail
mechanism. Thanks to volume rendering, caves, cliffes, holes and similar
geometry can be displayed.

* Volume Rendering via Dual Marching Cubes.
* LOD mechanism via a chunk tree and marching squares skirts for crack
  patching.
* Data Sources: 3D Textures with density values and the ability to buildup a
  CSG Tree with 3D Textures, Spheres, Cubes, Planes, Intersection, Union,
  Difference and Negation, SimplexNoise addition.
* An own compressible file format for discrete density values.

%package -n libOgreRTShaderSystem%{soname}
Summary:        Ogre Runtime Shader System
Group:          System/Libraries
Provides:       libOgreRTShaderSystem = %{version}

%description -n libOgreRTShaderSystem%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This component is used to generate shaders on the fly, based on object material
properties, scene setup and other user definitions.

* Runtime shader generation synchronized with scene state. Each time scene
  settings change, a new set of shaders is generated.
* Full FFP (Fixed Function Pipeline) emulation. This feature is most useful
  combined with render system that does not provide any FFP functionality
  (OpenGL ES 2.0, D3D10, D3D11, etc.).
* Shader language independent interface: the logic representation of the shader
  programs is completely independent from the target shader language.
* Pluggable interface allows extending the target shader languages set and
  adding new shader-based effects to the system in a seamless way. Each effect
  code will be automatically combined with the rest of the shader code.
* Automatic vertex shader compacting mechanism: no more compacting variables by
  hand. In case the amount of used vertex shader output registers exceeds the
  maximum allowed (12 to 32, depending on D3DPSHADERCAPS2_0.NumTemps(external
  link)), a compacting algorithm packs the vertex shader outputs and adds
  unpack code in the fragment shader side.
* Material script support, for both export and import.

%package -n libOgreTerrain%{soname}
Summary:        Ogre Terrain System component
Group:          System/Libraries
Provides:       libOgreTerrain = %{version}

%description -n libOgreTerrain%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.
The Ogre Terrain System features:

* SceneManager independent, integrates with (optional) Paging component
* Hierarchical geometry batching: batch count reduced at lower LODs as well as
  vertex count. At the lowest level of detail, the entire terrain page is a
  single batch which has obvious advantages for large paging terrains over the
  fixed tiles previously used.
* Skirts are used instead of stitching to avoid cracks in geometry. This means
  fewer indexing arrangements and lower overall index buffer usage.
* Built-in support for splatting layers, configurable sampler inputs and
  pluggable material generators.
* Support for generating global normal maps and light maps in a background
  thread.
* LOD now adapts in real-time to camera settings (viewport sizes & LOD bias) so
  you can use the same terrain with multiple views efficiently.

%package -n libOgreMain-devel
Summary:        Development files for the Ogre Terrain System
Group:          Development/Libraries/C and C++
Requires:       libOgreMain%{soname} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(OIS)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xaw7)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(xt)
Requires:       pkgconfig(zziplib)
# _includedir/OGRE/Threading/OgreThreadHeadersBoost.h includes headers from boost
%if 0%{?suse_version} >= 1500
Requires:       libboost_atomic-devel
Requires:       libboost_chrono-devel
Requires:       libboost_date_time-devel
Requires:       libboost_headers-devel
Requires:       libboost_system-devel
Requires:       libboost_thread-devel
%else
Requires:       boost-devel
%endif

%description -n libOgreMain-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%package -n libOgrePaging-devel
Summary:        Development headers for the Ogre Paging Scene Manager component
Group:          Development/Libraries/C and C++
Requires:       libOgreMain-devel
Requires:       libOgrePaging%{soname} = %{version}

%description -n libOgrePaging-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

The Paging Scene Manager allows scenes to be split into a set of pages. Only
those pages that are being used need be loaded at any given time, allowing
arbitrarily large scenes. Each page has its own heightmap, to which several
textures can be applied by height.

This package contains the development headers for the Paging Scene Manager
component.

%package -n libOgreProperty-devel
Summary:        Development files for the Ogre Property component
Group:          Development/Libraries/C and C++
Requires:       libOgreMain-devel
Requires:       libOgreProperty%{soname} = %{version}

%description -n libOgreProperty-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the property component.

%package -n libOgreOverlay-devel
Summary:        Development files for the Ogre Overlay component
Group:          Development/Libraries/C and C++
Requires:       libOgreMain-devel
Requires:       libOgreOverlay%{soname} = %{version}

%description -n libOgreOverlay-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the overlay component.

%package -n libOgreVolume-devel
Summary:        Development files for the Ogre Volume component
Group:          Development/Libraries/C and C++
Requires:       libOgreMain-devel
Requires:       libOgreVolume%{soname} = %{version}

%description -n libOgreVolume-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the volume component.

%package -n libOgreRTShaderSystem-devel
Summary:        Development files for the OGRE Runtime Shader System component
Group:          Development/Libraries/C and C++
Requires:       libOgreMain-devel
Requires:       libOgreRTShaderSystem%{soname} = %{version}

%description -n libOgreRTShaderSystem-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the Runtime Shader System
(RTSS) component.

%package -n libOgreTerrain-devel
Summary:        Development files for the Ogre Terrain System component
Group:          Development/Libraries/C and C++
Requires:       libOgreMain-devel
Requires:       libOgreTerrain%{soname} = %{version}

%description -n libOgreTerrain-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the Ogre Terrain System.

%package -n ogre-demos
Summary:        Ogre demo programs
Group:          Development/Libraries/C and C++
%if %{with cg}
Requires:       libOgreMain%{soname}-plugin-Cg = %{version}
%endif

%description -n ogre-demos
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the demo applications.

%package -n ogre-demos-devel
Summary:        Sources for the Ogre demo programs
Group:          Development/Sources
Requires:       libOgreMain-devel = %{version}
Requires:       libOgreRTShaderSystem-devel = %{version}
Requires:       libOgreTerrain-devel = %{version}
Requires:       pkgconfig(OIS)

%description -n ogre-demos-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the source of the demo applications.

%package -n ogre-tools
Summary:        Additional utilities for working with the Ogre 3D engine
Group:          Development/Libraries/C and C++

%description -n ogre-tools
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains various tools that make working with ogre easier.

%package -n ogre-docs
Summary:        Documentation for the Ogre 3D engine
Group:          Documentation/Other
# libOgreMain-doc was last used in openSUSE 11.4
Provides:       libOgreMain-doc = %{version}
Obsoletes:      libOgreMain-doc < %{version}

%description -n ogre-docs
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the documentation for OGRE.

%prep
%setup -q -n sinbad-ogre-dd30349ea667
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# Be sure we use system tinyxml
rm Tools/XMLConverter/src/tiny*
rm Tools/XMLConverter/include/tiny*

# Fixes FS#30088 (crashes with skeleton animations)
sed "51 s/GNUC/GNUCC/" -i OgreMain/src/OgreSIMDHelper.h

# fix BOM problem older GCC
sed $'s/^\xEF\xBB\xBF//' -i OgreMain/src/OgreProgressiveMeshGenerator.cpp

%if 0%{?sles_version}
%patch1 -p1
sed -e "s/ -Wno-unused-but-set-parameter//" -i CMakeLists.txt
%endif

%build
%ifarch %{ix86} %{arm}
%define largefiledef -DZZIP_LARGEFILE_SENSITIVE -D_ZZIP_LARGEFILE -DZZIP_LARGEFILE_RENAME
%endif

%cmake -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_FLAGS:STRING="%{optflags} %{?largefiledef}" \
      -DCMAKE_CXX_FLAGS:STRING="%{optflags} %{?largefiledef}" \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DOGRE_LIB_DIRECTORY=%{_lib} \
      -DOGRE_INSTALL_SAMPLES=ON \
      -DOGRE_INSTALL_SAMPLES_SOURCE=ON \
      -DOGRE_INSTALL_DOCS=ON \
      ..

make %{?_smp_mflags} VERBOSE=1

%install
cd build
%make_install VERBOSE=1
%fdupes %{buildroot}%{_includedir}/OGRE
%fdupes %{buildroot}%{_datadir}/OGRE

%post -n libOgreMain%{soname} -p /sbin/ldconfig
%postun -n libOgreMain%{soname} -p /sbin/ldconfig
%post -n libOgrePaging%{soname} -p /sbin/ldconfig
%postun -n libOgrePaging%{soname} -p /sbin/ldconfig
%post -n libOgreProperty%{soname} -p /sbin/ldconfig
%postun -n libOgreProperty%{soname} -p /sbin/ldconfig
%post -n libOgreVolume%{soname} -p /sbin/ldconfig
%postun -n libOgreVolume%{soname} -p /sbin/ldconfig
%post -n libOgreOverlay%{soname} -p /sbin/ldconfig
%postun -n libOgreOverlay%{soname} -p /sbin/ldconfig
%post -n libOgreRTShaderSystem%{soname} -p /sbin/ldconfig
%postun -n libOgreRTShaderSystem%{soname} -p /sbin/ldconfig
%post -n libOgreTerrain%{soname} -p /sbin/ldconfig
%postun -n libOgreTerrain%{soname} -p /sbin/ldconfig

%files -n libOgreMain%{soname}
%doc AUTHORS BUGS README COPYING
%{_libdir}/libOgreMain.so.%{version}

%files -n libOgreMain%{soname}-plugins
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/RenderSystem_GL.so
%{_libdir}/OGRE/Plugin_OctreeSceneManager.so
%{_libdir}/OGRE/Plugin_ParticleFX.so
%{_libdir}/OGRE/Plugin_BSPSceneManager.so
%{_libdir}/OGRE/Plugin_OctreeZone.so
%{_libdir}/OGRE/Plugin_PCZSceneManager.so
%{_libdir}/OGRE/RenderSystem_GL.so.%{version}
%{_libdir}/OGRE/Plugin_OctreeSceneManager.so.%{version}
%{_libdir}/OGRE/Plugin_ParticleFX.so.%{version}
%{_libdir}/OGRE/Plugin_BSPSceneManager.so.%{version}
%{_libdir}/OGRE/Plugin_OctreeZone.so.%{version}
%{_libdir}/OGRE/Plugin_PCZSceneManager.so.%{version}

%if %{with cg}
%files -n libOgreMain%{soname}-plugin-Cg
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/Plugin_CgProgramManager.so
%{_libdir}/OGRE/Plugin_CgProgramManager.so.%{version}
%endif

%files -n libOgrePaging%{soname}
%{_libdir}/libOgrePaging.so.%{version}

%files -n libOgreProperty%{soname}
%{_libdir}/libOgreProperty.so.%{version}

%files -n libOgreOverlay%{soname}
%{_libdir}/libOgreOverlay.so.%{version}

%files -n libOgreVolume%{soname}
%{_libdir}/libOgreVolume.so.%{version}

%files -n libOgreRTShaderSystem%{soname}
%{_libdir}/libOgreRTShaderSystem.so.%{version}

%files -n libOgreTerrain%{soname}
%{_libdir}/libOgreTerrain.so.%{version}

%files -n libOgreMain-devel
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/cmake/
%dir %{_includedir}/OGRE/
%{_includedir}/OGRE/*.h
%{_includedir}/OGRE/GLX/
%{_includedir}/OGRE/Plugins/
%{_includedir}/OGRE/RenderSystems/
%{_includedir}/OGRE/Threading/
%{_libdir}/libOgreMain.so
%{_libdir}/pkgconfig/OGRE.pc
%{_libdir}/pkgconfig/OGRE-PCZ.pc

%files -n libOgrePaging-devel
%{_includedir}/OGRE/Paging/
%{_libdir}/libOgrePaging.so
%{_libdir}/pkgconfig/OGRE-Paging.pc

%files -n libOgreProperty-devel
%{_includedir}/OGRE/Property/
%{_libdir}/libOgreProperty.so
%{_libdir}/pkgconfig/OGRE-Property.pc

%files -n libOgreVolume-devel
%{_includedir}/OGRE/Volume/
%{_libdir}/libOgreVolume.so
%{_libdir}/pkgconfig/OGRE-Volume.pc

%files -n libOgreOverlay-devel
%{_includedir}/OGRE/Overlay/
%{_libdir}/libOgreOverlay.so
%{_libdir}/pkgconfig/OGRE-Overlay.pc

%files -n libOgreRTShaderSystem-devel
%{_includedir}/OGRE/RTShaderSystem/
%{_libdir}/libOgreRTShaderSystem.so
%{_libdir}/pkgconfig/OGRE-RTShaderSystem.pc

%files -n libOgreTerrain-devel
%{_includedir}/OGRE/Terrain/
%{_libdir}/libOgreTerrain.so
%{_libdir}/pkgconfig/OGRE-Terrain.pc

%files -n ogre-demos
%dir %{_libdir}/OGRE/
%{_libdir}/OGRE/Samples/
%{_bindir}/SampleBrowser
%dir %{_datadir}/OGRE/
%{_datadir}/OGRE/Media/
%{_datadir}/OGRE/plugins.cfg
%{_datadir}/OGRE/samples.cfg
%{_datadir}/OGRE/resources.cfg
%{_datadir}/OGRE/quakemap.cfg
%{_datadir}/OGRE/tests.cfg

%files -n ogre-demos-devel
%{_datadir}/OGRE/Samples/
%{_datadir}/OGRE/CMakeLists.txt

%files -n ogre-tools
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter

%files -n ogre-docs
%doc %{_datadir}/OGRE/docs/

%changelog
