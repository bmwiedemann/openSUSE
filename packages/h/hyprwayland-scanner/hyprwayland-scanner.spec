#
# spec file for package hyprwayland-scanner
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Florian "sp1rit" <sp1rit@disroot.org>
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


Name:           hyprwayland-scanner
Version:        0.3.10
Release:        0
Summary:        Hyprland implementation of wayland-scanner
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprwayland-scanner
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}.rpmlintrc
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 11
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(pugixml)

%description
A Hyprland implementation of wayland-scanner, in and for C++.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
