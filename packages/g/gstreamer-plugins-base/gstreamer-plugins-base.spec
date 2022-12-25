#
# spec file for package gstreamer-plugins-base
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


%define _name gst-plugins-base
%define gst_branch 1.0
%define gstreamer_req_version %(echo %{version} | sed -e "s/+.*//")
Name:           gstreamer-plugins-base
Version:        1.20.5
Release:        0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/%{_name}/%{_name}-%{version}.tar.xz
Source1:        gstreamer-plugins-base.appdata.xml
Source2:        baselibs.conf

Patch4:         add_wayland_dep_to_tests.patch
Patch5:         MR-221-video-anc-add-two-new-CEA-608-caption-formats.patch

BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  cdparanoia-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.40.0
BuildRequires:  gobject-introspection-devel >= 1.31.1
BuildRequires:  libICE-devel
BuildRequires:  libSM-devel
BuildRequires:  libXext-devel
BuildRequires:  libXv-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  meson >= 0.59
BuildRequires:  orc >= 0.4.24
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa) >= 0.9.1
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2) >= 2.0.9
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.40
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libdrm) >= 2.4.55
BuildRequires:  pkgconfig(libvisual-0.4) >= 0.4.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(ogg) >= 1.0
BuildRequires:  pkgconfig(opus) >= 0.9.4
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(pangocairo) >= 1.22.0
BuildRequires:  pkgconfig(theoradec) >= 1.1
BuildRequires:  pkgconfig(theoraenc) >= 1.1
BuildRequires:  pkgconfig(vorbis) >= 1.0
BuildRequires:  pkgconfig(vorbisenc) >= 1.0
BuildRequires:  pkgconfig(wayland-client) >= 1.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0
BuildRequires:  pkgconfig(wayland-egl) >= 1.0
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(zlib)
Requires:       gstreamer >= %{gstreamer_req_version}
Supplements:    gstreamer
Conflicts:      gstreamer-plugins-bad < 1.18.1
# Generic name, never used in SuSE:
Provides:       gst-plugins-base = %{version}
Obsoletes:      libgstbadvideo-1_0-0
Obsoletes:      typelib-1_0-GstFft-1_0 < 1.14.0
%if 0%{?suse_version} < 1550
BuildRequires:  pkgconfig(cairo)
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(graphene-1.0)
%endif

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstallocators-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstallocators-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstAllocators-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstAllocators-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstapp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstapp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstApp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstApp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstaudio-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstaudio-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstAudio-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstAudio-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstfft-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstfft-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstFft-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstFft-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstgl-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstgl-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstGL-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGL-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n typelib-1_0-GstGLEGL-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGLEGL-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n typelib-1_0-GstGLWayland-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGLWayland-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n typelib-1_0-GstGLX11-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstGLX11-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstpbutils-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstpbutils-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstPbutils-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstPbutils-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstriff-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstriff-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstrtp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstrtp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstRtp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstRtp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstrtsp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstrtsp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstRtsp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstRtsp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstsdp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstsdp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstSdp-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstSdp-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgsttag-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgsttag-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstTag-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstTag-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package -n libgstvideo-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
# We want to have base modules installed:
Group:          System/Libraries
Requires:       %{name}

%description -n libgstvideo-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstVideo-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstVideo-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

This package provides the GObject Introspection bindings for GStreamer
plug-ins.

