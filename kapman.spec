#
# spec file for package kapman
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
%define qt6_version 6.6.0

%bcond_without released
Name:           kapman
Version:        24.05.1
Release:        0
Summary:        Pac-Man-like game by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/kapman
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KDEGames6) 
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6SvgWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      kapman5 < %{version}
Provides:       kapman5 = %{version}

%description
Kapman is a clone of the well known game Pac-Man. You must go through the levels
escaping ghosts in a maze. You lose a life when a ghost eats you, but you can
eat the ghosts for a few seconds when eating an energizer. You win points when
eating pills, energizers, and bonus, and you win one life for each 10,000
points. When you have eaten all the pills and energizers of a level, you go to
the next level, and the player and ghost speeds increase. The game ends when you
have lost all your lives.

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
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/kapman/
%{_kf6_applicationsdir}/org.kde.kapman.desktop
%{_kf6_appstreamdir}/org.kde.kapman.appdata.xml
%{_kf6_bindir}/kapman
%{_kf6_iconsdir}/hicolor/*/apps/kapman.*
%{_kf6_sharedir}/kapman/
%{_kf6_sharedir}/sounds/kapman/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kapman/

%changelog
