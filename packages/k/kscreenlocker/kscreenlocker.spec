#
# spec file for package kscreenlocker
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


%{!?_pam_vendordir:%global _pam_vendordir %_sysconfdir/pam.d}

%bcond_without released
Name:           kscreenlocker
Version:        5.26.5
Release:        0
Summary:        Library and components for secure lock screen architecture
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://projects.kde.org/kscreenlocker
Source:         https://download.kde.org/stable/plasma/%{version}/kscreenlocker-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kscreenlocker-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
Source3:        kde
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  pam-devel
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5Declarative)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IdleTime)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt5Quick) >= 5.15.0
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
Requires:       pam-config
Requires(post): /usr/bin/killall
Recommends:     %{name}-lang

%description
Library and components for secure lock screen architecture.

%package -n libKScreenLocker5
Summary:        Library and components for secure lock screen architecture
Group:          System/GUI/KDE

%description -n libKScreenLocker5
Library and components for secure lock screen architecture.

%package devel
Summary:        Library and components for secure lock screen architecture - development files
Group:          Development/Libraries/C and C++
Requires:       libKScreenLocker5 = %{version}
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5X11Extras)

%description devel
Development files for Library and components for secure lock screen architecture.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{version}

%build
  %cmake_kf5 -d build -- -DKDE4_COMMON_PAM_SERVICE=kde -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  # Ship our own file to not depend on a display manager being installed (boo#1108329)
  install -D -m0644 %{SOURCE3} %{buildroot}%{_pam_vendordir}/kde
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
%endif

%pre
# TODO: Add a check for kscreenlocker_greet version, once available.
# Upstream told that that would not be possible, but upstream is unreasonable.
if [ $1 = 2 ]; then
    touch /run/kscreenlocker_restart
fi
exit 0

%post
/sbin/ldconfig
if [ $1 = 2 ] && [ -f /run/kscreenlocker_restart ]; then
    /usr/bin/killall -q -TERM kscreenlocker_greet || :
    rm /run/kscreenlocker_restart
fi
exit 0

%post -n libKScreenLocker5 -p /sbin/ldconfig

%postun -n libKScreenLocker5 -p /sbin/ldconfig

%if %{with released}
%files lang -f %{name}.lang
%license COPYING*
%endif

%files
%license COPYING*
%{_pam_vendordir}/kde
%{_kf5_applicationsdir}/kcm_screenlocker.desktop
%{_kf5_sharedir}/kconf_update/
%{_kf5_plugindir}/
%{_kf5_notifydir}/
%{_kf5_sharedir}/ksmserver/
%dir %{_kf5_sharedir}/kpackage/
%dir %{_kf5_sharedir}/kpackage/kcms
%{_kf5_sharedir}/kpackage/kcms/kcm_screenlocker
%{_libexecdir}/kscreenlocker_greet

%files -n libKScreenLocker5
%license COPYING*
%{_kf5_libdir}/libKScreenLocker.so.*

%files devel
%license COPYING*
%{_kf5_libdir}/libKScreenLocker.so
%{_kf5_prefix}/include/KScreenLocker/
%{_kf5_libdir}/cmake/ScreenSaverDBusInterface/
%{_kf5_libdir}/cmake/KScreenLocker/
%{_kf5_sharedir}/dbus-1/interfaces/

%changelog
