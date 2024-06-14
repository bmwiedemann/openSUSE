#
# spec file for package kaddressbook
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
Name:           kaddressbook
Version:        24.05.1
Release:        0
Summary:        Address book application to manage contacts
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
URL:            https://apps.kde.org/kaddressbook
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KPim6Akonadi) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiContactWidgets) >= %{kpim6_version}
BuildRequires:  cmake(KPim6AkonadiSearch) >= %{kpim6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KontactInterface) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommonAkonadi) >= %{kpim6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       kdepim-runtime
Requires:       libKPim6AddressbookImportExport6 = %{version}
Recommends:     kaddressbook-doc
Provides:       kaddressbook5 = %{version}
Obsoletes:      kaddressbook5 < %{version}
# kdepim-runtime requires Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
KAddressbook is an application by KDE to manage contacts.

%package -n libKPim6AddressbookImportExport6
Summary:        Library which provides import/export functionality for KAddressbook
Obsoletes:      kdepim-apps-libs <= 20.08.3
Obsoletes:      kdepim-apps-libs-lang <= 20.08.3
Obsoletes:      libKPimAddressbookImportExport5 < %{version}
Obsoletes:      libKPim5AddressbookImportExport5 < %{version}

%description -n libKPim6AddressbookImportExport6
This library provides an interface to implement import/export plugins for KAddressbook.

%package -n libKPim6AddressbookImportExport6-devel
Summary:        Development headers for libKPimAddressbookImportExport
Requires:       libKPim6AddressbookImportExport6 = %{version}
Obsoletes:      libKPimAddressbookImportExport5-devel < %{version}
Obsoletes:      libKPim5AddressbookImportExport5-devel < %{version}

%description -n libKPim6AddressbookImportExport6-devel
This package includes development headers needed to develop and build import/export plugins
for KAddressbook.

%package doc
Summary:        Documentation for kaddressbook
BuildArch:      noarch

%description doc
This package includes the user guide for KAddressbook in HTML format.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%ldconfig_scriptlets
%ldconfig_scriptlets -n libKPim6AddressbookImportExport6

%files
%license LICENSES/*
%{_kf6_applicationsdir}/kaddressbook-importer.desktop
%{_kf6_applicationsdir}/kaddressbook-view.desktop
%{_kf6_applicationsdir}/org.kde.kaddressbook.desktop
%{_kf6_appstreamdir}/org.kde.kaddressbook.appdata.xml
%{_kf6_bindir}/kaddressbook
%{_kf6_debugdir}/kaddressbook.categories
%{_kf6_debugdir}/kaddressbook.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/kaddressbook.*
%{_kf6_libdir}/libkaddressbookprivate.so.*
%dir %{_kf6_plugindir}/pim6/
%dir %{_kf6_plugindir}/pim6/kcms/
%dir %{_kf6_plugindir}/pim6/kcms/kaddressbook/
%{_kf6_plugindir}/pim6/kcms/kaddressbook/kaddressbook_config_plugins.so
%{_kf6_plugindir}/pim6/kcms/kaddressbook/kaddressbook_config_userfeedback.so
%{_kf6_plugindir}/kaddressbookpart.so
%dir %{_kf6_plugindir}/pim6/kontact
%{_kf6_plugindir}/pim6/kontact/kontact_kaddressbookplugin.so
%{_kf6_sharedir}/kaddressbook/

%files -n libKPim6AddressbookImportExport6
%{_kf6_libdir}/libKPim6AddressbookImportExport.so.*

%files -n libKPim6AddressbookImportExport6-devel
%{_includedir}/KPim6/KAddressBookImportExport/
%{_kf6_cmakedir}/KPim6AddressbookImportExport/
%{_kf6_libdir}/libKPim6AddressbookImportExport.so

%files doc
%doc %lang(en) %{_kf6_htmldir}/en/kaddressbook/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kaddressbook/

%changelog
