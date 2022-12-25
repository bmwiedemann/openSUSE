#
# spec file for package gstreamer-plugins-libav
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


%define gst_branch 1.0

Name:           gstreamer-plugins-libav
Version:        1.20.5
Release:        0
Summary:        A ffmpeg/libav plugin for GStreamer
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org
Source0:        %{url}/src/gst-libav/gst-libav-%{version}.tar.xz
Source1000:     baselibs.conf

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-check-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(orc-0.4) >= 0.4.16
BuildRequires:  pkgconfig(zlib)
Requires:       gstreamer >= %{version}
Enhances:       gstreamer

%description
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related. Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This plugin contains the FFmpeg codecs, containing codecs for most popular
multimedia formats.

%package doc
Summary:        GStreamer Streaming-Media Framework Plug-Ins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description doc
GStreamer is a streaming media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related. Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This plugin contains the documentation

%prep
%autosetup -n gst-libav-%{version} -p1

%build
%meson \
	-Dpackage-name='openSUSE GStreamer-plugins-libav package' \
	-Dpackage-origin='http://download.opensuse.org' \
	-Ddoc=disabled \
	%{nil}
%meson_build

%install
%meson_install

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/gstreamer-%{gst_branch}/libgstlibav.so

%changelog
