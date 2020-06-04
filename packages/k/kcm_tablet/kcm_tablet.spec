#
# spec file for package kcm_tablet
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010 Raymond Wooninck <tittiatcoke@gmail.com>
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


%define rname wacomtablet
Name:           kcm_tablet
Version:        3.2.0
Release:        0
Summary:        KDE Config Module for Wacom Tablets
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://cgit.kde.org/wacomtablet.git/
Source:         https://download.kde.org/stable/%{rname}/%{version}/%{rname}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-build-with-Qt-5.15.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.7.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-wacom)
BuildRequires:  pkgconfig(xrandr)
Requires:       xf86-input-wacom >= 0.20
Recommends:     %{name}-lang = %{version}
Recommends:     xrandr >= 1.2
Supplements:    (plasma5-workspace and xf86-input-wacom)

%description
This module implements a GUI for the Wacom Linux Drivers and extends it
with profile support to handle different button / pen layouts per profile.

For hardware support have a look at http://www.linuxwacom.sourceforge.net

All tablets can be set up as long as they are found with the wacom kernel module.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %find_lang %{rname} %{name}.lang
  %find_lang plasma_applet_org.kde.plasma.%{rname} %{name}.lang
  %{kf5_find_htmldocs}

  %suse_update_desktop_file kde_wacom_tabletfinder Qt KDE Utility System Configuration

%files lang -f %{name}.lang

%files
%license COPYING
%doc AUTHORS README.md
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol
%{_kf5_applicationsdir}/kde_wacom_tabletfinder.desktop
%{_kf5_appstreamdir}/*.xml
%{_kf5_bindir}/kde_wacom_tabletfinder
%{_kf5_dbusinterfacesdir}/org.kde.Wacom*xml
%{_kf5_debugdir}/wacomtablet.categories
%{_kf5_notifydir}/wacomtablet.notifyrc
%{_kf5_plasmadir}/
%{_kf5_plugindir}/kcm_wacomtablet.so
%{_kf5_plugindir}/kf5/kded/wacomtablet.so
%dir %{_kf5_plugindir}/plasma/dataengine
%{_kf5_plugindir}/plasma/dataengine/plasma_engine_wacomtablet.so
%{_kf5_servicesdir}/kcm_wacomtablet.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.wacomtablet.desktop
%{_kf5_servicesdir}/plasma-dataengine-wacomtablet.desktop
%{_kf5_sharedir}/wacomtablet

%changelog
