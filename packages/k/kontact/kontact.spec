#
# spec file for package kontact
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
Name:           kontact
Version:        24.05.1
Release:        0
Summary:        Personal Information Manager
License:        GPL-2.0-or-later
URL:            https://kontact.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KPim6GrantleeTheme) >= %{kpim6_version}
BuildRequires:  cmake(KPim6KontactInterface) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommon) >= %{kpim6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Recommends:     kmail
Suggests:       akregator
Suggests:       kaddressbook
Suggests:       knotes
Suggests:       korganizer
Provides:       kontact5 = %{version}
Obsoletes:      kontact5 < %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
Kontact combines the individual applications KMail, KAddressBook and
KOrganizer as views in one window.

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

%files
%license LICENSES/*
# %%doc %%lang(en) %%{_kf6_htmldir}/en/kontact/
%{_kf6_applicationsdir}/org.kde.kontact.desktop
%{_kf6_appstreamdir}/org.kde.kontact.appdata.xml
%{_kf6_bindir}/kontact
%{_kf6_configkcfgdir}/kontact.kcfg
%{_kf6_debugdir}/kontact.categories
%{_kf6_debugdir}/kontact.renamecategories
%{_kf6_iconsdir}/hicolor/*/apps/kontact.png
%{_kf6_iconsdir}/hicolor/scalable/apps/kontact.svg
%dir %{_kf6_plugindir}/pim6
%dir %{_kf6_plugindir}/pim6/kcms
%dir %{_kf6_plugindir}/pim6/kcms/kontact
%{_kf6_plugindir}/pim6/kcms/kontact/kcm_kontact.so
%{_kf6_sharedir}/dbus-1/services/org.kde.kontact.service
%{_kf6_sharedir}/messageviewer/
%{_libdir}/libkontactprivate.so.*

%files lang -f %{name}.lang
# %%exclude %%{_kf6_htmldir}/en/kontact/

%changelog
