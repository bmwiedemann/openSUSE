#
# spec file for package akonadi-contacts
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
%define kpim6_version 6.1.2

%bcond_without released
Name:           akonadi-contacts
Version:        24.05.2
Release:        0
Summary:        KDE PIM Libraries for Akonadi Contacts
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Contacts) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Prison) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Provides:       akonadi-contact = %{version}
Obsoletes:      akonadi-contact < %{version}

%description
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n libKPim6AkonadiContactCore6
Summary:        Library for personal contact handling
Requires:       akonadi-contacts >= %{version}
Obsoletes:      akonadi-contact-lang < %{version}
Obsoletes:      akonadi-socialutils < %{version}
Obsoletes:      akonadi-socialutils-devel < %{version}
Obsoletes:      kdepim-apps-libs <= 20.08.3
Obsoletes:      kdepim-apps-libs-lang <= 20.08.3
Obsoletes:      libKF5AkonadiContact5 < %{version}
Obsoletes:      libKPim5AkonadiContact5 < %{version}

%description -n libKPim6AkonadiContactCore6
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n libKPim6AkonadiContactWidgets6
Summary:        Library for personal contact handling
Requires:       akonadi-contacts >= %{version}
Obsoletes:      libKF5ContactEditor5 < %{version}
Obsoletes:      libKPim5ContactEditor5 < %{version}

%description -n libKPim6AkonadiContactWidgets6
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n akonadi-plugin-contacts
Summary:        Plugins for personal contact handling
Requires:       akonadi-contacts >= %{version}

%description -n akonadi-plugin-contacts
This package provides plugins required by PIM applications to read and write contact data.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       libKPim6AkonadiContactCore6 = %{version}
Requires:       libKPim6AkonadiContactWidgets6 = %{version}
Requires:       cmake(KF6Contacts) >= %{kf6_version}
Requires:       cmake(KPim6Akonadi) >= %{kpim6_version}
Requires:       cmake(KPim6AkonadiContactCore) >= %{kpim6_version}
Requires:       cmake(KPim6GrantleeTheme) >= %{kpim6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      akonadi-contact-devel < %{version}
Obsoletes:      kdepim-apps-libs-devel <= 20.08.3

%description devel
This package contains all necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKPim6AkonadiContactCore6
%ldconfig_scriptlets -n libKPim6AkonadiContactWidgets6

%files
%{_kf6_datadir}/akonadi/contact/
%{_kf6_debugdir}/akonadi-contacts.categories
%{_kf6_debugdir}/akonadi-contacts.renamecategories

%files -n libKPim6AkonadiContactCore6
%license LICENSES/*
%{_kf6_libdir}/libKPim6AkonadiContactCore.so.*

%files -n libKPim6AkonadiContactWidgets6
%{_kf6_libdir}/libKPim6AkonadiContactWidgets.so.*

%files -n akonadi-plugin-contacts
%{_kf6_plugindir}/akonadi_serializer_addressee.so
%{_kf6_plugindir}/akonadi_serializer_contactgroup.so
%dir %{_kf6_sharedir}/akonadi
%dir %{_kf6_sharedir}/akonadi/plugins
%dir %{_kf6_sharedir}/akonadi/plugins/serializer
%{_kf6_sharedir}/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
%{_kf6_sharedir}/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop

%files devel
%doc %{_kf6_qchdir}/KPim6AkonadiContact*.*
%{_includedir}/KPim6/AkonadiContactCore/
%{_includedir}/KPim6/AkonadiContactWidgets/
%{_kf6_cmakedir}/KPim6AkonadiContactCore/
%{_kf6_cmakedir}/KPim6AkonadiContactWidgets/
%{_kf6_libdir}/libKPim6AkonadiContactCore.so
%{_kf6_libdir}/libKPim6AkonadiContactWidgets.so
%{_kf6_libdir}/libKPim6AkonadiContactWidgets.so

%files lang -f %{name}.lang

%changelog

