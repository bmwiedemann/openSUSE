#
# spec file for package plasma5-welcome
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
Name:           plasma5-welcome
Version:        5.27.1
Release:        0
Summary:        Onboarding wizard for Plasma
License:        GPL-2.0-only OR GPL-3.0-only
Group:          System/GUI/KDE
URL:            https://invent.kde.org/plasma/plasma-welcome
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-welcome-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-welcome-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0001-Use-the-openSUSE-wallpaper.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  cmake(KAccounts)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons) >= 5.98
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(Qt5Svg)
Requires:       kirigami2

%lang_package

%description
Welcome Center is the perfect introduction to KDE Plasma! It can help you learn how to connect to the internet, install apps, customize the system, and more!

%prep
%autosetup -p1 -n plasma-welcome-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%find_lang plasma-welcome

%files
%license LICENSES/*
%{_kf5_applicationsdir}/org.kde.plasma-welcome.desktop
%{_kf5_appstreamdir}/org.kde.plasma-welcome.appdata.xml
%{_sysconfdir}/xdg/autostart/org.kde.plasma-welcome.desktop
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%dir %{_kf5_qmldir}/org/kde/plasma/
%{_kf5_qmldir}/org/kde/plasma/welcome/
%{_kf5_bindir}/plasma-welcome

%files lang -f plasma-welcome.lang

%changelog
