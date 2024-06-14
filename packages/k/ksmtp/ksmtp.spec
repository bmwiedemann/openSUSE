#
# spec file for package ksmtp
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
Name:           ksmtp
Version:        24.05.1
Release:        0
Summary:        Job-based library to send email through an SMTP server
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
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}

%description
KSMTP is a job based library to send email through an SMTP server.

%package -n libKPim6SMTP6
Summary:        Job-based library to send email through an SMTP server
Requires:       ksmtp >= %{version}
Obsoletes:      ksmtp-lang <= 23.04.0
Obsoletes:      libKF5SMTP5 < %{version}
Obsoletes:      libKPim5SMTP5 < %{version}
Obsoletes:      libKPim5SMTP5-lang < %{version}

%description -n libKPim6SMTP6
KSMTP is a job based library to send email through an SMTP server. This
package contains the KSMTP library itself.

%package devel
Summary:        Development files for KSMTP
Requires:       libKPim6SMTP6 = %{version}
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KF6KIO) >= %{kf6_version}
Requires:       cmake(KPim6Mime) >= %{kpim6_version}

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the KSMTP library.

%lang_package -n libKPim6SMTP6

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang libKPim6SMTP6 --all-name

%ldconfig_scriptlets -n libKPim6SMTP6

%files
%{_kf6_debugdir}/ksmtp.categories

%files -n libKPim6SMTP6
%license LICENSES/*
%{_kf6_libdir}/libKPim6SMTP.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6SMTP.*
%{_includedir}/KPim6/KSMTP/
%{_kf6_cmakedir}/KPim6SMTP/
%{_kf6_libdir}/libKPim6SMTP.so

%files -n libKPim6SMTP6-lang -f libKPim6SMTP6.lang

%changelog
