#
# spec file for package gnome-music
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


Name:           gnome-music
Version:        3.36.5
Release:        0
Summary:        Music Player for GNOME
License:        SUSE-GPL-2.0-with-plugin-exception AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-music/3.36/%{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-devel >= 3.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(goa-1.0) >= 3.35.90
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.35.0
BuildRequires:  pkgconfig(grilo-0.3) >= 0.3.12
BuildRequires:  pkgconfig(grilo-plugins-0.3) >= 0.3.10
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.7
BuildRequires:  pkgconfig(libdazzle-1.0) >= 3.28.0
BuildRequires:  pkgconfig(libmediaart-2.0) >= 1.9.1
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(py3cairo) >= 1.14
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.29.1
BuildRequires:  pkgconfig(tracker-sparql-2.0) >= 2.3.0
Requires:       dbus-1-python3
# gnome-music requires grilo-plugin-tracker to interact with tracker and find files (bsc#1083659)
Requires:       grilo-plugin-tracker
# gnomemusic/albumArtCache.py imports cairo directly.
Requires:       python3-cairo >= 1.14
# This is a python 3 application
Requires:       python3-gobject
# ... a python3 GUI application
Requires:       python3-gobject-Gdk
# gnomemusic/player.py imports requests (not introspected)
Requires:       python3-requests
# gnome-music relies on tracker to find local files (bsc#1084861)
Requires:       tracker
# gnome-music relies on tracker to find local files.
Requires:       tracker-miner-files
Recommends:     gstreamer-plugins-ugly

%description
Music player and management application for GNOME.

%lang_package

%prep
%autosetup -p1
# Fix shebangs:
sed -i -e 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|' gnome-music.in

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%find_lang org.gnome.Music %{?no_lang_C} %{name}.lang
%fdupes %{buildroot}%{python3_sitelib}/gnomemusic
%fdupes %{buildroot}%{_datadir}/

%files
%license LICENSE
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-music
%{_datadir}/applications/org.gnome.Music.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Music.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Music*
%{_datadir}/metainfo/org.gnome.Music.appdata.xml
%{_datadir}/org.gnome.Music/
%{_libdir}/org.gnome.Music/
%{python3_sitelib}/gnomemusic/

%files lang -f %{name}.lang

%changelog
