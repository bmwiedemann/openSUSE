#
# spec file for package kpmcore
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.14.0
%define qt6_version 6.8.0

%bcond_without released
Name:           kpmcore
Version:        25.08.1
Release:        0
Summary:        KDE Partition Manager core library
License:        GPL-3.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(blkid) >= 2.33.2

%description
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

%package devel
Summary:        Development package for KDE Partition Manager core library
Requires:       libkpmcore13 = %{version}

%description devel
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

Development package for kpmcore.

%package -n libkpmcore13
Summary:        KDE Partition Manager core library
Requires:       kpmcore >= %{version}
Obsoletes:      libkpmcore12

%description -n libkpmcore13
Library for managing partitions. Common code for KDE Partition Manager and
other projects.

Main kpmcore library.

%lang_package

%prep
%autosetup -p1

%build

%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang kpmcore --all-name

%ldconfig_scriptlets -n libkpmcore13

%files
%{_kf6_dbuspolicydir}/org.kde.kpmcore.*.conf
%{_kf6_plugindir}/kpmcore/
%{_kf6_sharedir}/dbus-1/system-services/org.kde.kpmcore.helperinterface.service
%{_kf6_sharedir}/polkit-1/actions/org.kde.kpmcore.externalcommand.policy
%{_libexecdir}/kpmcore_externalcommand

%files -n libkpmcore13
%license LICENSES/*
%{_kf6_libdir}/libkpmcore.so.*

%files devel
%{_includedir}/kpmcore/
%{_kf6_cmakedir}/KPMcore/
%{_kf6_libdir}/libkpmcore.so

%files lang -f %{name}.lang

%changelog
