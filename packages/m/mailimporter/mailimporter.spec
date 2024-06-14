#
# spec file for package mailimporter
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
Name:           mailimporter
Version:        24.05.1
Release:        0
Summary:        Mail import functionality for KDE PIM applications
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiMime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommon) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}

%description
The mailimporter library is a KDE PIM project to provide a framework
for importing mail from different formats into Mail User Agents such as
KMail or Kontact.

%package devel
Summary:        Development package for mailimporter
License:        LGPL-2.1-or-later
Requires:       libKPim6MailImporter6 = %{version}
Requires:       libKPim6MailImporterAkonadi6 = %{version}
Requires:       cmake(KF6Archive) >= %{kf6_version}

%description devel
This package provides the development headers of the mailimporter library.

%package -n libKPim6MailImporter6
Summary:        MailImporter library for kdepim
License:        LGPL-2.1-or-later
Requires:       mailimporter >= %{version}
Obsoletes:      libKF5MailImporter5 < %{version}
Obsoletes:      libKPim5MailImporter5 < %{version}

%description -n libKPim6MailImporter6
This package provides the mailimporter library, used by KDE PIM applications
to import data from other mail formats (such as mbox, Maildir...).

%package -n libKPim6MailImporterAkonadi6
Summary:        MailImporter Akonadi based library for kdepim
License:        LGPL-2.1-or-later
Requires:       mailimporter >= %{version}
Obsoletes:      libKF5MailImporterAkonadi5 < %{version}
Obsoletes:      libKPim5MailImporterAkonadi5 < %{version}

%description -n libKPim6MailImporterAkonadi6
This package provides the mailimporter library for Akonadi based functions,
used by KDE PIM applications to import data from other mail formats
(such as mbox, Maildir...).

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6MailImporter6
%ldconfig_scriptlets -n libKPim6MailImporterAkonadi6

%files
%{_kf6_debugdir}/mailimporter.categories
%{_kf6_debugdir}/mailimporter.renamecategories

%files -n libKPim6MailImporter6
%license LICENSES/*
%{_kf6_libdir}/libKPim6MailImporter.so.*

%files -n libKPim6MailImporterAkonadi6
%{_kf6_libdir}/libKPim6MailImporterAkonadi.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6MailImporter.*
%doc %{_kf6_qchdir}/KPim6MailImporterAkonadi.*
%{_includedir}/KPim6/MailImporter/
%{_includedir}/KPim6/MailImporterAkonadi/
%{_kf6_cmakedir}/KPim6MailImporter/
%{_kf6_cmakedir}/KPim6MailImporterAkonadi/
%{_kf6_libdir}/libKPim6MailImporter.so
%{_kf6_libdir}/libKPim6MailImporterAkonadi.so

%files lang -f %{name}.lang

%changelog
