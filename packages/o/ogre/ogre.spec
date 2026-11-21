#
# spec file for package ogre
#
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


%define major 14
%define minor 6
%define third 1
%define sover  %{major}.%{minor}
%define soname %{major}_%{minor}
%define plugin_dir %{_libdir}/OGRE%{soname}
# Version from https://github.com/OGRECave/ogre/blob/v%version/Components/Overlay/CMakeLists.txt#L25
%define im_version 1.92.9b
# CG is non free, so not build by default
%bcond_with cg
# OpenEXR v3 is incompatible https://github.com/OGRECave/ogre/issues/2179
%bcond_with openexr
# Optionally build without mono bindings
%bcond_with mono
Name:           ogre
Version:        %{major}.%{minor}.%{third}
Release:        0
Summary:        Object-Oriented Graphics Rendering Engine
License:        LGPL-2.1-only
URL:            https://www.ogre3d.org/
Source0:        https://github.com/OGRECave/ogre/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/ocornut/imgui/archive/v%{im_version}.tar.gz#/imgui-%{im_version}.tar.gz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE python3-sitelib.patch -- Fix python path detected on build time
Patch0:         python3-sitelib.patch
# PATCH-FIX-UPSTREAM fix-sse-detection.patch -- Fix detection of sse for x86 (vs x64)
Patch1:         fix-sse-detection.patch
# PATCH-FIX-UPSTREAM swig-3-cpp11.patch -- noexcept instead of dynamic throw()
Patch2:         swig-3-cpp11.patch
# PATCH-FIX-UPSTREAM fix-glslang-plugin-compilation.patch -- include glslang Types.h
Patch3:         fix-glslang-plugin-compilation.patch
BuildRequires:  cmake >= 3.13
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  glslang-nonstd-devel
BuildRequires:  imgui-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  swig
BuildRequires:  cmake(SPIRV-Tools)
BuildRequires:  cmake(assimp)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zziplib)
Obsoletes:      libOgreMain <= %{version}
%if %{with mono}
BuildRequires:  mono(mcs)
%endif
%if %{with cg}
BuildRequires:  cg-devel
%endif
%if %{with openexr}
BuildRequires:  pkgconfig(OpenEXR) < 3.0
%endif

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package media
Summary:        Required media files for OGRE
# There must only one media package installed! As using programs hardcode the path
Conflicts:      %{name}-media < %{version}

%description media
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the required media files for OGRE, optional files are provided
with the %{name}-demos package.

%package mono
Summary:        Mono bindings OGRE

%description mono
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%package python
Summary:        Python bindings for OGRE

%description python
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%package -n libOgreMain%{soname}
Summary:        Ogre 3D: an open source graphics engine
Recommends:     %{name}-media >= %{version}
Recommends:     libOgreMain%{soname}-codecs
Recommends:     libOgreMain%{soname}-plugins

%description -n libOgreMain%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n libOgreBites%{soname}
Summary:        Ogre 3D: an open source graphics engine

%description -n libOgreBites%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.
Reusable utilities for rapid prototyping with Ogre.

%package -n libOgreBitesQt%{soname}
Summary:        Ogre 3D: an open source graphics engine

%description -n libOgreBitesQt%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.
Reusable utilities for rapid prototyping with Ogre.

%package -n libOgreMeshLodGenerator%{soname}
Summary:        Ogre 3D: an open source graphics engine

%description -n libOgreMeshLodGenerator%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.
Mesh LOD allows to swap the models to Low-poly models in far distance, which makes your game faster.

%package -n libOgreMain%{soname}-codecs
Summary:        Ogre 3D: an open source graphics engine
Provides:       libOgreMain-codecs = %{version}

%description -n libOgreMain%{soname}-codecs
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%package -n libOgreMain%{soname}-plugins
Summary:        Ogre 3D: an open source graphics engine
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      libOgreMain-plugins <= 1.12.13
Provides:       libOgreMain-plugins = %{version}

%description -n libOgreMain%{soname}-plugins
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%if %{with cg}
%package -n libOgreMain%{soname}-plugin-Cg
Summary:        Ogre 3D: an open source graphics engine
Provides:       libOgreMain-plugin-Cg = %{version}

%description -n libOgreMain%{soname}-plugin-Cg
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the Cg plugin.
%endif

%package -n libOgrePaging%{soname}
Summary:        Ogre 3D: an open source graphics engine

%description -n libOgrePaging%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

The Paging Scene Manager allows scenes to be split into a set of pages. Only
those pages that are being used need be loaded at any given time, allowing
arbitrarily large scenes. Each page has its own heightmap, to which several
textures can be applied by height.

