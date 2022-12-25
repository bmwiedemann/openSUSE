#
# spec file for package gstreamer-plugins-bad
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


%define gstreamer_req_version %(echo %{version} | sed -e "s/+.*//")
# Use rpmbuild -D 'BUILD_ORIG 1' to build original code.
# Use rpmbuild -D 'BUILD_ORIG 1' -D 'BUILD_ORIG_ADDON 1' to build patched build plus original as addon.
%define _name gst-plugins-bad
%define gst_branch 1.0
%bcond_with faac
%bcond_with faad

%if 0%{?is_opensuse} || 0%{?sle_version} >= 150400
%bcond_without avtp
%bcond_without bs2b
%bcond_without zbar
%else
%bcond_with avtp
%bcond_with bs2b
%bcond_with zbar
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%bcond_without fdk_aac
%else
%bcond_with fdk_aac
%endif

%if 0%{?is_opensuse}
%bcond_without fluidsynth
%bcond_without openjp2
%else
%bcond_with fluidsynth
%bcond_with openjp2
%endif

%if 0%{?suse_version} >= 1550 || (0%{?is_opensuse} && 0%{?sle_version} >= 150400)
%bcond_without zxing
%else
%bcond_with zxing
%endif

%ifarch s390x ppc64
%bcond_with ldacBT
%else
%bcond_without ldacBT
%endif

Name:           gstreamer-plugins-bad
Version:        1.20.5
Release:        0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/%{_name}/%{_name}-%{version}.tar.xz
Source2:        gstreamer-plugins-bad.appdata.xml
Source99:       baselibs.conf
# PATCH-FIX-SUSE Fix build with the old srt version inherited from SLE15 SP2
Patch0:         fix-build-with-srt-1.3.4.patch
# PATCH-FIX-OPENSUSE spandsp3.patch jengelh@inai.de -- Fix build against spandsp 3.x. Patch is not upstreamable in this form
Patch2:         spandsp3.patch

%if %{with fdk_aac}
BuildRequires:  pkgconfig(fdk-aac) >= 0.1.4
%endif
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  ladspa-devel
BuildRequires:  libgme-devel
BuildRequires:  libgsm-devel
BuildRequires:  meson >= 0.47.0
BuildRequires:  musepack-devel
BuildRequires:  orc >= 0.4.11
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  shaderc
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(aom)
%if %{with avtp}
BuildRequires:  pkgconfig(avtp)
%endif
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dirac) >= 0.10
BuildRequires:  pkgconfig(egl)
%if %{with fluidsynth}
BuildRequires:  pkgconfig(fluidsynth)
%endif
BuildRequires:  pkgconfig(gio-2.0) >= 2.25.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv1_cm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(graphene-1.0) >= 1.4.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= %{gstreamer_req_version}
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lcms2)
%if %{with ldacBT}
BuildRequires:  pkgconfig(ldacBT-enc)
%endif
BuildRequires:  pkgconfig(libass) >= 0.10.2
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcurl) >= 7.35.0
BuildRequires:  pkgconfig(libdc1394-2) >= 2.0.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.55
BuildRequires:  pkgconfig(libexif) >= 0.6.16
BuildRequires:  pkgconfig(libopenmpt)
BuildRequires:  pkgconfig(libpng) >= 1.2
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.14
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libsrtp2) >= 2.1.0
BuildRequires:  pkgconfig(libssh2) >= 1.4.3
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lilv-0) >= 0.16
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(microdns)
BuildRequires:  pkgconfig(mjpegtools)
BuildRequires:  pkgconfig(neon)
BuildRequires:  pkgconfig(nice) >= 0.1.14
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl) >= 0.9.5
BuildRequires:  pkgconfig(opus) >= 0.9.4
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(schroedinger-1.0) >= 1.0.10
BuildRequires:  pkgconfig(sndfile) >= 1.0.16
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(spandsp) >= 0.0.6
BuildRequires:  pkgconfig(srt)
# FIXME we do not have pkgconfig(storage_client) in openSUSE yet -- remove -Dgs=disabled
# BuildRequires:  pkgconfig(storage_client)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client) >= 1.0.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.0
BuildRequires:  pkgconfig(wayland-egl) >= 9.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.4
BuildRequires:  pkgconfig(wayland-scanner) >= 1.4.0
BuildRequires:  pkgconfig(webrtc-audio-processing) >= 0.2
# FIXME we do not have pkgconfig(webrtc-audio-coding-1) in openSUSE yet -- remove -D
#BuildRequires:  pkgconfig(webrtc-audio-coding-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb) >= 1.10
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(zvbi-0.2)
%if %{with zxing}
BuildRequires:  pkgconfig(zxing)
%endif
Requires(post): glib2-tools
Requires(postun):glib2-tools
# FIXME! - this leads to unresolvables currently
#%%define gstreamer_plugins_bad_req %%(xzgrep --text "^GST.*_REQ" %%{S:0} | sort -u | sed 's/GST_REQ=/gstreamer >= /;s/GSTPB_REQ=/gstreamer-plugins-base >= /' | tr '\\n' ' ')
#Requires:       %%gstreamer_plugins_bad_req
# FIXME
Enhances:       gstreamer
# Generic name, never used in SuSE:
Provides:       gst-plugins-bad = %{version}
Obsoletes:      libgstvdpau < 1.18.0
# Disabled - checking for opencv2/bgsegm.hpp... no
#BuildRequires:  pkgconfig(opencv)
%if %{with bs2b}
BuildRequires:  libbs2b-devel
%endif
%if %{with openjp2}
BuildRequires:  pkgconfig(libopenjp2)
%endif
%if %{with zbar}
BuildRequires:  pkgconfig(zbar) >= 0.9
%endif
%ifarch x86_64
BuildRequires:  pkgconfig(libmfx)
%endif

