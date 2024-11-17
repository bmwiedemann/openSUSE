#
# spec file for package AdwSteamGtk
#
# Copyright (c) 2024 SUSE LLC
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


%define         appname io.github.Foldex.AdwSteamGtk
Name:           AdwSteamGtk
Version:        0.7.1
Release:        0
Summary:        A Gtk wrapper for Adwaita-for-Steam
License:        GPL-3.0-only
URL:            https://github.com/Foldex/AdwSteamGtk
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  patch
BuildRequires:  python3-packaging
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libportal)
Requires:       typelib(XdpGtk4)

%description
A GTK wrapper that installs and updates the Adwaita for Steam skin.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang adwaita-steam-gtk

%files
%license LICENSE
%doc README.md
%{_bindir}/adwaita-steam-gtk
%{_datadir}/adwaita-steam-gtk
%{_datadir}/appdata/%{appname}.appdata.xml
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_iconsdir}/hicolor/scalable/apps/%{appname}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appname}-symbolic.svg

%files lang -f adwaita-steam-gtk.lang

%changelog
