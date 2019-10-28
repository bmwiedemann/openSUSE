#
# spec file for package libkdegames
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
Name:           libkdegames
Version:        19.08.2
Release:        0
Summary:        General Data for KDE Games
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch1:         libkdegames-bnc793185.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  karchive-devel
BuildRequires:  kbookmarks-devel
BuildRequires:  kcodecs-devel
BuildRequires:  kcompletion-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdnssd-framework-devel
BuildRequires:  kf5-filesystem
BuildRequires:  kglobalaccel-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kitemviews-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kservice-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libsndfile-devel
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
Obsoletes:      %{name}-kf5 < %{version}
Provides:       %{name}-kf5 = %{version}
Recommends:     %{name}-lang

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
  %make_jobs

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
Requires:       kcompletion-devel
Requires:       kconfig-devel
Requires:       kconfigwidgets-devel
Requires:       ki18n-devel
Requires:       kwidgetsaddons-devel
Requires:       libkf5kdegames6 = %{version}
Requires:       libsndfile-devel
Requires:       openal-soft-devel
Requires:       pkgconfig(Qt5Network)
Requires:       pkgconfig(Qt5Qml)
Requires:       pkgconfig(Qt5QuickWidgets)
Requires:       pkgconfig(Qt5Widgets)
Requires:       pkgconfig(Qt5Xml)
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
#don't obsolete kdegames4-carddecks-other yet, lskat is still KDE4 based
#Obsoletes:      kdegames4-carddecks-other < %{version}
BuildArch:      noarch

%description -n kdegames-carddecks-other
This package contains several further card deck set for KDE games.

%package -n kdegames-carddecks-default
Summary:        Default Card Decks for KDE Games
#don't obsolete kdegames4-carddecks-default yet, lskat is still KDE4 based and is broken without it
#Obsoletes:      kdegames4-carddecks-default < %{version}
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
