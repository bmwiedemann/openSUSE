#
# spec file for package gst-siddecfp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gst-siddecfp
Version:        19.1.0.1
Release:        0
Summary:        GStreamer C64 sid music plugin
License:        MIT and LGPL-2.0-or-later
URL:            https://github.com/kilikali-nc/gst-siddecfp
Source:         %{name}-%{version}.tar.zst

BuildRequires:  c++_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(libsidplayfp)

%description
GStreamer sidecfp plugin.
This plugin enables playback of Commodore 64
sid music files via gstreamer based audio players.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.MIT COPYING.LIB
%doc README.md
%{_libdir}/gstreamer-%{gst_branch}/libgstsidfp.so

%changelog

