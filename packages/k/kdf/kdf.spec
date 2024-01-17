#
# spec file for package kdf
#
# Copyright (c) 2023 SUSE LLC
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
Name:           kdf
Version:        23.08.4
Release:        0
Summary:        Disk Usage Viewer
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch1:         desktop-files.diff
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)

%description
KDE free disk space utility

%lang_package

%prep
%autosetup -p0 -n kdf-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kdf System Filesystem

%package -n kwikdisk
Summary:        Removable Media Utility

%description -n kwikdisk
This utility allows you to manage removable media.

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/blockdevices/
%doc %lang(en) %{_kf5_htmldir}/en/kdf/
%dir %{_kf5_htmldir}/en/kcontrol/
%{_kf5_applicationsdir}/org.kde.kdf.desktop
%{_kf5_applicationsdir}/kcm_kdf.desktop
%{_kf5_appstreamdir}/org.kde.kdf.appdata.xml
%{_kf5_bindir}/kdf
%{_kf5_debugdir}/kdf.categories
%{_kf5_iconsdir}/hicolor/*/*/kcmdf.png
%{_kf5_iconsdir}/hicolor/*/*/kdf.png
%{_kf5_kxmlguidir}/kdf/
%{_kf5_libdir}/libkdfprivate.so.*
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kdf.so

%files -n kwikdisk
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.kwikdisk.desktop
%{_kf5_bindir}/kwikdisk
%{_kf5_iconsdir}/hicolor/*/*/kwikdisk.png

%files lang -f %{name}.lang

%changelog
