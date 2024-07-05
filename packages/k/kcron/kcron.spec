#
# spec file for package kcron
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
Name:           kcron
Version:        24.05.2
Release:        0
Summary:        Cron job configuration tool
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules  >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kcron5 < %{version}
Provides:       kcron5 = %{version}

%description
KCron allows you to change your cron jobs setup.

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
%doc README
%{_kf6_applicationsdir}/kcm_cron.desktop
%{_kf6_appstreamdir}/org.kde.kcron.metainfo.xml
%{_kf6_dbuspolicydir}/local.kcron.crontab.conf
%{_kf6_debugdir}/kcron.categories
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_cron.so
%{_kf6_sharedir}/dbus-1/system-services/local.kcron.crontab.service
%{_kf6_sharedir}/polkit-1/actions/local.kcron.crontab.policy
%{_kf6_libexecdir}/kauth/kcron_helper

%files lang -f %{name}.lang

%changelog
