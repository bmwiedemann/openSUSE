#
# spec file for package knights
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


%bcond_without lang
Name:           knights
Version:        20.08.1
Release:        0
Summary:        A simple chess board
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Chess
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KDEGames)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Plotting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Widgets)
Requires:       gnuchess
Recommends:     %{name}-lang
Suggests:       crafty
Obsoletes:      kchess
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
Knights is KDE's chess frontend. It supports playing local games against
human players or against chess engines (XBoard and UIC),
as well as playing online games on FICS server.
Furthermore, it is possible to watch two different chess engines playing
against each other.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%if 0%{?suse_version}
%suse_update_desktop_file -r org.kde.knights Qt KDE Game BoardGame
%endif

%if %{with lang}
%find_lang %{name}
%{kf5_find_htmldocs}
%endif

%files
%license LICENSE
%doc README.themes
%{_kf5_applicationsdir}/org.kde.knights.desktop
%{_kf5_appstreamdir}/org.kde.knights.appdata.xml
%{_kf5_bindir}/knights
%{_kf5_configdir}/knights.knsrc
%dir %{_kf5_configkcfgdir}
%{_kf5_configkcfgdir}/knights.kcfg
%{_kf5_dbusinterfacesdir}/org.kde.Knights.xml
%{_kf5_debugdir}/knights.categories
%doc %{_kf5_htmldir}/en/knights/
%{_kf5_iconsdir}/*/*/*/knights.*
%{_kf5_kxmlguidir}/knights/
%{_kf5_sharedir}/knights/

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
