#
# spec file for package akonadi-contact
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


%define rname akonadi-contacts
%define sonum   5
%define kf5_version 5.104.0
%bcond_without released
Name:           akonadi-contact
Version:        23.04.1
Release:        0
Summary:        KDE PIM Libraries for Akonadi Contacts
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5Contacts) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5KCMUtils) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Prison) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5TextWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5GrantleeTheme)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       libKPim5AkonadiContact5 = %{version}
Requires:       libKPim5ContactEditor5 = %{version}
Provides:       akonadi-contacts = %{version}
Obsoletes:      akonadi-contacts < %{version}

%description
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n libKPim5AkonadiContact5
Summary:        Library for personal contact handling
Requires:       akonadi-contact >= %{version}
Obsoletes:      akonadi-socialutils
Obsoletes:      akonadi-socialutils-devel
Obsoletes:      kdepim-apps-libs <= 20.08.3
Obsoletes:      kdepim-apps-libs-lang <= 20.08.3

%description -n libKPim5AkonadiContact5
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n libKPim5ContactEditor5
Summary:        Library for personal contact handling
Requires:       akonadi-contact >= %{version}

%description -n libKPim5ContactEditor5
This package provides a library used for handling personal contacts,
as part of the KDE Personal Information Management (PIM) software.

%package -n akonadi-plugin-contacts
Summary:        Plugins for personal contact handling
Requires:       akonadi-contact >= %{version}

%description -n akonadi-plugin-contacts
This package provides plugins required by PIM applications to read and write contact data.

%package devel
Summary:        KDE PIM Libraries: Build Environment
Requires:       akonadi-contact = %{version}
Requires:       libKPim5AkonadiContact5 = %{version}
Requires:       libKPim5ContactEditor5 = %{version}
Requires:       cmake(Grantlee5)
Requires:       cmake(KPim5Akonadi)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KPim5GrantleeTheme)
Requires:       cmake(Qt5Widgets)
Provides:       akonadi-contacts-devel = %{version}
Obsoletes:      akonadi-contacts-devel < %{version}
Obsoletes:      kdepim-apps-libs-devel <= 20.08.3

%description devel
This package contains all necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n libKPim5AkonadiContact5
%ldconfig_scriptlets -n libKPim5ContactEditor5

%files
%license LICENSES/*
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/akonadi/
%dir %{_kf5_plugindir}/pim5/akonadi/contacts/
%dir %{_kf5_plugindir}/pim5/kcms/
%dir %{_kf5_plugindir}/pim5/kcms/kaddressbook
%{_kf5_datadir}/akonadi/contact/
%{_kf5_debugdir}/*.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_plugindir}/pim5/akonadi/contacts/plugins/
%{_kf5_plugindir}/pim5/kcms/kaddressbook/kcm_akonadicontact_actions.so

%files -n libKPim5AkonadiContact5
%{_kf5_libdir}/libKPim5AkonadiContact.so.*

%files -n libKPim5ContactEditor5
%{_kf5_libdir}/libKPim5ContactEditor.so.*

%files -n akonadi-plugin-contacts
%{_kf5_plugindir}/akonadi_serializer_addressee.so
%{_kf5_plugindir}/akonadi_serializer_contactgroup.so
%dir %{_kf5_sharedir}/akonadi
%dir %{_kf5_sharedir}/akonadi/plugins
%dir %{_kf5_sharedir}/akonadi/plugins/serializer
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
%{_kf5_sharedir}/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop

%files devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/AkonadiContact/
%{_includedir}/KPim5/AkonadiContactEditor/
%{_kf5_cmakedir}/KF5AkonadiContact/
%{_kf5_cmakedir}/KF5AkonadiContactEditor/
%{_kf5_cmakedir}/KPim5AkonadiContact/
%{_kf5_cmakedir}/KPim5ContactEditor/
%{_kf5_libdir}/libKPim5AkonadiContact.so
%{_kf5_libdir}/libKPim5ContactEditor.so
%{_kf5_mkspecsdir}/qt_AkonadiContact.pri
%{_kf5_mkspecsdir}/qt_ContactEditor.pri

%files lang -f %{name}.lang

%changelog
