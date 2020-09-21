#
# spec file for package Mesa-drivers
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


# Following define and the Name attribute are the only difference between
# Mesa.spec and Mesa-drivers.spec. Mesa-drivers.spec is generated from
# Mesa.spec using the pre_checkin.sh script.
#
# Mesa.spec builds everything that is hardware independent and does not
# require llvm. Most importantly it builds all OpenGL (ES) libraries.
#
# Mesa-drivers.spec builds hardware specific drivers and parts that require
# llvm.
#
# The purpose of this split is to be able to build most Mesa-* packages fast
# without waiting for llvm. This helps speed up whole distribution build in
# OBS. (https://bugzilla.suse.com/show_bug.cgi?id=1071297)
# Note that if you actually need to render something, you need the packages
# from Mesa-driver.

%ifarch armv6l armv6hl
%define _lto_cflags %{nil}
%endif

##### WARNING: please do not edit this auto generated spec file. Use the Mesa.spec! #####
%define drivers 1

%define glamor 1
%define _name_archive mesa
%define _version 20.1.8
%define with_opencl 0
%define with_vulkan 0
%define with_llvm 0

%ifarch %{ix86} x86_64 %{arm} aarch64 ppc64 ppc64le
  %define gallium_loader 1
%else
  %define gallium_loader 0
%endif

%define xvmc_support 0
%define vdpau_nouveau 0
%define vdpau_radeon 0

%ifarch %{ix86} x86_64 aarch64 %{arm} ppc64 ppc64le
  %define xvmc_support 1
  %define vdpau_nouveau 1
  %define vdpau_radeon 1
%endif

%ifarch %{ix86} x86_64 %{arm} aarch64
  %define with_nine 1
%endif

%if 0%{gallium_loader}
  %define with_opencl 1
  %ifarch %{ix86} x86_64
    %define with_vulkan 1
  %endif
%endif

%ifarch aarch64 %{arm} ppc64 ppc64le riscv64 s390x %{ix86} x86_64
  %define with_llvm 1
%endif

%if 0%{with_opencl}
%define have_gallium 1
%else
%define have_gallium 0
%endif

%if %{drivers}
  %define glamor 0
%else
  # No llvm dependencies
  %define with_llvm 0

  # OpenCL requires clang (LLVM)
  %define with_opencl 0

  # nine requires at least one non-swrast gallium driver
  %define with_nine 0

  # Not built because radeon driver is not built.
  %define vdpau_radeon 0

  # Not built because nouveau driver is not built.
  %define vdpau_nouveau 0

  # Not built. (Why?)
  %define xvmc_support 0

  # Vulkan includes radv driver which requires llvm
  %define with_vulkan 0
%endif

Name:           Mesa-drivers
Version:        20.1.8
Release:        0
Summary:        System for rendering 3-D graphics
License:        MIT
Group:          System/Libraries
URL:            http://www.mesa3d.org
#Git-Clone:     git://anongit.freedesktop.org/mesa/mesa
Source:         https://mesa.freedesktop.org/archive/%{_name_archive}-%{_version}.tar.xz
Source1:        https://mesa.freedesktop.org/archive/%{_name_archive}-%{_version}.tar.xz.sig
Source2:        baselibs.conf
Source3:        README.updates
Source4:        manual-pages.tar.bz2
Source6:        %{name}-rpmlintrc
Source7:        Mesa.keyring
Patch2:         n_add-Mesa-headers-again.patch
# never to be upstreamed
Patch54:        n_drirc-disable-rgb10-for-chromium-on-amd.patch
Patch58:        u_dep_xcb.patch
Patch60:        buildfix-ppc64le.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  imake
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-base
%if 0%{?suse_version} > 1320
BuildRequires:  python3-mako
%else
BuildRequires:  python3-Mako
%endif
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(dri3proto)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(libdrm) >= 2.4.75
BuildRequires:  pkgconfig(libdrm_amdgpu) >= 2.4.95
BuildRequires:  pkgconfig(libdrm_nouveau) >= 2.4.66
BuildRequires:  pkgconfig(libdrm_radeon) >= 2.4.71
BuildRequires:  pkgconfig(libglvnd) >= 0.1.0
%ifarch aarch64 %{ix86} x86_64 ppc64le s390x
BuildRequires:  pkgconfig(valgrind)
%endif
BuildRequires:  pkgconfig(libkms) >= 1.0.0
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(presentproto)
%if %{drivers}
BuildRequires:  pkgconfig(vdpau) >= 1.1
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xvmc)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(zlib)
Provides:       Mesa7 = %{version}
Obsoletes:      Mesa7 < %{version}
Provides:       intel-i810-Mesa = %{version}
Obsoletes:      intel-i810-Mesa < %{version}
Provides:       Mesa-libIndirectGL1 = %{version}
Obsoletes:      Mesa-libIndirectGL1 < %{version}
Provides:       Mesa-nouveau3d = %{version}
Provides:       xorg-x11-Mesa = %{version}
Obsoletes:      Mesa-nouveau3d < %{version}
Obsoletes:      xorg-x11-Mesa < %{version}
Provides:       s2tc = %{version}
Obsoletes:      s2tc < %{version}
Provides:       libtxc_dxtn = %{version}
Obsoletes:      libtxc_dxtn < %{version}
%ifarch %{arm} aarch64
BuildRequires:  pkgconfig(libdrm_etnaviv) >= 2.4.89
BuildRequires:  pkgconfig(libdrm_freedreno) >= 2.4.74
BuildRequires:  pkgconfig(libelf)
%endif
%ifarch x86_64 %{ix86}
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig(libdrm_intel) >= 2.4.75
%else
%if 0%{with_opencl}
BuildRequires:  libelf-devel
%endif
%endif
# Requirements for wayland bumped up from 17.0
BuildRequires:  pkgconfig(wayland-client) >= 1.11
BuildRequires:  pkgconfig(wayland-protocols) >= 1.8
BuildRequires:  pkgconfig(wayland-server) >= 1.11
%if 0%{with_llvm}
%if 0%{?suse_version} >= 1550
BuildRequires:  llvm-devel >= 10.0.0
%else
BuildRequires:  llvm9-devel
%endif
%endif

