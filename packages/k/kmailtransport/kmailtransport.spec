#
# spec file for package kmailtransport
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
Name:           kmailtransport
Version:        24.05.1
Release:        0
Summary:        KDE PIM Libraries: Mailtransport layer
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KPim6GAPI) >= %{kpim6_version}
BuildRequires:  cmake(KPim6SMTP) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
This package contains library to provide mailtransport functionality for
KDE PIM applications.

%package -n libKPim6MailTransport6
Summary:        Mail Transport library for KDE PIM applications
Requires:       kmailtransport >= %{version}
Obsoletes:      libKF5MailTransport5 < %{version}
Obsoletes:      libKPim5MailTransport5 < %{version}

%description -n libKPim6MailTransport6
The Mail Transport library for KDE PIM functionality

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       cyrus-sasl-devel
Requires:       libKPim6MailTransport6 = %{version}
Requires:       cmake(KF6Config) >= %{kf6_version}

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n kmailtransport-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang kmailtransport --with-man --all-name

%ldconfig_scriptlets -n libKPim6MailTransport6

%files
%{_kf6_configkcfgdir}/mailtransport.kcfg
%{_kf6_debugdir}/kmailtransport.categories
%{_kf6_debugdir}/kmailtransport.renamecategories
%dir %{_kf6_plugindir}/pim6/
%dir %{_kf6_plugindir}/pim6/mailtransport/
%{_kf6_plugindir}/pim6/mailtransport/mailtransport_smtpplugin.so

%files -n libKPim6MailTransport6
%license LICENSES/*
%{_kf6_libdir}/libKPim6MailTransport.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6MailTransport.*
%{_includedir}/KPim6/MailTransport/
%{_kf6_cmakedir}/KPim6MailTransport/
%{_kf6_libdir}/libKPim6MailTransport.so

%files lang -f kmailtransport.lang

%changelog
