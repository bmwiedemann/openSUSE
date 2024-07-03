#
# spec file for package key-rack
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


%define         appname app.drey.KeyRack
Name:           key-rack
Version:        0.2.0+177
Release:        0
Summary:        New GNOME secrets manager
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/sophie-h/key-rack
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libadwaita-1) >= 1.3
BuildRequires:  pkgconfig(gtk4) >= 4.6.0
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files

%description
Key Rack allows to view and edit keys, like passwords or tokens, stored by apps.
It supports Flatpak secrets as well as system wide secrets.

%prep
%autosetup -a1

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file %{appname}

%check
#non available
%meson_test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{appname}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appname}-symbolic.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml

%changelog
