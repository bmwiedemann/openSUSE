#
# spec file for package kup-backup
#
# Copyright (c) 2020 SUSE LLC
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


%define rname kup
%bcond_without lang
Name:           kup-backup
Version:        0.8.0
Release:        0
Summary:        Backup scheduler for the Plasma desktop
License:        GPL-2.0-only AND GPL-3.0-only
Group:          System/GUI/KDE
URL:            https://invent.kde.org/kde/kup
Source0:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/%{rname}/%{rname}-%{version}.tar.xz.sig
Source2:        %{rname}.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  libgit2-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5Init)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Widgets) >= 5.11.0
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
%setup -q -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
%find_lang %{rname}
%endif

%files
%license LICENSES/*
%doc README.md
%{_kf5_appstreamdir}/*.xml
%{_kf5_bindir}/kup-daemon
%{_kf5_bindir}/kup-filedigger
%{_kf5_configdir}/autostart/kup-daemon.desktop
%{_kf5_iconsdir}/hicolor/scalable/apps/kup.svgz
%{_kf5_libdir}/libkdeinit5_kup-daemon.so
%{_kf5_notifydir}/kupdaemon.notifyrc
%{_kf5_plugindir}/kcm_kup.so
%{_kf5_plugindir}/kio_bup.so
%{_kf5_plugindir}/plasma/
%{_kf5_sharedir}/plasma/
%{_kf5_servicesdir}

%if %{with lang}
%files lang -f %{rname}.lang
%license LICENSES/*
%endif

%changelog
