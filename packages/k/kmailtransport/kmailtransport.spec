#
# spec file for package kmailtransport
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


%define kf5_version 5.103.0
%bcond_without released
Name:           kmailtransport
Version:        23.04.0
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
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5GAPI)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KPim5SMTP)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Test)

%description
This package contains library to provide mailtransport functionality for
KDE PIM applications.

%package -n libKPim5MailTransport5
Summary:        Mail Transport library for KDE PIM applications
Requires:       %{name} >= %{version}

%description -n libKPim5MailTransport5
The Mail Transport library for KDE PIM functionality

%package -n libKPim5MailTransportAkonadi5
Summary:        libkdepim Akonadi library
Requires:       %{name} >= %{version}

%description -n libKPim5MailTransportAkonadi5
The Mail Transport library for Akonadi related functions

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       cyrus-sasl-devel
Requires:       libKPim5MailTransport5 = %{version}
Requires:       libKPim5MailTransportAkonadi5 = %{version}
Requires:       cmake(KF5Wallet) >= %{kf5_version}
Requires:       cmake(KPim5AkonadiMime)
Requires:       cmake(KPim5Mime)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n kmailtransport-%{version}

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets
%ldconfig_scriptlets -n libKPim5MailTransport5
%ldconfig_scriptlets -n libKPim5MailTransportAkonadi5

%files
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/mailtransport/
%{_kf5_configkcfgdir}/mailtransport.kcfg
%{_kf5_debugdir}/kmailtransport.categories
%{_kf5_debugdir}/kmailtransport.renamecategories
%{_kf5_plugindir}/kcm_mailtransport.so
%{_kf5_plugindir}/pim5/mailtransport/mailtransport_akonadiplugin.so
%{_kf5_plugindir}/pim5/mailtransport/mailtransport_smtpplugin.so
%{_kf5_servicesdir}/kcm_mailtransport.desktop

%files -n libKPim5MailTransport5
%license LICENSES/*
%{_kf5_libdir}/libKPim5MailTransport.so.5*

%files -n libKPim5MailTransportAkonadi5
%{_kf5_libdir}/libKPim5MailTransportAkonadi.so.5*

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/MailTransport/
%{_includedir}/KPim5/MailTransportAkonadi/
%{_kf5_cmakedir}/KF5MailTransport/
%{_kf5_cmakedir}/KF5MailTransportAkonadi/
%{_kf5_cmakedir}/KPim5MailTransport/
%{_kf5_cmakedir}/KPim5MailTransportAkonadi/
%{_kf5_libdir}/libKPim5MailTransport.so
%{_kf5_libdir}/libKPim5MailTransportAkonadi.so
%{_kf5_mkspecsdir}/qt_KMailTransport.pri
%{_kf5_mkspecsdir}/qt_KMailTransportAkonadi.pri

%files lang -f %{name}.lang

%changelog
