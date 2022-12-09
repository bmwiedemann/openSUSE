#
# spec file for package kanagram
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
Name:           kanagram
Version:        22.12.0
Release:        0
Summary:        Anagram Game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kanagram
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(LibKEduVocDocument)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5TextToSpeech)
Requires:       kdeedu-data
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
Kanagram is a letter order game.

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
%license COPYING*
%dir %{_kf5_iconsdir}/hicolor/24x24
%dir %{_kf5_iconsdir}/hicolor/24x24/apps
%dir %{_kf5_iconsdir}/hicolor/80x80
%dir %{_kf5_iconsdir}/hicolor/80x80/apps
%doc %lang(en) %{_kf5_htmldir}/en/kanagram/
%{_kf5_applicationsdir}/org.kde.kanagram.desktop
%{_kf5_appstreamdir}/org.kde.kanagram.appdata.xml
%{_kf5_bindir}/kanagram
%{_kf5_configkcfgdir}/kanagram.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/kanagram*.*
%{_kf5_knsrcfilesdir}/kanagram.knsrc
%{_kf5_sharedir}/kanagram/

%files lang -f %{name}.lang

%changelog
