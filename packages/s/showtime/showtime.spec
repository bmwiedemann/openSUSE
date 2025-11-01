#
# spec file for package showtime
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


%define appid org.gnome.Showtime

Name:           showtime
Version:        49.0
Release:        0
Summary:        Video player
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/showtime
Source:         %{name}-%{version}.tar

BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.18.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8.alpha
Requires:       gstreamer-plugins-rs
Recommends:     gstreamer-plugins-bad
Recommends:     gstreamer-plugins-good
Recommends:     gstreamer-plugins-libav
Recommends:     gstreamer-plugins-ugly
BuildArch:      noarch

%description
Watch without distraction.

Play your favorite movies and video files without hassle. Showtime
features simple playback controls that fade out of your way when
you're watching, fullscreen, adjustable playback speed, multiple
language and subtitle tracks, and screenshots — everything you need
for a straightforward viewing experience.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%dir %{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}/*
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/dbus-1/services/org.gnome.Showtime.service
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.gresource

%files lang -f %{name}.lang

%changelog
