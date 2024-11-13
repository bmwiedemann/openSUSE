#
# spec file for package switchboard-plug-onlineaccounts
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


%define         appid io.elementary.settings.onlineaccounts
Name:           switchboard-plug-onlineaccounts
Version:        8.0.1
Release:        0
Summary:        Online Accounts plug for Switchboard
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/switchboard-plug-onlineaccounts
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(camel-1.2) >= 3.28
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.1.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.4.0
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.40
BuildRequires:  pkgconfig(switchboard-3)
Requires:       switchboard

%description
This plug allow you to enable online accounts sync.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{appid}
%fdupes %{buildroot}%{_datadir}

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/{switchboard-3,switchboard-3/network}
%{_libdir}/switchboard-3/network/libonlineaccounts.so
%{_datadir}/icons/hicolor/*/apps/%{appid}.svg
%dir %{_datadir}/icons/hicolor/{128x128@2,128x128@2/apps,32x32@2,32x32@2/apps,48x48@2,48x48@2/apps,64x64@2,64x64@2/apps}
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{appid}.lang

%changelog
