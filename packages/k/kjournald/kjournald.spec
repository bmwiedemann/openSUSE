#
# spec file for package kjournald
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


%define soname  0
%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kjournald
Version:        24.05.1
Release:        0
Summary:        Qt browser for journald database
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/system/kjournald
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libsystemd)
Requires:       qt6-declarative-imports >= %{qt6_version}

%description
This project aims to provide an abstraction of the systemd’s journald API in
terms of QAbstractItemModel classes. The main purpose is to ease the
integration of journald into Qt based applications (both QML and QtWidget).
Additional to the library, the project provides a reference implementation of
the API, called kjournaldbrowser. Even though that application provides a
powerful journal database reader, we aim to do a clear split between
reuseable library and application logic.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

rm %{buildroot}%{_libdir}/libkjournald.so

%find_lang %{name} --all-name

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.kjournaldbrowser.desktop
%{_kf6_appstreamdir}/org.kde.kjournaldbrowser.appdata.xml
%{_kf6_bindir}/kjournaldbrowser
%{_kf6_debugdir}/kjournald.categories
%{_kf6_libdir}/libkjournald.so.*

%files lang -f %{name}.lang

%changelog
