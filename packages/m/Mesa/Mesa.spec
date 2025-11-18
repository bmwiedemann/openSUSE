#
# spec file for package Mesa
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


#!BuildIgnore: Mesa-dri

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "drivers"
%global psuffix -drivers
%else
%global psuffix %{nil}
%endif

%if 0%{?sle_version} == 150600 && 0%{?is_opensuse}
%define meson_build /usr/bin/meson compile -C %{_vpath_builddir} %{_smp_mflags} --verbose
%define meson_install /usr/bin/meson install -C %{_vpath_builddir} --no-rebuild --destdir=%{buildroot}
%endif

%ifarch %{ix86} x86_64 armv6l armv6hl
%define _lto_cflags %{nil}
%endif

# Possible patent issues, see
# https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/15258
# for more details
%if 0%{?BUILD_ORIG}
%define video_codecs 1
%else
%define video_codecs 0
%endif

%define drivers 0

%define glamor 1
%define _name_archive mesa
%ifnarch s390x
%define _version 25.3.0
%else
%define _version 24.1.7
%endif
%define with_opencl 0
%define with_rusticl 0
%define with_vulkan 0
%define with_llvm 0

%ifarch %{ix86} x86_64 %{arm} aarch64 loongarch64 ppc64 ppc64le riscv64
  %define gallium_loader 1
%else
  %define gallium_loader 0
%endif

%if 0%{gallium_loader}
  %define with_opencl 1
  %ifarch %{ix86} x86_64
    %define with_vulkan 1
    %if 0%{?suse_version} > 1600
    %define vulkan_drivers swrast,amd,intel,intel_hasvk,nouveau,microsoft-experimental
    %else
    %define vulkan_drivers swrast,amd,intel,intel_hasvk
    %endif
  %endif
  %ifarch %{arm} aarch64
    %define with_vulkan 1
    %if 0%{?suse_version} > 1600
      %define vulkan_drivers swrast,amd,broadcom,freedreno,intel,intel_hasvk,nouveau,panfrost
    %else
      %if 0%{?suse_version} == 1600
        %define vulkan_drivers swrast,amd,broadcom,freedreno,intel,intel_hasvk,panfrost
      %endif
    %endif
  %endif
  %ifarch riscv64
    %define with_vulkan 1
    %define vulkan_drivers swrast,amd,intel,intel_hasvk
  %endif
  %ifarch loongarch64
    %define with_vulkan 1
    %define vulkan_drivers swrast,amd,intel,intel_hasvk,nouveau
  %endif
%endif

%ifarch aarch64 %{arm} loongarch64 ppc64 ppc64le riscv64 s390x %{ix86} x86_64 ix86
  %define with_llvm 1
%endif

%if "%{flavor}" == "drivers"
  %define glamor 1
%if 0%{?suse_version} >= 1550 && 0%{with_opencl}
  %define with_rusticl 1
%endif
%else
  # No llvm dependencies
  %define with_llvm 0

  # OpenCL requires clang (LLVM)
  %define with_opencl 0

  # Vulkan includes radv driver which requires llvm
  %define with_vulkan 0
%endif

# NVK aka Vulkan Nouveau dependencies
%global _unicode_ident_crate_ver 1.0.12
%global _syn_crate_ver 2.0.87
%global _quote_crate_ver 1.0.35
%global _proc_macro2_ver 1.0.86
%global _paste_crate_ver 1.0.14
%global _rustc_hash_crate_ver 2.1.1

# Leap 15 and SLES 15 defaults to GCC 7, which does not have stable C++17 ABI.
# See https://bugzilla.suse.com/show_bug.cgi?id=1235697
%if 0%{?gcc_version} < 13
%define gcc_version 13
%endif

