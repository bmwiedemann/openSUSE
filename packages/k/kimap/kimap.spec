#
# spec file for package kimap
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define kpim6_version 6.1.1

%bcond_without released
Name:           kimap
Version:        24.05.1
Release:        0
Summary:        Library to assist working with IMAP servers
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KIMAP provides libraries to interface and communicate with
IMAP mail servers.

%package -n libKPim6IMAP6
Summary:        Library to assist working with IMAP servers
# Modules used for authentication
Requires:       cyrus-sasl-crammd5
Requires:       cyrus-sasl-digestmd5
Requires:       cyrus-sasl-gssapi
Requires:       cyrus-sasl-plain
Requires:       sasl2-kdexoauth2
Requires:       kimap >= %{version}
Obsoletes:      kimap-lang <= 23.04.0
Obsoletes:      libKF5IMAP5 < %{version}
Obsoletes:      libKPim5IMAP5 < %{version}
Obsoletes:      libKPim5IMAP5-lang < %{version}

%description  -n libKPim6IMAP6
This package provides the core library to interface and communicate with
IMAP mail servers.

%package devel
Summary:        Development files for kimap
Requires:       cyrus-sasl-devel
Requires:       libKPim6IMAP6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}

%description devel
This package contains development headers to add IMAP support to PIM
applications.

%lang_package -n libKPim6IMAP6

%prep
%autosetup -p1 -n kimap-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

%cmake_kf6 \
  -DBUILD_QCH:BOOL=TRUE \
  -DBUILD_TESTING:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libKPim6IMAP6 --all-name

%ldconfig_scriptlets -n libKPim6IMAP6

%files
%{_kf6_debugdir}/*.categories
%{_kf6_debugdir}/*.renamecategories

%files -n libKPim6IMAP6
%license LICENSES/*
%{_kf6_libdir}/libKPim6IMAP.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6Imap.*
%{_includedir}/KPim6/KIMAP/
%{_includedir}/KPim6/KIMAPTest/
%{_kf6_cmakedir}/KPim6IMAP/
%{_kf6_libdir}/libKPim6IMAP.so
%{_kf6_libdir}/libkimaptest6.a

%files -n libKPim6IMAP6-lang -f libKPim6IMAP6.lang

%changelog
