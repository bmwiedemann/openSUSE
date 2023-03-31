#
# spec file for package Mesa-demo
#
# Copyright (c) 2023 SUSE LLC
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
BuildRequires:  glew-devel
BuildRequires:  glslang-devel
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vulkan-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(osmesa)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
Requires:       Mesa-demo-egl = %{version}
Requires:       Mesa-demo-es = %{version}
Requires:       Mesa-demo-x = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

This package contains the demos shipped with Mesa.

* OpenGL is a trademark of Silicon Graphics Incorporated.

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
%setup -q -n mesa-demos-%{version} -b0

%build
%{meson} \
  -Dgles1=enabled \
  -Dgles2=enabled \
  -Dosmesa=enabled \
  -Dlibdrm=enabled \
  -Dwayland=disabled \
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
%defattr(-,root,root)
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
# conflict with line of util-linux
%exclude %{_bindir}/line

%files x
%defattr(-,root,root)
%{_bindir}/glxgears
%{_bindir}/glxinfo
%{_bindir}/pbinfo
%ifarch %ix86
%dir %{_libdir}/mesa-demos
%dir %{_libdir}/mesa-demos/xdemos
%{_libdir}/mesa-demos/xdemos/*
%endif

%files es
%defattr(-,root,root)
%{_bindir}/es2_info
%{_bindir}/es2gears_x11
%{_bindir}/es2tri
%ifarch %ix86
%dir %{_libdir}/mesa-demos/
%dir %{_libdir}/mesa-demos/egl
%dir %{_libdir}/mesa-demos/egl/opengles2
%{_libdir}/mesa-demos/egl/opengles2/*
%endif

%files egl
%defattr(-,root,root)
%{_bindir}/eglgears_x11
%{_bindir}/eglinfo
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
