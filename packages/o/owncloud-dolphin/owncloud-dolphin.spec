#
# spec file for package owncloud-dolphin
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


Name:           owncloud-dolphin
Version:        5.0.0
Release:        0
Summary:        Dolphin Integrations for the ownCloud desktop syncing client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://owncloud.org/download
Source0:        client-desktop-shell-integration-dolphin-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.11
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5KIO)
Provides:       owncloud-client-dolphin = %{version}
Obsoletes:      owncloud-client-dolphin < %{version}

%description

This package provides shell integration for the ownCloud desktop sync client for KDE dolphin.

%prep
%autosetup -p1 -n client-desktop-shell-integration-dolphin-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%{_libdir}/libownclouddolphinpluginhelper.so
%{_libdir}/qt5/plugins/kf5/overlayicon/ownclouddolphinoverlayplugin.so
%{_libdir}/qt5/plugins/ownclouddolphinactionplugin.so
%{_datadir}/kservices5/ownclouddolphinactionplugin.desktop
%dir %{_libdir}/qt5/plugins/kf5/overlayicon
%doc README
%license COPYING

%changelog
