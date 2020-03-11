#
# spec file for package kaddressbook
#
# Copyright (c) 2020 SUSE LLC
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kaddressbook
Version:        19.12.3
Release:        0
Summary:        Address book application to manage contacts 
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiSearch)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KdepimDBusInterfaces)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5Prison)
BuildRequires:  cmake(Qt5DBus) >= 5.2.0
BuildRequires:  cmake(Qt5Gui) >= 5.2.0
BuildRequires:  cmake(Qt5PrintSupport) >= 5.2.0
BuildRequires:  cmake(Qt5Test) >= 5.2.0
BuildRequires:  cmake(Qt5Widgets) >= 5.2.0
Requires:       kdepim-runtime
Recommends:     %{name}-lang
Recommends:     %{name}-doc
Provides:       kaddressbook5 = %{version}
Obsoletes:      kaddressbook5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
KAddressbook is an application by KDE to manage contacts.

%package doc
Summary:        Documentation for kaddressbook
Group:          Documentation/HTML

%description doc
This package includes the user guide for KAddressbook in HTML format.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files doc
%license COPYING COPYING.LIB COPYING.DOC
%doc %lang(en) %{_kf5_htmldir}/en/kaddressbook/

%files
%license COPYING COPYING.LIB COPYING.DOC
%{_kf5_debugdir}/kaddressbook.categories
%{_kf5_debugdir}/kaddressbook.renamecategories
%dir %{_kf5_appstreamdir}/
%{_kf5_applicationsdir}/kaddressbook-importer.desktop
%{_kf5_applicationsdir}/org.kde.kaddressbook*.desktop
%{_kf5_appstreamdir}/org.kde.kaddressbook.appdata.xml
%{_kf5_bindir}/kaddressbook
%{_kf5_iconsdir}/hicolor/*/apps/kaddressbook.png
%{_kf5_iconsdir}/hicolor/scalable/apps/kaddressbook.svg
%{_kf5_libdir}/libkaddressbookprivate.so.*
%{_kf5_plugindir}/kaddressbook_config_plugins.so
%{_kf5_plugindir}/kaddressbookpart.so
%{_kf5_plugindir}/kontact_kaddressbookplugin.so
%{_kf5_servicesdir}/kaddressbook_config_plugins.desktop
%{_kf5_servicesdir}/kaddressbookpart.desktop
%{_kf5_servicesdir}/kontact/
%{_kf5_sharedir}/kaddressbook/
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kontact/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
