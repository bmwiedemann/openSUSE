#
# spec file for package kf6-kded
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


%define qt6_version 6.6.0

%define rname kded
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kded
Version:        6.3.0
Release:        0
Summary:        Central daemon of KDE workspaces
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Config) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Crash) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6DocTools) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Service) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# One of the main tasks of kded is to run kconf_update when necessary
Requires:       kconf_update6

%description
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.

%package devel
Summary:        Central daemon of KDE workspaces: Build Environment
Requires:       kf6-kded >= %{version}

%description devel
KDED runs in the background and performs a number of small tasks.
Some of these tasks are built in, others are started on demand.
Development files.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kded6 --with-man --all-name

%preun
%{systemd_user_preun plasma-kded6.service}

%post
%ldconfig
%{systemd_user_post plasma-kded6.service}

%postun
%ldconfig
%{systemd_user_postun plasma-kded6.service}

%files
%license LICENSES/*
%doc README.md
%doc %lang(en) %{_kf6_mandir}/*/kded6.*
%{_kf6_applicationsdir}/org.kde.kded6.desktop
%{_kf6_bindir}/kded6
%{_kf6_debugdir}/kded.categories
%{_kf6_debugdir}/kded.renamecategories
%{_kf6_sharedir}/dbus-1/services/org.kde.kded6.service
%{_userunitdir}/plasma-kded6.service

%files devel
%{_kf6_cmakedir}/KF6KDED/
%{_kf6_dbusinterfacesdir}/org.kde.kded6.xml

%files lang -f kded6.lang

%changelog
