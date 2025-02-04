#
# spec file for package rust-cbindgen
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


# Use hardening ldflags.
%global crate_name cbindgen
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now
Name:           rust-%{crate_name}
Version:        0.28.0+git0
Release:        0
Summary:        A tool for generating C bindings from Rust code
License:        MPL-2.0
Group:          Development/Languages/Rust
URL:            https://crates.io/crates/cbindgen
Source0:        %{crate_name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
Source99:       UPDATING.md
BuildRequires:  cargo >= 1.70.0
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.70.0

%description
A tool for generating C bindings from Rust code.

%prep
%setup -q -T -b 0 -n %{crate_name}-%{version}
%setup -q -D -T -a 1 -n %{crate_name}-%{version}
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{crate_name}-%{version}/target/release/%{crate_name} %{buildroot}%{_bindir}/%{crate_name}

%files
%license LICENSE
%{_bindir}/%{crate_name}

%changelog
