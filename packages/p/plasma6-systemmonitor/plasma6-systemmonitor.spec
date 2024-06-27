#
# spec file for package plasma6-systemmonitor
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname plasma-systemmonitor

%bcond_without released
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           plasma6-systemmonitor
Version:        6.1.1
Release:        0
Summary:        An application for monitoring system resources
License:        GPL-3.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kiconthemes-imports >= %{kf6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       kf6-knewstuff-imports >= %{kf6_version}
Requires:       kf6-kquickcharts >= %{kf6_version}
Requires:       kf6-qqc2-desktop-style >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       ksystemstats6 >= %{_plasma6_bugfix}
Requires:       qt6-declarative-imports >= %{qt6_version}
Provides:       plasma5-systemmonitor = %{version}
Obsoletes:      plasma5-systemmonitor < %{version}
Obsoletes:      plasma5-systemmonitor-lang < %{version}

%description
plasma-systemmonitor provides an interface for monitoring system sensors,
process information and other system resources.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%suse_update_desktop_file org.kde.plasma-systemmonitor System Monitor

%fdupes %{buildroot}%{_kf6_sharedir}

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.plasma-systemmonitor.desktop
%{_kf6_appstreamdir}/org.kde.plasma-systemmonitor.metainfo.xml
%{_kf6_bindir}/plasma-systemmonitor
%{_kf6_configkcfgdir}/systemmonitor.kcfg
%{_kf6_knsrcfilesdir}/plasma-systemmonitor.knsrc
# FIXME result of 105cb99d & bb8d4048
%{_kf6_libdir}/libPlasmaSystemMonitorPage.so
%{_kf6_libdir}/libPlasmaSystemMonitorTable.so
%dir %{_kf6_qmldir}/org/kde/ksysguard/
%{_kf6_qmldir}/org/kde/ksysguard/page/
%{_kf6_qmldir}/org/kde/ksysguard/table/
%dir %{_kf6_sharedir}/ksysguard/
%{_kf6_sharedir}/ksysguard/sensorfaces/
%{_kf6_sharedir}/plasma-systemmonitor/
%dir %{_kf6_sharedir}/plasma/kinfocenter/
%dir %{_kf6_sharedir}/plasma/kinfocenter/externalmodules/
%{_kf6_sharedir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%dir %{_kf6_sharedir}/kglobalaccel/
%{_kf6_sharedir}/kglobalaccel/org.kde.plasma-systemmonitor.desktop

%files lang -f %{name}.lang

%changelog
