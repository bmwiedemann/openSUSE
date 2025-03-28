#
# spec file for package capnet-assist
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


%define         appid io.elementary.capnet-assist
Name:           capnet-assist
Version:        8.0.1
Release:        0
Summary:        Captive Portal Assistant
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/capnet-assist
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.28.0
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.0.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0.0
BuildRequires:  pkgconfig(webkitgtk-6.0)
Requires:       NetworkManager
Provides:       elementary-capnet-assist = %{version}
Obsoletes:      elementary-capnet-assist < %{version}

%description
Assists users in connective to Captive Portals such as those found on
public access points in train stations, coffee shops, universities, etc.
Upon detection, the assistant appears showing the captive portal. Once a
connection is known to have been established, it dismisses itself. Written
in Vala and using WebkitGtk+.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}/icons

%files
%license COPYING
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,16x16@2,16x16@2/apps,24x24@2,24x24@2/apps,32x32@2,32x32@2/apps,64x64@2,64x64@2/apps}

%files lang -f %{appid}.lang

%changelog
