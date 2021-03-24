#
# spec file for package celluloid
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


%define _name   io.github.celluloid_player.Celluloid
Name:           celluloid
Version:        0.21
Release:        0
Summary:        Simple GTK+ frontend for MPV
License:        GPL-3.0-or-later
URL:            https://celluloid-player.github.io/
Source:         https://github.com/celluloid-player/celluloid/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gettext >= 0.19.7
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.40.6
BuildRequires:  meson >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.23
BuildRequires:  pkgconfig(mpv) >= 1.101
Recommends:     %{name}-lang
Recommends:     youtube-dl
Obsoletes:      gnome-mpv < %{version}
Provides:       gnome-mpv = %{version}

%description
Celluloid is a simple GTK+ frontend for MPV.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{_name}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{_name}-symbolic.svg
%{_datadir}/metainfo/%{_name}.appdata.xml
%{_datadir}/dbus-1/services/%{_name}.service
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
