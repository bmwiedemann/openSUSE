#
# spec file for package protonup-rs
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


Name:           protonup-rs
Version:        0.15.1
Release:        0
Summary:        A app to automate the management of Linux Gaming Compatibility tools
License:        GPL-3.0-only
URL:            https://github.com/auyer/Protonup-rs
Source0:        https://github.com/auyer/Protonup-rs/archive/refs/tags/v%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description
A Rust app to automate the installation and update of Linux Gaming Compatibility tools, like ProtonGE, Luxtorpeda, Boxtron and others.

%prep
%autosetup -n Protonup-rs-%{version} -a1

%build
%{cargo_build} --locked

%install
install -Dm755 target/release/%{name} \
  %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md

%changelog

