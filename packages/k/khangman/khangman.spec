#
# spec file for package khangman
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
Name:           khangman
Version:        22.12.0
Release:        0
Summary:        Hangman Game
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/khangman
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LibKEduVocDocument)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
Requires:       kdeedu-data
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Obsoletes:      khangman-devel < %{version}
Obsoletes:      khangman5 < %{version}
Obsoletes:      libkhangmanengine5 < %{version}

%description
Classical hangman game by KDE.

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
%config %{_kf5_configdir}/khangman.knsrc
%doc %lang(en) %{_kf5_htmldir}/en/khangman/
%doc %{_kf5_mandir}/man6/khangman.6.gz
%doc AUTHORS ChangeLog README
%{_kf5_applicationsdir}/org.kde.khangman.desktop
%{_kf5_appstreamdir}/org.kde.khangman.appdata.xml
%{_kf5_bindir}/khangman
%{_kf5_configkcfgdir}/khangman.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/khangman.*
%{_kf5_sharedir}/khangman/

%files lang -f %{name}.lang

%changelog
