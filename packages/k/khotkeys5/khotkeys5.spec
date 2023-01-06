#
# spec file for package khotkeys5
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
Name:           khotkeys5
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        KDE's hotkey daemon
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/khotkeys-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/khotkeys-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch100:       0001-Use-qdbus-qt5-and-qdbusviewer-qt5.patch
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  xz
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Plasma)
BuildRequires:  cmake(KF5XmlGui)
#!BuildIgnore: kwin5
BuildRequires:  cmake(LibKWorkspace) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5X11Extras) >= 5.15
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
Requires:       libqt5-qdbus
Recommends:     %{name}-lang

%description
KDE's hotkey daemon module. It allows you to configure custom
keyboard shortcuts and mouse gestures.

%package devel
Summary:        KDE's hotkey daemon
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Conflicts:      kdebase4-workspace-devel

%description devel
Files to develop with KDE's hotkey daemon module.

%lang_package

%prep
%autosetup -p1 -n khotkeys-%{version}

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif

%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %kf5_find_lang
  %kf5_find_htmldocs
%endif

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_libdir}/libkhotkeysprivate.so.*
%{_kf5_plugindir}/
%dir %{_kf5_htmldir}/en
%dir %{_kf5_htmldir}
%doc %{_kf5_htmldir}/en/kcontrol/
%{_kf5_sharedir}/khotkeys/
%{_kf5_servicesdir}/

%files devel
%{_kf5_libdir}/cmake/KHotKeysDBusInterface/
%{_kf5_sharedir}/dbus-1/interfaces/org.kde.khotkeys.xml

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
