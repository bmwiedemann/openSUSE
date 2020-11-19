#
# spec file for package gnome-games
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


Name:           gnome-games
Version:        3.38.0
Release:        0
Summary:        Browse and play your games - all of them
License:        GPL-3.0-only
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Games
Source0:        https://download.gnome.org/sources/gnome-games/3.38/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson >= 0.46.1
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(grilo-0.3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libhandy-1) >= 0.90
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(manette-0.2) >= 0.2.0
BuildRequires:  pkgconfig(retro-gtk-1) >= 0.18.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(tracker-sparql-2.0)

%description
Games is a GNOME application to browse your video games library and
to easily pick and play a game from it.

%package -n gnome-shell-search-provider-gnome-games
Summary:        GNOME Games -- Search Provider for GNOME Shell
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Supplements:    packageand(gnome-shell:%{name})

%description -n gnome-shell-search-provider-gnome-games
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Games.


%lang_package

%prep
%autosetup -p1
chmod -x COPYING

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%suse_update_desktop_file org.gnome.Games -r Game Amusement
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}/%{name}/

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/org.gnome.Games*
%{_datadir}/applications/org.gnome.Games.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Games.gschema.xml
%{_datadir}/metainfo/org.gnome.Games.appdata.xml
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/options
%{_datadir}/%{name}/options/

%files lang -f %{name}.lang

%files -n gnome-shell-search-provider-gnome-games
%{_libexecdir}/gnome-games-search-provider
%{_datadir}/dbus-1/services/org.gnome.Games.SearchProvider.service
%{_datadir}/dbus-1/services/org.gnome.Games.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Games.SearchProvider.ini

%changelog
