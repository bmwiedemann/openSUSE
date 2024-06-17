#
# spec file for package lxqt-qt5plugin
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
%define _name lxqt-qtplugin

Name:           lxqt-qt5plugin
Version:        1.4.1
Release:        0
Summary:        LXQt Qt5 platform integration plugin
License:        LGPL-2.1-or-later
URL:            https://github.com/lxqt/lxqt-qtplugin
Source0:        %{url}/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{_name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  libQt5PlatformSupport-private-headers-devel
BuildRequires:  lxqt-build-tools-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(fm-qt)
BuildRequires:  pkgconfig(Qt5XdgIconLoader)
BuildRequires:  pkgconfig(dbusmenu-qt5)

%description
A library libqtlxqt to integrate Qt5 with LXQt. With this plugin, all
Qt5-based programs can adopt settings of LXQt, such as the icon theme.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_libdir}/qt5/plugins/platformthemes
%{_libdir}/qt5/plugins/platformthemes/libqtlxqt.so

%changelog

