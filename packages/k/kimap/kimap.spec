#
# spec file for package kimap
#
# Copyright (c) 2023 SUSE LLC
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


%define kf5_version 5.99.0
%define libname libKPim5IMAP5
%bcond_without released
Name:           kimap
Version:        23.04.0
Release:        0
Summary:        KDE PIM Libraries: IMAP library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Test)
Conflicts:      libKF5IMAP5 < %{version}

%description
KIMAP provides libraries to interface and communicate with
IMAP mail servers.

%package -n %{libname}
Summary:        KDE PIM Libraries: IMAP APIs
Provides:       %{name} = %{version}
# Modules used for authentication
Requires:       cyrus-sasl-crammd5
Requires:       cyrus-sasl-digestmd5
Requires:       cyrus-sasl-gssapi
Requires:       cyrus-sasl-plain
Requires:       sasl2-kdexoauth2
%requires_eq    %{name}
# Renamed
Obsoletes:      kimap-lang <= 23.04.0

%description  -n %{libname}
This package provides the core library to interface and communicate with
IMAP mail servers.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       cyrus-sasl-devel
Requires:       %{libname} = %{version}
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}
Requires:       cmake(KPim5Mime)

%description devel
This package contains development headers to add IMAP support to PIM
applications.

%lang_package -n %{libname}

%prep
%autosetup -p1 -n kimap-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake_kf5 -d build -- -DBUILD_TESTING=ON

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{libname} --with-man --all-name

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files -n %{libname}
%{_kf5_libdir}/libKPim5IMAP.so.*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KIMAP/
%{_includedir}/KPim5/KIMAPTest/
%{_kf5_cmakedir}/KF5IMAP/
%{_kf5_cmakedir}/KPim5IMAP/
%{_kf5_libdir}/libKPim5IMAP.so
%{_kf5_libdir}/libkimaptest.a
%{_kf5_mkspecsdir}/qt_KIMAP.pri

%files -n %{libname}-lang -f %{libname}.lang

%changelog
