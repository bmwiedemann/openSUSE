#
# spec file for package vokoscreenNG
#
# Copyright (c) 2021 SUSE LLC
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


Name:           vokoscreenNG
Version:        3.0.8
Release:        0
Summary:        Screencast creator
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Other
URL:            https://github.com/vkohaupt/vokoscreenNG
Source:         https://github.com/vkohaupt/%{name}/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM - Add AppStream metadata - PR#94
Patch0:         add_appstream_metadata.patch
BuildRequires:  appstream-glib
BuildRequires:  gstreamer-devel
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)

Requires:       gstreamer >= 1.12.5
Requires:       libQt5Core5 >= 5.9.4
%if 0%{?sle_version} && 0%{?sle_version} < 150300
Requires:       pulseaudio
%else
Requires:       pulseaudio-daemon
%endif
# Required for vorbis and opus audio
Requires:       gstreamer-plugins-base
# Required for mkv, avi, webm, mp4, vp8 video and flac audio
Requires:       gstreamer-plugins-good
# Required for x265, av1, camera
Requires:       gstreamer-plugins-bad
# Required for x264 and mp3lame
Requires:       gstreamer-plugins-ugly
# Required for x264
Recommends:     gstreamer-plugins-ugly-orig-addon
Requires:       gstreamer-plugins-libav
# Required for openh264
Recommends:     gstreamer-plugins-bad-orig-addon
# Required for H.264 and MPEG2 hardware encoding on Intel
Recommends:     gstreamer-plugins-vaapi
Recommends:     intel-vaapi-driver

Provides:       vokoscreen = %{version}
Obsoletes:      vokoscreen < %{version}

%description
vokoscreenNG is a user friendly Open Source screencaster for Linux and Windows.

%prep
%autosetup -p1

%build
cd src
%qmake5
%make_jobs

%install
mkdir -p %{buildroot}/usr/bin/
cp src/%{name} %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/applications/
cp src/applications/%{name}.desktop %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/share/pixmaps/
cp src/applications/%{name}.png %{buildroot}/usr/share/pixmaps/
mkdir -p %{buildroot}/usr/share/metainfo/
cp src/applications/vokoscreenNG.appdata.xml %{buildroot}/usr/share/metainfo/

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
