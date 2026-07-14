#
# spec file for package lutgen-cli
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           lutgen-cli
Version:        1.1.1
Release:        0
Summary:        Blazingly fast interpolated LUT generator and applicator for arbitrary and popular color palettes.
License:        MIT
URL:            https://github.com/ozwaldorf/lutgen-rs
Source0:        lutgen-rs-%{version}.tar.xz
Source1:        vendor.tar.zst

BuildRequires:  rust
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)

%description
A blazingly fast interpolated LUT utility for arbitrary and popular color palettes. Theme any image to your desktop colorscheme

%prep
%autosetup -a1 -n lutgen-rs-%{version}

%build
%{cargo_build} --package lutgen-cli

%install
install -Dm755 target/release/lutgen %{buildroot}%{_bindir}/lutgen
install -Dm644 docs/man/lutgen.1 %{buildroot}%{_mandir}/man1/lutgen.1

%check
%{cargo_test}

%files
%license LICENSE*
%doc README.md docs/pages/*.md
%{_bindir}/lutgen
%{_mandir}/man1/lutgen.1*

%changelog

