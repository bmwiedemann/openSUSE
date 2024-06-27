#
# spec file for package polkit-kde-agent-6
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

%define rname polkit-kde-agent-1
%bcond_without released
Name:           polkit-kde-agent-6
Version:        6.1.1
Release:        0
Summary:        PolicyKit authentication agent for Plasma
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(PolkitQt6-1) >= 0.103.0
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Provides:       polkit-kde-agent-5 = %{version}
Obsoletes:      polkit-kde-agent-5 < %{version}
Obsoletes:      polkit-kde-agent-5-lang < %{version}

%description
Provides Policy Kit Authentication Agent that nicely fits Plasma.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang polkit-kde-authentication-agent-1 %{name}.lang

%post
%{systemd_user_post plasma-polkit-agent.service}

%preun
%{systemd_user_preun plasma-polkit-agent.service}

%postun
%{systemd_user_postun plasma-polkit-agent.service}

%files lang -f %{name}.lang

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.polkit-kde-authentication-agent-1.desktop
%{_kf6_configdir}/autostart/polkit-kde-authentication-agent-1.desktop
%{_kf6_notificationsdir}/policykit1-kde.notifyrc
%{_libexecdir}/polkit-kde-authentication-agent-1
%{_userunitdir}/plasma-polkit-agent.service

%changelog
