#
# spec file for package kcron
#
# Copyright (c) 2022 SUSE LLC
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kcron
Version:        22.12.1
Release:        0
Summary:        Cron job configuration tool
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
KCron allows you to change your cron jobs setup.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol5/
%dir %{_libexecdir}/kauth
%{_kf5_appstreamdir}/org.kde.kcron.metainfo.xml
%{_kf5_dbuspolicydir}/local.kcron.crontab.conf
%{_kf5_debugdir}/kcron.categories
%{_kf5_plugindir}/kcm_cron.so
%{_kf5_servicesdir}/kcm_cron.desktop
%{_kf5_sharedir}/dbus-1/system-services/local.kcron.crontab.service
%{_kf5_sharedir}/polkit-1/actions/local.kcron.crontab.policy
%{_libexecdir}/kauth/kcron_helper

%files lang -f %{name}.lang

%changelog
