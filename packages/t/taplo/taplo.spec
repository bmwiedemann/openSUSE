#
# spec file for package taplo
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


Name:           taplo
Version:        0.10.0
Release:        0
Summary:        A TOML toolkit written in Rust
License:        MIT
Group:          Development/Tools/Other
URL:            https://github.com/tamasfe/taplo
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  openssl-devel

%description
Validate TOML documents syntactically or against JSON schemas.

%prep
%autosetup -a1

%build
%{cargo_build} --all-features

%check
%{cargo_test}

%install
install -Dm 755 -t "%{buildroot}%{_bindir}" target/release/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
