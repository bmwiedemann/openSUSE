#
# spec file for package knights
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.0.0
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           knights
Version:        24.05.2
Release:        0
Summary:        A simple chess board
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/knights
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Plotting) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       gnuchess
Suggests:       crafty
Obsoletes:      kchess

%description
Knights is KDE's chess frontend. It supports playing local games against
human players or against chess engines (XBoard and UIC),
as well as playing online games on FICS server.
Furthermore, it is possible to watch two different chess engines playing
against each other.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --with-html --all-name


%files
%license LICENSE
%doc README.themes
%doc %lang(en) %{_kf6_htmldir}/en/knights/
%{_kf6_applicationsdir}/org.kde.knights.desktop
%{_kf6_appstreamdir}/org.kde.knights.appdata.xml
%{_kf6_bindir}/knights
%{_kf6_configkcfgdir}/knights.kcfg
%{_kf6_dbusinterfacesdir}/org.kde.Knights.xml
%{_kf6_debugdir}/knights.categories
%{_kf6_iconsdir}/*/*/*/knights.*
%{_kf6_knsrcfilesdir}/knights.knsrc
%{_kf6_sharedir}/knights/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/knights/

%changelog
