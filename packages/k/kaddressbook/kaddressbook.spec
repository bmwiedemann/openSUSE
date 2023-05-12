#
# spec file for package kaddressbook
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
Name:           kaddressbook
Version:        23.04.1
Release:        0
Summary:        Address book application to manage contacts
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://apps.kde.org/kaddressbook
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Prison)
BuildRequires:  cmake(KPim5Akonadi)
BuildRequires:  cmake(KPim5AkonadiContact)
BuildRequires:  cmake(KPim5AkonadiSearch)
BuildRequires:  cmake(KPim5GrantleeTheme)
BuildRequires:  cmake(KPim5KontactInterface)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(KPim5TextEdit)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Requires:       kdepim-runtime
Requires:       libKPim5AddressbookImportExport5 = %{version}
Recommends:     %{name}-doc
Provides:       kaddressbook5 = %{version}
Obsoletes:      kaddressbook5 < %{version}

%description
KAddressbook is an application by KDE to manage contacts.

%package -n libKPim5AddressbookImportExport5
Summary:        Library which provides import/export functionality for KAddressbook
Obsoletes:      kdepim-apps-libs <= 20.08.3
Obsoletes:      kdepim-apps-libs-lang <= 20.08.3

%description -n libKPim5AddressbookImportExport5
This library provides an interface to implement import/export plugins for KAddressbook.

%package doc
Summary:        Documentation for kaddressbook
BuildArch:      noarch

%description doc
This package includes the user guide for KAddressbook in HTML format.

%package -n libKPim5AddressbookImportExport5-devel
Summary:        Development headers for libKPimAddressbookImportExport
Requires:       libKPim5AddressbookImportExport5 = %{version}

%description -n libKPim5AddressbookImportExport5-devel
This package includes development headers needed to develop and build import/export plugins
for KAddressbook.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%{kf5_find_htmldocs}

%ldconfig_scriptlets

%ldconfig_scriptlets -n libKPim5AddressbookImportExport5

%files doc
%doc %lang(en) %{_kf5_htmldir}/en/kaddressbook/

%files
%license LICENSES/*
%{_kf5_applicationsdir}/kaddressbook-importer.desktop
%{_kf5_applicationsdir}/kaddressbook-view.desktop
%{_kf5_applicationsdir}/org.kde.kaddressbook*.desktop
%{_kf5_appstreamdir}/org.kde.kaddressbook.appdata.xml
%{_kf5_bindir}/kaddressbook
%{_kf5_debugdir}/kaddressbook.categories
%{_kf5_debugdir}/kaddressbook.renamecategories
%{_kf5_iconsdir}/hicolor/*/apps/kaddressbook.png
%{_kf5_iconsdir}/hicolor/scalable/apps/kaddressbook.svg
%{_kf5_libdir}/libkaddressbookprivate.so.*
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/kcms/
%dir %{_kf5_plugindir}/pim5/kcms/kaddressbook/
%{_kf5_plugindir}/pim5/kcms/kaddressbook/kaddressbook_config_plugins.so
%{_kf5_plugindir}/kaddressbookpart.so
%{_kf5_plugindir}/pim5/kontact/
%{_kf5_sharedir}/kaddressbook/

%files -n libKPim5AddressbookImportExport5
%{_kf5_libdir}/libKPim5AddressbookImportExport.so.5
%{_kf5_libdir}/libKPim5AddressbookImportExport.so.5.*

%files -n libKPim5AddressbookImportExport5-devel
%dir %{_includedir}/KPim5
%{_includedir}/KPim5/KAddressBookImportExport/
%{_includedir}/KPim5/kaddressbookimportexport/
%{_includedir}/KPim5/kaddressbookimportexport_version.h
%{_kf5_cmakedir}/KPimAddressbookImportExport/
%{_kf5_cmakedir}/KPim5AddressbookImportExport/
%{_kf5_libdir}/libKPim5AddressbookImportExport.so
%{_kf5_mkspecsdir}/qt_KAddressbookImportExport.pri

%files lang -f %{name}.lang

%changelog
