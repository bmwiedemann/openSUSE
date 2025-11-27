#
# spec file for package Mesa-demo
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?sle_version} == 150600 && 0%{?is_opensuse}
%define meson_build /usr/bin/meson compile -C %{_vpath_builddir} %{_smp_mflags} --verbose
%define meson_install /usr/bin/meson install -C %{_vpath_builddir} --no-rebuild --destdir=%{buildroot}
%endif

Name:           Mesa-demo
Version:        9.0.0
Release:        0
Summary:        Mesa demo programs for the OpenGL stack
License:        MIT
Group:          Development/Tools/Other
URL:            https://www.mesa3d.org
Source0:        https://mesa.freedesktop.org/archive/demos/mesa-demos-%{version}.tar.xz
Source1:        https://mesa.freedesktop.org/archive/demos/mesa-demos-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libdecor-0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
Requires:       Mesa-demo-egl = %{version}
Requires:       Mesa-demo-es = %{version}
Requires:       Mesa-demo-x = %{version}

%description
Mesa is a 3-D graphics library with an API similar to OpenGL.
This package contains the demos shipped with Mesa.

%package x
Summary:        GLX-based demos
Group:          Development/Tools/Other

%description x
This package contains some common GLX-based demos.

%package es
Summary:        GLES-based demos
Group:          Development/Tools/Other
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengles2/es2_info
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengles2/es2gears_x11
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengles2/es2tri

%description es
This package contains some common GLES-based demos.

%package egl
Summary:        EGL-based demos
Group:          Development/Tools/Other
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengl/eglgears_x11
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengl/eglinfo
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengl/egltri_x11
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengl/peglgears
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengl/xeglgears
Provides:       Mesa-demo:%{_libdir}/mesa-demos/egl/opengl/xeglthreads

%description egl
This package contains some common EGL-based demos.

%prep
%autosetup -n mesa-demos-%{version} -b0

%build
%{meson} \
  -Dgles1=enabled \
  -Dgles2=enabled \
  -Dosmesa=disabled \
  -Dlibdrm=enabled \
  -Dwayland=enabled \
  -Dvulkan=enabled \
  %{nil}
%{meson_build}

%install
%{meson_install}
%ifarch %ix86
mkdir -p %{buildroot}%{_libdir}/mesa-demos/egl/{opengl,opengles2} \
         %{buildroot}%{_libdir}/mesa-demos/xdemos
cp -a %{buildroot}%{_bindir}/{eglgears_x11,eglinfo,egltri_x11,peglgears,xeglgears,xeglthreads} \
      %{buildroot}%{_libdir}/mesa-demos/egl/opengl
cp -a %{buildroot}%{_bindir}/{es2_info,es2gears_x11,es2tri} \
      %{buildroot}%{_libdir}/mesa-demos/egl/opengles2
cp -a %{buildroot}%{_bindir}/{glxgears,glxinfo,pbinfo} \
      %{buildroot}%{_libdir}/mesa-demos/xdemos
%endif

%files
%{_bindir}/*
%dir %{_datadir}/mesa-demos
%{_datadir}/mesa-demos/*
%exclude %{_bindir}/glxgears
%exclude %{_bindir}/glxinfo
%exclude %{_bindir}/pbinfo
%exclude %{_bindir}/es2_info
%exclude %{_bindir}/es2gears_x11
%exclude %{_bindir}/es2tri
%exclude %{_bindir}/eglgears_x11
%exclude %{_bindir}/eglinfo
%exclude %{_bindir}/egltri_x11
%exclude %{_bindir}/peglgears
%exclude %{_bindir}/xeglgears
%exclude %{_bindir}/xeglthreads
%exclude %{_bindir}/eglgears_wayland
%exclude %{_bindir}/egltri_wayland
%exclude %{_bindir}/es2gears_wayland
# conflict with line of util-linux
%exclude %{_bindir}/line
# conflict with bitmap of package bitmap
%exclude %{_bindir}/bitmap

%files x
%{_bindir}/glxgears
%{_bindir}/glxinfo
%{_bindir}/pbinfo
%ifarch %ix86
%dir %{_libdir}/mesa-demos
%dir %{_libdir}/mesa-demos/xdemos
%{_libdir}/mesa-demos/xdemos/*
%endif

%files es
%{_bindir}/es2_info
%{_bindir}/es2gears_wayland
%{_bindir}/es2gears_x11
%{_bindir}/es2tri
%ifarch %ix86
%dir %{_libdir}/mesa-demos/
%dir %{_libdir}/mesa-demos/egl
%dir %{_libdir}/mesa-demos/egl/opengles2
%{_libdir}/mesa-demos/egl/opengles2/*
%endif

%files egl
%{_bindir}/eglgears_wayland
%{_bindir}/eglgears_x11
%{_bindir}/eglinfo
%{_bindir}/egltri_wayland
%{_bindir}/egltri_x11
%{_bindir}/peglgears
%{_bindir}/xeglgears
%{_bindir}/xeglthreads
%ifarch %ix86
%dir %{_libdir}/mesa-demos
%dir %{_libdir}/mesa-demos/egl
%dir %{_libdir}/mesa-demos/egl/opengl
%{_libdir}/mesa-demos/egl/opengl/*
%endif

%changelog
