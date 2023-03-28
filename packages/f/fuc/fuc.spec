#
# spec file for package fuc
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


Name:           fuc
Version:        1.1.7
Release:        0
Summary:        Modern unix commands focused on performance
License:        Apache-2.0
URL:            https://github.com/SUPERCILEX/fuc
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
# for cargo_install -p
BuildRequires:  cargo-packaging >= 1.2.0
BuildRequires:  rust >= 1.68
ExclusiveArch:  %{rust_tier1_arches}

%description
The FUC-ing project provides modern unix commands focused on performance.
This package provides the commands "rmz" and "cpz", with a CLI interface
compatible with "rm" and "cp", respectively, in a "zippy" faster version.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build} --all

%install
%{cargo_install -p cpz}
%{cargo_install -p rmz}

%files
%license LICENSE
%doc README.md
%{_bindir}/cpz
%{_bindir}/rmz

%changelog
