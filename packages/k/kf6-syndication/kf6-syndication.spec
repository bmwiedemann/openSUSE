#
# spec file for package kf6-syndication
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

%define rname syndication
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-syndication
Version:        6.3.0
Release:        0
Summary:        RSS/Atom parsing library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  cmake(KF6Codecs) >= %{_kf6_bugfix_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
KF6Syndication is an RSS/Atom parsing library by KDE, which
also provides an API to fetch feeds from the network.

%package -n libKF6Syndication6
Summary:        RSS/Atom parsing library
Requires:       kf6-syndication >= %{version}

%description  -n libKF6Syndication6
KF6Syndication is an RSS/Atom parsing library, which
also provides an API to fetch feeds from the network.
This package contains the base library.

%package devel
Summary:        RSS/Atom parsing library - development headers
Requires:       libKF6Syndication6 = %{version}

%description devel
KF6Syndication is an RSS/Atom parsing library, which
also provides an API to fetch feeds from the network. This
package contains development headers.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKF6Syndication6

%files
%{_kf6_debugdir}/syndication.categories
%{_kf6_debugdir}/syndication.renamecategories

%files -n libKF6Syndication6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Syndication.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Syndication.*
%{_kf6_cmakedir}/KF6Syndication/
%{_kf6_includedir}/Syndication/
%{_kf6_libdir}/libKF6Syndication.so

%changelog
