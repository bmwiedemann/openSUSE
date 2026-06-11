#
# spec file for package ashell
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


Name:           ashell
Version:        0.9.0
Release:        0
Summary:        A Wayland status bar for Hyprland and Niri
License:        GPL-3.0-or-later
URL:            https://malpenzibo.github.io/ashell/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
## See https://malpenzibo.github.io/ashell/docs/configuration/full_config
Source2:        config.toml
BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  wayland-devel
BuildRequires:  rust
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse) 
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
A Wayland status bar for the Hyprland compositor, written in Rust.
It provides workspace, system, media, and privacy widgets.

%prep
%autosetup -p1 -a1
cp %{S:2} .

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc CHANGELOG.md config.toml 
%{_bindir}/ashell

%changelog

