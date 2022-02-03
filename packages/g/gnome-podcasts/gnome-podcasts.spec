#
# spec file for package gnome-podcasts
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 Bjørn Lie, Bryne, Norway.
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


%define commit de438a4d62196bddd134bb155a812fe1

Name:           gnome-podcasts
Version:        0.5.1
Release:        0
Summary:        Podcast app for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/podcasts
Source0:        %{url}/uploads/%{commit}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 6614bb62ecbec7c3b18ea7fe44beb50fe7942b27.patch -- Fix build with meson 0.60 and newer
Patch0:         https://gitlab.gnome.org/World/podcasts/-/commit/6614bb62ecbec7c3b18ea7fe44beb50fe7942b27.patch

BuildRequires:  cargo
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.56
BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-audio-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-bad-audio-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-player-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0) >= 1.16
BuildRequires:  pkgconfig(gstreamer-video-1.0) >= 1.16
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.11
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(openssl) >= 1.0
BuildRequires:  pkgconfig(sqlite3) >= 3.20

%lang_package

%description
A Podcast application for GNOME.
Listen to your favorite podcasts, right from your desktop.

%prep
%autosetup -p1

%build
%meson \
	-Dprofile=default \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Podcasts.desktop
%{_datadir}/dbus-1/services/org.gnome.Podcasts.service
%{_datadir}/glib-2.0/schemas/org.gnome.Podcasts.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Podcasts*.svg
%{_datadir}/metainfo/org.gnome.Podcasts.appdata.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/resources.gresource

%files lang -f %{name}.lang

%changelog
