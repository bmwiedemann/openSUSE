#
# spec file for package plasma5-firewall
#
# Copyright (c) 2021 SUSE LLC
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


# Internal QML imports
%global __requires_exclude qmlimport\\(org\\.kcm\\.firewall

%bcond_without lang
Name:           plasma5-firewall
Version:        5.21.5
Release:        0
Summary:        Config Module for the System Firewall
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/plasma/%{version}/plasma-firewall-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-firewall-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FEATURE-UPSTREAM
Patch1:         0001-Introduce-cmake-options-to-disable-backends.patch
BuildRequires:  cmake >= 3.8
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  python3-base
BuildRequires:  cmake(KF5CoreAddons) >= 5.30.0
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5PlasmaQuick)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5X11Extras)
Requires:       firewalld
# QML imports
Requires:       kdeclarative-components
Requires:       kirigami2
Requires:       kitemmodels-imports
Requires:       knewstuff-imports
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2

%description
Config Module for the System Firewall

%lang_package

%prep
%autosetup -p1 -n plasma-firewall-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_UFW_BACKEND=OFF
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}

%if %{with lang}
  %find_lang kcm_firewall %{name}.lang
%endif

%files
%license LICENSES/*
%doc README.md
%{_kf5_appstreamdir}/org.kde.plasma.firewall.metainfo.xml
%{_kf5_servicesdir}/kcm_firewall.desktop
%dir %{_kf5_plugindir}/kcms/
%{_kf5_plugindir}/kcms/kcm_firewall.so
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/plasma_firewall/
%{_kf5_plugindir}/kf5/plasma_firewall/firewalldbackend.so
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/kcms/
%{_kf5_sharedir}/kpackage/kcms/kcm_firewall/
%{_kf5_libdir}/libkcm_firewall_core.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
