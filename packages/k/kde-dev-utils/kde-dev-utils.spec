#
# spec file for package kde-dev-utils
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
Name:           kde-dev-utils
Version:        24.05.2
Release:        0
Summary:        KDE SDK Package
License:        GPL-2.0-only AND GFDL-1.2-only AND LGPL-2.0-only
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Designer) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiTools) >= %{qt6_version}

%description
This package suggests the packages, built from the kde-dev-utils module.

%package -n kpartloader
Summary:        Development tool to test KParts

%description -n kpartloader
kpartloader is a debugging tool used to test
loading of KParts.

%lang_package -n kpartloader
%lang_package -n kuiviewer

%package -n kuiviewer
Summary:        UI Files Viewer

%description -n kuiviewer
Displays Qt Designer UI files

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif

export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"

%cmake_kf6 -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"

%kf6_build

%install
%kf6_install

%find_lang kuiviewer
%find_lang kpartloader

%suse_update_desktop_file org.kde.kuiviewer Development GUIDesigner

%ldconfig_scriptlets -n kuiviewer

%files -n kuiviewer
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.kuiviewer.desktop
%{_kf6_bindir}/kuiviewer
%{_kf6_iconsdir}/hicolor/*/apps/kuiviewer.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kuiviewer.svg
%{_kf6_plugindir}/kf6/parts/kuiviewerpart.so
%dir %{_kf6_plugindir}/kf6/thumbcreator
%{_kf6_plugindir}/kf6/thumbcreator/quithumbnail.so
%{_kf6_appstreamdir}/org.kde.kuiviewer.metainfo.xml
%{_kf6_appstreamdir}/org.kde.kuiviewerpart.metainfo.xml

%ldconfig_scriptlets -n kpartloader

%files -n kpartloader
%license LICENSES/*
%{_kf6_bindir}/kpartloader

%files -n kuiviewer-lang -f kuiviewer.lang

%files -n kpartloader-lang -f kpartloader.lang

%changelog
