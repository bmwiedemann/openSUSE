#
# spec file for package pantheon-maps
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


%define         appid io.elementary.maps
Name:           pantheon-maps
Version:        8.1.0
Release:        0
Summary:        Map viewer designed for the pantheon desktop
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/maps
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.57.0
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(shumate-1.0)

%description
This is a fork of Atlas Maps and wouldn't exist without work of Steffen Schuhmann

%lang_package

%prep
%autosetup -n maps-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%if 0%{?suse_version} < 1600
%dir %{_datadir}/icons/hicolor/{16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,64x64@2,64x64@2/apps,128x128@2,128x128@2/apps}
%endif

%files lang -f %{appid}.lang

%changelog
