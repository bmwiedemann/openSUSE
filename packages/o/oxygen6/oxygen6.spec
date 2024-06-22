#
# spec file for package oxygen6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname oxygen

# Oxygen6 builds a style plugin compatible with KF5/Qt5
%bcond_without plasma5
%if %{with plasma5}
%define kf5_version 5.103.0
%define qt5_version 5.15.2
%endif

%bcond_without released
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Name:           oxygen6
Version:        6.1.0
Release:        0
Summary:        Oxygen style, KWin decoration and cursors
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
%if %{with plasma5}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5FrameworkIntegration) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_version}
%endif
BuildRequires:  cmake(KDecoration2) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FrameworkIntegration) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(xcb)
Requires:       oxygen6-decoration
Requires:       oxygen6-style
Recommends:     oxygen6-cursors
Recommends:     oxygen6-sounds

%description
Provides Oxygen style, KWin decoration, and cursors.

%package cursors
Summary:        The KDE Plasma Workspace Cursors
License:        GPL-3.0-or-later
Provides:       oxygen-cursors = %{version}
Provides:       oxygen-cursors4 = %{version}
Provides:       oxygen-cursors5 = %{version}
Provides:       oxygen4-cursors = %{version}
Provides:       oxygen5-cursors = %{version}
Obsoletes:      oxygen-cursors4 < %{version}
Obsoletes:      oxygen-cursors5 < %{version}
Obsoletes:      oxygen4-cursors < %{version}
Obsoletes:      oxygen5-cursors < %{version}
BuildArch:      noarch

%description cursors
This package contains the Oxygen cursor set.

%package style
Summary:        Oxygen style
License:        GPL-2.0-or-later
# Color schemes were moved to the oxygen repo
Conflicts:      plasma5-desktop < 5.16.90
Provides:       oxygen-style5 = %{version}
Obsoletes:      oxygen-style5 < %{version}
Provides:       oxygen5-style = %{version}
Obsoletes:      oxygen5-style < %{version}
Obsoletes:      oxygen5-style-lang < %{version}

%description style
This package contains the libraries of the Oxygen style.

%package decoration
Summary:        Oxygen's KWin decoration
License:        GPL-2.0-or-later
Requires:       oxygen6-style = %{version}
Supplements:    (oxygen6-style and kwin6)
Provides:       oxygen-decoration5 = %{version}
Obsoletes:      oxygen-decoration5 < %{version}
Provides:       oxygen5-decoration = %{version}
Obsoletes:      oxygen5-decoration < %{version}

%description decoration
This package contains the Oxygen's KWin decoration.

%lang_package -n %{name}-style

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DBUILD_QT6:BOOL=TRUE \
%if %{with plasma5}
  -DBUILD_QT5:BOOL=TRUE
%else
  -DBUILD_QT5:BOOL=FALSE
%endif

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets style

%files
%license LICENSES/*

%files style
%license LICENSES/*
%dir %{_kf6_sharedir}/color-schemes/
%{_kf6_appstreamdir}/org.kde.oxygen.appdata.xml
%{_kf6_bindir}/oxygen-demo6
%{_kf6_bindir}/oxygen-settings6
%{_kf6_iconsdir}/hicolor/*/apps/oxygen-settings.png
%{_kf6_libdir}/liboxygenstyle6.so.*
%{_kf6_libdir}/liboxygenstyleconfig6.so.*
%{_kf6_plasmadir}/look-and-feel/
%{_kf6_plugindir}/styles/
%{_kf6_plugindir}/kstyle_config/
%{_kf6_applicationsdir}/kcm_oxygendecoration.desktop
%{_kf6_sharedir}/color-schemes/Oxygen*.colors
%{_kf6_sharedir}/kstyle/
%if %{with plasma5}
%{_kf6_bindir}/oxygen-demo5
%{_kf5_libdir}/liboxygenstyle5.so.*
%{_kf5_libdir}/liboxygenstyleconfig5.so.*
%dir %{_kf5_plugindir}/styles
%{_kf5_plugindir}/styles/oxygen5.so
%endif

%files decoration
%license LICENSES/*
%{_kf6_plugindir}/org.kde.kdecoration2.kcm/
%{_kf6_plugindir}/org.kde.kdecoration2/

%files cursors
%license LICENSES/*
%{_kf6_iconsdir}/Oxygen_*/
%{_kf6_iconsdir}/KDE_Classic/

%files style-lang -f %{name}.lang

%changelog
