#
# spec file for package plasma5-phone-components
#
# Copyright (c) 2021 SUSE LLC
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


# org.kde.phone.homescreen is internal, MeeGo.QOfono is optional and not packaged yet
%global __requires_exclude qmlimport\\((org\\.kde\\.phone\\.homescreen|MeeGo\\.QOfono).*

%define kf5_version 5.74.0

%bcond_without lang
Name:           plasma5-phone-components
Version:        5.21.4
Release:        0
# Full Plasma 5 version (e.g. 5.9.3)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.3 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plasma Mobile
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-phone-components-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-phone-components-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5PlasmaQuick) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.1.90
# Forced on startup
Requires:       qqc2-breeze-style
# QML imports
Requires:       bluez-qt-imports
Requires:       kactivities5-imports
Requires:       kdeclarative-components
Requires:       kirigami2
Requires:       kwin5
Requires:       libqt5-qtwayland
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Requires:       milou5
Requires:       plasma-nm5
Requires:       plasma5-nano
Requires:       plasma5-pa
Requires:       plasma5-workspace >= %{_plasma5_bugfix}
# TODO: import MeeGo.QOfono 0.2

%description
Plasma shell and components targeted for phones.

%lang_package

%prep
%autosetup -p1 -n plasma-phone-components-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with lang}
  %kf5_find_lang
%endif

  # Wut?
  sed -i '#touch /tmp/simplelogin_starting#d' %{buildroot}%{_kf5_bindir}/kwinwrapper

  %fdupes %{buildroot}

%files
%license COPYING*
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/plasma/
%dir %{_kf5_qmldir}/org/kde/plasma/private/
%{_kf5_qmldir}/org/kde/plasma/private/mobileshell/
%{_kf5_bindir}/kwinwrapper
%dir %{_datadir}/kwin/
%dir %{_datadir}/kwin/scripts/
%{_datadir}/kwin/scripts/org.kde.phone.multitasking/
%dir %{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%dir %{_kf5_plasmadir}/look-and-feel/
%{_kf5_plasmadir}/look-and-feel/org.kde.plasma.phone/
%dir %{_kf5_plasmadir}/shells
%{_kf5_plasmadir}/shells/org.kde.plasma.phoneshell/
%dir %{_kf5_plasmadir}/plasmoids/
%{_kf5_plasmadir}/plasmoids/org.kde.phone.activities/
%{_kf5_plasmadir}/plasmoids/org.kde.phone.krunner/
%{_kf5_plasmadir}/plasmoids/org.kde.phone.panel/
%{_kf5_plasmadir}/plasmoids/org.kde.phone.homescreen/
%{_kf5_plasmadir}/plasmoids/org.kde.phone.taskpanel/
%{_kf5_servicesdir}/kwin-script-org.kde.phone.multitasking.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.phone.activities.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.phone.krunner.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.phone.panel.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.phone.homescreen.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.phone.taskpanel.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.phone.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.phoneshell.desktop
%{_kf5_notifydir}/plasma_phone_components.notifyrc
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/applets/
%{_kf5_plugindir}/plasma/applets/plasma_applet_phonepanel.so
%{_kf5_plugindir}/plasma/applets/plasma_containment_phone_homescreen.so
%{_kf5_plugindir}/plasma/applets/plasma_containment_phone_taskpanel.so
%{_kf5_appstreamdir}/org.kde.plasma.phone.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.phoneshell.appdata.xml
%{_kf5_appstreamdir}/org.kde.phone.activities.appdata.xml
%{_kf5_appstreamdir}/org.kde.phone.krunner.appdata.xml

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
