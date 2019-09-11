#
# spec file for package kmahjongg
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
Name:           kmahjongg
Version:        19.08.0
Release:        0
Summary:        Mahjongg game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
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
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdoctools-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  libkmahjongg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
Obsoletes:      kmahjongg5 < %{version}
Provides:       kmahjongg5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
KMahjongg is a clone of the well known tile based patience game of the
same name. In the game you have to empty a game board filled with piece
by removing pieces of the same type.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kmahjongg-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kmahjongg          Game BoardGame

%files
%license COPYING*
%{_kf5_bindir}/kmahjongg
%doc %lang(en) %{_kf5_htmldir}/en/kmahjongg/
%{_kf5_applicationsdir}/org.kde.kmahjongg.desktop
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/apps/kmahjongg.*
%{_kf5_sharedir}/kmahjongg/
%{_kf5_kxmlguidir}/
%{_kf5_appstreamdir}/org.kde.kmahjongg.appdata.xml
%{_kf5_debugdir}/kmahjongg.categories

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
