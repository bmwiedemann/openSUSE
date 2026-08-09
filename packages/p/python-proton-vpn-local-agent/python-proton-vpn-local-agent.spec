#
# spec file for package python-proton-vpn-local-agent
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


%define         _name python-proton-vpn-local-agent
%{?sle15_python_module_pythons}
Name:           python-proton-vpn-local-agent
Version:        1.6.3
Release:        0
Summary:        Proton VPN local agent written in Rust
License:        GPL-3.0-only
URL:            https://github.com/ProtonVPN/local-agent-rs
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cryptography
%python_subpackages

%description
It is a rust crate for communicating with the Proton LocalAgent, and Python bindings for that crate.

%prep
%autosetup -a1 -n local-agent-rs-%{version}

# https://github.com/ProtonVPN/local-agent-rs/pull/11
pushd local_agent_rs
sed -i 's/socket2 = "0.5.7"/socket2 = { version = "0.5.7", features = ["all"] }/' Cargo.toml
popd

# https://github.com/ProtonVPN/local-agent-rs/issues/18
cat > %{_name}/pyproject.toml <<'EOF'
[build-system]
requires = ["maturin>=1.0,<2.0"]
build-backend = "maturin"

[project]
name = "proton-vpn-local-agent"
version = "1.6.3"
requires-python = ">=3.9"
description = "Proton VPN local agent written in Rust"
classifiers = [
    "Programming Language :: Rust",
    "Programming Language :: Python :: Implementation :: CPython",
]

[tool.maturin]
manifest-path = "Cargo.toml"
module-name = "proton.vpn.local_agent"
python-source = "."
bindings = "pyo3"
EOF

pushd %{_name}
# https://github.com/ProtonVPN/local-agent-rs/issues/16
sed -i '/^\[lib\]/a name = "local_agent"' Cargo.toml

# https://github.com/ProtonVPN/local-agent-rs/issues/17
install -d proton/vpn
popd

%build
pushd %{_name}
%pyproject_wheel
popd

%install
pushd %{_name}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}/proton
popd

%check
pushd %{_name}
export PYTHONPATH=%{buildroot}%{python_sitearch}
%pytest
popd

%files %{python_files}
%doc README.md
%{python_sitearch}/proton
%{python_sitearch}/proton_vpn_local_agent*.dist-info

%changelog
