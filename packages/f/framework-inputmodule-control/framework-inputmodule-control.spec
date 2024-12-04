#
# spec file for package inputmodule-control
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


%define reponame inputmodule-rs
%define shortname inputmodule-control
Name:           framework-inputmodule-control
Version:        0.2.0
Release:        0
Summary:        Framework Laptop 16 Input Module software
License:        MIT
URL:            https://github.com/FrameworkComputer/inputmodule-rs
Source0:        https://github.com/FrameworkComputer/inputmodule-rs/archive/refs/tags/v%{version}.tar.gz#/%{shortname}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libsystemd)

%description
Framework Laptop 16 Input Module software

%package -n framework-inputmodule-udev-rules
Summary:        Inputmodule control udev rules

%description -n framework-inputmodule-udev-rules
Udev Rules for the Framework Laptop 16 Inputmodule

%prep
%autosetup -p1 -a1 -n %{reponame}-%{version}

%build
# inputmodule-control lives in a subdirectory of the inputmodule-rs repo
cd %{shortname}/
cargo build --release

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{reponame}-%{version}/target/release/%{shortname} %{buildroot}%{_bindir}/%{shortname}

install -D -m 0644 release/50-framework-inputmodule.rules %{buildroot}%{_udevrulesdir}/50-framework-inputmodule.rules

# no upstream tests

%post -n framework-inputmodule-udev-rules
%udev_rules_update

%postun -n framework-inputmodule-udev-rules
%udev_rules_update

%files
%license LICENSE
%{_bindir}/%{shortname}

%files -n framework-inputmodule-udev-rules
%{_udevrulesdir}/50-framework-inputmodule.rules

%changelog
