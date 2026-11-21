#
# spec file for package plasma6-kup
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.30.0
%define qt6_version 6.11.0

%define rname kup
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released

Name:           plasma6-kup
Version:        6.8.3
Release:        0
Summary:        A KDE-based frontend for the bup backup software
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/kup
Source0:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libgit2)
Requires:       kde-cli-tools6
Requires:       systemsettings6
# It can create two types of backups
Requires:       (bup or rsync)
Provides:       kup-backup = %{version}
Obsoletes:      kup-backup < %{version}
Recommends:     bup
Recommends:     rsync

%description
Kup consists of multiple parts:

- A configuration module, available in systemsettings
- A small program running in the background for monitoring and running the schedule plans
- A KIO worker for accessing bup archives
- A file browsing application for bup archives

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%doc README.md
%license LICENSES/*
%{_kf6_applicationsdir}/kcm_kup.desktop
%{_kf6_applicationsdir}/kup-daemon.desktop
%{_kf6_appstreamdir}/org.kde.kup.appdata.xml
%{_kf6_bindir}/kup-daemon
%{_kf6_bindir}/kup-filedigger
%{_kf6_bindir}/kup-purger
%{_kf6_configdir}/autostart/kup-daemon.desktop
%{_kf6_debugdir}/kup.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/kup.svg
%{_kf6_notificationsdir}/kupdaemon.notifyrc
%dir %{_kf6_plugindir}/kf6/kfileitemaction/
%{_kf6_plugindir}/kf6/kfileitemaction/kupfileitemaction.so
%{_kf6_plugindir}/kf6/kio/kio_bup.so
%{_kf6_plugindir}/plasma/applets/org.kde.kupapplet.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kup.so

%files lang -f %{name}.lang

%changelog
