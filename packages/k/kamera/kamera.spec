#
# spec file for package kamera
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
Name:           kamera
Version:        23.04.0
Release:        0
Summary:        Digital camera support for KDE applications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  libgphoto2-devel
BuildRequires:  oxygen-icon-theme-large
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)

%description
This package allows any KDE application to access and manipulate pictures on a
digital camera.

%package -n kio_kamera
Summary:        KDE I/O Slave for Cameras
License:        GPL-2.0-or-later
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n kio_kamera
This package contains a KIO slave to access digital cameras.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%ldconfig_scriptlets -n kio_kamera

%files -n kio_kamera
%license LICENSES/*
%doc README
%dir %{_kf5_htmldir}/en/kcontrol
%doc %lang(en) %{_kf5_htmldir}/en/kcontrol/kamera/
%dir %{_kf5_plugindir}/kf5
%dir %{_kf5_plugindir}/kf5/kio
%dir %{_kf5_plugindir}/plasma
%dir %{_kf5_plugindir}/plasma/kcms
%dir %{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets
%dir %{_kf5_sharedir}/solid/
%dir %{_kf5_sharedir}/solid/actions/
%{_kf5_applicationsdir}/kcm_kamera.desktop
%{_kf5_appstreamdir}/org.kde.kamera.metainfo.xml
%{_kf5_debugdir}/*.categories
%{_kf5_plugindir}/kf5/kio/kio_kamera.so
%{_kf5_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kamera.so
%{_kf5_sharedir}/solid/actions/solid_camera.desktop

%files lang -f %{name}.lang

%changelog
