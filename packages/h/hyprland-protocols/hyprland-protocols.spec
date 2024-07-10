#
# spec file for package hyprland-protocols
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


Name:           hyprland-protocols
Summary:        Wayland extension protocol for Hyprland
Group:          Development/Libraries/Other
License:        BSD-3-Clause
Version:        0.3.0
Release:        0
URL:            https://github.com/hyprwm/hyprland-protocols
Source0:        https://github.com/hyprwm/hyprland-protocols/archive/refs/tags/v%{version}.tar.gz#/hyprland-protocols-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildArch:      noarch

%package devel
Summary:        Wayland extension protocol for Hyprland
Group:          Development/Libraries/Other

%description devel
This provides additional extensions of the Wayland protocol for Hyprland.

Development files for %{name}.

%description
This provides additional extensions of the Wayland protocol for Hyprland.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files devel
%{_datadir}/pkgconfig/hyprland-protocols.pc
%dir %{_datadir}/hyprland-protocols
%dir %{_datadir}/hyprland-protocols/protocols
%{_datadir}/hyprland-protocols/protocols/*
%doc README.md
%license LICENSE

%changelog
