#
# spec file for package opencloud-dolphin
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


%define kf6_ver 6.1.0
%define qt6_ver 6.5.0
Name:           opencloud-dolphin
Version:        1.0.0
Release:        0
Summary:        Dolphin Integrations for the OpenCloud desktop syncing client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/opencloud-eu/desktop-shell-integration-dolphin
Source0:        https://github.com/opencloud-eu/desktop-shell-integration-dolphin/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake >= 2.8.11
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kf6-extra-cmake-modules >= 6.0.0
BuildRequires:  opencloud-extensions-resources
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_ver}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_ver}
BuildRequires:  cmake(KF6KIO) >= %{kf6_ver}
BuildRequires:  cmake(Qt6Core) >= %{qt6_ver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_ver}
BuildRequires:  cmake(Qt6Network) >= %{qt6_ver}
Requires:       opencloud-extensions-resources
Supplements:    (opencloud-desktop and dolphin)
Provides:       opencloud-client-dolphin = %{version}
Obsoletes:      opencloud-client-dolphin < %{version}

%description

This package provides shell integration for the OpenCloud desktop sync client for KDE dolphin.

%prep
%autosetup -n desktop-shell-integration-dolphin-%{version}

%build
%cmake_kf6
%{kf6_build}

%install
%{kf6_install}

%ldconfig_scriptlets

%check
%ctest

%files
%{_libdir}/libopenclouddolphinpluginhelper.so
%dir %{_libdir}/qt6/plugins/kf6/kfileitemaction

# sr/lib64/qt6/plugins/kf6/kfileitemaction/openclouddolphinactionplugin.so
%{_libdir}/qt6/plugins/kf6/kfileitemaction/openclouddolphinactionplugin.so
%dir %{_libdir}/qt6/plugins/kf6/overlayicon
%{_libdir}/qt6/plugins/kf6/overlayicon/openclouddolphinoverlayplugin.so

%doc README.md
%license COPYING

%changelog
