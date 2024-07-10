#
# spec file for package plasma6-firewall
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

%define rname plasma-firewall

%bcond_without released
Name:           plasma6-firewall
Version:        6.1.2
Release:        0
Summary:        Config Module for the System Firewall
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  python3-base
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Package) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
Requires:       firewalld
# QML imports
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Provides:       plasma5-firewall = %{version}
Obsoletes:      plasma5-firewall < %{version}
Obsoletes:      plasma5-firewall-lang < %{version}

%description
Config Module for the System Firewall

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_UFW_BACKEND:BOOL=FALSE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kcm_firewall %{name}.lang

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/kcm_firewall.desktop
%{_kf6_appstreamdir}/org.kde.plasma.firewall.metainfo.xml
%{_kf6_libdir}/libkcm_firewall_core.so
%dir %{_kf6_plugindir}/kf6/plasma_firewall
%{_kf6_plugindir}/kf6/plasma_firewall/firewalldbackend.so
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_firewall.so

%files lang -f %{name}.lang

%changelog
