#
# spec file for package kontact
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
Name:           kontact
Version:        22.12.1
Release:        0
Summary:        Personal Information Manager
License:        GPL-2.0-or-later
URL:            https://kontact.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KontactInterface)
BuildRequires:  cmake(KF5Libkdepim)
BuildRequires:  cmake(KF5PimCommonAkonadi)
BuildRequires:  cmake(KF5PimTextEdit)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     kmail
Suggests:       akregator
Suggests:       kaddressbook
Suggests:       knotes
Suggests:       korganizer
Provides:       kontact5 = %{version}
Obsoletes:      kontact5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
Kontact combines the individual applications KMail, KAddressBook and
KOrganizer as views in one window.

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

%suse_update_desktop_file org.kde.kontact Office Core-Office

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kontact/
%{_datadir}/messageviewer/
%{_kf5_applicationsdir}/org.kde.kontact.desktop
%{_kf5_appstreamdir}/org.kde.kontact.appdata.xml
%{_kf5_bindir}/kontact
%{_kf5_configkcfgdir}/kontact.kcfg
%{_kf5_debugdir}/kontact.categories
%{_kf5_debugdir}/kontact.renamecategories
%{_kf5_iconsdir}/hicolor/*/apps/kontact.png
%{_kf5_iconsdir}/hicolor/scalable/apps/kontact.svg
%dir %{_kf5_plugindir}/pim5
%dir %{_kf5_plugindir}/pim5/kcms
%dir %{_kf5_plugindir}/pim5/kcms/kontact
%{_kf5_plugindir}/pim5/kcms/kontact/kcm_kontact.so
%dir %{_kf5_sharedir}/dbus-1/services/
%{_kf5_sharedir}/dbus-1/services/org.kde.kontact.service
%{_libdir}/libkontactprivate.so.*

%files lang -f %{name}.lang

%changelog