%if 0%{?BUILD_ORIG}
BuildRequires:  libdca-devel
BuildRequires:  pkgconfig(dvdnav) >= 4.1.2
BuildRequires:  pkgconfig(dvdread) >= 4.1.2
BuildRequires:  pkgconfig(libde265) >= 0.9
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libopenaptx) == 0.2.0
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(openh264) >= 1.3.0
BuildRequires:  pkgconfig(vo-aacenc) >= 0.1.0
BuildRequires:  pkgconfig(vo-amrwbenc) >= 0.1.0
BuildRequires:  pkgconfig(x265)
%if %{with faac}
BuildRequires:  faac-devel
%endif
%if %{with faad}
BuildRequires:  libfaad-devel
%endif
%endif
%if 0%{?BUILD_ORIG}
%if 0%{?BUILD_ORIG_ADDON}
Provides:       patched_subset
%else
Provides:       %{name}-orig-addon = %{version}
%endif
%else
Provides:       patched_subset
%endif

%description
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package chromaprint
Summary:        Chromaprint plugin for GStreamer
Group:          Productivity/Multimedia/Other

%description chromaprint
Add chromaprint (Audio Fingerprinting) support to any GStreamer based tool.

%if %{with fluidsynth}
%package fluidsynth
Summary:        Fluidsynth plugin for GStreamer
Group:          Productivity/Multimedia/Other

%description fluidsynth
Add fluidsynth midi support to any GStreamer based tool.
%endif

%package -n libgstadaptivedemux-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstadaptivedemux-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstbadaudio-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstbadaudio-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstbasecamerabinsrc-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstbasecamerabinsrc-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstcodecs-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstcodecs-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstplay-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstplay-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstva-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstva-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstphotography-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstphotography-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstplayer-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstplayer-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstsctp-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstsctp-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstwayland-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins - Wayland backend
Group:          System/Libraries

%description -n libgstwayland-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstcodecparsers-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstcodecparsers-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstinsertbin-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstinsertbin-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstisoff-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstisoff-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstmpegts-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstmpegts-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgsturidownloader-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgsturidownloader-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstvulkan-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstvulkan-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n libgstwebrtc-1_0-0
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          System/Libraries

