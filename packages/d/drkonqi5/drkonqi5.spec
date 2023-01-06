#
# spec file for package drkonqi5
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


%define kf5_version 5.98.0
%bcond_without released
Name:           drkonqi5
# Full Plasma 5 version (e.g. 5.9.1)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.1 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Version:        5.26.5
Release:        0
Summary:        Helper for debugging and reporting crashes
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            http://www.kde.org/
Source:         https://download.kde.org/stable/plasma/%{version}/drkonqi-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/drkonqi-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCHES 100-199 are from upstream 5.16 branch
# PATCHES 200-299 and above are from upstream master/5.17+ branch
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5Declarative) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IdleTime) >= %{kf5_version}
BuildRequires:  cmake(KF5JobWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5SyntaxHighlighting) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlRpcClient) >= %{kf5_version}
# Only there to make it build, remove once upstream makes it optional
BuildRequires:  cmake(KUserFeedback)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(libsystemd)
%if 0%{?suse_version} < 1550
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif
# QML runtime dependencies (not detected automatically because the QML code is embedded as Qt Resource)
# if kirigami2 is not installed, it falls back to the old QWidgets-based UI though and doesn't need them...
Requires:       (kdeclarative-components if kirigami2)
Requires:       (kitemmodels-imports if kirigami2)
Requires:       (syntax-highlighting-imports if kirigami2)
# We want useful backtraces
Recommends:     gdb
# we want symbol install support
Recommends:     ptools
Recommends:     %{name}-lang
# In theory the coredump integration could be split into a subpackage
# and supplement systemd-coredump, but it's small enough to not be worth it.
# This however means there can't be any dependency on systemd-coredump, to
# not pull it in unconditionally.
%{?systemd_ordering}

%description
The KDE Crash Handler gives the user feedback if a program has crashed.

%lang_package

%prep
%setup -q -n drkonqi-%{version}

%build
%if 0%{?suse_version} < 1550
  export CXX=g++-10
%endif
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build

  %if %{with released}
    %{kf5_find_lang}
  %endif

  install -p -D -m755 src/doc/examples/installdbgsymbols_suse.sh \
  %{buildroot}%{_kf5_bindir}/installdbgsymbols.sh

%pre
%service_add_pre drkonqi-coredump-processor@.service

%post
%{systemd_user_post drkonqi-coredump-cleanup.service drkonqi-coredump-cleanup.timer drkonqi-coredump-launcher.socket}
%service_add_post drkonqi-coredump-processor@.service

%preun
%{systemd_user_preun drkonqi-coredump-cleanup.service drkonqi-coredump-cleanup.timer drkonqi-coredump-launcher.socket}
%service_del_preun drkonqi-coredump-processor@.service

%postun
%{systemd_user_postun drkonqi-coredump-cleanup.service drkonqi-coredump-cleanup.timer drkonqi-coredump-launcher.socket}
%service_del_postun drkonqi-coredump-processor@.service

%files
%license LICENSES/*
%{_kf5_bindir}/installdbgsymbols.sh
%{_kf5_sharedir}/drkonqi/
%{_kf5_applicationsdir}/org.kde.drkonqi.desktop
%{_kf5_debugdir}/drkonqi.categories
%{_libexecdir}/drkonqi

%{_kf5_bindir}/drkonqi-coredump-gui
%{_unitdir}/drkonqi-coredump-processor@.service
%{_userunitdir}/drkonqi-coredump-cleanup.service
%{_userunitdir}/drkonqi-coredump-cleanup.timer
%{_userunitdir}/drkonqi-coredump-launcher.socket
%{_userunitdir}/drkonqi-coredump-launcher@.service
%dir %{_kf5_plugindir}/drkonqi/
%{_kf5_plugindir}/drkonqi/KDECoredumpNotifierTruck.so
%{_libexecdir}/drkonqi-coredump-cleanup
%{_libexecdir}/drkonqi-coredump-launcher
%{_libexecdir}/drkonqi-coredump-processor
%{_kf5_applicationsdir}/org.kde.drkonqi.coredump.gui.desktop

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
