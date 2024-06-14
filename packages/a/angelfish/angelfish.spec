#
# spec file for package angelfish
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           angelfish
Version:        24.05.1
Release:        0
Summary:        Mobile web browser
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/angelfish
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        vendor.tar.zst
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-core-private-devel >= %{qt6_version}
BuildRequires:  qt6-webenginequick-private-devel >= %{qt6_version}
BuildRequires:  zstd
BuildRequires:  cmake(Corrosion)
BuildRequires:  cmake(FutureSQL6)
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.6
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core) >= 0.7.0
BuildRequires:  cmake(QCoro6Quick) >= 0.7.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineCore) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineQuick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-sql-sqlite >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Angelfish is a mobile web browser. It supports typical browser features, such
as bookmarks, history and tabs.

%prep
%autosetup -p1 -a3

%lang_package

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%doc README.md
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.angelfish.desktop
%{_kf6_appstreamdir}/org.kde.angelfish.metainfo.xml
%{_kf6_bindir}/angelfish
%{_kf6_bindir}/angelfish-webapp
%{_kf6_configkcfgdir}/angelfishsettings.kcfg
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.angelfish.svg
%{_kf6_notificationsdir}/angelfish.notifyrc

%files lang -f %{name}.lang

%changelog
