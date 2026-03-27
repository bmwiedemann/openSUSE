#
# spec file for package gst-thumbnailers
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gst-thumbnailers
Version:        1.0.0
Release:        0
Summary:        GStreamer Thumbnailers
License:        GPL-3.0
URL:            https://gitlab.gnome.org/GNOME/gst-thumbnailers
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  cargo-packaging >= 1.3.0
BuildRequires:  meson
BuildRequires:  pkgconfig(glycin-2) >= 2.0.0
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.26.0
BuildRequires:  pkgconfig(gstreamer-app-1.0) >= 1.26.0

%description
Provides two binaries that create a thumbnails for the libgnome-desktop thumbnailer:

- gst-video-thumbnailer tries to extract the stored cover art from a video file.
  If no cover art is found, it checks a few different frames and takes the frame
  with the largest variance between it's the pixels.
- gst-audio-thumbnailer tries to extract the stored cover art from an audio file.

%prep
%autosetup -p1 -a1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/gst-audio-thumbnailer
%{_bindir}/gst-video-thumbnailer
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/gst-audio-thumbnailer.thumbnailer
%{_datadir}/thumbnailers/gst-video-thumbnailer.thumbnailer

%changelog

