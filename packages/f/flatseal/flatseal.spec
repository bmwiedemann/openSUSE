#
# spec file for package flatseal
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


Name:           flatseal
Version:        2.4.0
Release:        0
Summary:        Manage Flatpak permissions
License:        GPL-3.0-or-later
URL:            https://github.com/tchx84/flatseal
Source:         %{name}-%{version}.tar.zst
BuildRequires:  meson >= 0.59.0
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildREquires:  pkgconfig(appstream) >= 1.0
BuildArch:      noarch

%description
Flatseal is a graphical utility to review and modify permissions from your Flatpak applications.

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
%doc README.md CHANGELOG.md DOCUMENTATION.md
%{_bindir}/com.github.tchx84.Flatseal
%{_datadir}/applications/com.github.tchx84.Flatseal.desktop
%{_datadir}/dbus-1/services/com.github.tchx84.Flatseal.service
%{_datadir}/glib-2.0/schemas/com.github.tchx84.Flatseal.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/com.github.tchx84.Flatseal.metainfo.xml
%{_datadir}/%{name}/
%{_datadir}/%{name}/com.github.tchx84.Flatseal.data.gresource
%{_datadir}/%{name}/com.github.tchx84.Flatseal.src.gresource

%files lang -f %{name}.lang

%changelog