%description -n libgstwebrtc-1_0-0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package devel
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gstreamer-plugins-bad-chromaprint
Requires:       libgstadaptivedemux-1_0-0 = %{version}
Requires:       libgstbadaudio-1_0-0 = %{version}
Requires:       libgstbasecamerabinsrc-1_0-0 = %{version}
Requires:       libgstcodecparsers-1_0-0 = %{version}
Requires:       libgstcodecs-1_0-0 = %{version}
Requires:       libgstinsertbin-1_0-0 = %{version}
Requires:       libgstisoff-1_0-0 = %{version}
Requires:       libgstmpegts-1_0-0 = %{version}
Requires:       libgstphotography-1_0-0 = %{version}
Requires:       libgstplay-1_0-0 = %{version}
Requires:       libgstplayer-1_0-0 = %{version}
Requires:       libgstsctp-1_0-0 = %{version}
Requires:       libgsturidownloader-1_0-0 = %{version}
Requires:       libgstva-1_0-0 = %{version}
Requires:       libgstvulkan-1_0-0 = %{version}
Requires:       libgstwayland-1_0-0 = %{version}
Requires:       libgstwebrtc-1_0-0 = %{version}
Requires:       typelib-1_0-GstBadAudio-1_0 = %{version}
Requires:       typelib-1_0-GstCodecs-1_0 = %{version}
Requires:       typelib-1_0-GstInsertBin-1_0 = %{version}
Requires:       typelib-1_0-GstMpegts-1_0 = %{version}
Requires:       typelib-1_0-GstPlay-1_0 = %{version}
Requires:       typelib-1_0-GstPlayer-1_0 = %{version}
Requires:       typelib-1_0-GstWebRTC-1_0 = %{version}
%if %{with fluidsynth}
Requires:       gstreamer-plugins-bad-fluidsynth
%endif

%description devel
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package orig-addon
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          Productivity/Multimedia/Other
Requires:       %{name} >= %{version}
Supplements:    %{name}

%description orig-addon
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related,from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstBadAudio-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstBadAudio-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstPlay-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstPlay-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstCodecs-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstCodecs-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstInsertBin-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstInsertBin-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstMpegts-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstMpegts-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstPlayer-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstPlayer-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstVulkan-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstVulkan-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstVulkanWayland-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstVulkanWayland-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstVulkanXCB-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstVulkanXCB-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n typelib-1_0-GstWebRTC-1_0
Summary:        GStreamer Streaming-Media Framework Plug-Ins -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GstWebRTC-1_0
GStreamer is a streaming media framework based on graphs of filters
that operate on media data. Applications using this library can do
anything media-related, from real-time sound processing to playing
videos. Its plug-in-based architecture means that new data types or
processing capabilities can be added simply by installing new plug-ins.

%package -n gstreamer-transcoder
Summary:        GStreamer Transcoding API
Group:          Productivity/Multimedia/Other

%description -n gstreamer-transcoder
GStreamer Transcoding cli tool and API

%package -n libgsttranscoder-1_0-0
Summary:        GStreamer Transcoder API
Group:          System/Libraries

%description -n libgsttranscoder-1_0-0
This subpackage contains the implementation of the GStreamer API.

%package -n typelib-1_0-GstTranscoder-1_0
Summary:        Introspection bindings for the GStreamer Transcoder API
Group:          System/Libraries

%description -n typelib-1_0-GstTranscoder-1_0
This subpackage contains the introspection bindings for the GStreamer Transcoding API.

%package -n gstreamer-transcoder-devel
Summary:        Development files for the GStreamer Transcoding API
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
# Needed due to gh#pitivi/gst-transcoder#4
Requires:       gstreamer-devel
Requires:       gstreamer-plugins-bad-devel = %{version}
Requires:       libgsttranscoder-1_0-0 = %{version}
Requires:       typelib-1_0-GstTranscoder-1_0 = %{version}

