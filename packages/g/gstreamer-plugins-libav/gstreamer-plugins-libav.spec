#
# spec file for package gstreamer-plugins-libav
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
Name:           gstreamer-plugins-libav
Version:        1.18.0
Release:        0
Summary:        A ffmpeg/libav plugin for GStreamer
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://gstreamer.freedesktop.org/
Source:         https://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz
Source1000:     baselibs.conf
Patch0:         add-gpl-option.patch
BuildRequires:  gcc-c++
BuildRequires:  hotdoc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  yasm
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-check-1.0) >= %{version}
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= %{version}
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(orc-0.4) >= 0.4.16
BuildRequires:  pkgconfig(zlib)
Requires:       gstreamer >= %{version}
Enhances:       gstreamer
Supplements:    packageand(%{name}:gstreamer)
%if 0%{?BUILD_ORIG}
# Depend on the full build of the same libavcodec.so.N we built against
Requires:       %(rpm --qf "%%{name}" -qf $(readlink -f %{_libdir}/libavcodec.so))(unrestricted)
%endif

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
%setup -q -n gst-libav-%{version}
%patch0 -p1

%build
%meson \
	-Dpackage-name='openSUSE GStreamer-plugins-good package' \
	-Dpackage-origin='http://download.opensuse.org' \
        -Dgpl=enabled \
	%{nil}

%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%files
%license COPYING
%{_libdir}/gstreamer-%{gst_branch}/libgstlibav.so

%files doc
%doc AUTHORS NEWS README.md

%changelog