%package -n libOgreProperty%{soname}
Summary:        Ogre 3D: an open source graphics engine

%description -n libOgreProperty%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

OGRE's property system allows you to associate values of arbitrary type with
names, and have those values exposed via a self-describing interface.

%package -n libOgreOverlay%{soname}
Summary:        Ogre Overlay library

%description -n libOgreOverlay%{soname}
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

An overlay is an additional plane that is layed over the finished render of a
scene. Commonly, scores or interaction menus for the player are positioned
there. In the Ogre demos, overlays are used to display the Ogre logo as well as
current information about the scene, such as polygon count or current frames
per second.

%package -n libOgreVolume%{soname}
Summary:        Ogre Volume component

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
Summary:        Development files for the Ogre Main library
Requires:       libOgreMain%{soname} = %{version}
Requires:       libOgreMain%{soname}-codecs = %{version}
Requires:       libOgreMain%{soname}-plugins = %{version}
Requires:       ogre-media
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xaw7)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(zziplib)

%description -n libOgreMain-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%package -n libOgreBites-devel
Summary:        Development headers for rapid prototyping
Requires:       libOgreBites%{soname} = %{version}
Requires:       libOgreBitesQt%{soname} = %{version}

%description -n libOgreBites-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

Reusable utilities for rapid prototyping with Ogre.

%package -n libOgreMeshLodGenerator-devel
Summary:        Development headers for Mesh LOD
Requires:       libOgreMeshLodGenerator%{soname} = %{version}

%description -n libOgreMeshLodGenerator-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.
Mesh LOD allows to swap the models to Low-poly models in far distance, which makes your game faster.

%package -n libOgrePaging-devel
Summary:        Development headers for the Ogre Paging Scene Manager component
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
Requires:       libOgreProperty%{soname} = %{version}

%description -n libOgreProperty-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the property component.

%package -n libOgreOverlay-devel
Summary:        Development files for the Ogre Overlay component
Requires:       libOgreOverlay%{soname} = %{version}

%description -n libOgreOverlay-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the overlay component.

%package -n libOgreVolume-devel
Summary:        Development files for the Ogre Volume component
Requires:       libOgreVolume%{soname} = %{version}

%description -n libOgreVolume-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the volume component.

%package -n libOgreRTShaderSystem-devel
Summary:        Development files for the OGRE Runtime Shader System component
Requires:       libOgreRTShaderSystem%{soname} = %{version}

%description -n libOgreRTShaderSystem-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the Runtime Shader System
(RTSS) component.

%package -n libOgreTerrain-devel
Summary:        Development files for the Ogre Terrain System component
Requires:       libOgreTerrain%{soname} = %{version}

%description -n libOgreTerrain-devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the development headers for the Ogre Terrain System.

%package devel
Summary:        Development files for the Ogre Engine
# By name rather than by pkgconfig(): the compat package ogre1 installs
# its pkgconfig files at the same unversioned paths, so asking for the
# symbols makes every consumer of ogre-devel ambiguous to the resolver.
Requires:       libOgreBites-devel = %{version}
Requires:       libOgreMain-devel = %{version}
Requires:       libOgreMeshLodGenerator-devel = %{version}
Requires:       libOgreOverlay-devel = %{version}
Requires:       libOgrePaging-devel = %{version}
Requires:       libOgreProperty-devel = %{version}
Requires:       libOgreRTShaderSystem-devel = %{version}
Requires:       libOgreTerrain-devel = %{version}
Requires:       libOgreVolume-devel = %{version}

%description devel
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

%package -n ogre-demos
Summary:        Ogre demo programs
Requires:       %{name}-media = %{version}
Requires:       libOgreMain%{soname}-plugins = %{version}
%if %{with cg}
Requires:       libOgreMain%{soname}-plugin-Cg = %{version}
%endif

%description -n ogre-demos
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented 3D engine.

This package contains the demo applications.

%package -n ogre-demos-devel
Summary:        Sources for the Ogre demo programs
Requires:       libOgreRTShaderSystem-devel = %{version}
Requires:       libOgreTerrain-devel = %{version}

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

%description -n ogre-docs
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented, flexible
3D engine written in C++ designed to make it easier and more intuitive for
developers to produce applications utilising hardware-accelerated 3D graphics.
The class library abstracts all the details of using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

This package contains the documentation for OGRE.

%prep
%setup -q -a1
%autopatch -p1
dos2unix ./Docs/ogre_style.css

