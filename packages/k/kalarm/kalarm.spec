#
# spec file for package kalarm
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.2

%bcond_without released
Name:           kalarm
Version:        24.05.2
Release:        0
Summary:        Personal Alarm Scheduler
License:        GPL-2.0-only
URL:            https://apps.kde.org/kalarm
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-breeze-icons
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  polkit-default-privs
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6CalendarUtils) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IdentityManagementWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(x11)
Provides:       kalarm5 = %{version}
Obsoletes:      kalarm5 < %{version}

%description
Personal alarm message, command and email scheduler by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README
%config %{_kf6_configdir}/autostart/kalarm.autostart.desktop
%doc %lang(en) %{_kf6_htmldir}/en/kalarm/
%{_kf6_applicationsdir}/org.kde.kalarm.desktop
%{_kf6_appstreamdir}/org.kde.kalarm.appdata.xml
%{_kf6_bindir}/kalarm
%{_kf6_bindir}/kalarmautostart
%{_kf6_configkcfgdir}/kalarmconfig.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.kalarm.kalarm.xml
%{_kf6_dbuspolicydir}/org.kde.kalarm.rtcwake.conf
%{_kf6_debugdir}/kalarm.categories
%{_kf6_debugdir}/kalarm.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/kalarm.png
%{_kf6_libdir}/libkalarmcalendar.so.*
%{_kf6_libdir}/libkalarmplugin.so.*
%{_kf6_libexecdir}/kauth/kalarm_helper
%{_kf6_notificationsdir}/kalarm.notifyrc
%dir %{_kf6_plugindir}/pim6/
%dir %{_kf6_plugindir}/pim6/kalarm/
%{_kf6_plugindir}/pim6/kalarm/akonadiplugin.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kalarm.rtcwake.service
%{_kf6_sharedir}/kalarm/
%{_kf6_sharedir}/polkit-1/actions/org.kde.kalarm.rtcwake.policy

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kalarm/

%changelog
