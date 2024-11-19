#
# spec file for package xdg-desktop-portal-pantheon
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


%define         appid io.elementary.portals
Name:           xdg-desktop-portal-pantheon
Version:        7.2.0
Release:        0
Summary:        Pantheon Backend Portal
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/portals
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  meson >= 0.58.0
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.56.1
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4-wayland)
BuildRequires:  pkgconfig(gtk4-x11)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  pkgconfig(x11)

%description
A Pantheon backend implementation for xdg-desktop-portal.

This package provides D-Bus interfaces that are used by xdg-desktop-portal
to implement portals.

%lang_package

%prep
%autosetup -n portals-%{version}

%build
export CFLAGS="%{optflags} -Wno-error=return-type"
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md
%{_userunitdir}/%{name}.service
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.pantheon.service
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/xdg-desktop-portal/portals/pantheon.portal
%dir %{_datadir}/{xdg-desktop-portal,xdg-desktop-portal/portals}

%files lang -f %{name}.lang

%changelog
