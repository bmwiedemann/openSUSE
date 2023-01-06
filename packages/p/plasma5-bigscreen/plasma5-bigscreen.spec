#
# spec file for package plasma5-bigscreen
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


# Ignore optional dependencies and privats imports
%global __requires_exclude qmlimport\\((Mycroft|org\\.kde\\.private\\.biglauncher|org\\.kde\\.plasma.settings).*

%define kf5_version 5.98.0

%bcond_without released
Name:           plasma5-bigscreen
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.9.3)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.3 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plasma Bigscreen
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-bigscreen-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-bigscreen-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5ActivitiesStats) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5PlasmaQuick) >= %{kf5_version}
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KPipeWire)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
Requires:       plasma5-workspace >= %{_plasma5_bugfix}

%description
Plasma shell for TVs.

%lang_package

%prep
%autosetup -p1 -n plasma-bigscreen-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with released}
%kf5_find_lang
%endif
# Not referenced by anything and not executable
rm %{buildroot}%{_kf5_bindir}/mycroft-skill-launcher.py

%fdupes %{buildroot}

%files
%license LICENSES/*
%{_kf5_bindir}/plasma-bigscreen-{wayland,x11}
%dir %{_kf5_plugindir}/kcms/
%{_kf5_plugindir}/kcms/kcm_mediacenter_audiodevice.so
%{_kf5_plugindir}/kcms/kcm_mediacenter_bigscreen_settings.so
%{_kf5_plugindir}/kcms/kcm_mediacenter_kdeconnect.so
%{_kf5_plugindir}/kcms/kcm_mediacenter_wifi.so
%dir %{_kf5_plugindir}/plasma/
%dir %{_kf5_plugindir}/plasma/applets/
%{_kf5_plugindir}/plasma/applets/plasma_containment_biglauncherhomescreen.so
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/mycroft/
%{_kf5_qmldir}/org/kde/mycroft/bigscreen/
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/genericqml/
%{_kf5_sharedir}/kpackage/genericqml/org.kde.plasma.settings/
%dir %{_kf5_sharedir}/kpackage/kcms/
%{_kf5_sharedir}/kpackage/kcms/kcm_mediacenter_audiodevice/
%{_kf5_sharedir}/kpackage/kcms/kcm_mediacenter_bigscreen_settings/
%{_kf5_sharedir}/kpackage/kcms/kcm_mediacenter_kdeconnect/
%{_kf5_sharedir}/kpackage/kcms/kcm_mediacenter_wifi/
%{_kf5_servicesdir}/bigscreensettings.desktop
%{_kf5_servicesdir}/kcm_mediacenter_audiodevice.desktop
%{_kf5_servicesdir}/mediacenter_kdeconnect.desktop
%{_kf5_servicesdir}/mediacenter_wifi.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.mycroft.bigscreen.homescreen.desktop
%{_kf5_servicesdir}/plasma-applet-org.kde.plasma.mycroft.bigscreen.desktop
%{_kf5_servicesdir}/plasma-lookandfeel-org.kde.plasma.mycroft.bigscreen.desktop
%{_kf5_appstreamdir}/org.kde.mycroft.bigscreen.homescreen.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.mycroft.bigscreen.appdata.xml
%{_kf5_appstreamdir}/org.kde.plasma.mycroft.bigscreen.metainfo.xml
%dir %{_kf5_plasmadir}/look-and-feel/
%{_kf5_plasmadir}/look-and-feel/org.kde.plasma.mycroft.bigscreen/
%dir %{_kf5_plasmadir}/plasmoids/
%{_kf5_plasmadir}/plasmoids/org.kde.mycroft.bigscreen.homescreen/
%dir %{_kf5_plasmadir}/shells/
%{_kf5_plasmadir}/shells/org.kde.plasma.mycroft.bigscreen/
%{_kf5_sharedir}/sounds/plasma-bigscreen/
%dir %{_kf5_sharedir}/wayland-sessions/
%{_kf5_sharedir}/wayland-sessions/plasma-bigscreen-wayland.desktop
%{_kf5_sharedir}/xsessions/plasma-bigscreen-x11.desktop

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