%if 0%{with_opencl}
%if 0%{?suse_version} >= 1550
BuildRequires:  clang-devel >= 10.0.0
%else
BuildRequires:  clang9-devel
%endif
BuildRequires:  libclc
%endif

Requires:       Mesa-libEGL1 = %{version}
Requires:       Mesa-libGL1 = %{version}
Requires:       libglvnd >= 0.1.0

# This dependency on Mesa-dri and Mesa-gallium is here to make sure users that
# do not install recommends on their system still get working Mesa. It is
# ignored in obs when Mesa is installed as build dependency.
Requires:       Mesa-dri = %{version}
%if 0%{have_gallium}
Requires:       Mesa-gallium = %{version}
%endif

%description
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL.* To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc.(SGI). However, the author does not possess an
OpenGL license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI. Those who
want a licensed implementation of OpenGL should contact a licensed
vendor.

Please do not refer to the library as MesaGL (for legal reasons). It's
just Mesa or The Mesa 3-D graphics library.

* OpenGL is a trademark of Silicon Graphics Incorporated.

%package devel
Summary:        Libraries, includes and more to develop Mesa applications
Group:          Development/Libraries/X11
Requires:       Mesa = %{version}
Requires:       Mesa-dri-devel = %{version}
Requires:       Mesa-libEGL-devel = %{version}
Requires:       Mesa-libGL-devel = %{version}
Requires:       Mesa-libGLESv1_CM-devel = %{version}
Requires:       Mesa-libGLESv2-devel = %{version}
Requires:       Mesa-libglapi-devel = %{version}
Requires:       libOSMesa-devel = %{version}
Requires:       libgbm-devel
Provides:       Mesa-devel-static = %{version}
Provides:       xorg-x11-Mesa-devel = %{version}
Requires:       libglvnd-devel >= 1.2.0
Obsoletes:      Mesa-devel-static < %{version}
Obsoletes:      xorg-x11-Mesa-devel < %{version}
Provides:       Mesa-libIndirectGL-devel = %{version}
Obsoletes:      Mesa-libIndirectGL-devel < %{version}
Provides:       s2tc-devel = %{version}
Obsoletes:      s2tc-devel < %{version}
Provides:       libtxc_dxtn-devel = %{version}
Obsoletes:      libtxc_dxtn-devel < %{version}

%description devel
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL.* To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc.(SGI). However, the author does not possess an
OpenGL license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI. Those who
want a licensed implementation of OpenGL should contact a licensed
vendor.

Please do not refer to the library as MesaGL (for legal reasons). It's
just Mesa or The Mesa 3-D graphics library.

* OpenGL is a trademark of Silicon Graphics Incorporated.

%package libEGL1
# Kudos to Debian for the descriptions
Summary:        EGL API implementation
Group:          System/Libraries
Requires:       libglvnd >= 0.1.0

