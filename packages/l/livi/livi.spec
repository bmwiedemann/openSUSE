#
# spec file for package livi
#
# Copyright (c) 2024 mantarimay
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


%bcond_without test
%define appid org.sigxcpu.Livi
Name:           livi
Version:        0.2.0
Release:        0
Summary:        A light video player with hardware acceleration support
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/guidog/livi
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  Mesa-libGL-devel
BuildRequires:  appstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk4) >= 4.13.7
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-play-1.0)
BuildRequires:  pkgconfig(gstreamer-gl-1.0)

%description
Minimalistic video player using GTK4 and GStreamer. The main purpose is
to make playing hw accelerated videos with hantro and OpenGL simple.

#lang_package

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

#find_lang #{name} #{?no_lang_C}

%check
%if %{with test}
%meson_test
%endif

%files
%license COPYING
%doc README* NEWS
%{_bindir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml

#files lang -f #{name}.lang

%changelog
