#
# spec file for package tuba
#
# Copyright (c) 2025 SUSE LLC
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


%define         appid dev.geopjr.Tuba
Name:           tuba
Version:        0.10.3
Release:        0
Summary:        Browse the Fediverse
License:        GPL-3.0-only
URL:            https://github.com/GeopJr/Tuba
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-tools
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.60
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.56
BuildRequires:  pkgconfig(clapper-0.0) >= 0.8.0
BuildRequires:  pkgconfig(clapper-gtk-0.0) >= 0.8.0
BuildRequires:  pkgconfig(gee-0.8) >= 0.8.5
BuildRequires:  pkgconfig(gexiv2) >= 0.14
BuildRequires:  pkgconfig(glib-2.0) >= 2.80.0
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.18.0
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.7.1
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.4.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1.7.5
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsecret-1) >= 0.20
BuildRequires:  pkgconfig(libsoup-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.10
BuildRequires:  pkgconfig(webkitgtk-6.0)

%lang_package

%description
%{summary}.

%prep
%autosetup -n Tuba-%{version}

%build
%meson \
  -Ddevel=false \
  -Ddistro=true \
  -Dclapper=true
%meson_build

%install
%meson_install
%find_lang %{appid}

%check
%meson_test

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/glib-2.0/schemas/dev.geopjr.Tuba.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/%{appid}.svg
%{_iconsdir}/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_mandir}/man?/%{appid}.?%{?ext_man}

%files lang -f %{appid}.lang

%changelog
