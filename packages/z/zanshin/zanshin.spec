#
# spec file for package zanshin
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           zanshin
Version:        24.05.1
Release:        0
Summary:        TODO Application
License:        GPL-2.0-only
URL:            https://zanshin.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  boost-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6CalendarCore) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiCalendar) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KontactInterface) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Zanshin Todo is an application for managing your day-to-day actions.
It helps you organize and reduce the cognitive pressure of what one has to do in his
job and personal life. You will never forget anything anymore.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%suse_update_desktop_file org.kde.zanshin Utility TimeUtility

%find_lang %{name}

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.zanshin.desktop
%{_kf6_appstreamdir}/org.kde.zanshin.metainfo.xml
%{_kf6_bindir}/zanshin
%{_kf6_bindir}/zanshin-migrator
%{_kf6_iconsdir}/hicolor/*/apps/zanshin.png
%{_kf6_iconsdir}/hicolor/scalable/apps/zanshin.svgz
%dir %{_kf6_plugindir}/kf6/krunner
%{_kf6_plugindir}/kf6/krunner/org.kde.zanshin.so
%dir %{_kf6_plugindir}/pim6
%dir %{_kf6_plugindir}/pim6/kontact
%{_kf6_plugindir}/pim6/kontact/kontact_zanshinplugin.so
%{_kf6_plugindir}/zanshin_part.so

%files lang -f %{name}.lang

%changelog
