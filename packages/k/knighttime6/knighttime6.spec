#
# spec file for package knighttime
#
# Copyright (c) 2025 SUSE LLC
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

%define kf6_version 6.18.0
%define qt6_version 6.9.0
%define soversion 0
%define rname knighttime
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           knighttime6
Version:        6.6.1
Release:        0
Summary:        Day-night cycle helper library
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Holidays) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Positioning) >= %{qt6_version}
Requires:       libKNightTime%{soversion} = %{version}

%description
KNightTime provides helpers for scheduling the dark-light cycle. It can be used to implement
features such as adjusting the screen color temperature based on time of day, etc.

%package -n libKNightTime%{soversion}
Summary:        Day-night cycle helper library

%description -n libKNightTime%{soversion}
This package contains the core library for KNightTime, a helper for dark-light day cycles.

%package devel
Summary:        Development files for KNightTime
Requires:       libKNightTime%{soversion} = %{version}

%description devel
Development files for KNightTime,  a helper for dark-light day cycles.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%ldconfig_scriptlets -n libKNightTime%{soversion}

%check
%ctest

%post
%{systemd_user_post plasma-knighttimed.service}

%preun
%{systemd_user_preun plasma-knighttimed.service}

%postun
%{systemd_user_postun plasma-knighttimed.service}

%files
%{_kf6_applicationsdir}/org.kde.knighttimed.desktop
%{_kf6_dbusinterfacesdir}/org.kde.NightTime.xml
%{_kf6_debugdir}/knighttime.categories
%{_kf6_sharedir}/dbus-1/services/org.kde.NightTime.service
%{_libexecdir}/knighttimed
%{_userunitdir}/plasma-knighttimed.service

%files -n libKNightTime%{soversion}
%license LICENSES/*
%{_kf6_libdir}/libKNightTime.so.%{soversion}
%{_kf6_libdir}/libKNightTime.so.*

%files devel
%doc README.md
%{_includedir}/KNightTime/
%{_kf6_cmakedir}/KNightTime/
%{_kf6_libdir}/libKNightTime.so

%changelog
