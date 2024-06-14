#
# spec file for package libkdegames
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
Name:           libkdegames
Version:        24.05.1
Release:        0
Summary:        General Data for KDE Games
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch0:         libkdegames-bnc793185.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libsndfile-devel
BuildRequires:  openal-devel
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6DNSSD) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
This package contains data which is required by the KDE games library.

%package imports
Summary:        QML modules for KDE games

%description imports
This package contains QML modules for KDE games.

%package -n libKDEGames6
Summary:        Library for KDE Games
Requires:       libkdegames >= %{version}
Requires:       libkdegames-imports >= %{version}

%description -n libKDEGames6
This package contains the KDE games library.

%package devel
Summary:        Library for KDE Games: Build Environment
Requires:       libKDEGames6 = %{version}
Requires:       cmake(KF6Completion) >= %{kf6_version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6ConfigWidgets) >= %{kf6_version}
Requires:       cmake(KF6I18n) >= %{kf6_version}
Requires:       cmake(KF6WidgetsAddons) >= %{kf6_version}
Requires:       cmake(Qt6Network) >= %{qt6_version}
Requires:       cmake(Qt6Qml) >= %{qt6_version}
Requires:       cmake(Qt6QuickWidgets) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}

%description devel
This package contains all necessary files and libraries needed to
develop KDE games.

%package -n kdegames-carddecks-other
Summary:        Further Card Decks for KDE Games
Requires:       kdegames-carddecks-default = %{version}
BuildArch:      noarch

%description -n kdegames-carddecks-other
This package contains several further card deck set for KDE games.

%package -n kdegames-carddecks-default
Summary:        Default Card Decks for KDE Games
BuildArch:      noarch

%description -n kdegames-carddecks-default
This package contains the default card deck set for KDE games.

%lang_package

%prep
%autosetup -p1

# bnc#793185
rm -r src/carddecks/svg-konqi-modern

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang libkdegames6

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKDEGames6

%files
%{_kf6_debugdir}/libkdegames.categories

%files imports
%{_kf6_qmldir}/org/kde/games/

%files -n libKDEGames6
%license LICENSES/*
%doc README
%{_kf6_libdir}/libKDEGames6.so.6
%{_kf6_libdir}/libKDEGames6.so.6.*
%{_kf6_libdir}/libKDEGames6Private.so.6
%{_kf6_libdir}/libKDEGames6Private.so.6.*

%files devel
%{_kf6_cmakedir}/KDEGames6/
%{_includedir}/KDEGames6/
%{_kf6_libdir}/libKDEGames6.so
%{_kf6_libdir}/libKDEGames6Private.so

%files -n kdegames-carddecks-other
%license LICENSES/*
%{_kf6_sharedir}/carddecks/
%exclude %{_kf6_sharedir}/carddecks/svg-oxygen-air

%files -n kdegames-carddecks-default
%license LICENSES/*
%{_kf6_sharedir}/carddecks/svg-oxygen-air/

%files lang -f libkdegames6.lang

%changelog
