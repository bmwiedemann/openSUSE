#
# spec file for package polkit-kde-agent-5
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
Name:           polkit-kde-agent-5
Version:        5.26.5
Release:        0
Summary:        PolicyKit authentication agent for KDE
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/polkit-kde-agent-1-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/polkit-kde-agent-1-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(PolkitQt5-1) >= 0.103.0
BuildRequires:  cmake(Qt5Core) >= 5.4.0
BuildRequires:  cmake(Qt5DBus) >= 5.4.0
BuildRequires:  cmake(Qt5Widgets) >= 5.4.0
Recommends:     %{name}-lang

%description
Provides Policy Kit Authentication Agent that nicely fits to KDE.

%lang_package

%prep
%setup -q -n polkit-kde-agent-1-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%if %{with released}
  %find_lang polkit-kde-authentication-agent-1 %{name}.lang
%endif

%post
%{systemd_user_post plasma-polkit-agent.service}

%preun
%{systemd_user_preun plasma-polkit-agent.service}

%postun
%{systemd_user_postun plasma-polkit-agent.service}

%if %{with released}
%files lang -f %{name}.lang
%endif

%files
%license LICENSES/*
%{_kf5_configdir}/autostart/polkit-kde-authentication-agent-1.desktop
%{_kf5_notifydir}/
%{_kf5_applicationsdir}/org.kde.polkit-kde-authentication-agent-1.desktop
%{_libexecdir}/polkit-kde-authentication-agent-1
%{_userunitdir}/plasma-polkit-agent.service

%changelog