Name:           Mesa%{psuffix}
%ifnarch s390x
Version:        25.3.0
%else
Version:        24.1.7
%endif
Release:        0
Summary:        System for rendering 3-D graphics
License:        MIT
Group:          System/Libraries
URL:            https://www.mesa3d.org
#Git-Clone:     git://anongit.freedesktop.org/mesa/mesa
Source0:        https://archive.mesa3d.org/%{_name_archive}-%{_version}.tar.xz
Source1:        https://archive.mesa3d.org/%{_name_archive}-%{_version}.tar.xz.sig
# NVK aka Vulkan Nouveau dependencies
# Explainer:
# Since Rust crates are not installed or discouraged to be installed as system
# dependencies because of the maintenance burden of being the next crates.io,
# we will have to download the following crates as vendored dependencies.
# Hence, do not be scared if the dependencies are done like this
# To check new crates or update the versions, just go to the subprojects folder and
# run `grep -r crates .` then set versions appropriately.
# download with 'osc service runall download_files'; github tarballs have different checksums!
Source2:        http://crates.io/api/v1/crates/unicode-ident/%{_unicode_ident_crate_ver}/download#/unicode-ident-%{_unicode_ident_crate_ver}.tar.gz
Source3:        http://crates.io/api/v1/crates/syn/%{_syn_crate_ver}/download#/syn-%{_syn_crate_ver}.tar.gz
Source4:        http://crates.io/api/v1/crates/quote/%{_quote_crate_ver}/download#/quote-%{_quote_crate_ver}.tar.gz
Source5:        http://crates.io/api/v1/crates/proc-macro2/%{_proc_macro2_ver}/download#/proc-macro2-%{_proc_macro2_ver}.tar.gz
Source6:        http://crates.io/api/v1/crates/paste/%{_paste_crate_ver}/download#/paste-%{_paste_crate_ver}.tar.gz
Source7:        baselibs.conf
Source8:        README.updates
Source9:        manual-pages.tar.bz2
Source10:       Mesa-rpmlintrc
Source11:       Mesa.keyring
Source12:       README-suse-maintenance.md
Source20:       https://archive.mesa3d.org/%{_name_archive}-25.3.0.tar.xz
Source21:       https://archive.mesa3d.org/%{_name_archive}-25.3.0.tar.xz.sig
# download with 'osc service runall download_files'; github tarballs have different checksums!
Source22:       http://crates.io/api/v1/crates/rustc-hash/%{_rustc_hash_crate_ver}/download#/rustc-hash-%{_rustc_hash_crate_ver}.tar.gz
Patch2:         n_add-Mesa-headers-again.patch
Patch11:        u_0001-intel-genxml-Drop-from-__future__-import-annotations.patch
Patch12:        u_0002-intel-genxml-Add-a-untyped-OrderedDict-fallback-for-.patch
%ifnarch s390x
Patch13:        python36-buildfix1.patch
%else
Patch13:        python36-buildfix1-s390x.patch
%endif
Patch17:        tlsdesc_test.patch
# never to be upstreamed
Patch54:        n_drirc-disable-rgb10-for-chromium-on-amd.patch
Patch100:       U_fix-mpeg1_2-decode-mesa-20.2.patch
%ifnarch s390x
Patch500:       u_dep_xcb.patch
%else
Patch500:       u_dep_xcb-s390x.patch
%endif
%ifnarch s390x
Patch700:       u_meson-lower-python-version-requirement.patch
Patch800:       u_d3d12.patch
%endif
%ifarch s390x
Patch1222040:   u_mesa-CVE-2023-45913-s390x.patch
%endif
Patch1222041:   u_mesa-CVE-2023-45919.patch
Patch1222042:   u_mesa-CVE-2023-45922.patch

