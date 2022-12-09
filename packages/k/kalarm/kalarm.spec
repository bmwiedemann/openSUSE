#
# spec file for package kalarm
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kalarm
Version:        22.12.0
Release:        0
Summary:        Personal Alarm Scheduler
License:        GPL-2.0-only
URL:            https://apps.kde.org/kalarm
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
BuildRequires:  libxslt-devel
BuildRequires:  polkit-default-privs
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IMAP)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5MailTransportAkonadi)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Gui) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.15.0
Provides:       kalarm5 = %{version}
Obsoletes:      kalarm5 < %{version}

%description
Personal alarm message, command and email scheduler by KDE.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kalarm Utility TimeUtility

%files
%license LICENSES/*
%doc README
%config %{_kf5_configdir}/autostart/kalarm.autostart.desktop
%doc %lang(en) %{_kf5_htmldir}/en/kalarm/
%{_kf5_applicationsdir}/org.kde.kalarm.desktop
%{_kf5_appstreamdir}/org.kde.kalarm.appdata.xml
%{_kf5_bindir}/kalarm*
%{_kf5_configkcfgdir}/kalarmconfig.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kalarm.kalarm.xml
%{_kf5_dbuspolicydir}/org.kde.kalarm.rtcwake.conf
%{_kf5_debugdir}/kalarm.categories
%{_kf5_debugdir}/kalarm.renamecategories
%{_kf5_iconsdir}/hicolor/*/apps/kalarm.png
%{_kf5_kxmlguidir}/kalarm/
%{_kf5_libdir}/libkalarmcalendar.so.*
%{_kf5_libdir}/libkalarmplugin.so.*
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/kalarm/
%{_kf5_plugindir}/pim5/kalarm/akonadiplugin.so
%{_kf5_notifydir}/kalarm.notifyrc
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kalarm.rtcwake.service
%{_kf5_sharedir}/kalarm/
%{_kf5_sharedir}/polkit-1/actions/org.kde.kalarm.rtcwake.policy
%{_libexecdir}/kauth/kalarm_helper

%files lang -f %{name}.lang

%changelog
