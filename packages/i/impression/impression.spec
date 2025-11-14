#
# spec file for package impression
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         appname io.gitlab.adhami3310.Impression
Name:           impression
Version:        3.5.4
Release:        0
Summary:        A straight-forward and modern application to create bootable drives
License:        GPL-3.0-only
URL:            https://gitlab.com/adhami3310/Impression
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  appstream-glib
BuildRequires:  cargo-packaging
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.59.0
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.81
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)

%description
Write disk images onto your drives with ease. Select an image, insert your
drive, and you're good to go! Impression is a useful tool for both avid
distro-hoppers and casual computer users. See Press for content mentioning
Impression from various writers, content creators, etc.

%lang_package

%prep
%autosetup -a1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/dbus-1/services/%{appname}.service
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/metainfo/%{appname}.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/%{appname}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appname}-symbolic.svg

%files lang -f %{name}.lang

%changelog
