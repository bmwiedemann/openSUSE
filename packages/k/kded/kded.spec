#
# spec file for package kded
#
# Copyright (c) 2021 SUSE LLC
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


%define _tar_path 5.101
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kded
Version:        5.101.0
Release:        0
Summary:        Central daemon of KDE workspaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF5Config) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0
BuildRequires:  cmake(Qt5Widgets) >= 5.15.0
BuildRequires:  cmake(Qt5Xml) >= 5.15.0

%description
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.

%package devel
Summary:        Central daemon of KDE workspaces: Build Environment
Requires:       %{name} = %{version}
Requires:       extra-cmake-modules

%description devel
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.
Development files.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%find_lang %{name} --with-man --all-name

%preun
%systemd_user_preun plasma-kded.service

%post
/sbin/ldconfig
%systemd_user_post plasma-kded.service

%postun
/sbin/ldconfig
%systemd_user_postun plasma-kded.service

%files lang -f %{name}.lang

%files
%license LICENSES/*
%doc README*
%{_kf5_bindir}/kded5
%{_kf5_sharedir}/dbus-1/services/org.kde.kded5.service
%dir %{_kf5_servicetypesdir}
%{_kf5_servicetypesdir}/kdedmodule.desktop
%doc %lang(en) %{_kf5_mandir}/*/kded5.*
%{_kf5_debugdir}/kded.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_applicationsdir}/org.kde.kded5.desktop
%{_userunitdir}/plasma-kded.service

%files devel
%{_kf5_libdir}/cmake/KDED/
%{_kf5_dbusinterfacesdir}/org.kde.kded5.xml

%changelog
