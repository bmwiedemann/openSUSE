#
# spec file for package b3sum
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


Name:           b3sum
Version:        1.5.5
Release:        0
Summary:        A multithreaded rust implementation of BLAKE3
License:        Apache-2.0 OR CC0-1.0
URL:            https://github.com/BLAKE3-team/BLAKE3
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
The official Rust implementation of the BLAKE3 cryptographic hash
function. It uses multithreading by default, making it an order of
magnitude faster than e.g. sha256sum on typical desktop hardware.

%prep
%autosetup -a1 -n %{name}-%{version}/b3sum
mv ../LICENSE_* .

%build
%{cargo_build}

%check
%{cargo_test}

%install
%{cargo_install}

%files
%license LICENSE_A2 LICENSE_A2LLVM LICENSE_CC0

%{_bindir}/%{name}

%changelog
