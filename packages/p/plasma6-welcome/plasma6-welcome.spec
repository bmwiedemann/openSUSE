#
# spec file for package plasma6-welcome
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

%define rname plasma-welcome
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %global _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           plasma6-welcome
Version:        6.1.2
Release:        0
Summary:        Onboarding wizard for Plasma
License:        GPL-2.0-only OR GPL-3.0-only
URL:            https://invent.kde.org/plasma/plasma-welcome
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0001-Use-the-openSUSE-wallpaper.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KAccounts6)
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.10.0
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6Svg) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Plasma) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 0.10.0
Requires:       wallpaper-branding-openSUSE
Provides:       plasma5-welcome = %{version}
Obsoletes:      plasma5-welcome < %{version}
Obsoletes:      plasma5-welcome-lang < %{version}

%description
Welcome Center is the perfect introduction to KDE Plasma! It can help you learn
how to connect to the internet, install apps, customize the system, and more!

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang plasma-welcome

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.plasma-welcome.desktop
%{_kf6_appstreamdir}/org.kde.plasma-welcome.appdata.xml
%{_kf6_bindir}/plasma-welcome
%{_kf6_plugindir}/kf6/kded/kded_plasma-welcome.so

%files lang -f plasma-welcome.lang

%changelog
