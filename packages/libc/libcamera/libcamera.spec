#
# spec file for package libcamera
#
# Copyright (c) 2024 SUSE LLC
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


%define lname       libcamera0_4
%define lname_base  libcamera-base0_4
%if "@BUILD_FLAVOR@" != ""
%define extname -@BUILD_FLAVOR@
%else
%define extname %nil
%endif
Name:           libcamera%extname
Version:        0.4.0
Release:        0
Summary:        A complex camera support library in C++
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND CC-BY-SA-4.0
Group:          Development/Libraries/C and C++
URL:            https://libcamera.org/
#Git-Web:       https://git.libcamera.org/libcamera/libcamera.git/

Source:         libcamera-%version.tar.xz
Source1:        baselibs.conf

BuildRequires:  boost-devel
BuildRequires:  c++_compiler
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%endif
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  meson >= 0.56
BuildRequires:  pkg-config
BuildRequires:  python3-Jinja2
BuildRequires:  python3-PyYAML
BuildRequires:  python3-ply
BuildRequires:  xz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(pybind11)
BuildRequires:  pkgconfig(yaml-0.1)
%if "@BUILD_FLAVOR@" != ""
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6OpenGLWidgets)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(sdl2)
%endif

%description
libcamera is an experimental camera user-space API.

A camera may consist of multiple sensors or function blocks, and can
expose multiple kernel device nodes in /dev for different stages of
the pipeline. The libcamera API groups and exposes these pieces as
what users consider one "camera".

%package -n %lname
Summary:        A complex camera support library in C++
Group:          System/Libraries

%description -n %lname
libcamera is an experimental camera user-space API.

A camera may consist of multiple sensors or function blocks, and can
expose multiple kernel device nodes in /dev for different stages of
the pipeline. The libcamera API groups and exposes these pieces as
what users consider one "camera".

%package -n %lname_base
Summary:        A complex camera support library in C++
Group:          System/Libraries

%description -n %lname_base
libcamera is an experimental camera user-space API.

A camera may consist of multiple sensors or function blocks, and can
expose multiple kernel device nodes in /dev for different stages of
the pipeline. The libcamera API groups and exposes these pieces as
what users consider one "camera".

%package devel
Summary:        Development for libcamera, a camera support library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       %lname_base = %version

%description devel
libcamera is an experimental camera user-space API.

This subpackage contains the header files.

%package tools
Summary:        Command-line utilities from libcamera
Group:          Development/Tools/Other

%description tools
libcamera is an experimental camera user-space API.

%package -n libcamera-cam
Summary:        Command-line interfaces for libcamera
Group:          Development/Tools/Other
# Heavy runtime deps (SDL, Qt6)

%description -n libcamera-cam
libcamera is an experimental camera user-space API.

"cam" is a command-line utility to interact with cameras. The initial state is
limited and only supports listing cameras in the system and selecting a camera
to interact with.

%package -n gstreamer-plugins-libcamera
Summary:        GStreamer plugins from libcamera
Group:          Productivity/Multimedia/Other

%description -n gstreamer-plugins-libcamera
libcamera is an experimental camera user-space API.
This is its integration plugin for gstreamer.

%package -n python3-libcamera
Summary:        Python bindings for libcamera
Group:          Development/Languages/Python

%description -n python3-libcamera
Python bindings for libcamera.

%prep
%autosetup -p1 -n libcamera-%version

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-11
export CXX=g++-11
%endif
%meson \
  -Ddocumentation=disabled \
%if "@BUILD_FLAVOR@" != ""
  -Dqcam=enabled \
%else
  -Dqcam=disabled \
%endif
  -Dv4l2=false -Dtracing=disabled \
  -Dpipelines=ipu3,rkisp1,simple,uvcvideo,vimc \
  -Dlc-compliance=disabled
%meson_build

%install
%meson_install
pushd "%buildroot"
%if "@BUILD_FLAVOR@" != ""
find . ! -type d ! -path ./usr/bin/cam ! -path ./usr/bin/qcam -print -delete
%else
rm -v usr/bin/cam
%endif
popd

%ldconfig_scriptlets -n %lname
%ldconfig_scriptlets -n %lname_base

%if "@BUILD_FLAVOR@" == ""
%files -n %lname
%_libdir/libcamera.so.*

%files -n %lname_base
%_libdir/libcamera-base.so.*

%files devel
%license LICENSES/*GPL*
%_includedir/libcamera/
%_libdir/libcamera-base.so
%_libdir/libcamera.so
%_libdir/pkgconfig/*.pc

%files tools
%_libexecdir/libcamera/
%_libdir/libcamera/
%_datadir/libcamera/

%files -n gstreamer-plugins-libcamera
%_libdir/gstreamer-1.0/

%files -n python3-libcamera
%python3_sitearch/*

%else

%files -n libcamera-cam
%_bindir/cam
%_bindir/qcam

%endif

%changelog
