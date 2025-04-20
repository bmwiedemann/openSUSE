#
# spec file for package swell-foop
#
# Copyright (c) 2025 SUSE LLC
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


Name:           swell-foop
Version:        48.1
Release:        0
Summary:        Same Game for GNOME
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://wiki.gnome.org/Apps/Swell_Foop
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.60
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.22.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gee-0.8) >= 0.14.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.74
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgnome-games-support-2) >= 2.0.0
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(pangocairo)

%description
Swell Foop is a puzzle game, of which the objective is to clear the
window of as many pieces as possible by clicking on groups of the same
colored pieces. That group will vanish and the pieces on top will fall
until there are none left or no more color groups.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SwellFoop.desktop

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.SwellFoop.desktop
%{_datadir}/dbus-1/services/org.gnome.SwellFoop.service
%{_datadir}/glib-2.0/schemas/org.gnome.SwellFoop.gschema.xml
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/org.gnome.SwellFoop.metainfo.xml

%files lang -f %{name}.lang

%changelog
