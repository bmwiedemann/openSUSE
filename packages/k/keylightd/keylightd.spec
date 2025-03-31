#
# spec file for package keylightd
#
# Copyright (c) 2025 SUSE LLC
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


Name:           keylightd
Version:        1+git20240806.b7b17e3
Release:        0
Summary:        Keyboard backlight daemon for the Framework Laptop
License:        ISC
URL:            https://github.com/piotr-yuxuan/keylightd
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust
BuildRequires:  systemd
Requires:       systemd

%description
keylightd is a system daemon for Framework laptops that listens to
keyboard and touchpad input, and turns on the keyboard backlight
while either is being used.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%check
cargo test --release

%install
install -Dm755 target/release/keylightd %{buildroot}%{_bindir}/keylightd
sed -i 's|/usr/local/bin/keylightd|%{_bindir}/keylightd --brightness 100|g' etc/keylightd.service
install -Dm644 etc/keylightd.service %{buildroot}/%{_unitdir}/keylightd.service

%pre
%systemd_pre keylightd.service

%post
%systemd_post keylightd.service

%preun
%systemd_preun keylightd.service

%postun
%systemd_postun_with_restart keylightd.service

%files
%doc README.md
%{_bindir}/keylightd
%{_unitdir}/keylightd.service

%changelog