%description libEGL1
This package contains the EGL native platform graphics interface
library. EGL provides a platform-agnostic mechanism for creating
rendering surfaces for use with other graphics libraries, such as
OpenGL|ES and OpenVG.

This package contains modules to interface with the existing system
GLX or DRI2 drivers to provide OpenGL via EGL. The Mesa main package
provides drivers to provide hardware-accelerated OpenGL|ES and OpenVG
support.

%package libEGL-devel
Summary:        Development files for the EGL API
Group:          Development/Libraries/C and C++
Requires:       Mesa-KHR-devel = %{version}
Requires:       Mesa-libEGL1 = %{version}
Requires:       libglvnd-devel >= 0.1.0
Requires:       pkgconfig(x11)
# Other requires taken care of by pkgconfig already

%description libEGL-devel
This package contains the development environment required for
compiling programs against EGL native platform graphics interface
library. EGL provides a platform-agnostic mechanism for creating
rendering surfaces for use with other graphics libraries, such as
OpenGL|ES and OpenVG.

This package provides the development environment for compiling
programs against the EGL library.

%package KHR-devel
Summary:        Mesa Khronos development headers
Group:          Development/Libraries/C and C++
Provides:       Mesa-libGL-devel:/usr/include/KHR/khrplatform.h

%description KHR-devel
Mesa Khronos development headers.

%package libGL1
Summary:        The GL/GLX runtime of the Mesa 3D graphics library
Group:          System/Libraries
Requires:       Mesa = %{version}
Requires:       libglvnd >= 0.1.0

%description libGL1
Mesa is a software library for 3D computer graphics that provides a
generic OpenGL implementation for rendering three-dimensional
graphics.

GLX ("OpenGL Extension to the X Window System") provides the
interface connecting OpenGL and the X Window System: it enables
programs wishing to use OpenGL to do so within a window provided by
the X Window System.

%package libGL-devel
Summary:        GL/GLX development files of the OpenGL API
Group:          Development/Libraries/C and C++
Requires:       Mesa-KHR-devel = %{version}
Requires:       Mesa-libGL1 = %{version}
Requires:       libglvnd-devel >= 0.1.0

%description libGL-devel
Mesa is a software library for 3D computer graphics that provides a
generic OpenGL implementation for rendering three-dimensional
graphics.

This package includes headers and static libraries for compiling
programs with Mesa.

%package libGLESv1_CM-devel
Summary:        Development files for the OpenGL ES 1.x API
Group:          Development/Libraries/C and C++
Requires:       Mesa-KHR-devel = %{version}
Requires:       libglvnd-devel >= 0.1.0
Requires:       pkgconfig(egl)

%description libGLESv1_CM-devel
OpenGL|ES is an API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 1.x provides an API for fixed-function hardware.

This package provides a development environment for building programs
using the OpenGL|ES 1.x APIs.

%package libGLESv2-devel
Summary:        Development files for the OpenGL ES 2.x API
Group:          Development/Libraries/C and C++
Requires:       Mesa-KHR-devel = %{version}
Requires:       libglvnd-devel >= 0.1.0
Requires:       pkgconfig(egl)

%description libGLESv2-devel
OpenGL|ES is an API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 2.x provides an API for programmable hardware including
vertex and fragment shaders.

This package provides a development environment for building
applications using the OpenGL|ES 2.x APIs.

%package libGLESv3-devel
Summary:        Development files for the OpenGL ES 3.x API
Group:          Development/Libraries/C and C++
Requires:       Mesa-KHR-devel = %{version}
Requires:       pkgconfig(egl)

%description libGLESv3-devel
OpenGL|ES is an API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

This package provides a development environment for building
applications using the OpenGL|ES 3.x APIs.

%package -n libOSMesa8
Summary:        Mesa Off-screen rendering extension
# Wrongly named package shipped .so.8
Group:          System/Libraries
Obsoletes:      libOSMesa9 < %{version}
Provides:       libOSMesa9 = %{version}

%description -n libOSMesa8
OSmesa is a Mesa extension that allows programs to render to an
off-screen buffer using the OpenGL API without having to create a
rendering context on an X Server. It uses a pure software renderer.

%package -n libOSMesa-devel
Summary:        Development files for the Mesa Offscreen Rendering extension
Group:          Development/Libraries/C and C++
Requires:       libOSMesa8 = %{version}

%description -n libOSMesa-devel
Development files for the OSmesa Mesa extension that allows programs to render to an
off-screen buffer using the OpenGL API without having to create a
rendering context on an X Server. It uses a pure software renderer.

%package libglapi0
Summary:        Free implementation of the GL API
Group:          System/Libraries

