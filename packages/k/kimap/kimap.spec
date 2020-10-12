#
# spec file for package kimap
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kimap
Version:        20.08.2
Release:        0
Summary:        KDE PIM Libraries: IMAP library
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(Qt5Test)
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
KIMAP provides libraries to interface and communicate with
IMAP mail servers.

%package -n libKF5IMAP5
Summary:        KDE PIM Libraries: IMAP APIs
Group:          Development/Libraries/KDE
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5IMAP5
This package provides the core library to interface and communicate with
IMAP mail servers.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
Requires:       cyrus-sasl-devel
Requires:       libKF5IMAP5 = %{version}
Requires:       cmake(KF5CoreAddons) >= %{kf5_version}
Requires:       cmake(KF5Mime)

%description devel
This package contains development headers to add IMAP support to PIM
applications.

%lang_package

%prep
%setup -q -n kimap-%{version}

%build
  %global _lto_cflags %{_lto_cflags} -ffat-lto-objects
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5IMAP5 -p /sbin/ldconfig
%postun -n libKF5IMAP5 -p /sbin/ldconfig

%files -n libKF5IMAP5
%license LICENSES/*
%{_kf5_libdir}/libKF5IMAP.so.*
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KF5IMAP/
%{_kf5_includedir}/KIMAP/
%{_kf5_includedir}/kimap_version.h
%{_kf5_includedir}/kimaptest/
%{_kf5_libdir}/libKF5IMAP.so
%{_kf5_libdir}/libkimaptest.a
%{_kf5_mkspecsdir}/qt_KIMAP.pri

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
