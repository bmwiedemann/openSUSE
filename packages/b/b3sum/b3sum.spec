#
# spec file for package b3sum
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


Name:           b3sum
Version:        1.8.3
Release:        0
Summary:        A multithreaded rust implementation of BLAKE3
License:        Apache-2.0 OR CC0-1.0
URL:            https://github.com/BLAKE3-team/BLAKE3
Source0:        https://github.com/BLAKE3-team/BLAKE3/archive/refs/tags/%{version}.tar.gz#/BLAKE3-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
The official Rust implementation of the BLAKE3 cryptographic hash
function. It uses multithreading by default, making it an order of
magnitude faster than e.g. sha256sum on typical desktop hardware.

%prep
export CARGO_HOME=%{_builddir}/BLAKE3-%{version}/b3sum/.cargo
%autosetup -a1 -n BLAKE3-%{version}/b3sum

%build
export CARGO_HOME=%{_builddir}/BLAKE3-%{version}/b3sum/.cargo
%{cargo_build}

%check
export CARGO_HOME=%{_builddir}/BLAKE3-%{version}/b3sum/.cargo
%{cargo_test}

%install
export CARGO_HOME=%{_builddir}/BLAKE3-%{version}/b3sum/.cargo
%{cargo_install}

%files
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0

%{_bindir}/%{name}

%changelog
