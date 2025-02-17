#
# spec file for package amdgpu_top
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


Name:           amdgpu_top
Version:        0.10.3
Release:        0
Summary:        Tool that displays AMD GPU utilization
License:        MIT
URL:            https://github.com/Umio-Yasuno/amdgpu_top
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging >= 1.2.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_amdgpu)
Requires:       libwayland-egl1
Requires:       libxkbcommon0

%description
Tool that displays AMD GPU utilization.
The tool displays information gathered from performance counters (GRBM, GRBM2), sensors, fdinfo, and AMDGPU driver.

%prep
%autosetup -a1 -p1

%build
%{cargo_build} --all

%install
install -Dm 0755 target/release/amdgpu_top %{buildroot}%{_bindir}/amdgpu_top
install -Dm 0644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 0644 assets/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm 0644 assets/%{name}-tui.desktop %{buildroot}%{_datadir}/applications/%{name}-tui.desktop

%files
%license LICENSE
%doc README.md docs/*.md
%{_bindir}/amdgpu_top
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-tui.desktop

%changelog
