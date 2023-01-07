#
# spec file for package kleopatra
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
Name:           kleopatra
Version:        22.12.1
Release:        0
Summary:        Certificate manager and GUI for OpenPGP and CMS cryptography
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kleopatra
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
# c++-20 required
%if 0%{?suse_version} == 1500
BuildRequires:  gcc10-c++
BuildRequires:  gcc10-PIE
%endif
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
Obsoletes:      kleopatra5 < %{version}
Provides:       kleopatra5 = %{version}

%description
Kleopatra is a certificate manager and GUI for OpenPGP and CMS cryptography.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} == 1500
export CXX=g++-10
%endif
%cmake_kf5 -d build

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%suse_update_desktop_file org.kde.kleopatra Utility Security

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/kleopatra/
%doc %lang(en) %{_kf5_htmldir}/en/kwatchgnupg/
%{_kf5_applicationsdir}/kleopatra_import.desktop
%{_kf5_applicationsdir}/org.kde.kleopatra.desktop
%{_kf5_appstreamdir}/org.kde.kleopatra.appdata.xml
%{_kf5_bindir}/kleopatra
%{_kf5_bindir}/kwatchgnupg
%{_kf5_debugdir}/kleopatra.categories
%{_kf5_debugdir}/kleopatra.renamecategories
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_iconsdir}/hicolor/*/apps/kleopatra.png
%{_kf5_libdir}/libkleopatraclientcore.so*
%{_kf5_libdir}/libkleopatraclientgui.so*
%dir %{_kf5_plugindir}/pim5/
%dir %{_kf5_plugindir}/pim5/kcms
%dir %{_kf5_plugindir}/pim5/kcms/kleopatra
%{_kf5_plugindir}/pim5/kcms/kleopatra/kleopatra_config_gnupgsystem.so
%{_kf5_sharedir}/kconf_update/
%{_kf5_sharedir}/kleopatra/
%{_kf5_sharedir}/kwatchgnupg/
%dir %{_kf5_sharedir}/kio
%dir %{_kf5_sharedir}/kio/servicemenus
%{_kf5_sharedir}/kio/servicemenus/kleopatra_decryptverifyfiles.desktop
%{_kf5_sharedir}/kio/servicemenus/kleopatra_decryptverifyfolders.desktop
%{_kf5_sharedir}/kio/servicemenus/kleopatra_signencryptfiles.desktop
%{_kf5_sharedir}/kio/servicemenus/kleopatra_signencryptfolders.desktop
%{_kf5_sharedir}/mime/packages/application-vnd-kde-kleopatra.xml

%files lang -f %{name}.lang

%changelog
