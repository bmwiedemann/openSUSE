#
# spec file for package khealthcertificate
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

%bcond_without released
Name:           khealthcertificate
Version:        24.05.2
Release:        0
Summary:        Handling of digital vaccination, test and recovery certificates
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(zlib)

%description
KHeathCertificate permits parsing of digital vaccination, test and recovery
certificates.
The following certificate formats can be parsed:
- Digital Infrastructure for Vaccination Open Credentialing (DIVOC), the
system used for Indian vaccination certificates.
- EU "Digital Green Certificate" (DCG) vaccination, test and recovery
certificates
- SMART Heath Cards (SHC) vaccination certificates, in use some areas of North
America.
Check the README.md file for formats with limited support.

%package imports
Summary:        QML imports for using KHealthCertificate

%description imports
QML imports for using KHealthCertificate.

%package -n libKHealthCertificate1
Summary:        Handling of digital vaccination, test and recovery certificates
Requires:       khealthcertificate >= %{version}

%description -n libKHealthCertificate1
KHeathCertificate permits parsing of digital vaccination, test and recovery
certificates.
The following certificate formats can be parsed:
- Digital Infrastructure for Vaccination Open Credentialing (DIVOC), the
system used for Indian vaccination certificates.
- EU "Digital Green Certificate" (DCG) vaccination, test and recovery
certificates
- SMART Heath Cards (SHC) vaccination certificates, in use some areas of North
America.
Check the README.md file for formats with limited support.

%package devel
Summary:        Development files for khealthcertificate
Requires:       libKHealthCertificate1 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the khealthcertificate library.

%prep
%autosetup -p1

%build

%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libKHealthCertificate1

%files
%{_kf6_debugdir}/org_kde_khealthcertificate.categories

%files imports
%{_kf6_qmldir}/org/kde/khealthcertificate/

%files -n libKHealthCertificate1
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKHealthCertificate.so.*

%files devel
%{_includedir}/KHealthCertificate/
%{_kf6_cmakedir}/KHealthCertificate/
%{_kf6_libdir}/libKHealthCertificate.so

%changelog
