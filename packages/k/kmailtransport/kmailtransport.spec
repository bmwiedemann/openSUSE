#
# spec file for package kmailtransport
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
Name:           kmailtransport
Version:        22.12.1
Release:        0
Summary:        KDE PIM Libraries: Mailtransport layer
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KPimGAPI)
BuildRequires:  cmake(KPimSMTP)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Test)

%description
This package contains library to provide mailtransport functionality for
KDE PIM applications.

%package -n libKF5MailTransport5
Summary:        Mail Transport library for KDE PIM applications
Requires:       %{name} >= %{version}
Requires:       sasl2-kdexoauth2 >= %{_kapp_version}

%description -n libKF5MailTransport5
The Mail Transport library for KDE PIM functionality

%package -n libKF5MailTransportAkonadi5
Summary:        libkdepim Akonadi library
Requires:       %{name} >= %{version}

%description -n libKF5MailTransportAkonadi5
The Mail Transport library for Akonadi related functions

%post -n libKF5MailTransport5  -p /sbin/ldconfig
%postun -n libKF5MailTransport5 -p /sbin/ldconfig
%post -n libKF5MailTransportAkonadi5  -p /sbin/ldconfig
%postun -n libKF5MailTransportAkonadi5 -p /sbin/ldconfig

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       cyrus-sasl-devel
Requires:       libKF5MailTransport5 = %{version}
Requires:       libKF5MailTransportAkonadi5 = %{version}
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KF5Mime)
Requires:       cmake(KF5Wallet) >= %{kf5_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n kmailtransport-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/mailtransport/
%{_kf5_configkcfgdir}/mailtransport.kcfg
%{_kf5_debugdir}/kmailtransport.categories
%{_kf5_debugdir}/kmailtransport.renamecategories
%{_kf5_plugindir}/kcm_mailtransport.so
%{_kf5_servicesdir}/kcm_mailtransport.desktop
%{_kf5_plugindir}/pim5/mailtransport/mailtransport_akonadiplugin.so
%{_kf5_plugindir}/pim5/mailtransport/mailtransport_smtpplugin.so

%files -n libKF5MailTransport5
%license LICENSES/*
%{_kf5_libdir}/libKF5MailTransport.so.5*

%files -n libKF5MailTransportAkonadi5
%{_kf5_libdir}/libKF5MailTransportAkonadi.so.5*

%files devel
%{_kf5_cmakedir}/KF5MailTransport/
%{_kf5_includedir}/MailTransport/
%{_kf5_includedir}/MailTransportAkonadi/
%{_kf5_libdir}/cmake/KF5MailTransportAkonadi/
%{_kf5_libdir}/libKF5MailTransport.so
%{_kf5_libdir}/libKF5MailTransportAkonadi.so
%{_kf5_mkspecsdir}/qt_KMailTransport.pri
%{_kf5_mkspecsdir}/qt_KMailTransportAkonadi.pri

%files lang -f %{name}.lang

%changelog
