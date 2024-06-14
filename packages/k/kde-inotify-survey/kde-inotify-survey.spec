#
# spec file for package kde-inotify-survey
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
Name:           kde-inotify-survey
Version:        24.05.1
Release:        0
Summary:        Monitor inotify limits and inform the user when they are reached
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}

%description
Tooling for monitoring inotify limits and informing the user
when they have been or are about to be reached.

%lang_package

%prep
%autosetup -p1

# No technical reason to require cmake 3.22
sed -i 's#VERSION 3.22#VERSION 3.20#' CMakeLists.txt

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy
%{_kf6_appstreamdir}/org.kde.inotify-survey.metainfo.xml
%{_kf6_bindir}/kde-inotify-survey
%{_kf6_dbuspolicydir}/org.kde.kded.inotify.conf
%{_kf6_libexecdir}/kauth/kded-inotify-helper
%{_kf6_notificationsdir}/org.kde.kded.inotify.notifyrc
%{_kf6_plugindir}/kf6/kded/inotify.so

%files lang -f %{name}.lang

%changelog
