#
# spec file for package kmailtransport
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
Name:           kmailtransport
Version:        20.08.2
Release:        0
Summary:        KDE PIM Libraries: Mailtransport layer
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KPimGAPI)
BuildRequires:  cmake(KPimSMTP)
BuildRequires:  cmake(Qt5Test)
Recommends:     %{name}-lang
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains library to provide mailtransport functionality for KDE PIM applications.

%package -n libKF5MailTransport5
Summary:        Mail Transport library for KDEPIM
Group:          System/Libraries
Requires:       %{name} >= %{version}
Requires:       sasl2-kdexoauth2 >= %{_kapp_version}

%description -n libKF5MailTransport5
The Mail Transport library for KDEPIM functionality

%package -n libKF5MailTransportAkonadi5
Summary:        libkdepim Akonadi library
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n libKF5MailTransportAkonadi5
The Mail Transport library for Akonadi related functions

%post -n libKF5MailTransport5  -p /sbin/ldconfig
%postun -n libKF5MailTransport5 -p /sbin/ldconfig
%post -n libKF5MailTransportAkonadi5  -p /sbin/ldconfig
%postun -n libKF5MailTransportAkonadi5 -p /sbin/ldconfig

%package devel
Summary:        KDE PIM Libraries: Build Environment
Group:          Development/Libraries/KDE
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
%setup -q -n kmailtransport-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=OFF -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_kf5_configkcfgdir}
%{_kf5_debugdir}/kmailtransport.categories
%{_kf5_debugdir}/kmailtransport.renamecategories
%dir %{_kf5_plugindir}/mailtransport
%{_kf5_configkcfgdir}/mailtransport.kcfg
%{_kf5_plugindir}/kcm_mailtransport.so
%{_kf5_plugindir}/mailtransport/*.so
%{_kf5_servicesdir}/kcm_mailtransport.desktop

%files -n libKF5MailTransport5
%license LICENSES/*
%{_kf5_libdir}/libKF5MailTransport.so.5*

%files -n libKF5MailTransportAkonadi5
%license LICENSES/*
%{_kf5_libdir}/libKF5MailTransportAkonadi.so.5*

%files devel
%license LICENSES/*
%{_kf5_cmakedir}/KF5MailTransport/
%{_kf5_includedir}/MailTransport/
%{_kf5_includedir}/MailTransportAkonadi/
%{_kf5_includedir}/mailtransport/
%{_kf5_includedir}/mailtransport_version.h
%{_kf5_includedir}/mailtransportakonadi/
%{_kf5_includedir}/mailtransportakonadi_version.h
%{_kf5_libdir}/libKF5MailTransport.so
%{_kf5_libdir}/libKF5MailTransportAkonadi.so
%{_kf5_mkspecsdir}/qt_KMailTransport.pri
%{_kf5_mkspecsdir}/qt_KMailTransportAkonadi.pri
%{_kf5_libdir}/cmake/KF5MailTransportAkonadi/

%if %{with lang}
%files lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