%ifarch %{ix86} x86_64
BuildRequires:  DirectX-Headers >= 1.613.0
%endif
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc%{?gcc_version} >= 9
BuildRequires:  gcc%{?gcc_version}-c++ >= 9
BuildRequires:  glslang-devel
BuildRequires:  imake
BuildRequires:  libtool
BuildRequires:  memory-constraints
BuildRequires:  meson >= 1.4.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base
# dataclasses is in standard library of python >= 3.7
%if 0%{?suse_version} < 1550
BuildRequires:  python3-dataclasses
%endif
BuildRequires:  python3-Mako
BuildRequires:  python3-PyYAML
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(dri3proto)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(libdrm) >= 2.4.109
BuildRequires:  pkgconfig(libdrm_amdgpu) >= 2.4.121
BuildRequires:  pkgconfig(libdrm_nouveau) >= 2.4.66
BuildRequires:  pkgconfig(libdrm_radeon) >= 2.4.71
BuildRequires:  pkgconfig(libglvnd) >= 1.3.2
%ifarch aarch64 x86_64 ppc64le s390x riscv64
BuildRequires:  pkgconfig(valgrind)
%endif
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(presentproto)
%if "%{flavor}" == "drivers"
%ifarch %{ix86} x86_64
BuildRequires:  pkgconfig(vulkan)
%endif
%endif
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xshmfence)
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
Provides:       libXvMC_nouveau = %{version}
Obsoletes:      libXvMC_nouveau < %{version}
Provides:       libXvMC_r600 = %{version}
Obsoletes:      libXvMC_r600 < %{version}
Provides:       libtxc_dxtn = %{version}
Obsoletes:      libtxc_dxtn < %{version}
Obsoletes:      libxatracker2 < %{version}
Obsoletes:      Mesa-gallium < %{version}
Obsoletes:      Mesa-libd3d < %{version}
Obsoletes:      Mesa-libOpenCL < %{version}
Obsoletes:      libvdpau_nouveau < %{version}
Obsoletes:      libvdpau_r600 < %{version}
Obsoletes:      libvdpau_radeonsi < %{version}
Obsoletes:      libvdpau_virtio_gpu < %{version}
Obsoletes:      libvdpau_d3d12 < %{version}
%ifarch %{arm} aarch64
%if 0%{?suse_version} >= 1550
BuildRequires:  python3-pycparser >= 2.20
BuildRequires:  pkgconfig(libdrm_etnaviv) >= 2.4.89
%endif
BuildRequires:  pkgconfig(libdrm_freedreno) >= 2.4.74
BuildRequires:  pkgconfig(libelf)
%endif
%ifarch x86_64 %{ix86} aarch64 %{arm} riscv64
BuildRequires:  libelf-devel
BuildRequires:  pkgconfig(libdrm_intel) >= 2.4.75
%else
%if 0%{with_opencl}
BuildRequires:  libelf-devel
%endif
%endif
# Requirements for wayland bumped up from 17.0
BuildRequires:  pkgconfig(wayland-client) >= 1.18
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(wayland-server) >= 1.18
%if 0%{with_llvm}
%if 0%{?suse_version} >= 1550
BuildRequires:  llvm-devel
%else
%if 0%{?sle_version} >= 150600
BuildRequires:  llvm21-devel
%endif
%endif
%endif

%if 0%{with_opencl}
%if 0%{?suse_version} >= 1550
BuildRequires:  clang-devel
%else
%if 0%{?sle_version} >= 150600
BuildRequires:  clang21-devel
%endif
%endif
BuildRequires:  libclc
BuildRequires:  pkgconfig(LLVMSPIRVLib)
BuildRequires:  pkgconfig(SPIRV-Tools)
# For NVK or libvulkan_nouveau.so
# Rust Cbindgen >=0.25 is required
# but it's only available on tumbleweed
%if 0%{?suse_version} > 1600
BuildRequires:  rust-cbindgen >= 0.25
%endif
%if 0%{with_rusticl}
BuildRequires:  rust
BuildRequires:  rust-bindgen >= 0.71.1
%endif
%endif

Requires:       Mesa-libEGL1 = %{version}
Requires:       Mesa-libGL1 = %{version}
Requires:       libglvnd >= 0.1.0

# This dependency on Mesa-dri is here to make sure users that
# do not install recommends on their system still get working Mesa. It is
# ignored in obs when Mesa is installed as build dependency.
Requires:       Mesa-dri = %{version}

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
%ifarch s390x
Requires:       Mesa-libglapi-devel = %{version}
%endif
Requires:       libgbm-devel = %{version}
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
Obsoletes:      libxatracker-devel < %{version}
Obsoletes:      Mesa-libd3d-devel < %{version}

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
Requires:       pkgconfig(x11)

