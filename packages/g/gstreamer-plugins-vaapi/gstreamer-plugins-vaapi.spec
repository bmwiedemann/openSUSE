#
# spec file for package gstreamer-plugins-vaapi
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


%define gst_branch 1.0

Name:           gstreamer-plugins-vaapi
Version:        1.24.5
Release:        0
Summary:        Gstreamer VA-API plugins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/gstreamer-vaapi/gstreamer-vaapi-%{version}.tar.xz

BuildRequires:  Mesa-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  meson >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  vaapi-wayland-tools
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
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
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
ExclusiveArch:  %{ix86} x86_64 aarch64

%description
gstreamer-vaapi is a collection of GStreamer plugins and helper
libraries that allow hardware accelerated video decoding through
VA-API.

%prep
%autosetup -n gstreamer-vaapi-%{version} -p1

%build
%meson \
	-Dpackage-origin='http://download.opensuse.org' \
	-Ddoc=disabled \
	-Degl=enabled \
	-Dencoders=enabled \
	-Ddrm=enabled \
	-Dglx=enabled \
	-Dwayland=enabled \
	-Dx11=enabled \
	-Dexamples=disabled \
	-Dtests=disabled \
	%{nil}
%meson_build

%install
%meson_install

%files
%license COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/gstreamer-%{gst_branch}/libgstvaapi.so

%changelog