%package devel
Summary:        Include files and librs mandatory for development with gstreamer-plugins-base
Group:          Development/Libraries/C and C++
Requires:       libgstallocators-1_0-0 = %{version}
Requires:       libgstapp-1_0-0 = %{version}
Requires:       libgstaudio-1_0-0 = %{version}
Requires:       libgstfft-1_0-0 = %{version}
Requires:       libgstgl-1_0-0 = %{version}
Requires:       libgstpbutils-1_0-0 = %{version}
Requires:       libgstriff-1_0-0 = %{version}
Requires:       libgstrtp-1_0-0 = %{version}
Requires:       libgstrtsp-1_0-0 = %{version}
Requires:       libgstsdp-1_0-0 = %{version}
Requires:       libgsttag-1_0-0 = %{version}
Requires:       libgstvideo-1_0-0 = %{version}
Requires:       typelib-1_0-GstAllocators-1_0 = %{version}
Requires:       typelib-1_0-GstApp-1_0 = %{version}
Requires:       typelib-1_0-GstAudio-1_0 = %{version}
Requires:       typelib-1_0-GstGL-1_0 = %{version}
Requires:       typelib-1_0-GstGLEGL-1_0 = %{version}
Requires:       typelib-1_0-GstGLWayland-1_0 = %{version}
Requires:       typelib-1_0-GstGLX11-1_0 = %{version}
Requires:       typelib-1_0-GstPbutils-1_0 = %{version}
Requires:       typelib-1_0-GstRtp-1_0 = %{version}
Requires:       typelib-1_0-GstRtsp-1_0 = %{version}
Requires:       typelib-1_0-GstSdp-1_0 = %{version}
Requires:       typelib-1_0-GstTag-1_0 = %{version}
Requires:       typelib-1_0-GstVideo-1_0 = %{version}
# Generic name, never used in SuSE:
Provides:       gst-plugins-base-devel = %{version}

%description devel
This package contains all necessary include files and libraries needed
to compile and link applications that use gstreamer-plugins-base.

%lang_package

%prep
%autosetup -n %{_name}-%{version} -N
%patch4 -p1
%patch5 -p1

%build
export PYTHON=%{_bindir}/python3
# TODO: tremor needs libvorbisidec
%meson \
	-Dpackage-name='openSUSE GStreamer-plugins-base package'\
	-Dpackage-origin='http://download.opensuse.org'\
	-Ddoc=disabled \
	-Dintrospection=enabled \
	-Dorc=enabled \
	-Dexamples=disabled \
	-Dtremor=disabled \
	%{nil}
%meson_build

%install
%meson_install
if [ -f %{buildroot}%{_datadir}/appdata/gstreamer-plugins-base.appdata.xml ]; then
  echo "Please remove the added gstreamer-plugins-base.appdata.xml file from the sources - the tarball installs it"
  false
else
  mkdir -p %{buildroot}%{_datadir}/appdata
  cp %{SOURCE1} %{buildroot}%{_datadir}/appdata/
fi

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}-%{gst_branch}

%ldconfig_scriptlets -n libgstallocators-1_0-0
%ldconfig_scriptlets -n libgstapp-1_0-0
%ldconfig_scriptlets -n libgstaudio-1_0-0
%ldconfig_scriptlets -n libgstfft-1_0-0
%ldconfig_scriptlets -n libgstgl-1_0-0
%ldconfig_scriptlets -n libgstpbutils-1_0-0
%ldconfig_scriptlets -n libgstriff-1_0-0
%ldconfig_scriptlets -n libgstrtp-1_0-0
%ldconfig_scriptlets -n libgstrtsp-1_0-0
%ldconfig_scriptlets -n libgstsdp-1_0-0
%ldconfig_scriptlets -n libgsttag-1_0-0
%ldconfig_scriptlets -n libgstvideo-1_0-0

%files
%license COPYING
%{_mandir}/man1/gst-device-monitor-*
%{_mandir}/man1/gst-discoverer-*
%{_mandir}/man1/gst-play-*
%{_bindir}/gst-device-monitor-%{gst_branch}
%{_bindir}/gst-discoverer-%{gst_branch}
%{_bindir}/gst-play-%{gst_branch}
%{_datadir}/appdata/gstreamer-plugins-base.appdata.xml
%{_libdir}/gstreamer-%{gst_branch}/libgstadder.so
%{_libdir}/gstreamer-%{gst_branch}/libgstalsa.so
%{_libdir}/gstreamer-%{gst_branch}/libgstapp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudioconvert.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudioresample.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiotestsrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiorate.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcdparanoia.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcompositor.so
%{_libdir}/gstreamer-%{gst_branch}/libgstencoding.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgio.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlibvisual.so
%{_libdir}/gstreamer-%{gst_branch}/libgstogg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopengl.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopus.so
%{_libdir}/gstreamer-%{gst_branch}/libgstoverlaycomposition.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpango.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpbtypes.so
%{_libdir}/gstreamer-%{gst_branch}/libgstplayback.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrawparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsubparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttcp.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttheora.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttypefindfunctions.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideoconvert.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideorate.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideoscale.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideotestsrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvolume.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvorbis.so
%{_libdir}/gstreamer-%{gst_branch}/libgstximagesink.so
%{_libdir}/gstreamer-%{gst_branch}/libgstxvimagesink.so

