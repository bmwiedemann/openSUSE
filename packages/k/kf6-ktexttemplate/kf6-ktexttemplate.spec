#
# spec file for package kf6-ktexttemplate
#
# Copyright (c) 2025 SUSE LLC
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


%define qt6_version 6.8.0

%define rname ktexttemplate
# Full KF6 version (e.g. 6.15.0)
%{!?_kf6_version: %global _kf6_version %{version}}
%bcond_without released
Name:           kf6-ktexttemplate
Version:        6.15.0
Release:        0
Summary:        String template library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
The goal of KTextTemplate is to make it easier for application developers to
separate the structure of documents from the data they contain, opening the door
for theming and advanced generation of other text such as code.

%package -n libKF6TextTemplate6
Summary:        Core library for ktexttemplate
Requires:       kf6-ktexttemplate >= %{version}

%description -n libKF6TextTemplate6
Library to allow application developers to separate the structure of documents
from the data they contain.

%package devel
Summary:        Development package for ktexttemplate
Requires:       libKF6TextTemplate6 = %{version}

%description devel
Library to allow application developers to separate the structure of documents
from the data they contain.

Development files.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKF6TextTemplate6

%files
%{_kf6_debugdir}/ktexttemplate.categories
%{_kf6_plugindir}/kf6/ktexttemplate/

%files -n libKF6TextTemplate6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6TextTemplate.so.*

%files devel
%{_kf6_cmakedir}/KF6TextTemplate/
%{_kf6_includedir}/KTextTemplate/
%{_kf6_libdir}/libKF6TextTemplate.so

%changelog
