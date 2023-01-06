#
# spec file for package oxygen5
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without released
%define kwin_deco 1

Name:           oxygen5
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Oxygen style, KWin decoration and cursors
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/oxygen-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/oxygen-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5FrameworkIntegration)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
%if %kwin_deco
BuildRequires:  cmake(KDecoration2) >= %{_plasma5_version}
%endif
BuildRequires:  xz
BuildRequires:  cmake(Qt5DBus) >= 5.15.0
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(xcb)
%if %kwin_deco
Requires:       oxygen5-decoration
%else
Obsoletes:      oxygen5-decoration
%endif
Requires:       oxygen5-style
Recommends:     %{name}-lang
Recommends:     oxygen-cursors
Recommends:     oxygen5-sounds

%description
Provides Oxygen style, KWin decoration, and cursors.

%package cursors
Summary:        The KDE Plasma Workspace Cursors
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
Provides:       oxygen-cursors = %{version}
%if 0%{?suse_version} > 1314 && "%{suse_version}" != "1320"
Obsoletes:      oxygen4-cursors < %{version}
Provides:       oxygen4-cursors = %{version}
Obsoletes:      oxygen-cursors4 < %{version}
Provides:       oxygen-cursors4 = %{version}
%else
Conflicts:      oxygen-cursors4
Conflicts:      oxygen4-cursors
%endif
Obsoletes:      oxygen-cursors5 < %{version}
Provides:       oxygen-cursors5 = %{version}
BuildArch:      noarch

%description cursors
This package contains the Oxygen cursor set.

%package style
Summary:        Oxygen style
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Obsoletes:      oxygen-style5 < %{version}
Provides:       oxygen-style5 = %{version}
# Color schemes were moved here
Conflicts:      plasma5-desktop < 5.16.90

%description style
This package contains the libraries of the Oxygen style.

%if %kwin_deco
%package decoration
Summary:        Oxygen's KWin decoration
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Supplements:    packageand(oxygen5-style:kwin5)
Obsoletes:      oxygen-decoration5 < %{version}
Provides:       oxygen-decoration5 = %{version}
%requires_eq oxygen5-style

%description decoration
This package contains the libraries Oxygen's KWin decoration.
%endif

%lang_package

%prep
%setup -q -n oxygen-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

%post     style -p /sbin/ldconfig

%postun   style -p /sbin/ldconfig

%if %kwin_deco
%post     decoration   -p /sbin/ldconfig

%postun   decoration   -p /sbin/ldconfig
%endif

%files
%license LICENSES/*

%files style
%license LICENSES/*
%{_kf5_bindir}/oxygen-demo5
%{_kf5_bindir}/oxygen-settings5
%{_kf5_libdir}/liboxygenstyle5.so.*
%{_kf5_libdir}/liboxygenstyleconfig5.so.*
%{_kf5_plugindir}/kstyle_oxygen_config.so
%{_kf5_plugindir}/styles/
%{_kf5_sharedir}/kstyle/
%dir %{_kf5_sharedir}/color-schemes/
%{_kf5_sharedir}/color-schemes/Oxygen*.colors
%{_kf5_plasmadir}/
%dir %{_kf5_servicesdir}
%{_kf5_servicesdir}/oxygenstyleconfig.desktop
%dir %{_kf5_iconsdir}/hicolor/*/
%dir %{_kf5_iconsdir}/hicolor/*/apps
%{_kf5_iconsdir}/hicolor/*/apps/oxygen-settings.png

%if %kwin_deco
%files decoration
%license LICENSES/*
%{_kf5_plugindir}/org.kde.kdecoration2/
%dir %{_kf5_servicesdir}
%{_kf5_servicesdir}/oxygendecorationconfig.desktop
%endif

%files cursors
%license LICENSES/*
%{_kf5_sharedir}/icons/Oxygen_*/
%{_kf5_sharedir}/icons/KDE_Classic/

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
