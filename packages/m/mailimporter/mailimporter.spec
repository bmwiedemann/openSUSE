#
# spec file for package mailimporter
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


%bcond_without released
Name:           mailimporter
Version:        23.04.0
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
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiMime)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5Mime)
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
Requires:       libKPim5MailImporter5 = %{version}
Requires:       libKPim5MailImporterAkonadi5 = %{version}
Requires:       cmake(KF5Archive)

%description devel
This package provides the development headers of the mailimporter library.

%package -n libKPim5MailImporter5
Summary:        MailImporter library for kdepim
License:        LGPL-2.1-or-later
Requires:       mailimporter >= %{version}

%description -n libKPim5MailImporter5
This package provides the mailimporter library, used by KDE PIM applications
to import data from other mail formats (such as mbox, Maildir...).

%package -n libKPim5MailImporterAkonadi5
Summary:        MailImporter Akonadi based library for kdepim
License:        LGPL-2.1-or-later
Requires:       mailimporter >= %{version}

%description -n libKPim5MailImporterAkonadi5
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

%ldconfig_scriptlets -n libKPim5MailImporter5
%ldconfig_scriptlets -n libKPim5MailImporterAkonadi5

%files
%{_kf5_debugdir}/mailimporter.categories
%{_kf5_debugdir}/mailimporter.renamecategories

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/MailImporter/
%{_includedir}/KPim5/MailImporterAkonadi/
%{_kf5_cmakedir}/KF5MailImporter/
%{_kf5_cmakedir}/KPim5MailImporter/
%{_kf5_cmakedir}/KF5MailImporterAkonadi/
%{_kf5_cmakedir}/KPim5MailImporterAkonadi/
%{_kf5_libdir}/libKPim5MailImporter.so
%{_kf5_libdir}/libKPim5MailImporterAkonadi.so
%{_kf5_mkspecsdir}/qt_MailImporter.pri
%{_kf5_mkspecsdir}/qt_MailImporterAkonadi.pri

%files -n libKPim5MailImporter5
%license LICENSES/*
%{_kf5_libdir}/libKPim5MailImporter.so.*

%files -n libKPim5MailImporterAkonadi5
%{_kf5_libdir}/libKPim5MailImporterAkonadi.so.*

%files lang -f %{name}.lang

%changelog
