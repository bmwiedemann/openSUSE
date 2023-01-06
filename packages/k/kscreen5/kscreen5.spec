#
# spec file for package kscreen5
#
# Copyright (c) 2023 SUSE LLC
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


%global __requires_exclude (org.kde.private.(kcm.)?kscreen)|(org.kde.KScreen)

%bcond_without released
Name:           kscreen5
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Screen management software by KDE
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kscreen-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kscreen-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Screen) >= %{_plasma5_version}
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt5QuickWidgets) >= 5.15.0
BuildRequires:  cmake(Qt5Sensors)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xi)
Requires:       kded
Requires:       libkscreen2-plugin >= %{_plasma5_version}
Requires:       xrdb
Recommends:     %{name}-lang
Recommends:     %{name}-plasmoid
Supplements:    packageand(libkscreen2-plugin:plasma5-workspace)
Provides:       kscreen = %{version}
Obsoletes:      kscreen < %{version}

%description
KScreen handles screen management for both X11 and Wayland sessions, including rotation, size, refresh rate, and scaling.

%lang_package

%prep
%setup -q -n kscreen-%{version}

%package plasmoid
Summary:        Plasma widget to control screen configuration
Group:          System/GUI/KDE
Requires:       %{name} = %{version}

%description plasmoid
This package provides a Plasma widget to control common screen configuration options.

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

%post
%systemd_user_post plasma-kscreen-osd.service

%preun
%systemd_user_preun plasma-kscreen-osd.service

%postun
%systemd_user_postun plasma-kscreen-osd.service

%files
%license LICENSES/*
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_bindir}/kscreen-console
%{_kf5_plugindir}/
%{_kf5_sharedir}/kpackage/kcms/kcm_kscreen/
%dir %{_kf5_sharedir}/kded_kscreen/
%dir %{_kf5_sharedir}/kded_kscreen/qml
%{_kf5_sharedir}/kded_kscreen/qml/*.qml
%{_kf5_sharedir}/dbus-1/services/org.kde.kscreen.osdService.service
%{_libexecdir}/kscreen_osd_service
%{_kf5_servicesdir}/
%{_kf5_debugdir}/kscreen.categories
%{_kf5_appstreamdir}/org.kde.kscreen.appdata.xml
%{_userunitdir}/plasma-kscreen-osd.service
%{_kf5_applicationsdir}/kcm_kscreen.desktop

%files plasmoid
%license LICENSES/*
%dir %{_kf5_plasmadir}/plasmoids/
%dir %{_kf5_plasmadir}/plasmoids/org.kde.kscreen
%{_kf5_plasmadir}/plasmoids/org.kde.kscreen/

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
