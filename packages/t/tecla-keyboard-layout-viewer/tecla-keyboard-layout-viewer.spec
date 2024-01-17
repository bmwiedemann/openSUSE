#
# spec file for package tecla-keyboard-layout-viewer
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


Name:           tecla-keyboard-layout-viewer
Version:        45.rc
Release:        0
Summary:        A keyboard layout viewer
License:        GPL-2.0-only
URL:            https://gitlab.gnome.org/GNOME/tecla
Source:         https://download.gnome.org/sources/tecla/45/tecla-%{version}.tar.xz

BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary} from the GNOME project.

%lang_package

%prep
%autosetup -p1 -n tecla-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang tecla %{?no_lang_C}

%files
%license LICENSE
%doc NEWS README.md
%{_bindir}/tecla
%{_datadir}/applications/org.gnome.Tecla.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tecla.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Tecla-symbolic.svg
%{_datadir}/pkgconfig/tecla.pc

%files lang -f tecla.lang

%changelog

