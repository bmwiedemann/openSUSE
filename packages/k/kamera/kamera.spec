#
# spec file for package kamera
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
Name:           kamera
Version:        24.05.2
Release:        0
Summary:        Digital camera support for KDE applications
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  pkgconfig(libgphoto2) >= 2.5.0

%description
This package allows any KDE application to access and manipulate pictures on a
digital camera.

%package -n kio_kamera
Summary:        KDE I/O Slave for cameras
License:        GPL-2.0-or-later
Obsoletes:      kamera-lang

%description -n kio_kamera
This package contains a KIO slave to access digital cameras.

%lang_package -n kio_kamera

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets -n kio_kamera

%files -n kio_kamera
%license LICENSES/*
%doc README
%dir %{_kf6_htmldir}/en/kcontrol
%doc %lang(en) %{_kf6_htmldir}/en/kcontrol/kamera/
%{_kf6_applicationsdir}/kcm_kamera.desktop
%{_kf6_appstreamdir}/org.kde.kamera.metainfo.xml
%{_kf6_debugdir}/kamera.categories
%{_kf6_plugindir}/kf6/kio/kio_kamera.so
%{_kf6_plugindir}/plasma/kcms/systemsettings_qwidgets/kcm_kamera.so
%dir %{_kf6_sharedir}/solid/
%dir %{_kf6_sharedir}/solid/actions/
%{_kf6_sharedir}/solid/actions/solid_camera.desktop

%files -n kio_kamera-lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcontrol

%changelog
