#
# spec file for package kapptemplate
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
Name:           kapptemplate
Version:        24.05.2
Release:        0
Summary:        Template for KDE Application Development
License:        GPL-2.0-only AND GFDL-1.2-only
URL:            https://apps.kde.org/kapptemplate
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
# Disabled upstream
# BuildRequires:  cmake(KF6NewStuff) >= %%{kf6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kapptemplate5 < %{version}
Provides:       kapptemplate5 = %{version}

%description
This package contains templates to start the development of a new KDE
application/part/plugin.

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
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/org.kde.kapptemplate.desktop
%{_kf6_appstreamdir}/org.kde.kapptemplate.appdata.xml
%{_kf6_bindir}/kapptemplate
%{_kf6_configkcfgdir}/kapptemplate.kcfg
%{_kf6_debugdir}/kapptemplate.categories
%{_kf6_iconsdir}/hicolor/*/apps/kapptemplate.*
%{_kf6_sharedir}/kdevappwizard/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
