#
# spec file for package owncloud-dolphin
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           owncloud-dolphin
Version:        6.0.0
Release:        0
Summary:        Dolphin Integrations for the ownCloud desktop syncing client
License:        GPL-2.0-or-later
URL:            https://github.com/owncloud/client-desktop-shell-integration-dolphin
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake >= 3.18
BuildRequires:  kf6-extra-cmake-modules >= 6.0.0
BuildRequires:  owncloud-extensions-resources
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_ver}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_ver}
BuildRequires:  cmake(KF6KIO) >= %{kf6_ver}
BuildRequires:  cmake(Qt6Core) >= %{qt6_ver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_ver}
BuildRequires:  cmake(Qt6Network) >= %{qt6_ver}
Supplements:    (owncloud-client and dolphin)
Requires:       owncloud-extensions-resources
Provides:       owncloud-client-dolphin = %{version}
Obsoletes:      owncloud-client-dolphin < %{version}

%description

This package provides shell integration for the ownCloud desktop sync client
for KDE dolphin.

%prep
%autosetup -n client-desktop-shell-integration-dolphin-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets

%check
%ctest

%files
%license COPYING
%doc README.md
%{_libdir}/libownclouddolphinpluginhelper.so
%dir %{_libdir}/qt6/plugins/kf6/kfileitemaction
%{_libdir}/qt6/plugins/kf6/kfileitemaction/ownclouddolphinactionplugin.so
%dir %{_libdir}/qt6/plugins/kf6/overlayicon
%{_libdir}/qt6/plugins/kf6/overlayicon/ownclouddolphinoverlayplugin.so
%{_libdir}/qt6/plugins/ownclouddolphinactionplugin.so

%changelog
