#
# spec file for package switchboard-plug-pantheon-shell
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


%define         appid io.elementary.settings.desktop
Name:           switchboard-plug-pantheon-shell
Version:        8.1.0
Release:        0
Summary:        Plug to configure various aspects of the Pantheon desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/switchboard-plug-pantheon-shell
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(granite-7) >= 7.5.0
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(switchboard-3)
Requires:       switchboard

%description
The desktop plug is a section in Switchboard, the elementary System
Settings app, where users can configure the wallpaper, dock, and
hotcorners. In the future the desktop plug might also handle other desktop
settings such as the panel, app launcher, and window manager.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}
%find_lang %{appid}

%files
%license COPYING
%doc README.md
%dir %{_libdir}/{switchboard-3,switchboard-3/personal}
%{_libdir}/switchboard-3/personal/libdesktop.so
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f %{appid}.lang

%changelog
