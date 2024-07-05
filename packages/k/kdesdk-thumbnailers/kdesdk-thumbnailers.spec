#
# spec file for package kdesdk-thumbnailers
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
Name:           kdesdk-thumbnailers
Version:        24.05.2
Release:        0
Summary:        Translation file thumbnail generators
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
# libgettextpo.so is needed
BuildRequires:  gettext-tools
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This package allows KDE applications to show thumbnails and previews of po files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_configkcfgdir}/pocreatorsettings.kcfg
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/pothumbnail.so

%files lang -f %{name}.lang

%changelog
