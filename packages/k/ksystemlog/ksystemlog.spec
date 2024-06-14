#
# spec file for package ksystemlog
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
Name:           ksystemlog
Version:        24.05.1
Release:        0
Summary:        System Log Viewer Tool
License:        GPL-2.0-only
URL:            https://apps.kde.org/ksystemlog
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  kf6-breeze-icons
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemViews) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libsystemd)
Obsoletes:      ksystemlog5 < %{version}
Provides:       ksystemlog5 = %{version}

%description
This program is developed for use by beginner users, who do not know
how to find information about their Linux system and how the log files
are in their computer. But it is also designed for advanced users, who
want to quickly see problems occurring on their server.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

mkdir -p %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps
cp %{_kf6_iconsdir}/breeze/apps/48/utilities-log-viewer.svg %{buildroot}%{_kf6_iconsdir}/hicolor/scalable/apps/

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%{_kf6_applicationsdir}/org.kde.ksystemlog.desktop
%{_kf6_appstreamdir}/org.kde.ksystemlog.appdata.xml
%{_kf6_bindir}/ksystemlog
%{_kf6_debugdir}/ksystemlog.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/utilities-log-viewer.svg

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
