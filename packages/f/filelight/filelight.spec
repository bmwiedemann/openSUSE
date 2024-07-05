#
# spec file for package filelight
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
Name:           filelight
Version:        24.05.2
Release:        0
Summary:        Graphical disk usage viewer
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://apps.kde.org/filelight
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kf6-qqc2-desktop-style >= %{kf6_version}
Requires:       kirigami-addons6
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Filelight creates an interactive visualization of disk usage
and the sizes of files and directories on the system.

%lang_package

%prep
%autosetup -p1 -n filelight-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%suse_update_desktop_file org.kde.filelight System Filesystem

%files
%license LICENSES/*
%doc AUTHORS README.md
%config %{_kf6_configdir}/filelightrc
%doc %lang(en) %{_kf6_htmldir}/en/filelight/
%{_kf6_applicationsdir}/org.kde.filelight.desktop
%{_kf6_appstreamdir}/org.kde.filelight.appdata.xml
%{_kf6_bindir}/filelight
%{_kf6_debugdir}/filelight.categories
%{_kf6_iconsdir}/hicolor/*/*/filelight.png

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/filelight/

%changelog
