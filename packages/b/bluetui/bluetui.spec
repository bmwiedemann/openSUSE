#
# spec file for package bluetui
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2026 mantarimay
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


Name:           bluetui
Version:        0.8.3
Release:        0
Summary:        TUI for managing bluetooth devices
# Legal-Review-Notice: option-ext is linked, not shipped separately
# - MPL-2.0: option-ext 0.2.0 via dirs-sys/dirs on Linux; source in vendor.tar.zst
License:        GPL-3.0-or-later AND MPL-2.0
URL:            https://github.com/pythops/bluetui
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
# Stripped from vendor.tar.zst: wit-bindgen prebuilt src/rt/libwit_bindgen_cabi.a
# and wasi-cli@*.wasm (wasm-only inputs; Linux build never uses them)
# Source-Binary-Exception: vendor.tar.zst:vendor/winapi-*/lib/* -- other-platform: Windows import libraries for winapi crates, unused by Linux build
# Source-Binary-Exception: vendor.tar.zst:vendor/wit-bindgen-*/src/rt/*.o -- other-platform: prebuilt CABI objects for wasm32-wasip2/wasip3 targets, unused by Linux build
# Source-Binary-Exception: vendor.tar.zst:vendor/psm-*/src/arch/wasm32.o -- other-platform: wasm32 relocatable object psm uses only on wasm32 targets
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.78.0
BuildRequires:  pkgconfig(dbus-1)
Requires:       bluez

%description
bluetui is a TUI-based bluetooth connection manager written in Rust.
Which can interact with bluetooth adapters and devices. It aims to be
an alternative to most bluetooth managers, like blueman.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%files
%license LICEN*
%doc Readme.md Release.md
%{_bindir}/%{name}

%changelog
