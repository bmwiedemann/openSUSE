#
# spec file for package hyprland-qt-support
#
# Copyright (c) 2025 Shawn W Dunn <sfalken@opensuse.org>
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


Name:           hyprland-qt-support
Version:        0.1.0
Release:        0
Summary:        Qt6 qml style provider for Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-qt-support
Source0:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)

BuildRequires:  pkgconfig(hyprlang) >= 0.6.0

%description
A qt6 qml style provider for hypr* apps

%prep
%autosetup -p1

%build
%cmake_qt6 -DINSTALL_QMLDIR=%{_qt6_qmldir}
%{qt6_build}

%install
%{qt6_install}

%check
%ctest

%files
%license LICENSE
%doc README.md
%dir %{_qt6_qmldir}/org
%dir %{_qt6_qmldir}/org/hyprland
%{_prefix}/lib/*.so
%{_qt6_qmldir}/org/hyprland/style/


%changelog

