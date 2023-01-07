#
# spec file for package filelight
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           filelight
Version:        22.12.1
Release:        0
Summary:        Graphical disk usage viewer
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://apps.kde.org/filelight
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Filelight creates an interactive visualization of disk usage
and the sizes of files and directories on the system.

%lang_package

%prep
%autosetup -p1 -n filelight-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.filelight System Filesystem

%files
%license LICENSES/*
%doc AUTHORS README.md
%config %{_kf5_configdir}/filelightrc
%doc %lang(en) %{_kf5_htmldir}/en/filelight/
%{_kf5_applicationsdir}/org.kde.filelight.desktop
%{_kf5_appstreamdir}/org.kde.filelight.appdata.xml
%{_kf5_bindir}/filelight
%{_kf5_debugdir}/filelight.categories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/filelight/

%files lang -f %{name}.lang

%changelog
