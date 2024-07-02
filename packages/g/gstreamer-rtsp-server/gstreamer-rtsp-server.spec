#
# spec file for package gstreamer-rtsp-server
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


%define gstreamer_req_version %(echo %{version} | sed -e "s/+.*//")
%define _name gst-rtsp-server

Name:           gstreamer-rtsp-server
Version:        1.24.5
Release:        0
Summary:        GStreamer-based RTSP server library
License:        LGPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/gst-rtsp-server/%{_name}-%{version}.tar.xz
Source99:       gstreamer-rtsp-server-rpmlintrc

BuildRequires:  meson >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.31.1
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-net-1.0)
BuildRequires:  pkgconfig(gstreamer-rtp-1.0)
BuildRequires:  pkgconfig(gstreamer-rtsp-1.0)
BuildRequires:  pkgconfig(gstreamer-sdp-1.0)

%description
A library on top of GStreamer for building an RTSP server.

%package  -n libgstrtspserver-1_0-0
Summary:        GStreamer-based RTSP server library
Group:          System/Libraries

%description  -n libgstrtspserver-1_0-0
Library on top of GStreamer for building an RTSP server - Library files.

%package  -n typelib-1_0-GstRtspServer-1_0
Summary:        Introspection bindings for the GStreamer-based RTSP server library
Group:          System/Libraries

%description  -n typelib-1_0-GstRtspServer-1_0
Introspection bindings for the GStreamer library for building an RTSP server.

%package devel
Summary:        Development files for the GStreamer-based RTSP server library
Group:          Development/Languages/C and C++
Requires:       libgstrtspserver-1_0-0 = %{version}
Requires:       typelib-1_0-GstRtspServer-1_0 = %{version}
Provides:       gst-rtsp-server-devel = %{version}
Obsoletes:      gst-rtsp-server-devel < %{version}

%description devel
Development files for the GStreamer library for building an RTSP server.

%prep
%autosetup -n %{_name}-%{version} -p1

%build
%meson \
	-Dintrospection=enabled \
	-Dpackage-name='openSUSE GStreamer-rtsp-server package' \
	-Dpackage-origin='http://download.opensuse.org' \
	-Dtests=disabled \
	-Dexamples=disabled \
	-Ddoc=disabled \
	%{nil}
%meson_build

%install
%meson_install

%post -n libgstrtspserver-1_0-0 -p /sbin/ldconfig
%postun -n libgstrtspserver-1_0-0 -p /sbin/ldconfig

%files -n libgstrtspserver-1_0-0
%license COPYING
%{_libdir}/libgstrtspserver-1.0.so.*

%files -n typelib-1_0-GstRtspServer-1_0
%{_libdir}/girepository-1.0/GstRtspServer-1.0.typelib

%files devel
%doc ChangeLog README
%{_datadir}/gir-1.0/GstRtspServer-1.0.gir
%{_includedir}/gstreamer-1.0/gst/rtsp-server/
%{_libdir}/libgstrtspserver-1.0.so
%{_libdir}/gstreamer-1.0/libgstrtspclientsink.so
%{_libdir}/pkgconfig/gstreamer-rtsp-server-1.0.pc

%changelog
