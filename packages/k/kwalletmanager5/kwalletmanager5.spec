#
# spec file for package kwalletmanager5
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


%define rname   kwalletmanager
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kwalletmanager5
Version:        22.12.0
Release:        0
Summary:        Wallet Management Tool
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kwalletmanager5
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
Provides:       kwalletmanager = %{version}
Obsoletes:      kwalletmanager < %{version}

%description
This application allows you to manage your KDE password wallet.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/*/
%{_kf5_applicationsdir}/*kwalletmanager5*.desktop
%{_kf5_appstreamdir}/org.kde.kwalletmanager5.appdata.xml
%{_kf5_bindir}/kwalletmanager5
%{_kf5_dbuspolicydir}/org.kde.kcontrol.kcmkwallet5.conf
%{_kf5_debugdir}/kwalletmanager.categories
%{_kf5_iconsdir}/hicolor/*/*/*.*
%{_kf5_plugindir}/kcm_kwallet5.so
%{_kf5_servicesdir}/kwalletconfig5.desktop
%{_kf5_servicesdir}/kwalletmanager5_show.desktop
%{_kf5_sharedir}/dbus-1/services/org.kde.kwalletmanager5.service
%{_kf5_sharedir}/dbus-1/system-services/org.kde.kcontrol.kcmkwallet5.service
%{_kf5_sharedir}/polkit-1/actions/org.kde.kcontrol.kcmkwallet5.policy
%{_libexecdir}/kauth/kcm_kwallet_helper5

%files lang -f %{name}.lang

%changelog
