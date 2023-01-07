#
# spec file for package libksieve
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


%define soversion 5
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libksieve
Version:        22.12.1
Release:        0
Summary:        Sieve and Managesieve support library for KDE PIM applications
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_headers-devel
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5IdentityManagement)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5MailTransport)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
This package contains the libksieve library, which is used to support
the Sieve server-side mail filtering protocol in KDE PIM applications.

%package -n libksieve%{soversion}
Summary:        Sieve and Managesieve support library for KDE PIM applications
Requires:       libksieve = %{version}
# Before 21.08.3, the libraries were in libksieve
Conflicts:      libksieve < 21.08.3

%description -n libksieve%{soversion}
This package contains the libksieve library, which is used to support
the Sieve server-side mail filtering protocol in KDE PIM applications.

%package devel
Summary:        Development package for libksieve
Requires:       libksieve%{soversion} = %{version}

%description devel
This package contains development headers of libksieve.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post   -n libksieve%{soversion} -p /sbin/ldconfig
%postun -n libksieve%{soversion} -p /sbin/ldconfig

%files
%{_kf5_debugdir}/libksieve.categories
%{_kf5_debugdir}/libksieve.renamecategories
%{_kf5_knsrcfilesdir}/ksieve_script.knsrc
%{_kf5_sharedir}/sieve/

%files -n libksieve%{soversion}
%license LICENSES/*
%{_kf5_libdir}/libKF5KManageSieve.so.*
%{_kf5_libdir}/libKF5KSieve.so.*
%{_kf5_libdir}/libKF5KSieveUi.so.*

%files devel
%{_kf5_includedir}/KManageSieve/
%{_kf5_includedir}/KSieveUi/
%{_kf5_includedir}/KSieve/
%{_kf5_libdir}/cmake/KF5LibKSieve/
%{_kf5_libdir}/libKF5KManageSieve.so
%{_kf5_libdir}/libKF5KSieve.so
%{_kf5_libdir}/libKF5KSieveUi.so
%{_kf5_mkspecsdir}/qt_KManageSieve.pri
%{_kf5_mkspecsdir}/qt_KSieveUi.pri

%files lang -f %{name}.lang

%changelog