%build
mkdir %{__builddir}
ln -s {..,%{__builddir}}/imgui-%{im_version}
%cmake \
      -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DOGRE_LIB_DIRECTORY=%{_lib} \
      -DOGRE_BUILD_SAMPLES=ON \
      -DOGRE_INSTALL_DOCS=ON \
      -DOGRE_PLUGINS_PATH="%{_lib}/OGRE%{soname}" \
      -DOGRE_BUILD_RENDERSYSTEM_VULKAN=ON \
      -DOGRE_BUILD_DEPENDENCIES=OFF
%cmake_build

%install
%cmake_install
%if %{without mono}
rm %{buildroot}%{_includedir}/OGRE/Ogre.i
%endif
mkdir -p "%{buildroot}%{_docdir}"
mv "%{buildroot}%{_datadir}/doc/OGRE" "%{buildroot}%{_docdir}/OGRE"
# Install samples' source
mkdir -p %{buildroot}%{_datadir}/OGRE-%{sover}
cp -R Samples %{buildroot}%{_datadir}/OGRE-%{sover}/
# create a dummy target for /etc/alternatives/ogre (plugins config)
mv %{buildroot}%{_datadir}/OGRE-%{sover}/plugins.cfg %{buildroot}%{_datadir}/OGRE-%{sover}/plugins%{sover}.cfg
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/ogre %{buildroot}%{_datadir}/OGRE-%{sover}/plugins.cfg
# Fix file and directory permissions
find %{buildroot}%{_datadir}/OGRE-%{sover}/ -type f -exec chmod 0644 \{\} +
find %{buildroot}%{_datadir}/OGRE-%{sover}/ -type d -exec chmod 0755 \{\} +
# Remove duplicates
%fdupes %{buildroot}%{_includedir}/OGRE
%fdupes %{buildroot}%{_datadir}

%post -n libOgreMain%{soname}-plugins
update-alternatives --install \
  %{_datadir}/OGRE-%{sover}/plugins.cfg \
  ogre \
  %{_datadir}/OGRE-%{sover}/plugins%{sover}.cfg \
  $(printf '%02d%02d' %{major} %{minor})

%postun -n libOgreMain%{soname}-plugins
if [ ! -f %{_datadir}/OGRE-%{sover}/plugins%{sover}.cfg ] ; then
   update-alternatives --remove ogre %{_datadir}/OGRE-%{sover}/plugins%{sover}.cfg
fi

%ldconfig_scriptlets -n libOgreBites%{soname}
%ldconfig_scriptlets -n libOgreBitesQt%{soname}
%ldconfig_scriptlets -n libOgreMain%{soname}
%ldconfig_scriptlets -n libOgreMeshLodGenerator%{soname}
%ldconfig_scriptlets -n libOgrePaging%{soname}
%ldconfig_scriptlets -n libOgreProperty%{soname}
%ldconfig_scriptlets -n libOgreVolume%{soname}
%ldconfig_scriptlets -n libOgreOverlay%{soname}
%ldconfig_scriptlets -n libOgreRTShaderSystem%{soname}
%ldconfig_scriptlets -n libOgreTerrain%{soname}

%files -n libOgreMain%{soname}
%license LICENSE
%dir %{_libdir}/OGRE
%{_libdir}/libOgreMain.so.%{sover}

%files media
%dir %{_datadir}/OGRE-%{sover}
%dir %{_datadir}/OGRE-%{sover}/Media
%dir %{_datadir}/OGRE-%{sover}/Media/packs
%{_datadir}/OGRE-%{sover}/resources.cfg
%{_datadir}/OGRE-%{sover}/Media/Main
%{_datadir}/OGRE-%{sover}/Media/RTShaderLib
%{_datadir}/OGRE-%{sover}/Media/packs/SdkTrays.zip
%{_datadir}/OGRE-%{sover}/Media/packs/profiler.zip

%if %{with mono}
%files mono
%{_includedir}/OGRE/Ogre.i
%dir %{_prefix}/lib/cli
%dir %{_prefix}/lib/cli/ogre-sharp-%{version}
%{_prefix}/lib/cli/ogre-sharp-%{version}/Ogre.dll
%{_prefix}/lib/cli/ogre-sharp-%{version}/libOgre.so
%endif

%files python
%{python3_sitelib}/Ogre

%files -n libOgreMain%{soname}-codecs
%{plugin_dir}/Codec_Assimp.so{,.%{sover}}
%{plugin_dir}/Codec_FreeImage.so{,.%{sover}}
%{plugin_dir}/Codec_STBI.so{,.%{sover}}
%if %{with openexr}
%{plugin_dir}/Codec_EXR.so{,.%{sover}}
%endif

