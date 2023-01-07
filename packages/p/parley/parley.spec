#
# spec file for package parley
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
Name:           parley
Version:        22.12.1
Release:        0
Summary:        Vocabulary Trainer
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/parley
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LibKEduVocDocument)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
Requires:       kdeedu-data
Obsoletes:      %{name}5 < %{version}
Obsoletes:      parley5 < %{version}
Provides:       %{name}5 = %{version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64

%description
Parley is a vocabulary trainer by KDE.

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

%files
%license LICENSES/*
%doc AUTHORS README.md
%doc %lang(en) %{_kf5_htmldir}/en/parley/
%{_kf5_applicationsdir}/org.kde.parley.desktop
%{_kf5_appstreamdir}/org.kde.parley.appdata.xml
%{_kf5_bindir}/parley
%{_kf5_configkcfgdir}/documentsettings.kcfg
%{_kf5_configkcfgdir}/languagesettings.kcfg
%{_kf5_configkcfgdir}/parley.kcfg
%{_kf5_iconsdir}/*/*/*/*
%{_kf5_knsrcfilesdir}/parley*.knsrc
%{_kf5_kxmlguidir}/parley/
%{_kf5_sharedir}/parley/

%files lang -f %{name}.lang

%changelog
