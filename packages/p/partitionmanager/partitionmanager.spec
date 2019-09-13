#
# spec file for package partitionmanager
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_without lang

Name:           partitionmanager
Version:        3.3.1
Release:        0
Url:            https://www.kde.org/applications/system/kdepartitionmanager/
Source:         http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Summary:        Easily manage disks, partitions and file systems on your KDE Desktop
License:        GPL-3.0-only
Group:          Productivity/File utilities
BuildRequires:  extra-cmake-modules >= 1.0.0
BuildRequires:  kf5-filesystem
BuildRequires:  libatasmart-devel
BuildRequires:  libblkid-devel
BuildRequires:  parted-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config) >= 5.31.0
BuildRequires:  cmake(KF5ConfigWidgets) >= 5.31.0
BuildRequires:  cmake(KF5CoreAddons) >= 5.31.0
BuildRequires:  cmake(KF5Crash) >= 5.31.0
BuildRequires:  cmake(KF5DocTools) >= 5.31.0
BuildRequires:  cmake(KF5I18n) >= 5.31.0
BuildRequires:  cmake(KF5IconThemes) >= 5.31.0
BuildRequires:  cmake(KF5JobWidgets) >= 5.31.0
BuildRequires:  cmake(KF5KIO) >= 5.31.0
BuildRequires:  cmake(KF5Service) >= 5.31.0
BuildRequires:  cmake(KF5WidgetsAddons) >= 5.31.0
BuildRequires:  cmake(KF5XmlGui) >= 5.31.0
BuildRequires:  cmake(KPMcore) >= %(echo %{version} | awk -F. '{print $1"."$2}')
BuildRequires:  cmake(Qt5Core) >= 5.7.0
BuildRequires:  cmake(Qt5Gui) >= 5.7.0
BuildRequires:  cmake(Qt5Widgets) >= 5.7.0
# A file moved from -lang into the main package
Conflicts:      %{name}-lang < %{version}-%{release}
Recommends:     %{name}-lang = %{version}
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
%setup -q

%build
  %cmake_kf5 -d build -- -DKDE_INSTALL_USE_QT_SYS_PATHS=OFF
  %make_jobs

%install
  %kf5_makeinstall -C build
  %suse_update_desktop_file org.kde.partitionmanager
  %if %{with lang}
    %find_lang partitionmanager
    %kf5_find_htmldocs
  %endif

%files
%doc README.md
%license COPYING.GPL3
%{_kf5_bindir}/partitionmanager
%{_kf5_appstreamdir}/org.kde.partitionmanager.appdata.xml
%{_kf5_applicationsdir}/org.kde.partitionmanager.desktop
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/partitionmanager.svg
%{_kf5_kxmlguidir}/partitionmanager/
%doc %lang(en) %{_kf5_htmldir}/en/partitionmanager/

%if %{with lang}
%files lang -f partitionmanager.lang
%endif

%changelog
