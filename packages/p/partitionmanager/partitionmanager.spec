#
# spec file for package partitionmanager
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
Name:           partitionmanager
Version:        24.05.1
Release:        0
Summary:        Easily manage disks, partitions and file systems on your KDE Desktop
License:        GPL-3.0-or-later
URL:            https://apps.kde.org/partitionmanager
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPMcore)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
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
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang partitionmanager --with-html

%files
%doc README.md
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/partitionmanager/
%{_kf6_applicationsdir}/org.kde.partitionmanager.desktop
%{_kf6_appstreamdir}/org.kde.partitionmanager.appdata.xml
%{_kf6_bindir}/partitionmanager
%{_kf6_configkcfgdir}/partitionmanager.kcfg
%{_kf6_iconsdir}/hicolor/*/apps/partitionmanager.svg
%dir %{_kf6_sharedir}/solid
%dir %{_kf6_sharedir}/solid/actions
%{_kf6_sharedir}/solid/actions/open_in_partitionmanager.desktop

%files lang -f partitionmanager.lang
%exclude %{_kf6_htmldir}/en/partitionmanager/

%changelog
