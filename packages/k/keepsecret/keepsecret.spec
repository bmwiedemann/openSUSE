#
# spec file for package keepsecret
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define kf6_version 6.27.0
%define qt6_version 6.9.0

%bcond_without released
Name:           keepsecret
Version:        26.08.3
Release:        0
Summary:        Password manager GUI
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/keepsecret/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6ItemModels) >= %{kf6_version}
BuildRequires:  cmake(KF6Kirigami) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiAppComponents) >= 1.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(libsecret-1)
Requires:       kirigami-app-components6
Requires:       kirigami-addons6

%description
KeepSecret is a Password manager GUI intended to be a client for a Secret
Service compatible provider.
It can be used with KWallet, but also other systems such as oo7, Gnome-keyring
or KeepassXC.
When the service is running (or is dbus activated) this app will automatically
find and use it, showing all the secret colletions and the secrets contained
within.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%files
%license LICENSES/*
%doc README.md
%{_kf6_applicationsdir}/org.kde.keepsecret.desktop
%{_kf6_appstreamdir}/org.kde.keepsecret.metainfo.xml
%{_kf6_bindir}/keepsecret
%{_kf6_debugdir}/keepsecret.categories
%{_kf6_iconsdir}/hicolor/scalable/apps/org.kde.keepsecret.svg

%files lang -f %{name}.lang

%changelog
