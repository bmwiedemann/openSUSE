#
# spec file for package kgpg
#
# Copyright (c) 2021 SUSE LLC
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
Name:           kgpg
Version:        21.04.0
Release:        0
Summary:        Encryption Tool
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://apps.kde.org/kgpg
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch0:         kgpg-autostart.diff
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libgpgme-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GrantleeTheme)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
Requires:       gpg2
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
BuildRequires:  libboost_headers-devel
Recommends:     %{name}-lang

%description
Kgpg is a simple GUI for gpg

%lang_package

%prep
%autosetup -p0

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
#suse_update_desktop_file org.kde.kgpg.deskt Utility Security

%files
%license COPYING
%doc AUTHORS
%config %{_kf5_configdir}/autostart/org.kde.kgpg.desktop
%doc %lang(en) %{_kf5_htmldir}/en/kgpg/
%{_kf5_applicationsdir}/org.kde.kgpg.desktop
%{_kf5_appstreamdir}/org.kde.kgpg.appdata.xml
%{_kf5_bindir}/kgpg
%{_kf5_configkcfgdir}/kgpg.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.kgpg.Key.xml
%{_kf5_debugdir}/kgpg.categories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kgpg/
%{_kf5_servicesdir}/ServiceMenus/
%{_kf5_sharedir}/kgpg/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
