#
# spec file for package systemsettings6
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


%global __requires_exclude qt6qmlimport\\(org\\.kde\\.systemsettings.*

%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname systemsettings
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           systemsettings6
Version:        6.1.0
Release:        0
Summary:        KDE's control center
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-UPSTREAM
Patch1:         0001-runner-Don-t-match-if-just-one-query-word-matches.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6Runner) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(PlasmaActivities) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Provides:       systemsettings5 = %{version}
Obsoletes:      systemsettings5 < %{version}
Obsoletes:      systemsettings5-lang < %{version}

%description
This package provides modules to control settings of Plasma and other
applications by KDE.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name --with-html

%suse_update_desktop_file  kdesystemsettings X-SuSE-core

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/systemsettings/
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_systemsettings
%{_kf6_applicationsdir}/kdesystemsettings.desktop
%{_kf6_applicationsdir}/systemsettings.desktop
%{_kf6_appstreamdir}/org.kde.systemsettings.metainfo.xml
%{_kf6_bindir}/systemsettings
%{_kf6_debugdir}/systemsettings.categories
%dir %{_kf6_plugindir}/kf6/krunner
%{_kf6_plugindir}/kf6/krunner/krunner_systemsettings.so
%{_kf6_sharedir}/kglobalaccel/systemsettings.desktop
%{_kf6_sharedir}/systemsettings/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/systemsettings

%changelog
