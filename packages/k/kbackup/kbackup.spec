#
# spec file for package kbackup
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
Name:           kbackup
Version:        24.05.2
Release:        0
Summary:        Backup program based on KDE Frameworks 5
License:        GPL-2.0-only
URL:            https://apps.kde.org/kbackup
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libarchive)

%description
kbackup is a backup program based on KDE Frameworks 5. It allows backing
folders and files up and setting profiles to exclude or include directories
or files from the backup. It can save to both local files or remote locations.
Although GUI based, it also offers an automated, GUI-less mode.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man --all-name

%files
%license COPYING
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/kbackup
%doc %lang(en) %{_mandir}/man1/kbackup.1%{ext_man}
%{_datadir}/mime/packages/kbackup.xml
%{_kf6_applicationsdir}/org.kde.kbackup.desktop
%{_kf6_appstreamdir}/org.kde.kbackup.appdata.xml
%{_kf6_bindir}/kbackup
%{_kf6_iconsdir}/hicolor/*/*/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kbackup

%changelog
