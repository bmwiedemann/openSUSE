#
# spec file for package kleopatra
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
Name:           kleopatra
Version:        20.08.1
Release:        0
Summary:        KDE Key Manager
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  libboost_headers-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Libkleo)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     paperkey
Recommends:     %{name}-lang
Obsoletes:      kleopatra5 < %{version}
Provides:       kleopatra5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
Kleopatra is a Key Manager for KDE.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%suse_update_desktop_file org.kde.kleopatra      Utility Security

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/kleopatra.categories
%{_kf5_debugdir}/kleopatra.renamecategories
%dir %{_kf5_appstreamdir}
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%doc %lang(en) %{_kf5_htmldir}/en/kleopatra/
%doc %lang(en) %{_kf5_htmldir}/en/kwatchgnupg/
%{_kf5_applicationsdir}/kleopatra_import.desktop
%{_kf5_applicationsdir}/org.kde.kleopatra.desktop
%{_kf5_appstreamdir}/org.kde.kleopatra.appdata.xml
%{_kf5_bindir}/kleopatra
%{_kf5_bindir}/kwatchgnupg
%{_kf5_iconsdir}/hicolor/*/apps/kleopatra.png
%{_kf5_libdir}/libkleopatraclientcore.so*
%{_kf5_libdir}/libkleopatraclientgui.so*
%{_kf5_plugindir}/kcm_kleopatra.so
%{_kf5_servicesdir}/kleopatra_*.desktop
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kleopatra/
%{_kf5_sharedir}/kwatchgnupg/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