%description libGL-devel
Mesa is a software library for 3D computer graphics that provides a
generic OpenGL implementation for rendering three-dimensional
graphics.

This package includes headers and static libraries for compiling
programs with Mesa.

%package libGLESv1_CM-devel
Summary:        Development files for the OpenGL ES 1.x Common Profile API
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
using the OpenGL|ES 1.x Common Profile APIs.

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
%if 0%{with_vulkan}
Requires:       libvulkan1
Requires:       libvulkan_lvp
%endif
Supplements:    Mesa
# merged into libgallium in 25.0.0
%ifnarch s390x
Obsoletes:      Mesa-libglapi0 < 25.0.0
%endif

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

%package -n Mesa-libRusticlOpenCL
Summary:        Mesa OpenCL implementation (Rusticl)
Group:          System/Libraries
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
Requires:       libclc(llvm%{_llvm_sonum})
%else
Requires:       libclc
%endif

%description -n Mesa-libRusticlOpenCL
This package contains the Mesa Rust-written OpenCL implementation.

%package -n Mesa-libva
Summary:        Mesa VA-API implementation
Group:          System/Libraries
Supplements:    Mesa

%description -n Mesa-libva
This package contains the Mesa VA-API implementation provided through gallium.

%package -n libvulkan_intel
Summary:        Mesa vulkan driver for Intel GPU
Group:          System/Libraries
Supplements:    modalias(pci:v00008086d*sv*sd*bc03sc*i*)
Requires:       Mesa-vulkan-device-select = %{version}
# get rid of this package, which is no longer neeeded at all
Provides:       Mesa-libVulkan-devel = 22.0.0
Obsoletes:      Mesa-libVulkan-devel < 22.0.0

%description -n libvulkan_intel
This package contains the Vulkan parts for Mesa.

# Only available on Tumbleweed because of rust-cbindgen >= 1.25 requirement
%if 0%{?suse_version} > 1600
%package -n libvulkan_nouveau
Summary:        Mesa vulkan driver for NVK (Nouveau Vulkan)
Group:          System/Libraries
Requires:       Mesa-vulkan-device-select = %{version}

%description -n libvulkan_nouveau
This package contains the Vulkan parts for Mesa.
%endif

%ifarch %{ix86} x86_64
%if 0%{?suse_version} > 1600
%package -n libvulkan_dzn
Summary:        Mesa vulkan driver for dzn (D3D12)
Group:          System/Libraries
Requires:       Mesa-vulkan-device-select = %{version}

%description -n libvulkan_dzn
This package contains the Vulkan parts for Mesa.
%endif
%endif

%package -n libvulkan_radeon
Summary:        Mesa vulkan driver for AMD GPU
Group:          System/Libraries
Supplements:    modalias(pci:v00001002d*sv*sd*bc03sc*i*)
Requires:       Mesa-vulkan-device-select = %{version}

%description -n libvulkan_radeon
This package contains the Vulkan parts for Mesa.

%package -n libvulkan_lvp
Summary:        Mesa vulkan driver for LVP
Group:          System/Libraries
Requires:       Mesa-vulkan-device-select = %{version}

%description -n libvulkan_lvp
This package contains the Vulkan parts for Mesa.

%ifarch %{arm} aarch64
%package -n libvulkan_broadcom
Summary:        Mesa vulkan driver for Broadcom
Group:          System/Libraries

%description -n libvulkan_broadcom
This package contains the Vulkan parts for Mesa.

%package -n libvulkan_freedreno
Summary:        Mesa vulkan driver for Freedreno
Group:          System/Libraries

%description -n libvulkan_freedreno
This package contains the Vulkan parts for Mesa.

%package -n libvulkan_panfrost
Summary:        Mesa vulkan driver for ARM Mali
Group:          System/Libraries

