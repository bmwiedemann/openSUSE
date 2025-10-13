#
# spec file for package lsd
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           lsd
Version:        1.2.0
Release:        0
Summary:        Ls command with a lot of pretty colors and some other stuff
License:        Apache-2.0
URL:            https://crates.io/crates/lsd
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
Ls command with a lot of pretty colors and some other stuff.

%prep
%autosetup -a1

%build
%{cargo_build} --all

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/lsd

%changelog
