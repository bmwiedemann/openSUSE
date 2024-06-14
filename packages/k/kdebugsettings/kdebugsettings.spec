#
# spec file for package kdebugsettings
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
Name:           kdebugsettings
Version:        24.05.1
Release:        0
Summary:        Program to set debug verbosity for KDE applications
License:        LGPL-2.0-or-later
URL:            https://apps.kde.org/kdebugsettings
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kdebugsettings5 < %{version}
Provides:       kdebugsettings5 = %{version}

%description
This program allows to tune the debug output of KDE applications, ranging
from verbose to completely silent.

%lang_package

%prep
%autosetup -p1 -n kdebugsettings-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%suse_update_desktop_file org.kde.kdebugsettings Utility DesktopUtility

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.kdebugsettings.desktop
%{_kf6_appstreamdir}/org.kde.kdebugsettings.appdata.xml
%{_kf6_bindir}/kdebugsettings
%{_kf6_debugdir}/kde.renamecategories
%{_kf6_debugdir}/kdebugsettings.categories
%{_kf6_libdir}/libkdebugsettings.so.*
%{_kf6_libdir}/libkdebugsettingscore.so.*
%{_kf6_sharedir}/kdebugsettings/

%files lang -f %{name}.lang

%changelog