%description -n gstreamer-transcoder-devel
This subpackage contains the header files needed to build applications
making use of the GStreamer Transcoding API.

%lang_package

%prep
%setup -q -n %{_name}-%{version}

%if %{pkg_vcmp srt < 1.4.0}
%patch0 -p1
%endif
%if %{pkg_vcmp spandsp-devel >= 3}
%patch2 -p1
%endif

%build
%global optflags %{optflags} -fcommon
export PYTHON=%{_bindir}/python3
%meson \
%if ! 0%{?BUILD_ORIG}
	-Dpackage-name='openSUSE GStreamer-plugins-bad package' \
	-Dpackage-origin='http://download.opensuse.org' \
	-Ddts=disabled \
	-Dlibde265=disabled \
	-Dmodplug=disabled \
	-Dopenh264=disabled \
	-Dresindvd=disabled \
	-Drtmp=disabled \
	-Dsiren=disabled \
	-Dvoamrwbenc=disabled \
	-Dvoaacenc=disabled \
	-Dx265=disabled \
	-Dopenaptx=disabled \
%else
	-Dopenh264=enabled \
%endif
	-Dgpl=enabled \
%if %{without avtp}
	-Davtp=disabled \
%endif
%if %{without faac}
	-Dfaac=disabled \
%endif
%if %{without faad}
	-Dfaad=disabled \
%endif
%if %{without fdk_aac}
	-Dfdkaac=disabled \
%endif
	-Ddirectfb=disabled \
	-Ddoc=disabled \
	-Dexamples=disabled \
	-Dfestival=disabled \
	-Dflite=disabled \
%if %{without fluidsynth}
	-Dfluidsynth=disabled \
%endif
%if %{without openjp2}
	-Dopenjpeg=disabled \
%endif
%if %{without zxing}
	-Dzxing=disabled \
%endif
%if %{without zbar}
	-Dzbar=disabled \
%endif
%if %{without ldacBT}
	-Dldac=disabled \
%endif
	-Dhls-crypto=openssl \
	-Dintrospection=enabled \
	-Diqa=disabled \
	-Dkate=disabled \
	-Dmagicleap=disabled \
	-Dmicrodns=enabled \
	-Dopencv=disabled \
	-Dopenni2=disabled \
	-Dopensles=disabled \
	-Dsctp=disabled \
	-Dsvthevcenc=disabled \
	-Dtinyalsa=disabled \
	-Dwasapi=disabled \
	-Dwasapi2=disabled \
	-Dwayland=enabled \
	-Dwildmidi=disabled \
	-Dwpe=disabled \
	-Dgs=disabled \
	-Disac=disabled \
	-Donnx=disabled \
%ifarch x86_64
	-Dmsdk=enabled \
%else
	-Dmsdk=disabled \
%endif
	%{nil}
%meson_build

%install
%meson_install

# Fail when upstream provides appdata
if [ -f %{buildroot}%{_datadir}/appdata/gstreamer-plugins-bad.appdata.xml ]; then
  echo "Please remove the added gstreamer-plugins-bad.appdata.xml file from the sources - the tarball installs it"
  false
else
  mkdir -p %{buildroot}%{_datadir}/appdata
  install -D -m 644 %{SOURCE2} %{buildroot}%{_datadir}/appdata/$(basename %{SOURCE2})
fi
# end appdata fail test

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}-%{gst_branch}

