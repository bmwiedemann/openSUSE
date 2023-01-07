#
# spec file for package kbackup
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
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
Name:           kbackup
Version:        22.12.1
Release:        0
Summary:        Backup program based on KDE Frameworks 5
License:        GPL-2.0-only
URL:            https://apps.kde.org/kbackup
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)

%description
kbackup is a backup program based on KDE Frameworks 5. It allows backing
folders and files up and setting profiles to exclude or include directories
or files from the backup. It can save to both local files or remote locations.
Although GUI based, it also offers an automated, GUI-less mode.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --with-qt --all-name
%{kf5_find_htmldocs}

%files
%license COPYING
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/kbackup
%{_datadir}/mime/packages/kbackup.xml
%{_kf5_applicationsdir}/org.kde.kbackup.desktop
%{_kf5_appstreamdir}/org.kde.kbackup.appdata.xml
%{_kf5_bindir}/kbackup
%{_kf5_iconsdir}/hicolor/*/*/
%{_kf5_kxmlguidir}/kbackup/
%{_mandir}/man1/kbackup.1.gz

%files lang -f %{name}.lang

%changelog