%description libglapi0
The Mesa GL API module is responsible for dispatching all the gl*
functions. It is intended to be mainly used by the Mesa-libGLES*
packages.

%package libglapi-devel
Summary:        Development files for the Mesa GL API implementation
Group:          Development/Libraries/C and C++
Requires:       Mesa-libglapi0 = %{version}

%description libglapi-devel
Development files for the Mesa GL API module which is responsible for
dispatching all the gl* functions. It is intended to be mainly used by
the Mesa-libGLES* packages.

%package -n Mesa-dri
Summary:        DRI plug-ins for 3D acceleration
Group:          System/Libraries
Requires:       Mesa = %{version}
Supplements:    Mesa

%description -n Mesa-dri
This package contains Mesa DRI drivers for 3D acceleration.

%package dri-devel
Summary:        Development files for the DRI API
Group:          Development/Libraries/C and C++
Requires:       Mesa = %{version}

%description dri-devel
This package contains the development environment required for
compiling programs and libraries using the DRI API.

%package -n Mesa-dri-nouveau
Summary:        Mesa DRI plug-in for 3D acceleration via Nouveau
Group:          System/Libraries
Requires:       Mesa = %{version}
Supplements:    xf86-video-nouveau

%description -n Mesa-dri-nouveau
This package contains nouveau_dri.so, which is necessary for
Nouveau's 3D acceleration to work. It is packaged separately
since it is still experimental.

%package -n Mesa-dri-vc4
Summary:        Mesa DRI plug-in for 3D acceleration on Raspberry Pi
Group:          System/Libraries
Requires:       Mesa = %{version}

%description -n Mesa-dri-vc4
This package contains vc4_dri.so, which is necessary for 3D
acceleration on the Raspberry Pi to work. It is packaged separately
since it is still experimental.

%package -n Mesa-gallium
Summary:        Mesa Gallium GPU drivers
Group:          System/Libraries
Requires:       Mesa = %{version}
Supplements:    Mesa

%description -n Mesa-gallium
This package contains Mesa Gallium drivers for 3D acceleration.

%package -n libgbm1
Summary:        Generic buffer management API
Group:          System/Libraries

%description -n libgbm1
This package contains the GBM buffer management library. It provides
a mechanism for allocating buffers for graphics rendering tied to
Mesa.

GBM is intended to be used as a native platform for EGL on drm or
openwfd.

%package -n libgbm-devel
Summary:        Development files for the EGL API
Group:          Development/Libraries/C and C++
Requires:       libgbm1 = %{version}

%description -n libgbm-devel
This package contains the GBM buffer management library. It provides
a mechanism for allocating buffers for graphics rendering tied to
Mesa.

GBM is intended to be used as a native platform for EGL on drm or
openwfd.

This package provides the development environment for compiling
programs against the GBM library.

%package -n Mesa-libd3d
Summary:        Mesa Direct3D9 state tracker
# Manually provide d3d library (bnc#918294)
Group:          System/Libraries
%ifarch x86_64 s390x ppc64 ppc64le aarch64 riscv64
Provides:       d3dadapter9.so.1()(64bit)
%else
Provides:       d3dadapter9.so.1
%endif

%description -n Mesa-libd3d
Mesa Direct3D9 state tracker

%package -n Mesa-libd3d-devel
Summary:        Mesa Direct3D9 state tracker development package
Group:          Development/Libraries/C and C++
Requires:       Mesa-libd3d = %{version}

%description -n Mesa-libd3d-devel
Mesa Direct3D9 state tracker development package

%package -n libXvMC_nouveau
Summary:        XVMC state tracker for Nouveau
Group:          System/Libraries

%description -n libXvMC_nouveau
This package contains the XvMC state tracker for Nouveau. This is
still "work in progress", i.e. expect poor video quality, choppy
videos and artefacts all over.

%package -n libXvMC_r600
Summary:        XVMC state tracker for R600
Group:          System/Libraries

%description -n libXvMC_r600
This package contains the XvMC state tracker for R600. This is
still "work in progress", i.e. expect poor video quality, choppy
videos and artefacts all over.

%package -n libvdpau_nouveau
Summary:        XVMC state tracker for Nouveau
Group:          System/Libraries
Supplements:    xf86-video-nouveau

%description -n libvdpau_nouveau
This package contains the VDPAU state tracker for Nouveau.

%package -n libvdpau_r300
Summary:        XVMC state tracker for R300
Group:          System/Libraries
Supplements:    xf86-video-ati

%description -n libvdpau_r300
This package contains the VDPAU state tracker for R300.