%ldconfig_scriptlets -n libgstadaptivedemux-1_0-0
%ldconfig_scriptlets -n libgstbadaudio-1_0-0
%ldconfig_scriptlets -n libgstbasecamerabinsrc-1_0-0
%ldconfig_scriptlets -n libgstcodecs-1_0-0
%ldconfig_scriptlets -n libgstcodecparsers-1_0-0
%ldconfig_scriptlets -n libgstinsertbin-1_0-0
%ldconfig_scriptlets -n libgstisoff-1_0-0
%ldconfig_scriptlets -n libgstmpegts-1_0-0
%ldconfig_scriptlets -n libgstphotography-1_0-0
%ldconfig_scriptlets -n libgstplayer-1_0-0
%ldconfig_scriptlets -n libgstsctp-1_0-0
%ldconfig_scriptlets -n libgsturidownloader-1_0-0
%ldconfig_scriptlets -n libgstvulkan-1_0-0
%ldconfig_scriptlets -n libgstwebrtc-1_0-0
%ldconfig_scriptlets -n libgstplay-1_0-0
%ldconfig_scriptlets -n libgstva-1_0-0
%ldconfig_scriptlets -n libgstwayland-1_0-0
%ldconfig_scriptlets -n libgsttranscoder-1_0-0

%files
%license COPYING
%dir %{_datadir}/gstreamer-%{gst_branch}/presets/
%{_datadir}/gstreamer-%{gst_branch}/presets/GstFreeverb.prs
%{_datadir}/appdata/gstreamer-plugins-bad.appdata.xml
%{_libdir}/gstreamer-%{gst_branch}/libgstaccurip.so
%{_libdir}/gstreamer-%{gst_branch}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaes.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaiff.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaom.so
%{_libdir}/gstreamer-%{gst_branch}/libgstasfmux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstassrender.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiobuffersplit.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiolatency.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiomixmatrix.so
%{_libdir}/gstreamer-%{gst_branch}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{gst_branch}/libgstautoconvert.so
%if %{with avtp}
%{_libdir}/gstreamer-%{gst_branch}/libgstavtp.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstbayer.so
%{_libdir}/gstreamer-%{gst_branch}/libgstbluez.so
%{_libdir}/gstreamer-%{gst_branch}/libgstbz2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcamerabin.so
%{_libdir}/gstreamer-%{gst_branch}/libgstclosedcaption.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcodecalpha.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcolormanagement.so
%{_libdir}/gstreamer-%{gst_branch}/libgstcurl.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdash.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdc1394.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdecklink.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdtls.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvb.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvbsubenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdvdspu.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfaceoverlay.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfbdevsink.so
%if %{with fdk_aac}
%{_libdir}/gstreamer-%{gst_branch}/libgstfdkaac.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfreeverb.so
%{_libdir}/gstreamer-%{gst_branch}/libgstfrei0r.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgdp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgme.so
%{_libdir}/gstreamer-%{gst_branch}/libgstgsm.so
%{_libdir}/gstreamer-%{gst_branch}/libgsthls.so
%if %{with ldacBT}
%{_libdir}/gstreamer-%{gst_branch}/libgstldac.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstid3tag.so
%{_libdir}/gstreamer-%{gst_branch}/libgstipcpipeline.so
%{_libdir}/gstreamer-%{gst_branch}/libgstinter.so
%{_libdir}/gstreamer-%{gst_branch}/libgstinterlace.so
%{_libdir}/gstreamer-%{gst_branch}/libgstivfparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstivtc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{gst_branch}/libgstjpegformat.so
%{_libdir}/gstreamer-%{gst_branch}/libgstkms.so
%{_libdir}/gstreamer-%{gst_branch}/libgstladspa.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmicrodns.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmidi.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmplex.so
%ifarch x86_64
%{_libdir}/gstreamer-%{gst_branch}/libgstmsdk.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstmusepack.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmxf.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlegacyrawparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstnetsim.so
%{_libdir}/gstreamer-%{gst_branch}/libgstnvcodec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopenexr.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopusparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpcapparse.so
%{_libdir}/gstreamer-%{gst_branch}/libgstpnm.so
%{_libdir}/gstreamer-%{gst_branch}/libgstproxy.so
%{_libdir}/gstreamer-%{gst_branch}/libgstqroverlay.so
%{_libdir}/gstreamer-%{gst_branch}/libgstremovesilence.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrist.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrsvg.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtmp2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtpmanagerbad.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtponvif.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsbc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsdpelem.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{gst_branch}/libgstshm.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsmooth.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsndfile.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsoundtouch.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspandsp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstspeed.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsrt.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsubenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstswitchbin.so
%{_libdir}/gstreamer-%{gst_branch}/libgsttimecode.so
%{_libdir}/gstreamer-%{gst_branch}/libgstttmlsubs.so
%{_libdir}/gstreamer-%{gst_branch}/libgstv4l2codecs.so
%{_libdir}/gstreamer-%{gst_branch}/libgstva.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideoframe_audiolevel.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvideosignal.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvmnc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvulkan.so
%{_libdir}/gstreamer-%{gst_branch}/libgstlv2.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopenal.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopenmpt.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsrtp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwaylandsink.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwebrtc.so
%if %{with zxing}
%{_libdir}/gstreamer-%{gst_branch}/libgstzxing.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstwebrtcdsp.so
%{_libdir}/gstreamer-%{gst_branch}/libgsty4mdec.so
%{_libdir}/gstreamer-%{gst_branch}/libgstuvch264.so
%{_libdir}/gstreamer-%{gst_branch}/libgstwebp.so

