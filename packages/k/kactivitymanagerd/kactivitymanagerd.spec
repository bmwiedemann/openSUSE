#
# spec file for package kactivitymanagerd
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%global kf5_version 5.98.0
%global qt5_version 5.15.0

%bcond_without released
Name:           kactivitymanagerd
Version:        5.26.4
Release:        0
Summary:        KDE Plasma Activities support
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Url:            http://projects.kde.org/kactivitymanagerd
Source:         https://download.kde.org/stable/plasma/%{version}/kactivitymanagerd-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kactivitymanagerd-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.49.0
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  fdupes
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5Qml) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Sql) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
Recommends:     %{name}-lang
# for kactivitymanagerd_plugin_sqlite.so
Requires:       libQt5Sql5-sqlite
Provides:       kactivities4 = %{version}
Obsoletes:      kactivities4 < %{version}
Provides:       kactivities5 = 5.20.0
Obsoletes:      kactivities5 < 5.20.0

%description
Kactivities provides an API for using and interacting with the Plasma Activities Manager.

%package lang
Summary:        KDE Plasma Activities support
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Provides:       libKF5Activities5-lang = 5.20.0
Obsoletes:      libKF5Activities5-lang < 5.20.0

%description lang
Provides translations to the package %{name}.

%prep
%setup -q -n kactivitymanagerd-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with released}
%find_lang kactivities5
%endif

%post 
/sbin/ldconfig
%{systemd_user_post plasma-kactivitymanagerd.service}

%preun
%{systemd_user_preun plasma-kactivitymanagerd.service}

%postun 
/sbin/ldconfig
%{systemd_user_postun plasma-kactivitymanagerd.service}

%if %{with released}
%files -n %name-lang -f kactivities5.lang
%endif

%files
%license LICENSES/*
%{_kf5_libdir}/libkactivitymanagerd_plugin.so
%{_kf5_plugindir}/kactivitymanagerd/
%{_kf5_servicesdir}/kactivitymanagerd.desktop
%dir %{_kf5_sharedir}/krunner/
%dir %{_kf5_sharedir}/krunner/dbusplugins/
%{_kf5_sharedir}/krunner/dbusplugins/plasma-runnners-activities.desktop
%{_kf5_sharedir}/dbus-1/services/org.kde.ActivityManager.service
%{_kf5_debugdir}/kactivitymanagerd.categories
%{_libexecdir}/kactivitymanagerd
%{_userunitdir}/plasma-kactivitymanagerd.service

%changelog
