#
# spec file for package neochat
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           neochat
Version:        24.05.1
Release:        0
Summary:        A chat client for Matrix, the decentralized communication protocol
License:        BSD-2-Clause AND GPL-3.0-only AND GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://apps.kde.org/neochat/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# Needed for leap 15.5
BuildRequires:  cmark
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  fdupes
# Both kquickimageeditor flavors provide the same CMake target name, use the devel package name instead
# BuildRequires:  cmake(KQuickImageEditor)
BuildRequires:  kquickimageeditor6-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.7.2
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Multimedia) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebView) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(QuotientQt6) >= 0.7.0
BuildRequires:  pkgconfig(icu-uc) >= 61.0
BuildRequires:  pkgconfig(libcmark)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       kf6-kquickcharts >= %{kf6_version}
Requires:       kf6-prison-imports >= %{kf6_version}
Requires:       kf6-qqc2-desktop-style >= %{kf6_version}
Requires:       kf6-syntax-highlighting-imports >= %{kf6_version}
Requires:       kirigami-addons6 >= 0.7.2
Requires:       qt6-location >= %{qt6_version}
Requires:       qt6-positioning-imports >= %{qt6_version}
Requires:       qt6qmlimport(org.kde.kquickimageeditor.1)

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang %{name} --all-name --with-man

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.neochat.desktop
%{_kf6_appstreamdir}/org.kde.neochat.appdata.xml
%{_kf6_bindir}/neochat
%{_kf6_debugdir}/neochat.categories
%{_kf6_iconsdir}/hicolor/*/apps/org.kde.neochat.svg
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.neochat.tray.svg
%{_kf6_mandir}/man1/neochat.1%{?ext_man}
%dir %{_kf6_plugindir}/kf6/purpose
%{_kf6_plugindir}/kf6/purpose/neochatplugin.so
%{_kf6_notificationsdir}/neochat.notifyrc
%{_kf6_sharedir}/krunner/dbusplugins/plasma-runner-neochat.desktop

%files lang -f %{name}.lang

%changelog
