#
# spec file for package extest
#
# Copyright (c) 2023 SUSE LLC
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


Name:           extest
Version:        1+git20241105.1a419a1
Release:        0
Summary:        X11 XTEST reimplementation primarily for Steam Controller on Wayland
License:        MIT
URL:            https://github.com/Supreeeme/extest
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
Source99:       baselibs.conf
BuildRequires:  rust
BuildRequires:	cargo
BuildRequires:  cargo-packaging

%description
Extest is a drop in replacement for the X11 XTEST extension.
It creates a virtual device with the uinput kernel module.
It's been primarily developed for allowing the desktop functionality
on the Steam Controller to work while Steam is open on Wayland.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%check
cargo test --release

%install
install -Dm755 target/release/libextest.so %{buildroot}%{_libdir}/libextest.so

%files
%doc README.md
%{_libdir}/libextest.so

%changelog
