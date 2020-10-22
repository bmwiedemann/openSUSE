#
# spec file for package polkit-kde-agent-5
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without lang
Name:           polkit-kde-agent-5
Version:        5.20.1
Release:        0
Summary:        PolicyKit authentication agent for KDE
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Development/Libraries/KDE
URL:            http://www.kde.org/
Source:         polkit-kde-agent-1-%{version}.tar.xz
%if %{with lang}
Source1:        polkit-kde-agent-1-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 1.2.0
BuildRequires:  kf5-filesystem
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

%if %{with lang}
  %find_lang polkit-kde-authentication-agent-1 %{name}.lang
%endif

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files
%license COPYING
%{_kf5_configdir}/autostart/polkit-kde-authentication-agent-1.desktop
%{_kf5_libdir}/libexec/polkit-kde-authentication-agent-1
%{_kf5_notifydir}/
%{_kf5_applicationsdir}/org.kde.polkit-kde-authentication-agent-1.desktop

%changelog
