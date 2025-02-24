#
# spec file for package ProtonPlus
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


%define         appid com.vysp3r.ProtonPlus
Name:           ProtonPlus
Version:        0.4.25
Release:        0
Summary:        A Wine and Proton-based compatibility tools manager for GNOME
License:        GPL-3.0-only
URL:            https://github.com/vysp3r/ProtonPlus
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  meson >= 0.62.0
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.5
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)

%description
ProtonPlus is a Proton version manager for installing and managing Proton
versions. It works with Steam, Lutris, Heroic Games Launcher and Bottles. It
uses GTK4.

%lang_package

%prep
%autosetup

%build
%meson --prefix=/usr
%meson_build

%install
%meson_install

%find_lang %{appid}

%fdupes %{buildroot}

%files
%{_bindir}/%{appid}
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.png

%files lang -f %{appid}.lang

%changelog