%description -n libvulkan_panfrost
This package contains the Vulkan parts for Mesa.
%endif

%package -n Mesa-vulkan-device-select
Summary:        Vulkan layer to select Vulkan devices provided by Mesa
Group:          System/Libraries

%description -n Mesa-vulkan-device-select
This package contains the VK_MESA_device_select Vulkan layer

%package -n Mesa-vulkan-overlay
Summary:        Mesa Vulkan Overlay layer
Group:          System/Libraries

%description -n Mesa-vulkan-overlay
This package contains the VK_MESA_Overlay Vulkan layer

%prep
%setup -q -n %{_name_archive}-%{_version} -b9
# remove some docs
rm -rf docs/README.{VMS,WIN32,OS2}

# Rust crates to subprojects
mkdir -p subprojects/packagecache
cp %{SOURCE2} subprojects/packagecache/
cp %{SOURCE3} subprojects/packagecache/
cp %{SOURCE4} subprojects/packagecache/
cp %{SOURCE5} subprojects/packagecache/
cp %{SOURCE6} subprojects/packagecache/
cp %{SOURCE22} subprojects/packagecache/

%patch -P 2 -p1
# fixes build against python 3.6
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 17 -p1
# no longer needed since gstreamer-plugins-vaapi 1.18.4
%if 0%{?suse_version} < 1550
%patch -P 54 -p1
%endif
%patch -P 100 -p1
%patch -P 500 -p1
%ifnarch s390x
%patch -P 700 -p1
%patch -P 800 -p1
%endif
%ifarch s390x
%patch -P 1222040 -p1
%endif
%patch -P 1222041 -p1
%patch -P 1222042 -p1
# Remove requires to vulkan libs from baselibs.conf on platforms
# where vulkan build is disabled; ugly ...
%if 0%{?with_vulkan} == 0
grep -v -i vulkan "%{_sourcedir}/baselibs.conf" >"%{_sourcedir}/temp" && \
  mv "%{_sourcedir}/temp" "%{_sourcedir}/baselibs.conf"
%endif

%build
# try to avoid OOM on ppc64 (boo#1194739)
%ifarch ppc64 ppc64le
%limit_build -m 1024
%endif
export CC=gcc-%{gcc_version}
export CXX=g++-%{gcc_version}

egl_platforms=x11,wayland

# needed to fix build of Mesa 23.1
# Mesa-drivers: -Dshader-cache=enabled
# Mesa: -Dxlib-lease=enabled
# recommended for both Mesa and Mesa-drivers to avoid some scary messages when
# comparing fds: -Dallow-kcmp=enabled
# Credits for figuring this out go to "llyyr" <llyyr.public@gmail.com>

%meson \
            --auto-features=disabled \
%if "%{flavor}" == "drivers"
            -Dglx=disabled \
            -Dxmlconfig=enabled \
            -Dexpat=enabled \
            -Dshader-cache=enabled \
%ifnarch s390x
            -Dspirv-tools=enabled \
%endif
%else
            -Dglx=auto \
            -Dllvm=disabled \
            -Dvulkan-drivers= \
%endif
            -Dxlib-lease=enabled \
            -Dglvnd=enabled \
            -Dgles1=enabled \
            -Dgles2=enabled \
            -Degl=enabled \
            -Dallow-kcmp=enabled \
            -Dplatforms=$egl_platforms \
%ifarch s390x
            -Dshared-glapi=enabled \
%endif
%if %{glamor}
            -Dgbm=enabled \
%endif
%if 0%{with_opencl}
%if 0%{?suse_version} >= 1550
            --sysconfdir=%{_datadir} \
%endif
%if 0%{with_rusticl}
            -Dgallium-rusticl=true \
            -Drust_std=2021 \
%endif
%endif
%if 0%{with_llvm}
            -Dllvm=enabled \
            -Dshared-llvm=enabled \
%endif
%if "%{flavor}" == "drivers"
%if %{video_codecs}
            -Dvideo-codecs=all \
