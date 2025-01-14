#
# spec file for package hyprland-qtutils
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Malcolm J Lewis <malcolmlewis@opensuse.org>
# Copyright (c) 2024 Shawn W Dunn <sfalken@opensuse.org>
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


Name:           hyprland-qtutils
Version:        0.1.3
Release:        0
Summary:        Hyprland QT/qml utility apps
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-qtutils
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
# PATCH-FIX-openSUSE 0001-Remove-donate-screen-module.patch <sfalken@opensuse.org>
# A Donate button was added in the v0.1.2 release, which was small and out of the way
# Adding a Donate Screen like this just feels like crossing a line, and has been
# Removed.
Patch0:         0001-Remove-donate-screen-module.patch
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  qt6-waylandclient-private-devel
BuildRequires:  pkgconfig(Qt6Platform)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6WaylandClient)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(hyprutils)
## MANUAL BEGIN
Requires:       hyprland-qt-support
## MANUAL END

%description
QT and QML utilities that might be used by various hypr* apps.

%prep
%autosetup -p1 -S git_am

%build
%cmake
%cmake_build

%install
%cmake_install
## Remove binary-or-shlib-defines-rpath
chrpath --delete %{buildroot}%{_bindir}/hyprland-*

%check
%ctest

%files
%license LICENSE
%{_bindir}/hyprland-dialog
%{_bindir}/hyprland-update-screen

%changelog
