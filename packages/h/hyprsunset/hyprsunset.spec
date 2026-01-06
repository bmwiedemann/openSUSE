#
# spec file for package hyprsunset
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


Name:           hyprsunset
Version:        0.3.3
Release:        0
Summary:        Blue light filter application for Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprsunset
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(hyprland-protocols) >= 0.4.0
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils) >= 0.2.3
BuildRequires:  pkgconfig(hyprwayland-scanner) >= 0.4.0
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
# For systemd macros
%{?systemd_requires}

%description
Hyprsunset is an application to enable a blue light filter on Hyprland.
It works through the hyprland-ctm-control-v1 protocol and requires Hyprland
version 0.45.0 or newer.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%changelog