%package -n libvdpau_r600
Summary:        XVMC state tracker for R600
Group:          System/Libraries
Supplements:    xf86-video-ati

%description -n libvdpau_r600
This package contains the VDPAU state tracker for R600.

%package -n libvdpau_radeonsi
Summary:        XVMC state tracker for radeonsi
Group:          System/Libraries
Supplements:    xf86-video-ati

%description -n libvdpau_radeonsi
This package contains the VDPAU state tracker for radeonsi.

%package -n Mesa-libOpenCL
Summary:        Mesa OpenCL implementation
Group:          System/Libraries
Requires:       libclc

%description -n Mesa-libOpenCL
This package contains the Mesa OpenCL implementation or GalliumCompute.

%package -n Mesa-libva
Summary:        Mesa VA-API implementation
Group:          System/Libraries
Supplements:    Mesa

%description -n Mesa-libva
This package contains the Mesa VA-API implementation provided through gallium.

%package -n libvulkan_intel
Summary:        Mesa vulkan driver for Intel GPU
Group:          System/Libraries
Supplements:    xf86-video-intel

%description -n libvulkan_intel
This package contains the Vulkan parts for Mesa.

%package -n libvulkan_radeon
Summary:        Mesa vulkan driver for AMD GPU
Group:          System/Libraries
Supplements:    xf86-video-amdgpu
Supplements:    xf86-video-ati

%description -n libvulkan_radeon
This package contains the Vulkan parts for Mesa.

%package -n Mesa-libVulkan-devel
Summary:        Mesa's Vulkan development files
Group:          Development/Libraries/C and C++
Requires:       libvulkan_intel = %{version}
Requires:       libvulkan_radeon = %{version}

%description -n Mesa-libVulkan-devel
This package contains the development files for Mesa's Vulkan implementation.

%package -n Mesa-vulkan-device-select
Summary:        Vulkan layer to select Vulkan devices provided by Mesa
Group:          System/Libraries
Requires:       libvulkan_intel = %{version}
Requires:       libvulkan_radeon = %{version}

%description -n Mesa-vulkan-device-select
This package contains the VK_MESA_device_select Vulkan layer

%package -n Mesa-vulkan-overlay
Summary:        Mesa Vulkan Overlay layer
Group:          System/Libraries
Requires:       libvulkan_intel = %{version}
Requires:       libvulkan_radeon = %{version}

%description -n Mesa-vulkan-overlay
This package contains the VK_MESA_Overlay Vulkan layer

%package -n libxatracker2
Version:        1.0.0
Release:        0
Summary:        XA state tracker
Group:          System/Libraries

%description -n libxatracker2
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx
video driver.

%package -n libxatracker-devel
Version:        1.0.0
Release:        0
Summary:        Development files for the XA API
Group:          Development/Libraries/C and C++
Requires:       libxatracker2 = %{version}

%description -n libxatracker-devel
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx
video driver.

This package provides the development environment for compiling
programs against the XA state tracker.

%prep
%setup -q -n %{_name_archive}-%{_version} -b4
# remove some docs
rm -rf docs/README.{VMS,WIN32,OS2}

%patch2 -p1
%patch54 -p1
%patch58 -p1
%ifarch ppc64le
%patch60 -p1
%endif

# Remove requires to vulkan libs from baselibs.conf on platforms
# where vulkan build is disabled; ugly ...
%if 0%{?with_vulkan} == 0
grep -v -i vulkan "%{_sourcedir}/baselibs.conf" >"%{_sourcedir}/temp" && \
  mv "%{_sourcedir}/temp" "%{_sourcedir}/baselibs.conf"
%endif

# Avoid build error for PowerPC
# https://bugzilla.opensuse.org/show_bug.cgi?id=1171045
%ifarch ppc64 ppc64le
sed -i -e s/cpp_std=gnu++11/cpp_std=gnu++14/g meson.build
%endif

%build
egl_platforms=x11,drm,surfaceless,wayland

%meson \
            --auto-features=disabled \
%if %{drivers}
            -Dgles1=false \
            -Dgles2=false \
            -Degl=true \
            -Dglx=disabled \
            -Dosmesa=none \
%else
            -Dglvnd=true \
            -Dgles1=true \
            -Dgles2=true \
            -Degl=true \
            -Dosmesa=classic \
            -Dglx=auto \
            -Dllvm=false \
            -Dvulkan-drivers= \
%endif
            -Dplatforms=$egl_platforms \
            -Ddri3=true \
            -Dshared-glapi=true \
%if 0%{?with_nine}
            -Dgallium-nine=true \
