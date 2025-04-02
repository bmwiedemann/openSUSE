#
# spec file for package kio-stash
#
# Copyright (c) 2025 SUSE LLC
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


%define kf6_version 6.8
%define qt6_version 6.6

Name:           kio-stash
Version:        1.0git.20250301T021103~51f07b6
Release:        0
Summary:        KIO slave for stashing temporary files
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
BuildRequires:  intltool
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}

%description
This KIO slave can be used to stash files in a virtual
folder temporarily. It requires use of a KIO-compatible
file manager, like dolphin.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_kf6_appstreamdir}/org.kde.filestash.appdata.xml
%{_kf6_dbusinterfacesdir}/org.kde.kio.StashNotifier.xml
%dir %{_kf6_plugindir}/kf6/kded
%{_kf6_plugindir}/kf6/kded/stashnotifier.so
%{_kf6_plugindir}/kf6/kio/filestash.so

%files lang -f %{name}.lang

%changelog
