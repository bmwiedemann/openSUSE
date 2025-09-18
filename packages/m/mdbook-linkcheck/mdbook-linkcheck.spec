#
# spec file for package mdbook-linkcheck
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


Name:           mdbook-linkcheck
Version:        0.7.7
Release:        0
Summary:        A backend for mdbook which will check your links for you
License:        MIT
URL:            https://github.com/Michael-F-Bryan/mdbook-linkcheck
Source0:        https://github.com/Michael-F-Bryan/mdbook-linkcheck/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd
ExclusiveArch:  %{rust_tier1_arches}

%description
A backend for mdbook which will check your links for you. For use alongside the
built-in HTML renderer.

%prep
%autosetup -a 1

%build
rm .cargo/config
%{cargo_build} --all-features

%install
%{cargo_install} --all-features

%files
%license LICENSE
%doc README.md
%{_bindir}/mdbook-linkcheck

%changelog
