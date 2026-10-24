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
Version:        0.83.0
Release:        0%{?dist}
Summary:        Input router and remapper daemon for Linux
# spec-cleaner deviation: upstream Cargo.toml declares GPL-3.0-or-later,
# not GPL-3.0-only as the mechanical rewrite suggested.
License:        GPL-3.0-or-later
URL:            https://github.com/ShadowBlip/InputPlumber
Source0:        InputPlumber-%{version}.tar.xz
Source1:        vendor.tar.zst
# PATCH-FIX-OPENSUSE polkit-rules.patch -- grant access to inputplumber group only, drop debug logging
Patch0:         polkit-rules.patch
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig
BuildRequires:  rust
# spec-cleaner deviation: plain devel package name kept on purpose;
# the pkgconfig form resolves to the same devel package.
BuildRequires:  libevdev-devel
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(systemd)
Requires:       polkit
Conflicts:      python3-hhd
Provides:       InputPlumber

%description
InputPlumber is a input routing and control daemon for Linux.
It can be used to combine any number of input devices (like gamepads,
mice, and keyboards) and translate their input to a variety of
virtual device formats.

%prep
%autosetup -p1 -a1 -n InputPlumber-%{version}

%build
%make_build build

%install
make install PREFIX=%{buildroot}%{_prefix} NO_RELOAD=true

%check
%make_build test

%pre
# spec-cleaner deviation: scriptlet macros below stay in bare form
# because they consume the service names as arguments.
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
%dir %{_modulesloaddir}
%{_modulesloaddir}/*.conf
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
