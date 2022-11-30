#
# spec file for package bluedevil5
#
# Copyright (c) 2022 SUSE LLC
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
%global __requires_exclude qmlimport\\(org\\.kde\\.bluedevil\\.kcm.*

%bcond_without released
Name:           bluedevil5
Version:        5.26.4
Release:        0
Summary:        Bluetooth Manager for KDE Plasma
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/bluedevil-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/bluedevil-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KDED) >= 5.98.0
BuildRequires:  cmake(KF5BluezQt)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Widgets)
Requires:       bluez-qt-imports >= %{version}
Requires:       bluez-qt-udev >= %{version}
# atop of the bluez itself, we also need bluez-obexd for kio_obexftp and both send/receive
Requires:       bluez
# for connecting A2DP profile
Recommends:     (pulseaudio-module-bluetooth if pulseaudio)
Recommends:     %{name}-lang
Supplements:    packageand(bluez:plasma5-workspace)
Conflicts:      bluedevil
Requires(post): shared-mime-info
Requires(postun):shared-mime-info

%description
Bluetooth daemon for KDE Plasma, handling connections.

%lang_package

%prep
%setup -q -n bluedevil-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with released}
%kf5_find_lang
%kf5_find_htmldocs
%endif

%post
%mime_database_post

%postun
%mime_database_postun

%files
%license LICENSES/*
%doc README
%dir %{_kf5_appstreamdir}/
%dir %{_kf5_sharedir}/kpackage
%dir %{_kf5_sharedir}/kpackage/kcms
%dir %{_kf5_htmldir}/en/kcontrol
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/bluedevil/
%{_kf5_applicationsdir}/kcm_bluetooth.desktop
%{_kf5_debugdir}/bluedevil.categories
%{_kf5_sharedir}/kpackage/kcms/kcm_bluetooth/
%{_kf5_sharedir}/mime/packages/bluedevil-mime.xml
%{_kf5_applicationsdir}/org.kde.bluedevil*.desktop
%{_kf5_sharedir}/bluedevilwizard/
%{_kf5_bindir}/bluedevil-*
%{_kf5_sharedir}/remoteview/
%{_kf5_notifydir}/
%{_kf5_plugindir}/
%{_kf5_servicesdir}/
%{_kf5_qmldir}/
%{_kf5_plasmadir}/
%{_kf5_appstreamdir}/*.xml

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
