#
# spec file for package lxqt-qtplugin
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


Name:           lxqt-qtplugin
Version:        2.0.0
Release:        0
Summary:        LXQt platform integration plugin
License:        LGPL-2.1-or-later
Group:          System/GUI/LXQt
URL:            https://github.com/lxqt/lxqt-qtplugin
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui) >= 6.3.0
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(fm-qt6)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(Qt6XdgIconLoader)
BuildRequires:  pkgconfig(dbusmenu-lxqt)

%description
A library libqtlxqt to integrate Qt with LXQt. With this plugin, all
Qt-based programs can adopt settings of LXQt, such as the icon theme.

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_qt6_pluginsdir}/platformthemes
%{_qt6_pluginsdir}/platformthemes/libqtlxqt.so

%changelog
