#
# spec file for package latte-dock
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017 Smith AR <audoban@openmailbox.org>
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


%global __requires_exclude qmlimport\\(org\\.kde\\.latte\\.private\\.app

%bcond_without released
%define kf5_version 5.88.0
Name:           latte-dock
Version:        0.11.0~20220619T183501
Release:        0
Summary:        Replacement Dock for Plasma Desktops
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://invent.kde.org/plasma/latte-dock
Source0:        latte-dock-%{version}.tar.xz
# Temporarily using a git snapshot with -lang tarball
Source1:        latte-dock-lang.tar.xz
#%if %{with released}
#Source1:        https://download.kde.org/stable/latte-dock/latte-dock-%{version}.tar.xz.sig
#Source2:        latte-dock.keyring
#%endif
BuildRequires:  fdupes
BuildRequires:  libSM-devel
BuildRequires:  pkgconfig
BuildRequires:  plasma-wayland-protocols
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
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{kf5_version}
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
BuildRequires:  cmake(Qt5WaylandClient)
BuildRequires:  cmake(Qt5X11Extras) >= 5.9.0
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
Latte is an alternative application launcher and dock for Plasma.
It animates its contents by using a parabolic zoom effect and tries to be there only when it is needed.

%lang_package

%prep
%autosetup -p1 -a 1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%if 0%{?suse_version}
%suse_update_desktop_file -r org.kde.%{name} Utility DesktopUtility
%endif
%if %{with released}
%find_lang %{name} --all-name
%endif

%files
%doc README.md
%license LICENSES/*
%{_kf5_bindir}/%{name}
%{_kf5_plasmadir}/
%{_kf5_qmldir}/
%{_kf5_servicetypesdir}/latte-indicator.desktop
%{_kf5_sharedir}/dbus-1/interfaces/
%{_kf5_notifydir}/
%{_kf5_iconsdir}/hicolor/24x24/
%{_kf5_iconsdir}/hicolor/*/apps/%{name}.svg
%{_kf5_iconsdir}/breeze/
%{_kf5_appstreamdir}/*.appdata.xml
%{_kf5_applicationsdir}/org.kde.%{name}.desktop
%dir %{_kf5_plugindir}/plasma/containmentactions/
%{_kf5_plugindir}/plasma/containmentactions/plasma_containmentactions_lattecontextmenu.so
%{_kf5_plugindir}/kpackage/packagestructure/latte_indicator.so
%{_kf5_sharedir}/latte/
%{_kf5_knsrcfilesdir}/latte-indicators.knsrc
%{_kf5_knsrcfilesdir}/latte-layouts.knsrc

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
