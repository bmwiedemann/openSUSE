#
# spec file for package python-proton-vpn-local-agent
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


%{?sle15_python_module_pythons}
%define         _name python-proton-vpn-local-agent
Name:           python-proton-vpn-local-agent
Version:        1.6.0
Release:        0
Summary:        Proton VPN local agent written in Rust
License:        GPL-3.0-only
URL:            https://github.com/ProtonVPN/local-agent-rs
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module base}
BuildRequires:  cargo-packaging
BuildRequires:  python-rpm-macros
Requires:       proton-vpn-local-agent = %{version}
%python_subpackages

%description
This repo contains a rust crate for communicating with a proton LocalAgent,
server, and python bindings for that crate.

%package -n proton-vpn-local-agent
Summary:        The library file for the local agent

%description -n proton-vpn-local-agent
%{summary}.

%prep
%autosetup -a1 -n local-agent-rs-%{version}
# See https://github.com/ProtonVPN/local-agent-rs/pull/11
pushd local_agent_rs
sed -i 's/socket2 = "0.5.7"/socket2 = { version = "0.5.7", features = ["all"] }/' Cargo.toml
popd

%build
pushd %{_name}
%{cargo_build}
popd

%install
for p in $(echo "%{pythons}" | sed s/python31/python3.1/g); do
install -d %{buildroot}%{_libdir}/$p/site-packages/{proton,proton/vpn};
ln -sr %{buildroot}%{_libdir}/proton/local_agent.so  %{buildroot}%{_libdir}/$p/site-packages/proton/vpn/local_agent.so;
done
install -Dm0644 target/release/libpython_proton_vpn_local_agent.so %{buildroot}%{_libdir}/proton/local_agent.so

%files %{python_files}
%doc README.md
%dir %{python_sitearch}/proton
%dir %{python_sitearch}/proton/vpn
%{python_sitearch}/proton/vpn/local_agent.so

%files -n proton-vpn-local-agent
%dir %{_libdir}/proton
%{_libdir}/proton/local_agent.so

%changelog
