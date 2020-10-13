#
# spec file for package khangman
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
Name:           khangman
Version:        20.08.2
Release:        0
Summary:        Hangman Game
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Language
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5Declarative)
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
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Classical hangman game for KDE.

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

%files
%license COPYING*
%doc AUTHORS ChangeLog README
%config %{_kf5_configdir}/khangman.knsrc
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/khangman/
%doc %{_kf5_mandir}/man6/khangman.6.gz
%{_kf5_applicationsdir}/org.kde.khangman.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/khangman
%{_kf5_configkcfgdir}/khangman.kcfg
%{_kf5_iconsdir}/hicolor/*/apps/khangman.*
%{_kf5_sharedir}/khangman/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
