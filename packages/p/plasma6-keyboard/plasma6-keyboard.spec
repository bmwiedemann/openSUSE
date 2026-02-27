#
# spec file for package plasma6-keyboard
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 Shawn W Dunn <sfalken@opensuse.org>
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
%global kf6_version 6.5.0
%global qt6_version 6.8.0

# Internal
%global __requires_exclude qt6qmlimport\\(org\\.kde\\.plasma\\.keyboard.*

%global rname plasma-keyboard
# Full Plasma6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.80.0 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-keyboard
Version:        6.6.1
Release:        0
Summary:        Virtual Keyboard for Qt based desktops
License:        GPL-2.0-or-later AND GPL-3.0-only
URL:            https://invent.kde.org/plasma/plasma-keyboard
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif

BuildRequires:  cmake >= 3.22
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig

BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6GuiPrivate) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6VirtualKeyboard) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClient) >= %{qt6_version}
BuildRequires:  cmake(Qt6WaylandClientPrivate) >= %{qt6_version}

BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

Requires:       (plasma6-keyboard-kcm if systemsettings6)

# qrc:/qt/qml/org/kde/plasma/keyboard/maim.qml
Requires:       qt6qmlimport(org.kde.layershell)

%description
The plasma-keyboard is a virtual keyboard based on Qt Virtual Keyboard
designed to integrate in Plasma.

%package kcm
Summary:        Plasma KCM for %{rname}
Requires:       %{name} = %{version}
Requires:       systemsettings6

%description kcm
KCM for plasmakeyboard, for systemsettings integration

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6
%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang plasma-keyboard --with-qt
%find_lang kcm_plasmakeyboard --with-qt

%check
desktop-file-validate %{buildroot}%{_kf6_applicationsdir}/kcm_plasmakeyboard.desktop
desktop-file-validate %{buildroot}%{_kf6_applicationsdir}/org.kde.plasma.keyboard.desktop

%files -f plasma-keyboard.lang
%license LICENSES/*
%doc README.md
%dir %{_kf6_qmldir}/QtQuick/VirtualKeyboard
%dir %{_kf6_qmldir}/QtQuick/VirtualKeyboard/Styles
%{_kf6_qmldir}/QtQuick/VirtualKeyboard/Styles/Breeze/
%dir %{_kf6_qmldir}/org/kde/plasma
%{_kf6_bindir}/%{rname}
%{_kf6_qmldir}/org/kde/plasma/keyboard/
%{_kf6_applicationsdir}/org.kde.plasma.keyboard.desktop
%{_kf6_appstreamdir}/org.kde.plasma.keyboard.metainfo.xml
%dir %{_kf6_plasmadir}/keyboard
%{_kf6_plasmadir}/keyboard/layouts

%files kcm -f kcm_plasmakeyboard.lang
%{_kf6_applicationsdir}/kcm_plasmakeyboard.desktop
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_plasmakeyboard.so

%changelog

