#
# spec file for package kajongg
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
Name:           kajongg
Version:        20.08.1
Release:        0
Summary:        4 Player Mahjongg game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  python3-Twisted >= 16.6.0
BuildRequires:  python3-base >= 3.5.0
BuildRequires:  python3-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KMahjongglib)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
Requires:       python3-Twisted
Requires:       python3-qt5
BuildArch:      noarch
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Recommends:     %{name}-lang

%description
Kajongg is a version of the four player Mahjongg tile game.

%lang_package

%prep
%setup -q -n kajongg-%{version}

%build
  # Workaround for kde#376303
  export PYTHONDONTWRITEBYTECODE=1
  export DESTDIR=%{buildroot}
  %cmake_kf5 -d build
  %cmake_build

%install
  %make_install -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
    %{kf5_find_htmldocs}
  %endif
  %suse_update_desktop_file -r org.kde.kajongg         Game BoardGame

%files
%license COPYING*
%doc README
%doc %lang(en) %{_kf5_htmldir}/en/kajongg/
%{_kf5_applicationsdir}/org.kde.kajongg.desktop
%{_kf5_appsdir}/kajongg/
%{_kf5_appstreamdir}/
%{_kf5_bindir}/kajongg
%{_kf5_bindir}/kajonggserver
%{_kf5_iconsdir}/hicolor/*/actions/games-kajongg-law.*
%{_kf5_iconsdir}/hicolor/*/apps/kajongg.*
%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
