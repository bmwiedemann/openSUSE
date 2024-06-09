#
# spec file for package kf6-kdav
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

%define rname kdav
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-kdav
Version:        6.3.0
Release:        0
Summary:        DAV protocol implementation
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6I18n) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6KIO) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
kdav is a library providing a KJob-based implementation of DAV protocols such as
CardDAV, WebDAV, and CalDAV.

%package -n libKF6DAV6
Summary:        Core library for kdav
Requires:       kf6-kdav >= %{version}

%description -n libKF6DAV6
kdav is a library providing a KJob-based implementation of DAV protocols such as
CardDAV, WebDAV, and CalDAV.

%package devel
Summary:        Development package for kdav
Requires:       libKF6DAV6 = %{version}

%description devel
This package contains development files needed to use kdav in other applications.

%lang_package -n libKF6DAV6

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libkdav6 --with-man --all-name

%ldconfig_scriptlets -n libKF6DAV6

%files
%{_kf6_debugdir}/kdav.categories
%{_kf6_debugdir}/kdav.renamecategories

%files -n libKF6DAV6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6DAV.so.*

%files devel
%doc %{_kf6_qchdir}/KF6DAV.*
%{_kf6_includedir}/KDAV/
%{_kf6_cmakedir}/KF6DAV/
%{_kf6_libdir}/libKF6DAV.so

%files -n libKF6DAV6-lang -f libkdav6.lang

%changelog
