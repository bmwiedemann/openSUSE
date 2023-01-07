#
# spec file for package kdesdk-thumbnailers
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
Name:           kdesdk-thumbnailers
Version:        22.12.1
Release:        0
Summary:        Translation file thumbnail generators
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext-tools
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5Widgets)

%description
This package allows KDE applications to show thumbnails
and previews of po files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/thumbcreator
%{_kf5_configkcfgdir}/pocreatorsettings.kcfg
%{_kf5_plugindir}/kf5/thumbcreator/pothumbnail.so

%files lang -f %{name}.lang

%changelog
