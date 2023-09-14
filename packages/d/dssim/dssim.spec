#
# spec file for package dssim
#
# Copyright (c) 2023 SUSE LLC
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
Version:        3.2.3
Release:        0
Summary:        This tool computes (dis)similarity between two (or more) PNG images
License:        AGPL-3.0-only and (BSD-2-Clause AND AOMPL-1.0) and Apache-2.0 and BSD-2-Clause and (MIT or Apache2) and MIT and VP8 and MPL-2.0 and Apache-2.0 WITH LLVM-exception
Group:          Productivity/Graphics/Other
URL:            https://kornel.ski/dssim
Source:         https://github.com/pornel/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
This tool computes (dis)similarity between two PNG images using
(my approximation of) algorithms approximating human vision.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%{cargo_install}

%files
%license LICENSE
%doc README.md
%{_bindir}/dssim

%changelog
