#
# spec file for package gstreamer-plugins-vaapi
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


%define gst_branch 1.0
Name:           gstreamer-plugins-vaapi
Version:        1.18.0
Release:        0
Summary:        Gstreamer VA-API plugins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz
BuildRequires:  Mesa-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  gtk-doc
BuildRequires:  hotdoc
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  vaapi-wayland-tools
BuildRequires:  yasm
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-codecparsers-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva) >= 0.30.4
BuildRequires:  pkgconfig(libva-drm) >= 0.33.0
BuildRequires:  pkgconfig(libva-glx)
BuildRequires:  pkgconfig(libva-wayland)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(wayland-client) >= 1.0.2
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
ExclusiveArch:  %{ix86} x86_64

%description
gstreamer-vaapi is a collection of GStreamer plugins and helper libraries that allow hardware accelerated video decoding through VA-API.

%package doc
Summary:        Documentation for gstreamer-plugins-vaapi
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
This package contains documentation for gstreamer-plugins-vaapi.

%prep
%autosetup -n gstreamer-vaapi-%{version} -p1

%build
%meson \
	-Dwith_egl=yes \
	-Dwith_encoders=yes \
	-Dwith_drm=yes \
	-Dwith_glx=yes \
	-Dwith_wayland=yes \
	-Dwith_x11=yes \
	-Dexamples=disabled \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING.LIB
%{_libdir}/gstreamer-%{gst_branch}/libgstvaapi.so

%files doc
%doc AUTHORS NEWS README

%changelog
