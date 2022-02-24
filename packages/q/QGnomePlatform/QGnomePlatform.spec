#
# spec file for package QGnomePlatform
#
# Copyright (c) 2022 SUSE LLC
# Copyright © 2016      Yuriy Gorodilin <yurg27@gmail.com>
# Copyright © 2018–2019 Markus S. <kamikazow@opensuse.org>
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


Name:           QGnomePlatform
Version:        0.8.4
Release:        0
Summary:        A better Qt application inclusion in GNOME
# Most code is LGPL-2.1-or-later but qgtk3dialoghelpers files forked from
# Qt 5 result in this licensing scheme for the combined work:
License:        GPL-2.0-or-later OR LGPL-3.0-only
Group:          System/GUI/GNOME
URL:            https://github.com/FedoraQt/QGnomePlatform/
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
# QGnomePlatform relies on glib's pkgconfig file to find gsettings files
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libqt5-qtwayland-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5ThemeSupport)
BuildRequires:  pkgconfig(Qt5DBus) >= 5.12.2
BuildRequires:  pkgconfig(Qt5WaylandClient) >= 5.12.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12.2
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.12.2
BuildRequires:  pkgconfig(adwaita-qt) >= 1.4.1
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(x11)
Requires:       adwaita-qt5

Supplements:    (libQt5Gui5 and gnome-session)

%description
QGnomePlatform is a Qt Platform Theme designed to use as many of the GNOME
settings as possible in unmodified Qt applications. It allows Qt applications
to fit into the environment as well as possible.

%define libqt5_archdatadir  %{_libdir}/qt5
%define libqt5_plugindir    %{libqt5_archdatadir}/plugins

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_libdir}/libqgnomeplatform.so
%dir %{libqt5_plugindir}
%dir %{libqt5_plugindir}/platformthemes
%{libqt5_plugindir}/platformthemes/libqgnomeplatformtheme.so
%{libqt5_plugindir}/wayland-decoration-client/libqgnomeplatformdecoration.so

%changelog
