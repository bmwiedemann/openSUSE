#
# spec file for package kaddressbook
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kaddressbook
Version:        19.08.3
Release:        0
Summary:        Address Manager
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  akonadi-search-devel
BuildRequires:  akonadi-server-devel >= %{_kapp_version}
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  grantleetheme-devel
BuildRequires:  kcmutils-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kontactinterface-devel
BuildRequires:  kpimtextedit-devel
BuildRequires:  libkdepim-devel >= %{_kapp_version}
BuildRequires:  pkgconfig
BuildRequires:  prison-qt5-devel
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5KdepimDBusInterfaces)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
Requires:       kdepim-runtime
Recommends:     %{name}-lang
Provides:       kaddressbook5 = %{version}
Obsoletes:      kaddressbook5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
The KDE Address Book

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

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
