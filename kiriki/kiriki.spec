#
# spec file for package kiriki
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
Name:           kiriki
Version:        19.08.1
Release:        0
Summary:        Yahtzee-like Game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdnssd-framework-devel
BuildRequires:  kdoctools-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kservice-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libkdegames-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      kiriki5 < %{version}
Provides:       kiriki5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
Kiriki is the KDE version of the dice game Yahtzee where you roll dices
to get higher scores in several combinations

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n kiriki-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kiriki          Game BoardGame

%files
%license COPYING*
%dir %{_kf5_appstreamdir}
%doc %lang(en) %{_kf5_htmldir}/en/kiriki/
%{_kf5_applicationsdir}/org.kde.kiriki.desktop
%{_kf5_appsdir}/kiriki/
%{_kf5_appstreamdir}/org.kde.kiriki.appdata.xml
%{_kf5_bindir}/kiriki
%{_kf5_iconsdir}/hicolor/*/apps/kiriki.*
%{_kf5_kxmlguidir}/kiriki/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
