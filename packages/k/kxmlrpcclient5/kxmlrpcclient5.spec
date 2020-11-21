#
# spec file for package kxmlrpcclient5
#
# Copyright (c) 2020 SUSE LLC
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


%define rname kxmlrpcclient
%define lname libKF5XmlRpcClient5
%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kxmlrpcclient5
Version:        5.75.0
Release:        0
Summary:        Library containing simple XML-RPC Client support
License:        BSD-2-Clause
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{rname}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/portingAids/%{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Test) >= 5.12.0

%description
Library containing simple XML-RPC Client support.

%package -n %{lname}
Summary:        Library containing simple XML-RPC Client support
Group:          Development/Libraries/KDE
%if %{with lang}
Recommends:     %{lname}-lang = %{version}
%endif

%description  -n %{lname}
Library containing simple XML-RPC Client support.

%package devel
Summary:        Library containing simple XML-RPC Client support: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       cmake(KF5KIO) >= %{_kf5_bugfix_version}

%description devel
Library containing simple XML-RPC Client support. Development files.

%lang_package -n %{lname}

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON
  %cmake_build

%install
  %kf5_makeinstall -C build

%if %{with lang}
%find_lang libkxmlrpcclient5 %{name}.lang
%endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%if %{with lang}
%files -n %{lname}-lang -f %{name}.lang
%endif

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libKF5XmlRpcClient.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license LICENSES/*
%{_kf5_libdir}/cmake/KF5XmlRpcClient/
%{_kf5_libdir}/libKF5XmlRpcClient.so
%{_kf5_includedir}/KXmlRpcClient/
%{_kf5_includedir}/kxmlrpcclient_version.h
%{_kf5_mkspecsdir}/qt_KXmlRpcClient.pri

%changelog