%endif
%if %{glamor}
            -Dgbm=true \
%endif
%if 0%{with_opencl}
            -Dgallium-opencl=icd \
%if 0%{?suse_version} >= 1550
            --sysconfdir=%{_datadir} \
%endif
%endif
            -Ddri-search-path=%{_libdir}/dri \
%if 0%{with_llvm}
            -Dllvm=true \
            -Dshared-llvm=true \
%endif
%if %{drivers}
%if %{gallium_loader}
            -Dgallium-vdpau=true \
            -Dgallium-xvmc=true \
            -Dgallium-va=true \
            -Dgallium-xa=true \
%endif
%if 0%{with_vulkan}
            -Dvulkan-drivers=intel,amd \
            -Dvulkan-device-select-layer=true \
            -Dvulkan-overlay-layer=true \
%else
            -Dvulkan-drivers= \
%endif
  %ifarch %{ix86} x86_64
            -Ddri-drivers=i915,i965,nouveau,r100,r200 \
            -Dgallium-drivers=r300,r600,radeonsi,nouveau,swrast,svga,virgl,iris \
  %else
  %ifarch %{arm} aarch64
            -Ddri-drivers=nouveau \
            -Dgallium-drivers=r300,r600,nouveau,swrast,virgl,freedreno,vc4,etnaviv,lima,panfrost,kmsro,v3d \
  %else
  %ifarch ppc64 ppc64le
            -Ddri-drivers=nouveau \
            -Dgallium-drivers=r300,r600,radeonsi,nouveau,swrast \
  %else
            -Ddri-drivers= \
            -Dgallium-drivers=swrast \
  %endif
  %endif
  %endif
%else
            -Ddri-drivers=swrast \
            -Dgallium-drivers= \
%endif
%ifarch aarch64 %{ix86} x86_64 ppc64le s390x
            -Dvalgrind=true \
%endif
            -Db_ndebug=true \
            -Dc_args="%{optflags}" \
            -Dcpp_args="%{optflags}"

%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

# libwayland-egl is provided by wayland itself
rm -f %{buildroot}/%{_libdir}/libwayland-egl.so*
rm -f %{buildroot}/%{_libdir}/pkgconfig/wayland-egl.pc

%if %{drivers}
# Delete things that we do not package in the Mesa-drivers variant, but can
# not disable from buildling and installing.

# in Mesa
rm -rf %{buildroot}/%{_datadir}/drirc.d

rm -f %{buildroot}/%{_libdir}/libEGL.so*
# in Mesa-libEGL-devel
rm %{buildroot}/%{_includedir}/EGL/egl.h
rm %{buildroot}/%{_includedir}/EGL/eglext.h
rm %{buildroot}/%{_includedir}/EGL/eglextchromium.h
rm %{buildroot}/%{_includedir}/EGL/eglmesaext.h
rm %{buildroot}/%{_includedir}/EGL/eglplatform.h
rm %{buildroot}/%{_libdir}/pkgconfig/egl.pc

# in Mesa-libGL-devel
rm -rf %{buildroot}/%{_includedir}/GL

# in Mesa-libglapi0
rm %{buildroot}/%{_libdir}/libglapi.so*

# in libwayland-egl1
rm -f %{buildroot}/%{_libdir}/libwayland-egl.so*
rm -f %{buildroot}/%{_libdir}/pkgconfig/wayland-egl.pc

# in Mesa-dri-devel
rm %{buildroot}/%{_libdir}/pkgconfig/dri.pc

# in libgbm-devel
rm %{buildroot}/%{_includedir}/gbm.h
rm %{buildroot}/%{_libdir}/libgbm.so*
rm %{buildroot}/%{_libdir}/pkgconfig/gbm.pc

# in KHR-devel
rm -rf %{buildroot}/%{_includedir}/KHR

# workaround needed since Mesa 19.0.2
rm -f %{buildroot}/%{_libdir}/vdpau/libvdpau_gallium.so

%else

rm -rf %{buildroot}/%{_libdir}/dri/swrast_dri.so

rm -f %{buildroot}%{_libdir}/libGLES*
# glvnd needs a default provider for indirect rendering where it cannot
# determine the vendor
ln -s %{_libdir}/libGLX_mesa.so.0 %{buildroot}%{_libdir}/libGLX_indirect.so.0

# pickup pkgconfig files from libglvnd build
rm -f %{buildroot}/%{_libdir}/pkgconfig/{gl,egl,glesv1_cm,glesv2}.pc
install -m 0644 /usr/share/doc/packages/libglvnd/pkgconfig/{gl,egl,glesv1_cm,glesv2}.pc \
   %{buildroot}/%{_libdir}/pkgconfig/

