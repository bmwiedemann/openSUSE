#
# spec file for package kup-backup
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


%define kf6_version 6.1.0
%define qt6_version 6.6.0

%define rname kup
%bcond_without released
Name:           kup-backup
Version:        0.10.0
Release:        0
Summary:        Backup scheduler for the Plasma desktop
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/kup/
Source0:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz.sig
Source2:        kup.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= 6.0
BuildRequires:  cmake(Plasma5Support) >= 6.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libgit2)
Requires:       systemsettings6
Recommends:     bup
Recommends:     rsync

%description
Kup is created for helping people to keep up-to-date backups of their personal files.
Connecting a USB hard drive is the primary supported way to store files, but saving
files to a server over a network connection is also possible for advanced users.

When you plug in your external hard drive Kup will automatically start copying your
latest changes, but of course it will only do so if you have been active on your
computer for some number of hours since the last time you took a backup (and it can
of course ask you first, before copying anything). In general Kup tries to not
disturb you needlessly.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/kcm_kup.desktop
%{_kf6_appstreamdir}/org.kde.kup.appdata.xml
%{_kf6_appstreamdir}/org.kde.kupapplet.appdata.xml
%{_kf6_bindir}/kup-daemon
%{_kf6_bindir}/kup-filedigger
%{_kf6_bindir}/kup-purger
%{_kf6_configdir}/autostart/kup-daemon.desktop
%{_kf6_debugdir}/kup.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/kup.svg
%{_kf6_notificationsdir}/kupdaemon.notifyrc
%{_kf6_plasmadir}/plasmoids/org.kde.kupapplet/
%{_kf6_plugindir}/kf6/kio/kio_bup.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kup.so
%{_kf6_plugindir}/plasma5support
%dir %{_kf6_plugindir}/plasma5support/dataengine
%{_kf6_plugindir}/plasma5support/dataengine/plasma_engine_kup.so
%dir %{_kf6_sharedir}/plasma5support
%dir %{_kf6_sharedir}/plasma5support/services
%{_kf6_sharedir}/plasma5support/services/kupdaemonservice.operations
%{_kf6_sharedir}/plasma5support/services/kupservice.operations

%files lang -f %{name}.lang

%changelog
