#
# spec file for package khangman
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           khangman
Version:        19.08.1
Release:        0
Summary:        Hangman Game
License:        GPL-2.0-or-later
Group:          Amusements/Teaching/Language
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifications-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkeduvocdocument-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
Requires:       kdeedu-data
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Obsoletes:      khangman-devel < %{version}
Obsoletes:      khangman5 < %{version}
Obsoletes:      libkhangmanengine5 < %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Classical hangman game for KDE.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

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