# Explicitly list openSUSE only plugins
%if %{with bs2b}
%{_libdir}/gstreamer-%{gst_branch}/libgstbs2b.so
%endif

%if %{with openjp2}
%{_libdir}/gstreamer-%{gst_branch}/libgstopenjpeg.so
%endif
%{_libdir}/gstreamer-%{gst_branch}/libgstteletext.so
%if %{with zbar}
%{_libdir}/gstreamer-%{gst_branch}/libgstzbar.so
%endif

%if %{with fluidsynth}
%files fluidsynth
%{_libdir}/gstreamer-%{gst_branch}/libgstfluidsynthmidi.so
%endif

%files chromaprint
%{_libdir}/gstreamer-%{gst_branch}/libgstchromaprint.so

%files -n libgstplay-1_0-0
%{_libdir}/libgstplay-%{gst_branch}.so.0*

%files -n libgstva-1_0-0
%{_libdir}/libgstva-%{gst_branch}.so.0*

%files -n libgstadaptivedemux-1_0-0
%{_libdir}/libgstadaptivedemux-%{gst_branch}.so.0*

%files -n libgstbadaudio-1_0-0
%{_libdir}/libgstbadaudio-%{gst_branch}.so.0*

%files -n libgstphotography-1_0-0
%{_libdir}/libgstphotography-%{gst_branch}.so.0*

%files -n libgstplayer-1_0-0
%{_libdir}/libgstplayer-%{gst_branch}.so.0*

%files -n libgstsctp-1_0-0
%{_libdir}/libgstsctp-%{gst_branch}.so.0*

%files -n libgstbasecamerabinsrc-1_0-0
%{_libdir}/libgstbasecamerabinsrc-%{gst_branch}.so.0*

%files -n libgstcodecs-1_0-0
%{_libdir}/libgstcodecs-%{gst_branch}.so.0*

%files -n libgstcodecparsers-1_0-0
%{_libdir}/libgstcodecparsers-%{gst_branch}.so.0*

%files -n libgstinsertbin-1_0-0
%{_libdir}/libgstinsertbin-%{gst_branch}.so.0*

%files -n libgstmpegts-1_0-0
%{_libdir}/libgstmpegts-%{gst_branch}.so.0*

%files -n libgsturidownloader-1_0-0
%{_libdir}/libgsturidownloader-%{gst_branch}.so.0*

%files -n libgstisoff-1_0-0
%{_libdir}/libgstisoff-%{gst_branch}.so.0*

%files -n libgstvulkan-1_0-0
%{_libdir}/libgstvulkan-%{gst_branch}.so.0*

%files -n libgstwebrtc-1_0-0
%{_libdir}/libgstwebrtc-%{gst_branch}.so.0*

%files -n libgstwayland-1_0-0
%{_libdir}/libgstwayland-1.0.so.*

