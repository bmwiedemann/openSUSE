#
# spec file for package mailimporter
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           mailimporter
Version:        22.12.0
Release:        0
Summary:        Mail import functionality for KDE PIM applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiMime)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

%description
The mailimporter library is a KDE PIM project to provide a framework
for importing mail from different formats into Mail User Agents such as
KMail or Kontact.

%package devel
Summary:        Development package for mailimporter
License:        LGPL-2.1-or-later
Requires:       libKF5MailImporter5 = %{version}
Requires:       libKF5MailImporterAkonadi5 = %{version}
Requires:       cmake(KF5Archive)

%description devel
This package provides the development headers of the mailimporter library.

%package -n libKF5MailImporter5
Summary:        MailImporter library for kdepim
License:        LGPL-2.1-or-later
Requires:       %{name} >= %{version}

%description -n libKF5MailImporter5
This package provides the mailimporter library, used by KDE PIM applications
to import data from other mail formats (such as mbox, Maildir...).

%package -n libKF5MailImporterAkonadi5
Summary:        MailImporter Akonadi based library for kdepim
License:        LGPL-2.1-or-later
Requires:       %{name} >= %{version}

%description -n libKF5MailImporterAkonadi5
This package provides the mailimporter library for Akonadi based functions,
used by KDE PIM applications to import data from other mail formats
(such as mbox, Maildir...).

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%post  -n libKF5MailImporter5 -p /sbin/ldconfig
%postun -n libKF5MailImporter5 -p /sbin/ldconfig
%post  -n libKF5MailImporterAkonadi5 -p /sbin/ldconfig
%postun -n libKF5MailImporterAkonadi5 -p /sbin/ldconfig

%files devel
%{_kf5_cmakedir}/KF5MailImporter/
%{_kf5_cmakedir}/KF5MailImporterAkonadi/
%{_kf5_includedir}/MailImporter/
%{_kf5_includedir}/MailImporterAkonadi/
%{_kf5_libdir}/libKF5MailImporter.so
%{_kf5_libdir}/libKF5MailImporterAkonadi.so
%{_kf5_mkspecsdir}/qt_MailImporter.pri
%{_kf5_mkspecsdir}/qt_MailImporterAkonadi.pri

%files -n libKF5MailImporter5
%license LICENSES/*
%{_kf5_libdir}/libKF5MailImporter.so.*

%files -n libKF5MailImporterAkonadi5
%{_kf5_libdir}/libKF5MailImporterAkonadi.so.*

%files
%{_kf5_debugdir}/mailimporter.categories
%{_kf5_debugdir}/mailimporter.renamecategories

%files lang -f %{name}.lang

%changelog
