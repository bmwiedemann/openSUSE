#
# spec file for package inputplumber
#
# Copyright (c) 2026 SUSE LLC
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

Name:           inputplumber
Version:        0.77.7
Release:        0%{?dist}
Summary:        Input router and remapper daemon for Linux
License:        GPL-3.0
URL:            https://github.com/ShadowBlip/InputPlumber
Source0:        InputPlumber-%{version}.tar.xz
Source1:        vendor.tar.zst
Patch0:         polkit-rules.patch
Patch1:         0001-fix-compilation-Fix-Rust-1.97-clippy-build-errors.patch
BuildRequires:  rust
BuildRequires:	cargo
BuildRequires:  cargo-packaging
BuildRequires:  libevdev-devel
BuildRequires:  pkgconfig(libiio)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  llvm-devel
BuildRequires:  clang-devel
BuildRequires:  pkgconfig(systemd)
Requires:       polkit
Provides:       InputPlumber
Conflicts:      python3-hhd

%description
InputPlumber is a input routing and control daemon for Linux.
It can be used to combine any number of input devices (like gamepads,
mice, and keyboards) and translate their input to a variety of
virtual device formats.

%prep
%autosetup -p1 -a1 -n InputPlumber-%{version}

%build
make build

%install
make install PREFIX=%{buildroot}%{_prefix} NO_RELOAD=true

%check
make test

%pre
%systemd_pre inputplumber-suspend.service inputplumber.service

%post
%systemd_post inputplumber-suspend.service inputplumber.service

%preun
%systemd_preun inputplumber-suspend.service inputplumber.service

%postun
%systemd_postun inputplumber-suspend.service inputplumber.service

%files
%doc README.md
%{_bindir}/inputplumber
%{_datadir}/dbus-1/system.d/org.shadowblip.InputPlumber.conf
%{_unitdir}/inputplumber.service
%{_unitdir}/inputplumber-suspend.service
%dir %{_udevhwdbdir}
%{_udevhwdbdir}/*.hwdb
%{_udevrulesdir}/*.rules
%dir %{_datadir}/inputplumber
%dir %{_datadir}/inputplumber/capability_maps
%{_datadir}/inputplumber/capability_maps/*.yaml
%dir %{_datadir}/inputplumber/devices
%{_datadir}/inputplumber/devices/*.yaml
%dir %{_datadir}/inputplumber/profiles
%{_datadir}/inputplumber/profiles/*.yaml
%dir %{_datadir}/inputplumber/schema
%{_datadir}/inputplumber/schema/*.json
%{_datadir}/polkit-1/actions/org.shadowblip.InputPlumber.policy
%{_datadir}/polkit-1/rules.d/org.shadowblip.InputPlumber.rules

%changelog
