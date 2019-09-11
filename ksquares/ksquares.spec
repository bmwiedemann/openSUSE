#
# spec file for package ksquares
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
Name:           ksquares
Version:        19.08.1
Release:        0
Summary:        "Dots and boxes" board game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdnssd-framework-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  libkmahjongg-devel
BuildRequires:  phonon4qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
Recommends:     %{name}-lang

%description
KSquares is an implementation of the popular paper-based game
squares, better known as "La Pipopipette" in its original French
form, or "Dots and Boxes" in English. One must draw lines to complete
squares, and the player with the most squares wins. This
implementation can be played with up to 4 players, any number of
which may be controlled by the computer.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n ksquares-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.ksquares          Game BoardGame

%files
%license COPYING COPYING.DOC
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/ksquares/
%{_kf5_applicationsdir}/org.kde.ksquares.desktop
%{_kf5_appstreamdir}/
%{_kf5_bindir}/ksquares
%{_kf5_configkcfgdir}/ksquares.kcfg
%{_kf5_iconsdir}/hicolor/*/*/ksquares.*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
