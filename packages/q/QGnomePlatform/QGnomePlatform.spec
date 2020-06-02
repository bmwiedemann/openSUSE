#
# spec file for package QGnomePlatform
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.6.1
Release:        0
Summary:        A better Qt application inclusion in GNOME
# Most code is LGPL-2.1-or-later but qgtk3dialoghelpers files forked from
# Qt 5 result in this licensing scheme for the combined work:
License:        LGPL-3.0-only OR GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://github.com/FedoraQt/QGnomePlatform/
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM QGnomePlatform-qt-5.15.patch dimstar@opensuse.org -- Fix build with Qt 5.15
Patch0:         QGnomePlatform-qt-5.15.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  libqt5-qtwayland-devel
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
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
qmake-qt5
make %{?_smp_mflags}

%install
%qmake5_install

%files
%doc README.md
%license LICENSE
%dir %{libqt5_plugindir}
%dir %{libqt5_plugindir}/platformthemes
%{libqt5_plugindir}/platformthemes/libqgnomeplatform.so
%{libqt5_plugindir}/wayland-decoration-client/libqgnomeplatformdecoration.so

%changelog
