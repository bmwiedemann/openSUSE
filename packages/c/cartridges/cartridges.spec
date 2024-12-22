#
# spec file for package cartridges
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


%define lname   page.kramo.Cartridges
Name:           cartridges
Version:        2.11
Release:        0
Summary:        A GTK4 + Libadwaita game launcher 
License:        GPL-3.0-only
URL:            https://github.com/kra-mo/cartridges
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5.0
Requires:       python3-gobject
Requires:       python3-pyaml
Requires:       python3-Pillow
BuildArch:      noarch

%description
Cartridges is a simple game launcher written in Python using GTK4 and
Libadwaita.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_datadir}/locale/zh_Hans
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{lname}.desktop
%{_datadir}/glib-2.0/schemas/%{lname}.gschema.xml
%{_datadir}/metainfo/%{lname}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{lname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{lname}-symbolic.svg
%{_datadir}/%{name}/
%{python_sitelib}/%{name}
%{_libexecdir}/%{name}-search-provider
%{_datadir}/dbus-1/services/%{lname}.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/%{lname}.SearchProvider.ini

%files lang -f %{name}.lang

%changelog