%files -n typelib-1_0-GstBadAudio-1_0
%{_libdir}/girepository-1.0/GstBadAudio-1.0.typelib

%files -n typelib-1_0-GstPlay-1_0
%{_libdir}/girepository-1.0/GstPlay-1.0.typelib

%files -n typelib-1_0-GstCodecs-1_0
%{_libdir}/girepository-1.0/GstCodecs-1.0.typelib

%files -n typelib-1_0-GstInsertBin-1_0
%{_libdir}/girepository-1.0/GstInsertBin-1.0.typelib

%files -n typelib-1_0-GstMpegts-1_0
%{_libdir}/girepository-1.0/GstMpegts-1.0.typelib

%files -n typelib-1_0-GstPlayer-1_0
%{_libdir}/girepository-1.0/GstPlayer-1.0.typelib

%files -n typelib-1_0-GstVulkan-1_0
%{_libdir}/girepository-1.0/GstVulkan-1.0.typelib

%files -n typelib-1_0-GstVulkanWayland-1_0
%{_libdir}/girepository-1.0/GstVulkanWayland-1.0.typelib

%files -n typelib-1_0-GstVulkanXCB-1_0
%{_libdir}/girepository-1.0/GstVulkanXCB-1.0.typelib

%files -n typelib-1_0-GstWebRTC-1_0
%{_libdir}/girepository-1.0/GstWebRTC-1.0.typelib

%files devel
%doc AUTHORS NEWS README.md RELEASE REQUIREMENTS
%{_includedir}/gstreamer-%{gst_branch}
%{_libdir}/*.so
%{_libdir}/pkgconfig/gstreamer-bad-audio-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-photography-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-player-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-sctp-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-wayland-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-vulkan-xcb-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-webrtc-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-play-%{gst_branch}.pc
%{_libdir}/pkgconfig/gstreamer-wayland-%{gst_branch}.pc
%{_datadir}/gir-1.0/*.gir

%files -n gstreamer-transcoder
%license COPYING
%{_bindir}/gst-transcoder-%{gst_branch}
%{_libdir}/gstreamer-%{gst_branch}/libgsttranscode.so
%{_datadir}/gstreamer-%{gst_branch}/encoding-profiles/

%files -n libgsttranscoder-1_0-0
%{_libdir}/libgsttranscoder-%{gst_branch}.so.0

%files -n typelib-1_0-GstTranscoder-1_0
%{_libdir}/girepository-1.0/GstTranscoder-%{gst_branch}.typelib

%files -n gstreamer-transcoder-devel
%{_libdir}/libgsttranscoder-%{gst_branch}.so
%{_libdir}/pkgconfig/gstreamer-transcoder-%{gst_branch}.pc

%files lang -f %{_name}-%{gst_branch}.lang

%if 0%{?BUILD_ORIG}
%if 0%{?BUILD_ORIG_ADDON}
%files orig-addon
%endif
%{_datadir}/gstreamer-%{gst_branch}/presets/GstVoAmrwbEnc.prs
%{_libdir}/gstreamer-%{gst_branch}/libgstvoamrwbenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstvoaacenc.so
%{_libdir}/gstreamer-%{gst_branch}/libgstdtsdec.so

%if %{with faac}
%{_libdir}/gstreamer-%{gst_branch}/libgstfaac.so
%endif

%if %{with faad}
%{_libdir}/gstreamer-%{gst_branch}/libgstfaad.so
%endif

%{_libdir}/gstreamer-%{gst_branch}/libgstde265.so
%{_libdir}/gstreamer-%{gst_branch}/libgstmodplug.so
%{_libdir}/gstreamer-%{gst_branch}/libgstopenh264.so
%{_libdir}/gstreamer-%{gst_branch}/libgstrtmp.so
%{_libdir}/gstreamer-%{gst_branch}/libgstsiren.so
%{_libdir}/gstreamer-%{gst_branch}/libgstx265.so
%{_libdir}/gstreamer-%{gst_branch}/libgstresindvd.so
%endif

%changelog
