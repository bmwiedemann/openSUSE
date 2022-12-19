#
# spec file for package python-mitmproxy-wireguard
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) specCURRENT_YEAR SUSE LINUX GmbH, Nuernberg, Germany.
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


%define modname mitmproxy_wireguard
Name:           python-mitmproxy-wireguard
Version:        0.1.19
Release:        0
Summary:        WireGuard interface for mitmproxy
License:        MIT
URL:            https://github.com/decathorpe/mitmproxy_wireguard
Source0:        https://files.pythonhosted.org/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz
# use `osc service disabledrun` to regenerate
Source2:        vendor.tar.zst
Source3:        cargo_config
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module maturin >= 0.13.0}
BuildRequires:  %{python_module maturin-debuginfo}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo >= 1.41.0
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  rust >= 1.58.0
BuildRequires:  zstd
# python-base is not enough, we need the _ssl module
Requires:       python >= 3.7
%python_subpackages

%description
Transparently proxy any device that can be configured as a WireGuard client!

%prep
%autosetup -a2 -p1 -n %{modname}-%{version}

mkdir -p .cargo
cp %{SOURCE3} .cargo/config
rm -fv .cargo/config.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%{cargo_test}

%files %python_files
%license LICENSE
%doc CHANGELOG.md README.md
%{python_sitearch}/mitmproxy_wireguard
%{python_sitearch}/mitmproxy_wireguard-%{version}*-info

%changelog
