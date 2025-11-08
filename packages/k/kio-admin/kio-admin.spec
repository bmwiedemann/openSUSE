#
# spec file for package kio-admin
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.14.0
%define qt6_version 6.8.0

%bcond_without released
Name:           kio-admin
Version:        25.08.3
Release:        0
Summary:        Manage files as administrator using the admin:// KIO protocol
# 'GPL-2.0-only_OR_GPL-3.0-only_OR_LicenseRef-KDE-Accepted-GPL'
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://invent.kde.org/system/kio-admin
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source3:        README.SUSE
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}

%description
kio-admin implements a new protocol "admin:///" which gives administrative access
to the entire system. This is achieved by talking, over dbus, with a root-level
helper binary that in turn uses existing KIO infrastructure to run file://
operations in root-scope.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install
mkdir -p %{buildroot}/%{_docdir}/kio-admin
cp %{SOURCE3} %{buildroot}/%{_docdir}/kio-admin

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_datadir}/dbus-1/system-services/org.kde.kio.admin.service
%{_datadir}/polkit-1/actions/org.kde.kio.admin.policy
%{_docdir}/kio-admin
%{_kf6_appstreamdir}/org.kde.kio.admin.metainfo.xml
%{_kf6_dbuspolicydir}/org.kde.kio.admin.conf
%{_kf6_libexecdir}/kio-admin-helper
%dir %{_kf6_plugindir}/kf6/kfileitemaction
%{_kf6_plugindir}/kf6/kfileitemaction/kio-admin.so
%{_kf6_plugindir}/kf6/kio/admin.so

%files lang -f %{name}.lang

%changelog
