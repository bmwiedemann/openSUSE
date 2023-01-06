#
# spec file for package plasma5-systemmonitor
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


%define kf5_version 5.98.0
%bcond_without released
Name:           plasma5-systemmonitor
Version:        5.26.5
Release:        0
Summary:        An application for monitoring system resources
License:        GPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/plasma/%{version}/plasma-systemmonitor-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-systemmonitor-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5ItemModels) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5NewStuff) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KSysGuard)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kdeclarative-components
Requires:       kirigami2
Requires:       kitemmodels-imports
Requires:       knewstuff-imports
Requires:       kquickcharts
Requires:       ksystemstats5
Requires:       libqt5-qtquickcontrols2
Requires:       qqc2-desktop-style

%description
plasma-systemmonitor provides an interface for monitoring system sensors,
process information and other system resources.

%lang_package

%prep
%autosetup -p1 -n plasma-systemmonitor-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%make_install -C build
%suse_update_desktop_file org.kde.plasma-systemmonitor System Monitor
%fdupes %{buildroot}/%{_kf5_sharedir}

%if %{with released}
  %find_lang %{name} --with-man --all-name
%endif

%files
%license LICENSES/*
%doc README.md
%{_kf5_bindir}/plasma-systemmonitor
%dir %{_kf5_qmldir}/org/kde/ksysguard/
%{_kf5_qmldir}/org/kde/ksysguard/page/
%{_kf5_qmldir}/org/kde/ksysguard/table/
%{_kf5_applicationsdir}/org.kde.plasma-systemmonitor.desktop
%{_kf5_configkcfgdir}/systemmonitor.kcfg
%{_kf5_knsrcfilesdir}/plasma-systemmonitor.knsrc
%dir %{_kf5_sharedir}/ksysguard/
%{_kf5_sharedir}/ksysguard/sensorfaces/
%{_kf5_sharedir}/plasma-systemmonitor/
%dir %{_kf5_sharedir}/plasma/
%dir %{_kf5_sharedir}/plasma/kinfocenter/
%dir %{_kf5_sharedir}/plasma/kinfocenter/externalmodules/
%{_kf5_sharedir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
%{_kf5_appstreamdir}/org.kde.plasma-systemmonitor.metainfo.xml

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
