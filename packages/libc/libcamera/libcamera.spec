#
# spec file for package libcamera
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


Name:           libcamera
%define lname   libcamera-suse2
Version:        0~1118.4de31cc
Release:        0
Summary:        A complex camera support library in C++
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://libcamera.org/

Source:         %name-%version.tar.xz
Patch1:         vers.diff
Patch2:         noforcedsize.diff
BuildRequires:  c++_compiler
BuildRequires:  meson >= 0.47
BuildRequires:  pkg-config
BuildRequires:  python3-PyYAML
BuildRequires:  xz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(libudev)

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
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# Together with patch1, this makes for the "-release" feature from libtool
mv "%buildroot/%_libdir/libcamera-suse.so" "%buildroot/%_libdir/libcamera.so"
perl -i -pe 's{-lcamera-suse}{-lcamera}' "%buildroot/%_libdir/pkgconfig"/*.pc

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libcamera*.so.*

%files devel
%license licenses/*gpl*
%_includedir/libcamera/
%_libdir/libcamera.so
%_libdir/pkgconfig/*.pc

%files tools
%_bindir/cam
%_libexecdir/libcamera/
%_libdir/libcamera/

%files -n gstreamer-plugins-libcamera
%_libdir/gstreamer-1.0/

%changelog
