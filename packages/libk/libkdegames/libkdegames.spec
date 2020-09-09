#
# spec file for package libkdegames
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
Name:           libkdegames
Version:        20.08.1
Release:        0
Summary:        General Data for KDE Games
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch1:         libkdegames-bnc793185.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libsndfile-devel
BuildRequires:  openal-soft-devel
BuildRequires:  xz
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DNSSD)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
Recommends:     %{name}-lang
Obsoletes:      %{name}-kf5 < %{version}
Provides:       %{name}-kf5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains data which is required by the KDE games library.

%lang_package

%prep
%setup -q
%patch1 -p1

# bnc#793185
rm -rf carddecks/svg-konqi-modern

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif
  %fdupes -s %{buildroot}

%package -n libkf5kdegames6
Summary:        Library for KDE Games
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
Requires:       libkdegames = %{version}

%description -n libkf5kdegames6
This package contains the KDE games library.

%post -n libkf5kdegames6 -p /sbin/ldconfig
%postun -n libkf5kdegames6 -p /sbin/ldconfig

%package devel
Summary:        Library for KDE Games: Build Environment
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libkf5kdegames6 = %{version}
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
Group:          System/GUI/KDE
Requires:       kdegames-carddecks-default = %{version}
BuildArch:      noarch

%description -n kdegames-carddecks-other
This package contains several further card deck set for KDE games.

%package -n kdegames-carddecks-default
Summary:        Default Card Decks for KDE Games
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
BuildArch:      noarch

%description -n kdegames-carddecks-default
This package contains the default card deck set for KDE games.

%files
%license COPYING*
%doc README
%{_kf5_sharedir}/kconf_update/

%files -n libkf5kdegames6
%license COPYING*
%doc README
%{_kf5_libdir}/libKF5KDEGames.so.*
%{_kf5_libdir}/libKF5KDEGamesPrivate.so.*
%{_kf5_qmldir}/
%{_kf5_debugdir}/libkdegames.categories

%files devel
%license COPYING*
%doc README
%{_kf5_cmakedir}/KF5KDEGames/
%{_kf5_includedir}/KF5KDEGames/
%{_kf5_libdir}/libKF5KDEGames.so
%{_kf5_libdir}/libKF5KDEGamesPrivate.so

%files -n kdegames-carddecks-other
%license COPYING
%doc README
%exclude %{_kf5_sharedir}/carddecks/svg-oxygen-air
%{_kf5_sharedir}/carddecks

%files -n kdegames-carddecks-default
%license COPYING
%doc README
%{_kf5_sharedir}/carddecks/svg-oxygen-air

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
