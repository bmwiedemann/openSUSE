#
# spec file for package libkdegames
#
# Copyright (c) 2022 SUSE LLC
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

%define sover 7
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           libkdegames
Version:        22.12.1
Release:        0
Summary:        General Data for KDE Games
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch0:         libkdegames-bnc793185.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libsndfile-devel
BuildRequires:  openal-soft-devel
BuildRequires:  xz
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Obsoletes:      %{name}-kf5 < %{version}
Provides:       %{name}-kf5 = %{version}
Conflicts:      libkf5kdegames6 < %{version}
# Breaks debuginfo extraction of subpackages
#BuildArch:      noarch

%description
This package contains data which is required by the KDE games library.

%package qt5-imports
Summary:        QML modules for KDE games
License:        LGPL-2.1-or-later
Conflicts:      libkf5kdegames6 < %{version}

%description qt5-imports
This package contains QML modules for KDE games.

%package -n libKF5KDEGames%{sover}
Summary:        Library for KDE Games
License:        LGPL-2.1-or-later
Requires:       libkdegames >= %{version}
Requires:       %{name}-qt5-imports >= %{version}
# libkf5kdegames6 actually contained libKF5KDEGames.so.7 at some point,
# so obsolete that explicitly.
Provides:       libkf5kdegames6 = %{version}
Obsoletes:      libkf5kdegames6 < %{version}

%description -n libKF5KDEGames%{sover}
This package contains the KDE games library.

%package devel
Summary:        Library for KDE Games: Build Environment
License:        LGPL-2.1-or-later
Requires:       libKF5KDEGames%{sover} = %{version}
Requires:       libsndfile-devel
Requires:       openal-soft-devel
Requires:       cmake(KF5Completion)
Requires:       cmake(KF5Config)
Requires:       cmake(KF5ConfigWidgets)
Requires:       cmake(KF5I18n)
Requires:       cmake(KF5WidgetsAddons)
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Qml)
Requires:       cmake(Qt5QuickWidgets)
Requires:       cmake(Qt5Widgets)
Requires:       cmake(Qt5Xml)
Obsoletes:      %{name}-kf5-devel < %{version}
Provides:       %{name}-kf5-devel = %{version}

%description devel
This package contains all necessary files and libraries needed to
develop KDE games.

%package -n kdegames-carddecks-other
Summary:        Further Card Decks for KDE Games
License:        LGPL-2.1-or-later
Requires:       kdegames-carddecks-default = %{version}
BuildArch:      noarch

%description -n kdegames-carddecks-other
This package contains several further card deck set for KDE games.

%package -n kdegames-carddecks-default
Summary:        Default Card Decks for KDE Games
License:        LGPL-2.1-or-later
BuildArch:      noarch

%description -n kdegames-carddecks-default
This package contains the default card deck set for KDE games.

# Should be called libkdegames5-lang, but that requires replacing the
# macro with the expansion to Provide/Obsolete the old name.
%lang_package

%prep
%autosetup -p1

# bnc#793185
rm -r src/carddecks/svg-konqi-modern

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang libkdegames5

%fdupes %{buildroot}

%post -n libKF5KDEGames%{sover} -p /sbin/ldconfig
%postun -n libKF5KDEGames%{sover} -p /sbin/ldconfig

%files
# Unversioned
%{_kf5_sharedir}/kconf_update/
%{_kf5_debugdir}/libkdegames.categories

%files -n libkdegames-qt5-imports
# Qt/KF-versioned
%license LICENSES/*
%{_kf5_qmldir}/

%files -n libKF5KDEGames%{sover}
# sover-versioned
%license LICENSES/*
%doc README
%{_kf5_libdir}/libKF5KDEGames.so.%{sover}
%{_kf5_libdir}/libKF5KDEGames.so.%{sover}.*
%{_kf5_libdir}/libKF5KDEGamesPrivate.so.%{sover}
%{_kf5_libdir}/libKF5KDEGamesPrivate.so.%{sover}.*

%files devel
%{_kf5_cmakedir}/KF5KDEGames/
%{_kf5_includedir}/KDEGames/
%{_kf5_libdir}/libKF5KDEGames.so
%{_kf5_libdir}/libKF5KDEGamesPrivate.so

%files -n kdegames-carddecks-other
%license LICENSES/*
%doc README
%exclude %{_kf5_sharedir}/carddecks/svg-oxygen-air
%{_kf5_sharedir}/carddecks

%files -n kdegames-carddecks-default
%license LICENSES/*
%doc README
%{_kf5_sharedir}/carddecks/svg-oxygen-air

%files lang -f libkdegames5.lang

%changelog
