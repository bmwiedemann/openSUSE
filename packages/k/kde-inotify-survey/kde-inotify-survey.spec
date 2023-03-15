#
# spec file for package kde-inotify-survey
#
# Copyright (c) 2023 SUSE LLC
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


%define kf5_version 5.93.0
Name:           kde-inotify-survey
Version:        1.0.0
Release:        0
Summary:        Monitor inotify limits and inform the user when they are reached
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.zst
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.zst.sig
Source2:        kde-inotify-survey.keyring
# PATCH-FIX-UPSTREAM
Patch0:          install-i18n.patch
BuildRequires:  cmake >= 3.22
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  zstd
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)

%description
Tooling for monitoring inotify limits and informing the user
when they have been or are about to be reached.

%lang_package

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-qt --with-man --all-name

%files
%license LICENSES/*
%{_kf5_bindir}/kde-inotify-survey
%{_libexecdir}/kauth/kded-inotify-helper
%{_kf5_plugindir}/kf5/kded/inotify.so
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_kf5_dbuspolicydir}/org.kde.kded.inotify.conf
%{_kf5_notifydir}/org.kde.kded.inotify.notifyrc
%{_kf5_appstreamdir}/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy

%files lang -f %{name}.lang

%changelog
