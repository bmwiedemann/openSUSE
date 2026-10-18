#
# spec file for package dssim
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


Name:           dssim
Version:        3.5.1
Release:        0
Summary:        This tool computes (dis)similarity between two (or more) PNG images
License:        AGPL-3.0-only AND Apache-2.0 AND BSD-3-Clause AND MIT AND Zlib
URL:            https://kornel.ski/dssim
Source:         https://static.crates.io/crates/%{name}/%{name}-%{version}.crate#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.90

%description
This tool computes (dis)similarity between two PNG images using
(my approximation of) algorithms approximating human vision.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
# Upstream's release profile sets strip=true; keep DWARF for debuginfo packages.
export CARGO_PROFILE_RELEASE_STRIP=none
%{cargo_build}

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dssim

%changelog
