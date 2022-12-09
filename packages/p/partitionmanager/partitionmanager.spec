#
# spec file for package partitionmanager
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


%bcond_without released
Name:           partitionmanager
Version:        22.12.0
Release:        0
Summary:        Easily manage disks, partitions and file systems on your KDE Desktop
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/partitionmanager
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.73
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
# Update for each minor change
BuildRequires:  cmake(KPMcore) >= 21.12
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(Qt5Core) >= 5.14.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      partitionmanager5 < %{version}
Provides:       partitionmanager5 = %{version}

%description
This software allows you to manage your disks, partitions and
file systems: Create, resize, delete, copy, backup and restore
partitions with a large number of supported file systems (ext2/3,
reiserfs, NTFS, FAT32 and more). It makes use of external
programs to get its job done, so you might have to install
additional software (preferably packages from your distribution)
to make use of all features and get full support for all file
systems.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang partitionmanager
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.partitionmanager

%files
%doc README.md
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/partitionmanager/
%dir %{_kf5_sharedir}/solid
%dir %{_kf5_sharedir}/solid/actions
%{_kf5_applicationsdir}/org.kde.partitionmanager.desktop
%{_kf5_appstreamdir}/org.kde.partitionmanager.appdata.xml
%{_kf5_bindir}/partitionmanager
%{_kf5_configkcfgdir}/partitionmanager.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/partitionmanager.svg
%{_kf5_kxmlguidir}/partitionmanager/
%{_kf5_sharedir}/solid/actions/open_in_partitionmanager.desktop

%files lang -f partitionmanager.lang

%changelog
