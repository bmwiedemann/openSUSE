#
# spec file for package ksmtp
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


%bcond_without released
Name:           ksmtp
Version:        22.12.0
Release:        0
Summary:        Job-based library to send email through an SMTP server
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
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)

%description
KSMTP is a job based library to send email through an SMTP server.

%package -n libKPimSMTP5
Summary:        Job-based library to send email through an SMTP server
Requires:       %{name}
Recommends:     %{name}-lang = %{version}

%description -n libKPimSMTP5
KSMTP is a job based library to send email through an SMTP server. This
package contains the KSMTP library itself.

%package devel
Summary:        Development files for KSMTP
Requires:       libKPimSMTP5 = %{version}
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5KIO)
Requires:       cmake(KF5Mime)

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the KSMTP library.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=ON
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --with-qt --all-name

%post -n libKPimSMTP5 -p /sbin/ldconfig
%postun -n libKPimSMTP5 -p /sbin/ldconfig

%files -n libKPimSMTP5
%license LICENSES/*
%{_kf5_libdir}/libKPimSMTP.so.*

%files
%{_kf5_debugdir}/ksmtp.categories

%files devel
%{_includedir}/KPim/
%{_kf5_cmakedir}/KPimSMTP/
%{_kf5_libdir}/libKPimSMTP.so
%{_kf5_mkspecsdir}/qt_KSMTP.pri

%files lang -f %{name}.lang

%changelog
