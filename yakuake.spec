#
# spec file for package yakuake
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
%define plasma6_version 5.27.80
%define qt6_version 6.6.0

%bcond_without released
Name:           yakuake
Version:        24.05.2
Release:        0
Summary:        Drop-down terminal emulator based on Konsole technologies
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/yakuake
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GlobalAccel) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KWayland) >= %{plasma6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(x11)
Requires:       konsole-part
Recommends:     konsole

%description
Yakuake is a Drop-down terminal emulator based on Konsole technologies.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name}

%fdupes -s %{buildroot}

%files
%license LICENSES/*
%doc README.md AUTHORS ChangeLog NEWS
%{_kf6_applicationsdir}/org.kde.yakuake.desktop
%{_kf6_appstreamdir}/org.kde.yakuake.appdata.xml
%{_kf6_bindir}/yakuake
%{_kf6_knsrcfilesdir}/yakuake.knsrc
%{_kf6_iconsdir}/hicolor/*/apps/yakuake.*
%{_kf6_notificationsdir}/yakuake.notifyrc
%{_kf6_sharedir}/yakuake/
%{_kf6_sharedir}/dbus-1/services/org.kde.yakuake.service

%files lang -f %{name}.lang

%changelog
