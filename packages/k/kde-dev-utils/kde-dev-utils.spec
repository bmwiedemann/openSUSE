#
# spec file for package kde-dev-utils
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
Name:           kde-dev-utils
Version:        22.12.1
Release:        0
Summary:        KDE SDK Package
License:        GPL-2.0-only AND GFDL-1.2-only AND LGPL-2.0-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5UiTools)

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
%cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang kuiviewer
%find_lang kpartloader

%suse_update_desktop_file org.kde.kuiviewer Development GUIDesigner

%post -n kuiviewer -p /sbin/ldconfig
%postun -n kuiviewer -p /sbin/ldconfig

%files -n kuiviewer
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.kuiviewer.desktop
%{_kf5_bindir}/kuiviewer
%{_kf5_iconsdir}/hicolor/*/apps/kuiviewer.png
%{_kf5_iconsdir}/hicolor/scalable/apps/kuiviewer.svg
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/parts
%{_kf5_plugindir}/kf5/parts/kuiviewerpart.so
%{_kf5_plugindir}/quithumbnail.so
%{_kf5_servicesdir}/designerthumbnail.desktop
%{_kf5_servicesdir}/kuiviewer_part.desktop
%{_kf5_appstreamdir}/org.kde.kuiviewer.metainfo.xml
%{_kf5_appstreamdir}/org.kde.kuiviewerpart.metainfo.xml

%post -n kpartloader -p /sbin/ldconfig
%postun -n kpartloader -p /sbin/ldconfig

%files -n kpartloader
%license LICENSES/*
%{_kf5_bindir}/kpartloader

%files -n kuiviewer-lang -f kuiviewer.lang

%files -n kpartloader-lang -f kpartloader.lang

%changelog
