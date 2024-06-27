#
# spec file for package bluedevil6
#
# Copyright (c) 2024 SUSE LLC
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


# Internal QML import
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.plasma\\.private\\.bluetooth.*

%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname bluedevil

%bcond_without released
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           bluedevil6
Version:        6.1.1
Release:        0
Summary:        Bluetooth Manager for KDE Plasma
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6BluezQt) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# atop of the bluez itself, we also need bluez-obexd for kio_obexftp and both send/receive
Requires:       bluez
Requires:       kf6-bluez-qt-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
# for connecting A2DP profile
Recommends:     (pulseaudio-module-bluetooth if pulseaudio)
Supplements:    (bluez and plasma6-workspace)
Provides:       bluedevil5 = %{version}
Obsoletes:      bluedevil5 < %{version}
Obsoletes:      bluedevil5-lang < %{version}

%description
Bluetooth daemon for KDE Plasma, handling connections.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol
%{_kf6_applicationsdir}/kcm_bluetooth.desktop
%{_kf6_applicationsdir}/org.kde.bluedevilsendfile.desktop
%{_kf6_applicationsdir}/org.kde.bluedevilwizard.desktop
%{_kf6_appstreamdir}/org.kde.plasma.bluetooth.appdata.xml
%{_kf6_bindir}/bluedevil-sendfile
%{_kf6_bindir}/bluedevil-wizard
%{_kf6_debugdir}/bluedevil.categories
%{_kf6_notificationsdir}/bluedevil.notifyrc
%{_kf6_plasmadir}/plasmoids/org.kde.plasma.bluetooth/
%{_kf6_plugindir}/kf6/kded/bluedevil.so
%{_kf6_plugindir}/kf6/kio/kio_bluetooth.so
%{_kf6_plugindir}/kf6/kio/kio_obexftp.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_bluetooth.so
%dir %{_kf6_qmldir}/org/kde/plasma/private
%{_kf6_qmldir}/org/kde/plasma/private/bluetooth/
%dir %{_kf6_sharedir}/bluedevilwizard
%{_kf6_sharedir}/bluedevilwizard/pin-code-database.xml
%{_kf6_sharedir}/mime/packages/bluedevil-mime.xml
%dir %{_kf6_sharedir}/remoteview
%{_kf6_sharedir}/remoteview/bluetooth-network.desktop

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol

%changelog
