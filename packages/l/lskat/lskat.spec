#
# spec file for package lskat
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
Name:           lskat
Version:        19.08.3
Release:        0
Summary:        German Skat game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Card
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       kdegames-carddecks-default
Recommends:     %{name}-lang
Obsoletes:      lskat5 < %{version}
Provides:       lskat5 = %{version}

%description
Lieutenant Skat is a nice two player card game which follows the rules
for the German game (Offiziers)-Skat. The program includes many
different carddecks to choose. A computer opponent can play for any of
the players.

%lang_package

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
  %suse_update_desktop_file -r org.kde.lskat          Game CardGame

%files
%license COPYING*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/lskat/
%{_kf5_debugdir}/*.categories
%{_kf5_applicationsdir}/org.kde.lskat.desktop
%{_kf5_appsdir}/lskat/
%{_kf5_appstreamdir}/org.kde.lskat.appdata.xml
%{_kf5_bindir}/lskat
%{_kf5_iconsdir}/hicolor/*/apps/lskat.*
%{_kf5_kxmlguidir}/lskat/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
