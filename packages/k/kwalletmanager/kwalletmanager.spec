#
# spec file for package kwalletmanager
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.6.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kwalletmanager
Version:        25.04.3
Release:        0
Summary:        Wallet Management Tool
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kwalletmanager
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE -- boo#1217190 don't require password to save settings
Patch0:         0001-Don-t-require-password-when-changing-settings.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Provides:       kwalletmanager5 = %{version}
Obsoletes:      kwalletmanager5 < %{version}
Obsoletes:      kwalletmanager5-lang < %{version}

%description
This application allows you to manage your KDE password wallet.

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
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/kwalletmanager5-kwalletd.desktop
%{_kf6_applicationsdir}/org.kde.kwalletmanager.desktop
%{_kf6_appstreamdir}/org.kde.kwalletmanager5.appdata.xml
%{_kf6_bindir}/kwalletmanager5
%{_kf6_debugdir}/kwalletmanager.categories
%{_kf6_iconsdir}/hicolor/*/*/*.*
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kwallet5.so
%{_kf6_sharedir}/dbus-1/services/org.kde.kwalletmanager.service

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
