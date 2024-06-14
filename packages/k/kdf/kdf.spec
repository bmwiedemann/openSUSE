#
# spec file for package kdf
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
Name:           kdf
Version:        24.05.1
Release:        0
Summary:        Disk Usage Viewer
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch0:         desktop-files.diff
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KDE free disk space utility

%package -n kwikdisk
Summary:        Removable Media Utility

%description -n kwikdisk
This utility allows you to manage removable media.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file org.kde.kdf System Filesystem

%ldconfig_scriptlets

%files
%license LICENSES/*
%dir %{_kf6_htmldir}/en/kcontrol/
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol/blockdevices/
%doc %lang(en) %{_kf6_htmldir}/en/kdf/
%{_kf6_applicationsdir}/org.kde.kdf.desktop
%{_kf6_applicationsdir}/kcm_kdf.desktop
%{_kf6_appstreamdir}/org.kde.kdf.appdata.xml
%{_kf6_bindir}/kdf
%{_kf6_debugdir}/kdf.categories
%{_kf6_iconsdir}/hicolor/*/*/kcmdf.png
%{_kf6_iconsdir}/hicolor/*/*/kdf.png
%{_kf6_libdir}/libkdfprivate.so.*
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kdf.so

%files -n kwikdisk
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.kwikdisk.desktop
%{_kf6_bindir}/kwikdisk
%{_kf6_iconsdir}/hicolor/*/*/kwikdisk.png

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol/blockdevices/
%exclude %{_kf6_htmldir}/en/kdf/

%changelog
