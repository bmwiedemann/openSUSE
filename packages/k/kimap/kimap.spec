#
# spec file for package kimap
#
# Copyright (c) 2022 SUSE LLC
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
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kimap
Version:        22.12.0
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
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(Qt5Test)

%description
KIMAP provides libraries to interface and communicate with
IMAP mail servers.

%package -n libKF5IMAP5
Summary:        KDE PIM Libraries: IMAP APIs
Recommends:     %{name}-lang
Provides:       %{name} = %{version}
# Modules used for authentication
Requires:       cyrus-sasl-crammd5
Requires:       cyrus-sasl-digestmd5
Requires:       cyrus-sasl-gssapi
Requires:       cyrus-sasl-plain
Requires:       sasl2-kdexoauth2

%description  -n libKF5IMAP5
This package provides the core library to interface and communicate with
IMAP mail servers.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       cyrus-sasl-devel
Requires:       libKF5IMAP5 = %{version}
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}
Requires:       cmake(KF5Mime)

%description devel
This package contains development headers to add IMAP support to PIM
applications.

%lang_package

%prep
%autosetup -p1 -n kimap-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -n libKF5IMAP5 -p /sbin/ldconfig
%postun -n libKF5IMAP5 -p /sbin/ldconfig

%files -n libKF5IMAP5
%license LICENSES/*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5IMAP.so.*

%files devel
%{_kf5_cmakedir}/KF5IMAP/
%{_kf5_includedir}/KIMAP/
%{_kf5_includedir}/KIMAPTest/
%{_kf5_libdir}/libKF5IMAP.so
%{_kf5_libdir}/libkimaptest.a
%{_kf5_mkspecsdir}/qt_KIMAP.pri

%files lang -f %{name}.lang

%changelog