for dir in ../xc/doc/man/{GL/gl,GL/glx}; do
 pushd $dir
   xmkmf -a
   make %{?_smp_mflags} V=1
   make install.man DESTDIR=%{buildroot} MANPATH=%{_mandir} LIBMANSUFFIX=3gl
 popd
done
%endif

%fdupes -s %{buildroot}/%{_mandir}

%if !%{drivers}
# Use dummy README file that can be included in both Mesa and Mesa-32bit. This way Mesa-32bit will be build (otherwise it would be skipped as empty) and it can be used by the other *-32bit packages.
echo "The \"Mesa\" package does not have the ability to render, but is supplemented by \"Mesa-dri\" and \"Mesa-gallium\" which contain the drivers for rendering" > docs/README.package.%{_arch}
%endif

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post   libEGL1 -p /sbin/ldconfig

%postun libEGL1 -p /sbin/ldconfig

%post   libGL1 -p /sbin/ldconfig

%postun libGL1 -p /sbin/ldconfig

%post   -n libOSMesa8 -p /sbin/ldconfig

%postun -n libOSMesa8 -p /sbin/ldconfig

%post   -n libgbm1 -p /sbin/ldconfig

%postun -n libgbm1 -p /sbin/ldconfig

%post   -n libxatracker2 -p /sbin/ldconfig

%postun -n libxatracker2 -p /sbin/ldconfig

%post   libglapi0 -p /sbin/ldconfig

%postun libglapi0 -p /sbin/ldconfig

%post -n Mesa-libd3d -p /sbin/ldconfig

%postun -n Mesa-libd3d -p /sbin/ldconfig

