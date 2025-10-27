#
# spec file for package wl-clipboard-rs
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


Name:           wl-clipboard-rs
Version:        0.9.2
Release:        0
Summary:        Wayland Clipboard Utility in Rust
License:        Apache-2.0 AND MIT
URL:            https://github.com/YaLTeR/wl-clipboard-rs
Source0:        https://github.com/YaLTeR/wl-clipboard-rs/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.61
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  wayland-devel
BuildRequires:  zstd
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.17
BuildRequires:  pkgconfig(wayland-server) >= 1.16
Recommends:     mailcap
Recommends:     xdg-utils
Conflicts:      wl-clipboard

%description
A safe Rust crate for working with the Wayland clipboard.

%prep
%autosetup -a1

%build
pushd wl-clipboard-rs-tools
CARGO_INCREMENTAL=0 %{cargo_build}

%install
pushd wl-clipboard-rs-tools
CARGO_INCREMENTAL=0 %{cargo_install}

# Removing unnecessary crate related files
find %{buildroot}%{_prefix} -type f \( -name ".crates.toml" -or -name ".crates2.json" \) -delete -print

%files
%{_bindir}/wl-copy
%{_bindir}/wl-paste
%{_bindir}/wl-clip
%license LICENSE-APACHE LICENSE-MIT
%doc README.md CHANGELOG.md doc/index.html

%changelog
