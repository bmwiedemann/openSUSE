#
# spec file for package drkonqi6
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

%define rname drkonqi

%bcond_without released
Name:           drkonqi6
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Version:        6.1.2
Release:        0
Summary:        Helper for debugging and reporting crashes
License:        GPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IdleTime) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6Service) >= %{kf6_version}
BuildRequires:  cmake(KF6StatusNotifierItem) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6UserFeedback) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(libsystemd)
# To install debug packages
Requires:       konsole
# QML runtime dependencies (not detected automatically because the QML code is embedded as Qt Resource)
# if kirigami2 is not installed, it falls back to the old QWidgets-based UI though and doesn't need them...
Requires:       (kf6-kdeclarative-imports if kf6-kirigami-imports)
Requires:       python3-psutil
Requires:       (kf6-kitemmodels-imports if kf6-kirigami-imports)
Requires:       (kf6-syntax-highlighting-imports if kf6-kirigami-imports)
# The gdb script for crash info extraction can use this for reporting error
# of the error extraction itself. The openSUSE package has all integrations
# listed as hard requirements though, which pulls in 260MiB of pure bloat.
# Recommends:   python3-sentry-sdk
# Only needed for QML traces
Recommends:     python3-pygdbmi
# We want useful backtraces
Recommends:     gdb
# we want symbol install support
Recommends:     ptools
Provides:       drkonqi5 = %{version}
Obsoletes:      drkonqi5 < %{version}
Obsoletes:      drkonqi5-lang < %{version}
# In theory the coredump integration could be split into a subpackage
# and supplement systemd-coredump, but it's small enough to not be worth it.
# This however means there can't be any dependency on systemd-coredump, to
# not pull it in unconditionally.
%{?systemd_ordering}

%description
The KDE Crash Handler gives the user feedback if a program has crashed.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 \
  -DWITH_PYTHON_VENDORING:BOOL=FALSE
# Temporarily disabled to test if generating backtraces gets better without it
# %%if 0%%{?suse_version} >= 1550
#   -DWITH_GDB12:BOOL=TRUE
# %%endif

%kf6_build

%install
%kf6_install

%find_lang drkonqi

install -p -D -m755 src/doc/examples/installdbgsymbols_suse.sh \
%{buildroot}%{_kf6_bindir}/installdbgsymbols.sh

%pre
%service_add_pre drkonqi-coredump-processor@.service

%post
%{systemd_user_post drkonqi-coredump-cleanup.service drkonqi-coredump-cleanup.timer drkonqi-coredump-launcher.socket drkonqi-sentry-postman.path drkonqi-sentry-postman.service drkonqi-sentry-postman.timer}
%service_add_post drkonqi-coredump-processor@.service

%preun
%{systemd_user_preun drkonqi-coredump-cleanup.service drkonqi-coredump-cleanup.timer drkonqi-coredump-launcher.socket drkonqi-coredump-pickup.service drkonqi-sentry-postman.path drkonqi-sentry-postman.service drkonqi-sentry-postman.timer}
%service_del_preun drkonqi-coredump-processor@.service

%postun
%{systemd_user_postun drkonqi-coredump-cleanup.service drkonqi-coredump-cleanup.timer drkonqi-coredump-launcher.socket drkonqi-coredump-pickup.service drkonqi-sentry-postman.path drkonqi-sentry-postman.service drkonqi-sentry-postman.timer}
%service_del_postun_without_restart drkonqi-coredump-processor@.service

%files
%license LICENSES/*
%{_kf6_applicationsdir}/org.kde.drkonqi.coredump.gui.desktop
%{_kf6_applicationsdir}/org.kde.drkonqi.desktop
%{_kf6_bindir}/drkonqi-coredump-gui
# Not optional anymore but opt-in
%{_kf6_bindir}/drkonqi-sentry-data
%{_kf6_bindir}/installdbgsymbols.sh
%{_kf6_debugdir}/drkonqi.categories
%{_kf6_libexecdir}/drkonqi-polkit-helper
%dir %{_kf6_plugindir}/drkonqi/
%{_kf6_plugindir}/drkonqi/KDECoredumpNotifierTruck.so
%{_kf6_sharedir}/dbus-1/system-services/org.kde.drkonqi.service
%{_kf6_sharedir}/dbus-1/system.d/org.kde.drkonqi.conf
%{_kf6_sharedir}/polkit-1/actions/org.kde.drkonqi.policy
%{_kf6_sharedir}/drkonqi/
%{_libexecdir}/drkonqi
%{_libexecdir}/drkonqi-coredump-cleanup
%{_libexecdir}/drkonqi-coredump-launcher
%{_libexecdir}/drkonqi-coredump-processor
%{_libexecdir}/drkonqi-sentry-postman
%{_unitdir}/drkonqi-coredump-processor@.service
%dir %{_unitdir}/systemd-coredump@.service.wants
%{_unitdir}/systemd-coredump@.service.wants/drkonqi-coredump-processor@.service
%{_userunitdir}/drkonqi-coredump-cleanup.service
%{_userunitdir}/drkonqi-coredump-cleanup.timer
%{_userunitdir}/drkonqi-coredump-launcher.socket
%{_userunitdir}/drkonqi-coredump-launcher@.service
%{_userunitdir}/drkonqi-coredump-pickup.service
%{_userunitdir}/drkonqi-sentry-postman.path
%{_userunitdir}/drkonqi-sentry-postman.service
%{_userunitdir}/drkonqi-sentry-postman.timer
%dir %{_userunitdir}/default.target.wants
%{_userunitdir}/default.target.wants/drkonqi-coredump-cleanup.service
%{_userunitdir}/default.target.wants/drkonqi-sentry-postman.path
%dir %{_userunitdir}/plasma-core.target.wants
%{_userunitdir}/plasma-core.target.wants/drkonqi-coredump-pickup.service
%{_userunitdir}/plasma-core.target.wants/drkonqi-sentry-postman.path
%{_userunitdir}/plasma-core.target.wants/drkonqi-sentry-postman.timer
%dir %{_userunitdir}/sockets.target.wants
%{_userunitdir}/sockets.target.wants/drkonqi-coredump-launcher.socket
%dir %{_userunitdir}/timers.target.wants
%{_userunitdir}/timers.target.wants/drkonqi-coredump-cleanup.timer
%{_userunitdir}/timers.target.wants/drkonqi-sentry-postman.timer

%files lang -f drkonqi.lang

%changelog
