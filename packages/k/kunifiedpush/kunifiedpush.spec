#
# spec file for package kunifiedpush
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


%bcond_without released

%define kf6_version 6.6.0
%define qt6_version 6.5.0
#
Name:           kunifiedpush
Version:        24.12.2
Release:        0
Summary:        UnifiedPush client components
License:        LGPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/kunifiedpush/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kunifiedpush/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# For %%check
BuildRequires:  dbus-1
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebSockets) >= %{qt6_version}
# The KCM is slightly useless without the library
Requires:       libKUnifiedPush1
Requires:       systemsettings6

%description
KUnifiedPush provides push notifications for KDE applications. Push
notifications are a mechanism to support applications that occasionally need to
receive some kind of information from their server-side part, and where
receiving in a timely manner matters.

Three possible provider backends are provided:
- Ntfy
- Nextpush
- Gotify

%package -n libKUnifiedPush1
Summary:        KUnifiedPush library
Recommends:     kunifiedpush

%description -n libKUnifiedPush1
KUnifiedPush provides push notifications for KDE applications. Push
notifications are a mechanism to support applications that occasionally need to
receive some kind of information from their server-side part, and where
receiving in a timely manner matters.

%package devel
Summary:        Development files for KUnifiedPush
Requires:       libKUnifiedPush1 = %{version}

%description devel
Development files for using KUnifiedPush in your applications.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKUnifiedPush1

%check
pushd %{__kf6_builddir}
# The connectortest test passes locally but fails when running in a KVM
dbus-run-session /usr/bin/ctest --output-on-failure --exclude-regex "connectortest"
popd

%files
%license LICENSES/*
%doc README.md
%dir %{_kf6_configdir}/KDE
%config %{_kf6_configdir}/KDE/kunifiedpush-distributor.conf
%{_kf6_applicationsdir}/kcm_push_notifications.desktop
%{_kf6_bindir}/kunifiedpush-distributor
%{_kf6_configdir}/autostart/org.kde.kunifiedpush-distributor.desktop
%{_kf6_debugdir}/org_kde_kunifiedpush.categories
%{_kf6_plugindir}/plasma/kcms/systemsettings/kcm_push_notifications.so

%files -n libKUnifiedPush1
%license LICENSES/*
%{_kf6_libdir}/libKUnifiedPush.so.*

%files devel
%{_includedir}/KUnifiedPush/
%{_kf6_cmakedir}/KUnifiedPush/
%{_kf6_libdir}/libKUnifiedPush.so

%files lang -f %{name}.lang

%changelog