%endif
%if %{gallium_loader}
            -Dgallium-va=enabled \
%endif
%if 0%{with_vulkan}
            -Dvulkan-drivers=%{?vulkan_drivers} \
            -Dvulkan-layers=device-select,overlay \
            -Dvulkan-beta=true \
%else
            -Dvulkan-drivers= \
%endif
  %ifarch %{ix86} x86_64
            -Dgallium-drivers=r300,r600,radeonsi,nouveau,softpipe,llvmpipe,svga,virgl,iris,crocus,i915,d3d12,zink \
            -Dgallium-d3d12-graphics=enabled \
          %ifarch x86_64
            -Dintel-rt=enabled \
          %endif
  %else
  %ifarch %{arm} aarch64
%if 0%{?suse_version} >= 1550
            -Dgallium-drivers=r300,r600,radeonsi,nouveau,softpipe,llvmpipe,virgl,iris,freedreno,vc4,etnaviv,lima,panfrost,v3d,svga,tegra,zink \
%else
            -Dgallium-drivers=r300,r600,radeonsi,nouveau,softpipe,llvmpipe,virgl,iris,freedreno,vc4,lima,panfrost,v3d,svga,tegra,zink \
%endif
  %else
  %ifarch loongarch64 ppc64 ppc64le riscv64
            -Dgallium-drivers=r300,r600,radeonsi,nouveau,softpipe,llvmpipe,virgl,iris,zink \
  %else
            -Dgallium-drivers=swrast \
  %endif
  %endif
  %endif
%ifarch riscv64
            -Dllvm-orcjit=true \
%endif
%else
%ifnarch s390x
            -Dgallium-drivers=softpipe \
%else
            -Dgallium-drivers=swrast \
%endif
%endif
%ifarch aarch64 x86_64 ppc64le s390x riscv64
            -Dvalgrind=enabled \
%endif
            -Db_ndebug=true \
            -Dc_args="%{optflags}" \
%ifarch %ix86
            -Dcpp_args="$(echo %{optflags}|sed 's/-flto=auto//')"
%else
            -Dcpp_args="%{optflags}"
%endif

%meson_build

%install
export MESON_PACKAGE_CACHE_DIR="%{_sourcedir}"
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

# libwayland-egl is provided by wayland itself
rm -fv %{buildroot}/%{_libdir}/libwayland-egl.so* \
	%{buildroot}/%{_libdir}/pkgconfig/wayland-egl.pc

%if "%{flavor}" == "drivers"
# Delete things that we do not package in the Mesa-drivers variant, but can
# not disable from buildling and installing.

# in libvulkan_dzn
%ifarch %{ix86} x86_64
%if 0%{?suse_version} > 1600
rm -fv %{buildroot}/%{_libdir}/libspirv_to_dxil.a
%endif
%endif

rm -fv %{buildroot}/%{_libdir}/libEGL.so*
# in Mesa-libEGL-devel
rm -v %{buildroot}/%{_includedir}/EGL/egl.h \
	%{buildroot}/%{_includedir}/EGL/eglext.h \
	%{buildroot}/%{_includedir}/EGL/eglext_angle.h \
	%{buildroot}/%{_includedir}/EGL/eglmesaext.h \
	%{buildroot}/%{_includedir}/EGL/eglplatform.h

# in Mesa-libGL-devel
rm -Rfv %{buildroot}/%{_includedir}/GL

#in Mesa-libGLESv1_CM-devel
rm -Rfv %{buildroot}/%{_includedir}/GLES

#in Mesa-libGLESv2-devel
rm -Rfv %{buildroot}/%{_includedir}/GLES2

#in Mesa-libGLESv3-devel
rm -Rfv %{buildroot}/%{_includedir}/GLES3

#in Mesa-libEGL1
rm -Rfv %{buildroot}/%{_libdir}/libEGL_mesa.so* \
	%{buildroot}/%{_datadir}/glvnd

# in Mesa-libglapi0
%ifarch s390x
rm -v %{buildroot}/%{_libdir}/libglapi.so*
%endif

