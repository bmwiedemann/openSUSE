#
# spec file for package hyprpolkitagent
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           hyprpolkitagent
Version:        0.1.3
Release:        0
Summary:        A Qt/QML-based polkit authentication agent for Hyprland
License:        BSD-3-Clause
URL:            https://wiki.hyprland.org/Hypr-Ecosystem/hyprpolkitagent/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  cmake(Qt6QuickControls2Impl)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(polkit-qt6-1)
Requires:       qt6qmlimport(QtQuick)
Requires:       qt6qmlimport(QtQuick.Controls)
Requires:       qt6qmlimport(QtQuick.Layouts)

%description
hyprpolkitagent is a polkit authentication daemon. It is required for GUI
applications to be able to request elevated privileges.

%prep
%autosetup -p1

%build
%cmake \
  -D CMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_userunitdir}/hyprpolkitagent.service
%{_libexecdir}/hyprpolkitagent
%{_datadir}/dbus-1/services/org.hyprland.hyprpolkitagent.service

%changelog
