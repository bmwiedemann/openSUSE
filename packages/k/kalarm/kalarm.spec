#
# spec file for package kalarm
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kalarm
Version:        20.08.2
Release:        0
Summary:        Personal Alarm Scheduler
License:        GPL-2.0-only
Group:          Productivity/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-devel
BuildRequires:  libxslt-devel
BuildRequires:  polkit-default-privs
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5AlarmCalendar)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5CalendarUtils)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5Holidays)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailCommon)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5DBus) >= 5.2.0
BuildRequires:  cmake(Qt5Gui) >= 5.2.0
BuildRequires:  cmake(Qt5Network) >= 5.2.0
BuildRequires:  cmake(Qt5Widgets) >= 5.2.0
BuildRequires:  cmake(Qt5X11Extras) >= 5.2.0
Recommends:     %{name}-lang
Provides:       kalarm5 = %{version}
Obsoletes:      kalarm5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  libboost_headers-devel

%description
Personal alarm message, command and email scheduler for KDE

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%suse_update_desktop_file org.kde.kalarm          Utility  TimeUtility

%files
%license COPYING COPYING.LIB COPYING.DOC
%doc README
%{_kf5_debugdir}/kalarm.categories
%{_kf5_debugdir}/kalarm.renamecategories
%{_kf5_dbuspolicydir}/org.kde.kalarm.rtcwake.conf
%dir %{_libdir}/libexec/kauth/
%{_kf5_applicationsdir}/org.kde.kalarm.desktop
%{_kf5_appstreamdir}/org.kde.kalarm.appdata.xml
%{_kf5_bindir}/kalarm*
%config %{_kf5_configdir}/autostart/kalarm.autostart.desktop
%{_kf5_configkcfgdir}/kalarmconfig.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kalarm.kalarm.xml
%doc %lang(en) %{_kf5_htmldir}/en/kalarm/
%{_kf5_iconsdir}/hicolor/*/apps/kalarm.png
%{_kf5_libdir}/libexec/kauth/kalarm_helper
%{_kf5_kxmlguidir}/kalarm/
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kalarm.rtcwake.service
%{_kf5_sharedir}/kalarm/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/polkit-1/actions/org.kde.kalarm.rtcwake.policy

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
