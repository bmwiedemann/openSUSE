#
# spec file for package tokodon
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
Name:           tokodon
Version:        24.05.1
Release:        0
Summary:        Mastodon client by KDE
License:        GPL-3.0-only
URL:            https://apps.kde.org/tokodon/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAddons) >= 0.11.40
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6QQC2DesktopStyle) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(MpvQt)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebSockets) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebView) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(mpv)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} %x86_64 aarch64 riscv64
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kf6-kitemmodels-imports >= %{kf6_version}
Requires:       kf6-sonnet-imports >= %{kf6_version}
Requires:       kirigami-addons6
Requires:       qt6-declarative-imports >= %{qt6_version}
Requires:       qt6-webview >= %{qt6_version}
Requires:       qt6-webview-imports >= %{qt6_version}

%description
Tokodon is a Mastodon client. It allows you to interact with the Fediverse
community.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang tokodon tokodon.lang

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.tokodon.desktop
%{_kf6_appstreamdir}/org.kde.tokodon.appdata.xml
%{_kf6_bindir}/tokodon
%{_kf6_debugdir}/tokodon.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.tokodon.svg
%{_kf6_iconsdir}/hicolor/scalable/actions/*.svg
%{_kf6_notificationsdir}/tokodon.notifyrc
%{_kf6_plugindir}/kf6/purpose/tokodonplugin.so
# TODO: only installed if kunifiedpush BR is present
# %%{_kf6_sharedir}/dbus-1/services/org.kde.tokodon.service

%files lang -f tokodon.lang

%changelog
