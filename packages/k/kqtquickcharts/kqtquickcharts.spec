#
# spec file for package kqtquickcharts
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


%define kf6_version 6.19.0
%define qt6_version 6.9.0
#
%bcond_without released
Name:           kqtquickcharts
Version:        25.12.0
Release:        0
Summary:        Plugin to render beautiful and interactive graphs
License:        LGPL-2.1-or-later
URL:            https://edu.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  kf6-filesystem
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}

%description
A QtQuick plugin to render beautiful and interactive graphs.

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%files
%license LICENSES/*
%{_kf6_includedir}/kqtquickcharts_version.h
%{_kf6_cmakedir}/KQtQuickCharts/
%{_kf6_qmldir}/org/kde/charts/

%changelog
