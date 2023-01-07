#
# spec file for package yakuake
#
# Copyright (c) 2022 SUSE LLC
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
Name:           yakuake
Version:        22.12.1
Release:        0
Summary:        Drop-down terminal emulator based on Konsole technologies
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/yakuake
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  fdupes
%if 0%{?suse_version} < 1550
# c++-20 required
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif
BuildRequires:  kf5-filesystem
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
Requires:       konsole-part > 15.12
Recommends:     konsole > 15.12

%description
Yakuake is a Drop-down terminal emulator based on Konsole technologies.

%lang_package

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1550
  export CXX=g++-10
%endif
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%suse_update_desktop_file -G "Terminal Program" org.kde.yakuake System TerminalEmulator

%find_lang %{name}

%fdupes -s %{buildroot}

%files
%license LICENSES/*
%doc README.md AUTHORS ChangeLog NEWS
%{_kf5_applicationsdir}/org.kde.yakuake.desktop
%{_kf5_appstreamdir}/org.kde.yakuake.appdata.xml
%{_kf5_bindir}/yakuake
%{_kf5_knsrcfilesdir}/yakuake.knsrc
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_iconsdir}/hicolor/*/apps/yakuake.*
%{_kf5_notifydir}/
%{_kf5_sharedir}/yakuake/
%{_kf5_sharedir}/dbus-1/services/org.kde.yakuake.service

%files lang -f %{name}.lang

%changelog