%if !%{drivers}
%files
%license docs/license.html
%doc docs/README*
%dir %{_datadir}/drirc.d
%config %{_datadir}/drirc.d/*

%files libEGL1
%{_libdir}/libEGL_mesa.so*
%dir %{_datadir}/glvnd
%dir %{_datadir}/glvnd/egl_vendor.d
%{_datadir}/glvnd/egl_vendor.d/50_mesa.json

%files libEGL-devel
%{_includedir}/EGL
%{_libdir}/pkgconfig/egl.pc

%files KHR-devel
%dir %{_includedir}/KHR
%{_includedir}/KHR

%files libGL1
%{_libdir}/libGLX_mesa.so*
%{_libdir}/libGLX_indirect.so*

%files libGL-devel
%dir %{_includedir}/GL
%{_includedir}/GL/*.h
%exclude %{_includedir}/GL/osmesa.h
%{_libdir}/pkgconfig/gl.pc
%{_mandir}/man3/gl[A-Z]*

%files libGLESv1_CM-devel
%{_includedir}/GLES
%{_libdir}/pkgconfig/glesv1_cm.pc

%files libGLESv2-devel
%{_includedir}/GLES2
%{_libdir}/pkgconfig/glesv2.pc

%files libGLESv3-devel
%{_includedir}/GLES3

%files -n libOSMesa8
%{_libdir}/libOSMesa.so.8.0.0
%{_libdir}/libOSMesa.so.8

%files -n libOSMesa-devel
%{_includedir}/GL/osmesa.h
%{_libdir}/libOSMesa.so
%{_libdir}/pkgconfig/osmesa.pc

%files -n libgbm1
%{_libdir}/libgbm.so.1*

%files -n libgbm-devel
%{_includedir}/gbm.h
%{_libdir}/libgbm.so
%{_libdir}/pkgconfig/gbm.pc
%endif

%if %{drivers}
%ifarch aarch64 %{ix86} x86_64 %{arm} ppc64 ppc64le
%files -n libxatracker2
%{_libdir}/libxatracker.so.2*

%files -n libxatracker-devel
%{_includedir}/xa_*.h
%{_libdir}/libxatracker.so
%{_libdir}/pkgconfig/xatracker.pc
%endif

%if %{xvmc_support}
%files -n libXvMC_nouveau
%{_libdir}/libXvMCnouveau.so*

%files -n libXvMC_r600
%{_libdir}/libXvMCr600.so*
%endif

%if %{vdpau_nouveau}
%files -n libvdpau_nouveau
%{_libdir}/vdpau/libvdpau_nouveau.so
%{_libdir}/vdpau/libvdpau_nouveau.so.1
%{_libdir}/vdpau/libvdpau_nouveau.so.1.0
%{_libdir}/vdpau/libvdpau_nouveau.so.1.0.0
%endif

%if %{vdpau_radeon}
%files -n libvdpau_r300
%{_libdir}/vdpau/libvdpau_r300.so
%{_libdir}/vdpau/libvdpau_r300.so.1
%{_libdir}/vdpau/libvdpau_r300.so.1.0
%{_libdir}/vdpau/libvdpau_r300.so.1.0.0

%files -n libvdpau_r600
%{_libdir}/vdpau/libvdpau_r600.so
%{_libdir}/vdpau/libvdpau_r600.so.1
%{_libdir}/vdpau/libvdpau_r600.so.1.0
%{_libdir}/vdpau/libvdpau_r600.so.1.0.0
%endif

%ifarch %{ix86} x86_64 ppc64 ppc64le
%files -n libvdpau_radeonsi
%{_libdir}/vdpau/libvdpau_radeonsi.so
%{_libdir}/vdpau/libvdpau_radeonsi.so.1
%{_libdir}/vdpau/libvdpau_radeonsi.so.1.0
%{_libdir}/vdpau/libvdpau_radeonsi.so.1.0.0
%endif
%endif

%if !%{drivers}
%files libglapi0
%{_libdir}/libglapi.so.0*

%files libglapi-devel
%{_libdir}/libglapi.so
%endif

%if %{drivers}
%files -n Mesa-dri
%dir %{_libdir}/dri
%{_libdir}/dri/*_dri.so
%ifarch %{ix86} x86_64 aarch64 %{arm} ppc64 ppc64le
%exclude %{_libdir}/dri/nouveau_dri.so
%exclude %{_libdir}/dri/nouveau_vieux_dri.so
%endif
%ifarch %{arm} aarch64
%exclude %{_libdir}/dri/vc4_dri.so
%endif

%if 0%{with_opencl}
# only built with opencl
%files -n Mesa-gallium
%dir %{_libdir}/gallium-pipe/
%{_libdir}/gallium-pipe/pipe_*.so
%endif

%ifarch %{ix86} x86_64 aarch64 %{arm} ppc64 ppc64le
%files -n Mesa-dri-nouveau
%{_libdir}/dri/nouveau_dri.so
%{_libdir}/dri/nouveau_vieux_dri.so
%endif

%ifarch aarch64 %{arm}
%files -n Mesa-dri-vc4
%{_libdir}/dri/vc4_dri.so
%endif

# drivers
%endif

%if !%{drivers}
%files dri-devel
%{_includedir}/GL/internal
%{_libdir}/pkgconfig/dri.pc

%files devel
%doc docs/*.html

# !drivers
%endif

%if 0%{?with_nine}
%files -n Mesa-libd3d
%dir %{_libdir}/d3d/
%{_libdir}/d3d/*.so.*

%files -n Mesa-libd3d-devel
%{_libdir}/pkgconfig/d3d.pc
%{_includedir}/d3dadapter/
%{_libdir}/d3d/*.so
%endif

%if 0%{with_opencl}
%files -n Mesa-libOpenCL
%if 0%{?suse_version} >= 1550
%dir %{_datadir}/OpenCL
%dir %{_datadir}/OpenCL/vendors
%{_datadir}/OpenCL/vendors/mesa.icd
%else
%dir %{_sysconfdir}/OpenCL
%dir %{_sysconfdir}/OpenCL/vendors
%{_sysconfdir}/OpenCL/vendors/mesa.icd
%endif
%{_libdir}/libMesaOpenCL.so*
%endif

%if %{drivers}
%ifarch %{ix86} x86_64 aarch64 %{arm} ppc64 ppc64le
%files -n Mesa-libva
%{_libdir}/dri/*_drv_video.so
%endif
%endif

%if 0%{with_vulkan}
%files -n libvulkan_intel
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/intel_icd.*.json
%{_libdir}/libvulkan_intel.so

%files -n libvulkan_radeon
%{_libdir}/libvulkan_radeon.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/radeon_icd.*.json

%files -n Mesa-libVulkan-devel
%dir %{_includedir}/vulkan
%{_includedir}/vulkan/*

%files -n Mesa-vulkan-device-select
%{_libdir}/libVkLayer_MESA_device_select.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/implicit_layer.d
%{_datadir}/vulkan/implicit_layer.d/VkLayer_MESA_device_select.json

%files -n Mesa-vulkan-overlay
%{_bindir}/mesa-overlay-control.py
%{_libdir}/libVkLayer_MESA_overlay.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/explicit_layer.d
%{_datadir}/vulkan/explicit_layer.d/VkLayer_MESA_overlay.json
%endif

%changelog
