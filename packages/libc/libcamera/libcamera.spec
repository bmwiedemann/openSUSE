#
# spec file for package libcamera
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


%define lname       libcamera0_0_3
%define lname_base  libcamera-base0_0_3
Name:           libcamera
Version:        0.0.3
Release:        0
Summary:        A complex camera support library in C++
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libcamera.org/

Source:         %name-%version.tar.xz
Source1:        baselibs.conf

BuildRequires:  boost-devel
BuildRequires:  c++_compiler
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc9
BuildRequires:  gcc9-c++
%endif
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  meson >= 0.56
BuildRequires:  pkgconfig
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
BuildRequires:  pkgconfig(yaml-0.1)

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

"cam" is a command-line utility to interact with cameras. The initial state is
limited and only supports listing cameras in the system and selecting a camera
to interact with.

%package -n gstreamer-plugins-libcamera
Summary:        GStreamer plugins from libcamera
Group:          Productivity/Multimedia/Other

%description -n gstreamer-plugins-libcamera
libcamera is an experimental camera user-space API.
This is its integration plugin for gstreamer.

%prep
%autosetup -p1

%build
%if %{pkg_vcmp gcc < 8}
export CC=gcc-9
export CXX=g++-9
%endif
%meson \
  -Ddocumentation=disabled \
  -Dqcam=enabled \
  -Dv4l2=false -Dtracing=disabled \
  -Dpipelines=ipu3,rkisp1,simple,uvcvideo,vimc \
  -Dlc-compliance=disabled
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %lname
%ldconfig_scriptlets -n %lname_base

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
%_bindir/cam
%_bindir/qcam
%_libexecdir/libcamera/
%_libdir/libcamera/
%_datadir/libcamera/

%files -n gstreamer-plugins-libcamera
%_libdir/gstreamer-1.0/

%changelog
