#
# spec file for package illuminanced
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


Name:           illuminanced
Version:        1+git20250306.4c6178c
Release:        0
Summary:        Ambient Light Sensor Daemon for Linux
License:        GPL-3.0
URL:            https://github.com/mikhail-m1/illuminanced
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
Source2:        illuminanced-service-dropin.conf
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libudev)
BuildRequires:  rust
BuildRequires:  pkgconfig(systemd)

%description
A user-space daemon that automatically adjusts screen brightness based on light sensor readings.

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%check
cargo test --release

%pre
%systemd_pre illuminanced.service

%post
%systemd_post illuminanced.service

%preun
%systemd_preun illuminanced.service

%postun
%systemd_postun_with_restart illuminanced.service

%install
install -Dm755 target/release/illuminanced %{buildroot}%{_bindir}/illuminanced
install -Dm644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/illuminanced.service.d/override.conf
install -Dm644 illuminanced.service %{buildroot}/usr/lib/systemd/system/illuminanced.service
install -Dm644 illuminanced.toml %{buildroot}/etc/illuminanced.toml

%files
%doc README.md
%license LICENSE
%{_bindir}/illuminanced
%dir /usr/lib/systemd/system/illuminanced.service.d
/usr/lib/systemd/system/illuminanced.service.d/override.conf
/usr/lib/systemd/system/illuminanced.service
%config /etc/illuminanced.toml

%changelog