%files -n libOgreMain%{soname}-plugins
%dir %{plugin_dir}
%{_datadir}/OGRE-%{sover}/plugins%{sover}.cfg
%{_datadir}/OGRE-%{sover}/plugins.cfg
%ghost %{_sysconfdir}/alternatives/plugins.cfg
%ifnarch aarch64 %{arm}
%{plugin_dir}/RenderSystem_GL.so{,.%{sover}}
%{plugin_dir}/RenderSystem_GL3Plus.so{,.%{sover}}
%endif
%{plugin_dir}/RenderSystem_GLES2.so{,.%{sover}}
%{plugin_dir}/RenderSystem_Vulkan.so{,.%{sover}}
%{plugin_dir}/Plugin_BSPSceneManager.so{,.%{sover}}
%{plugin_dir}/Plugin_DotScene.so{,.%{sover}}
%{plugin_dir}/Plugin_OctreeZone.so{,.%{sover}}
%{plugin_dir}/Plugin_OctreeSceneManager.so{,.%{sover}}
%{plugin_dir}/Plugin_ParticleFX.so{,.%{sover}}
%{plugin_dir}/Plugin_PCZSceneManager.so{,.%{sover}}
%{plugin_dir}/Plugin_GLSLangProgramManager.so{,.%{sover}}

%if %{with cg}
%files -n libOgreMain%{soname}-plugin-Cg
%dir %{plugin_dir}
%{plugin_dir}/Plugin_CgProgramManager.so{,.%{sover}}
%endif

%files -n libOgreBites%{soname}
%{_libdir}/libOgreBites.so.%{sover}

%files -n libOgreBitesQt%{soname}
%{_libdir}/libOgreBitesQt.so.%{sover}

%files -n libOgreMeshLodGenerator%{soname}
%{_libdir}/libOgreMeshLodGenerator.so.%{sover}

%files -n libOgrePaging%{soname}
%{_libdir}/libOgrePaging.so.%{sover}

%files -n libOgreProperty%{soname}
%{_libdir}/libOgreProperty.so.%{sover}

%files -n libOgreOverlay%{soname}
%{_libdir}/libOgreOverlay.so.%{sover}

%files -n libOgreVolume%{soname}
%{_libdir}/libOgreVolume.so.%{sover}

%files -n libOgreRTShaderSystem%{soname}
%{_libdir}/libOgreRTShaderSystem.so.%{sover}

%files -n libOgreTerrain%{soname}
%{_libdir}/libOgreTerrain.so.%{sover}

%files -n libOgreMain-devel
%dir %{_includedir}/OGRE/
%{_includedir}/OGRE/*.h
%{_includedir}/OGRE/Plugins/
%{_includedir}/OGRE/RenderSystems/
%{_includedir}/OGRE/Threading/
%{_libdir}/libOgreMain.so
%{_libdir}/pkgconfig/OGRE.pc
%{_libdir}/pkgconfig/OGRE-PCZ.pc

%files -n libOgreBites-devel
%{_includedir}/OGRE/Bites/
%{_libdir}/libOgreBites.so
%{_libdir}/libOgreBitesQt.so
%{_libdir}/pkgconfig/OGRE-Bites.pc
%{_libdir}/pkgconfig/OGRE-BitesQt.pc

%files -n libOgreMeshLodGenerator-devel
%{_includedir}/OGRE/MeshLodGenerator
%{_libdir}/libOgreMeshLodGenerator.so
%{_libdir}/pkgconfig/OGRE-MeshLodGenerator.pc

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

%files devel
%doc AUTHORS README.md
%{_libdir}/OGRE/cmake/

%files -n ogre-demos
%{_libdir}/OGRE/Samples/
%{_bindir}/SampleBrowser
%{_datadir}/OGRE-%{sover}/Media/*
%exclude %{_datadir}/OGRE-%{sover}/Media/packs/SdkTrays.zip
%exclude %{_datadir}/OGRE-%{sover}/Media/packs/profiler.zip
%exclude %{_datadir}/OGRE-%{sover}/Media/Main
%exclude %{_datadir}/OGRE-%{sover}/Media/RTShaderLib
%{_datadir}/OGRE-%{sover}/GLX_backdrop.png
%{_datadir}/OGRE-%{sover}/samples.cfg

%files -n ogre-demos-devel
%{_datadir}/OGRE-%{sover}/Samples

%files -n ogre-tools
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%{_bindir}/VRMLConverter
%{_bindir}/OgreAssimpConverter

%files -n ogre-docs
%doc %{_docdir}/OGRE

%changelog
