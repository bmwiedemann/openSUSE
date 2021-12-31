#
# spec file for package libcamera
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libcamera
%define lname   libcamera-suse7
Version:        0.0.0+g3076.d79b4120
Release:        0
Summary:        A complex camera support library in C++
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libcamera.org/

Source:         %name-%version.tar.xz
Source1:        baselibs.conf
Patch1:         vers.diff
Patch2:         fix-ppc64.patch
BuildRequires:  boost-devel
BuildRequires:  c++_compiler
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  meson >= 0.55
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

%package devel
Summary:        Development for libcamera, a camera support library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

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
%autosetup -p1 -N
%patch1 -p1
%ifarch ppc64 ppc64le
%patch2 -p1
%endif

%build
export CFLAGS="%optflags -Wno-error"
export CXXFLAGS="$CFLAGS"
%meson \
  -Ddocumentation=disabled \
  -Dqcam=enabled \
  -Dv4l2=false -Dtracing=disabled \
  -Dpipelines=ipu3,rkisp1,simple,uvcvideo,vimc \
  -Dlc-compliance=disabled
%meson_build

%install
%meson_install
# libtool's -release would be so much more direct, but alas, meson...
mv "%buildroot/%_libdir/libcamera-suse.so" "%buildroot/%_libdir/libcamera.so"
mv "%buildroot/%_libdir/libcamera-base-suse.so" "%buildroot/%_libdir/libcamera-base.so"
mv "%buildroot/%_libdir/pkgconfig/libcamera-suse.pc" "%buildroot/%_libdir/pkgconfig/libcamera.pc"
mv "%buildroot/%_libdir/pkgconfig/libcamera-base-suse.pc" "%buildroot/%_libdir/pkgconfig/libcamera-base.pc"
perl -i -pe 's{camera-suse}{camera}' "%buildroot/%_libdir/pkgconfig"/*.pc
perl -i -pe 's{camera-base-suse}{camera-base}' "%buildroot/%_libdir/pkgconfig"/*.pc

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libcamera*.so.*

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
