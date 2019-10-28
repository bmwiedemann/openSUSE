#
# spec file for package latte-dock
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017  Smith AR <audoban@openmailbox.org>
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


%define kf5_version 5.38.0
Name:           latte-dock
Version:        0.9.4
Release:        0
Summary:        Task manager
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://phabricator.kde.org/source/latte-dock/
Source:         https://download.kde.org/stable/latte-dock/latte-dock-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  libSM-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Activities) >= %{kf5_version}
BuildRequires:  cmake(KF5Archive) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5GlobalAccel) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5NewStuff) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Plasma) >= %{kf5_version}
BuildRequires:  cmake(KF5PlasmaQuick) >= %{kf5_version}
BuildRequires:  cmake(KF5SysGuard)
BuildRequires:  cmake(KF5Wayland) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5X11Extras) >= 5.9.0
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang
%if 0%{?is_opensuse}
BuildRequires:  update-desktop-files
%endif

%description
Latte is a dock based on plasma frameworks that animating its
contents by using parabolic zoom effect.

%lang_package

%prep
%setup -q

%build
%if 0%{?suse_version} <= 1315
   %cmake_kf5 -d build -- -DENABLE_MAKE_UNIQUE=ON
%else
   %cmake_kf5 -d build
%endif

%make_jobs

%install
%kf5_makeinstall -C build
%find_lang %{name} --all-name
%if 0%{?is_opensuse}
%suse_update_desktop_file -r org.kde.%{name} Utility DesktopUtility
%endif

%files
%doc README.md
%license COPYING*
%config %{_kf5_configdir}/latte-indicators.knsrc
%config %{_kf5_configdir}/latte-layouts.knsrc
%{_kf5_bindir}/%{name}
%{_kf5_plasmadir}/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/
%{_kf5_servicetypesdir}/latte-indicator.desktop
%{_kf5_sharedir}/dbus-1/interfaces/
%{_kf5_notifydir}/
%{_kf5_iconsdir}/hicolor/24x24/
%{_kf5_iconsdir}/hicolor/*/apps/%{name}.svg
%{_kf5_iconsdir}/breeze/
%{_kf5_appstreamdir}/*.appdata.xml
%{_kf5_applicationsdir}/org.kde.%{name}.desktop
%{_kf5_plugindir}/plasma_containmentactions_lattecontextmenu.so
%{_kf5_plugindir}/kpackage/packagestructure/latte_packagestructure_indicator.so
%{_kf5_sharedir}/latte/

%files lang -f %{name}.lang

%changelog