# in libwayland-egl1
rm -fv %{buildroot}/%{_libdir}/libwayland-egl.so* \
	%{buildroot}/%{_libdir}/pkgconfig/wayland-egl.pc

# in Mesa-dri-devel
rm -v %{buildroot}/%{_libdir}/pkgconfig/dri.pc

# in KHR-devel
rm -Rfv %{buildroot}/%{_includedir}/KHR

# in libgbm-devel
rm -fv %{buildroot}%{_includedir}/gbm.h \
%ifnarch s390x
	%{buildroot}%{_includedir}/gbm_backend_abi.h \
%endif
	%{buildroot}%{_libdir}/libgbm.so* \
	%{buildroot}%{_libdir}/pkgconfig/gbm.pc

%else

# package in Mesa-dri
rm -Rfv %{buildroot}/%{_datadir}/drirc.d

rm -Rfv %{buildroot}/%{_libdir}/dri/*_dri.so \
	%{buildroot}%{_libdir}/libgallium-*.so \
	%{buildroot}%{_libdir}/gbm/ \
	%{buildroot}%{_libdir}/libGLES*
# glvnd needs a default provider for indirect rendering where it cannot
# determine the vendor
ln -sv %{_libdir}/libGLX_mesa.so.0 %{buildroot}%{_libdir}/libGLX_indirect.so.0

# pickup pkgconfig files from libglvnd build
for i in gl egl glesv1_cm glesv2; do
	rm -fv "%{buildroot}/%{_libdir}/pkgconfig/$i.pc"
	install -vm 0644 "%{_docdir}/libglvnd/pkgconfig/$i.pc" \
		%{buildroot}/%{_libdir}/pkgconfig/
done

for dir in GL/gl GL/glx; do
 cd "../xc/doc/man/$dir"
   xmkmf -a
   %make_build V=1
   make install.man DESTDIR=%{buildroot} MANPATH=%{_mandir} LIBMANSUFFIX=3gl
 cd -
done
%endif

%fdupes -s %{buildroot}/%{_mandir}

%if "%{flavor}" != "drivers"
# Use dummy README file that can be included in both Mesa and Mesa-32bit. This way Mesa-32bit will be build (otherwise it would be skipped as empty) and it can be used by the other *-32bit packages.
echo "The \"Mesa\" package does not have the ability to render, but is supplemented by \"Mesa-dri\" which contains the drivers for rendering" > docs/README.package.%{_arch}
%endif

%ldconfig_scriptlets
%ldconfig_scriptlets libEGL1
%ldconfig_scriptlets libGL1
%ldconfig_scriptlets -n libgbm1
%ldconfig_scriptlets libglapi0

%if "%{flavor}" != "drivers"
%files
%license docs/license.rst
%doc docs/README*

%files libEGL1
%{_libdir}/libEGL_mesa.so*
%dir %{_datadir}/glvnd
%dir %{_datadir}/glvnd/egl_vendor.d
%{_datadir}/glvnd/egl_vendor.d/50_mesa.json

%files libEGL-devel
%{_includedir}/EGL
%{_libdir}/pkgconfig/egl.pc

%files KHR-devel
%{_includedir}/KHR

%files libGL1
%{_libdir}/libGLX_mesa.so*
%{_libdir}/libGLX_indirect.so*

%files libGL-devel
%dir %{_includedir}/GL
%{_includedir}/GL/*.h
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

%files -n libgbm1
%{_libdir}/libgbm.so.1*

%files -n libgbm-devel
%{_includedir}/gbm.h
%ifnarch s390x
%{_includedir}/gbm_backend_abi.h
%endif
%{_libdir}/libgbm.so
%{_libdir}/pkgconfig/gbm.pc
%endif

%ifarch s390x
%if "%{flavor}" != "drivers"
%files libglapi0
%{_libdir}/libglapi.so.0*

%files libglapi-devel
%{_libdir}/libglapi.so
%endif
%endif

%if "%{flavor}" == "drivers"
%files -n Mesa-dri
%dir %{_datadir}/drirc.d
%config %{_datadir}/drirc.d/*
%dir %{_libdir}/dri
%{_libdir}/dri/*_dri.so
%ifarch %{ix86} x86_64 aarch64 %{arm} ppc64 ppc64le riscv64
%exclude %{_libdir}/dri/nouveau_dri.so
%endif
%ifarch %{arm} aarch64
%exclude %{_libdir}/dri/vc4_dri.so
%endif
%ifnarch s390x
%{_libdir}/libgallium-%{_version}.so
%dir %{_libdir}/gbm/
%{_libdir}/gbm/dri_gbm.so
%endif

%ifarch %{ix86} x86_64 aarch64 %{arm} loongarch64 ppc64 ppc64le riscv64
%files -n Mesa-dri-nouveau
%{_libdir}/dri/nouveau_dri.so
%endif

%ifarch aarch64 %{arm}
%files -n Mesa-dri-vc4
%{_libdir}/dri/vc4_dri.so
%endif

# drivers
%endif

%if "%{flavor}" != "drivers"
%files dri-devel
%{_includedir}/GL/internal
%{_libdir}/pkgconfig/dri.pc

%files devel
%doc docs/*.rst

# !drivers
%endif

%if 0%{with_rusticl}
%files -n Mesa-libRusticlOpenCL
%if 0%{?suse_version} >= 1550
%dir %{_datadir}/OpenCL
%dir %{_datadir}/OpenCL/vendors
%{_datadir}/OpenCL/vendors/rusticl.icd
%else
%dir %{_sysconfdir}/OpenCL
%dir %{_sysconfdir}/OpenCL/vendors
%{_sysconfdir}/OpenCL/vendors/rusticl.icd
%endif
%{_libdir}/libRusticlOpenCL.so*
%endif

%if "%{flavor}" == "drivers"
%ifarch %{ix86} x86_64 aarch64 %{arm} loongarch64 ppc64 ppc64le riscv64
%files -n Mesa-libva
%{_libdir}/dri/*_drv_video.so
%endif
%endif

%if 0%{with_vulkan}
%ifarch %{ix86} x86_64 aarch64 %{arm} loongarch64 riscv64
%files -n libvulkan_intel
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/intel_icd.*.json
%{_libdir}/libvulkan_intel.so
%{_datadir}/vulkan/icd.d/intel_hasvk_icd.*.json
%{_libdir}/libvulkan_intel_hasvk.so
%endif

%ifarch %{ix86} x86_64 aarch64 %{arm} loongarch64
# Only available on Tumbleweed because of rust-cbindgen >= 1.25 requirement
%if 0%{?suse_version} > 1600
%files -n libvulkan_nouveau
%{_libdir}/libvulkan_nouveau.so
%{_datadir}/vulkan/icd.d/nouveau_icd.*.json
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%endif
%endif

%ifarch %{ix86} x86_64
%if 0%{?suse_version} > 1600
%files -n libvulkan_dzn
%{_libdir}/libvulkan_dzn.so
%{_libdir}/libspirv_to_dxil.so
%{_bindir}/spirv2dxil
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/dzn_icd.*.json
%endif
%endif

%files -n libvulkan_radeon
%{_libdir}/libvulkan_radeon.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/radeon_icd.*.json

%files -n libvulkan_lvp
%{_libdir}/libvulkan_lvp.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/lvp_icd.*.json

%ifarch %{arm} aarch64
%files -n libvulkan_broadcom
%{_libdir}/libvulkan_broadcom.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/broadcom_icd.*.json

%files -n libvulkan_freedreno
%{_libdir}/libvulkan_freedreno.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/freedreno_icd.*.json

%files -n libvulkan_panfrost
%{_libdir}/libvulkan_panfrost.so
%dir %{_datadir}/vulkan
%dir %{_datadir}/vulkan/icd.d
%{_datadir}/vulkan/icd.d/panfrost_icd.*.json
%endif

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