%files -n libgstallocators-1_0-0
%{_libdir}/libgstallocators*.so.*

%files -n typelib-1_0-GstAllocators-1_0
%{_libdir}/girepository-1.0/GstAllocators-*.typelib

%files -n libgstapp-1_0-0
%{_libdir}/libgstapp*.so.*

%files -n typelib-1_0-GstApp-1_0
%{_libdir}/girepository-1.0/GstApp-*.typelib

%files -n libgstaudio-1_0-0
%{_libdir}/libgstaudio*.so.*

%files -n typelib-1_0-GstAudio-1_0
%{_libdir}/girepository-1.0/GstAudio-*.typelib

%files -n libgstfft-1_0-0
%{_libdir}/libgstfft*.so.*

%files -n libgstgl-1_0-0
%{_libdir}/libgstgl-%{gst_branch}.so.0*

%files -n typelib-1_0-GstGL-1_0
%{_libdir}/girepository-1.0/GstGL-*.typelib

%files -n typelib-1_0-GstGLEGL-1_0
%{_libdir}/girepository-1.0/GstGLEGL-1.0.typelib

%files -n typelib-1_0-GstGLWayland-1_0
%{_libdir}/girepository-1.0/GstGLWayland-1.0.typelib

%files -n typelib-1_0-GstGLX11-1_0
%{_libdir}/girepository-1.0/GstGLX11-1.0.typelib

%files -n libgstpbutils-1_0-0
%{_libdir}/libgstpbutils*.so.*

%files -n typelib-1_0-GstPbutils-1_0
%{_libdir}/girepository-1.0/GstPbutils-*.typelib

%files -n libgstriff-1_0-0
%{_libdir}/libgstriff*.so.*

%files -n libgstrtp-1_0-0
%{_libdir}/libgstrtp*.so.*

%files -n typelib-1_0-GstRtp-1_0
%{_libdir}/girepository-1.0/GstRtp-*.typelib

%files -n libgstrtsp-1_0-0
%{_libdir}/libgstrtsp*.so.*

%files -n typelib-1_0-GstRtsp-1_0
%{_libdir}/girepository-1.0/GstRtsp-*.typelib

%files -n libgstsdp-1_0-0
%{_libdir}/libgstsdp*.so.*

%files -n typelib-1_0-GstSdp-1_0
%{_libdir}/girepository-1.0/GstSdp-*.typelib

%files -n libgsttag-1_0-0
%{_libdir}/libgsttag*.so.*

%files -n typelib-1_0-GstTag-1_0
%{_libdir}/girepository-1.0/GstTag-*.typelib

%files -n libgstvideo-1_0-0
%{_libdir}/libgstvideo*.so.*

%files -n typelib-1_0-GstVideo-1_0
%{_libdir}/girepository-1.0/GstVideo-*.typelib

%files devel
%doc AUTHORS NEWS README.md RELEASE REQUIREMENTS
%{_includedir}/gstreamer-%{gst_branch}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gst-plugins-base/
%dir %{_datadir}/gst-plugins-base/%{gst_branch}/
%{_datadir}/gst-plugins-base/%{gst_branch}/license-translations.dict
%dir %{_libdir}/gstreamer-%{gst_branch}/include
%dir %{_libdir}/gstreamer-%{gst_branch}/include/gst
%dir %{_libdir}/gstreamer-%{gst_branch}/include/gst/gl
%{_libdir}/gstreamer-%{gst_branch}/include/gst/gl/gstglconfig.h

%files lang -f %{_name}-%{gst_branch}.lang

%changelog
