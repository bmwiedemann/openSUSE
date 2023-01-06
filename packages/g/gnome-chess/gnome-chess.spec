#
# spec file for package gnome-chess
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gnome-chess
Version:        43.1
Release:        0
Summary:        Chess Game for GNOME
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Chess
URL:            https://wiki.gnome.org/Apps/Chess
Source0:        https://download.gnome.org/sources/gnome-chess/43/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
# ITS Tool is needed because there are some XML formats that Gettext does not handle, at least not now (42.alpha).
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.35.7
BuildRequires:  pkgconfig(gio-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.44.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk4) >= 3.19.0
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.32.0
Requires:       chess_backend

%description
This is a game for playing the classic board game of chess, in which
two players simulate a battle by capturing the opponents pieces and
ultimately the king. It can be played in 2D or 3D mode, full screen or
in a window.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/
%{_bindir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/applications/org.gnome.Chess.desktop
%{_datadir}/dbus-1/services/org.gnome.Chess.service
%{_datadir}/glib-2.0/schemas/org.gnome.Chess.gschema.xml
%{_datadir}/metainfo/org.gnome.Chess.appdata.xml
%{_mandir}/man6/%{name}.6%{?ext_man}
%dir %{_sysconfdir}/gnome-chess
%config %{_sysconfdir}/gnome-chess/engines.conf

%files lang -f %{name}.lang

%changelog
