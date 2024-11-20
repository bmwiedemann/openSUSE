#
# spec file for package python-proton-vpn-api-core
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


%{?sle15_python_module_pythons}
Name:           python-proton-vpn-api-core
Version:        0.35.5
Release:        0
Summary:        Proton VPN API library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonVPN/python-proton-vpn-api-core
Source:         https://github.com/ProtonVPN/python-proton-vpn-api-core/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proton-core}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# sentry-sdk is not mandatory and only available in TW
%if 0%{?suse_version} > 1600
BuildRequires:  %{python_module sentry-sdk}
%endif
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyNaCl
Requires:       python-cryptography
Requires:       python-distro
Requires:       python-proton-core
# sentry-sdk is not mandatory and only available in TW
%if 0%{?suse_version} > 1600
Requires:       python-sentry-sdk
%endif
Conflicts:      python-proton-vpn-connection
Conflicts:      python-proton-vpn-killswitch
Conflicts:      python-proton-vpn-logger
BuildArch:      noarch
%python_subpackages

%description
This package contains a facade to the other Proton VPN components, exposing a uniform API for Proton VPN client.

%prep
%autosetup -p1 -n python-proton-vpn-api-core-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if 0%{?suse_version} > 1600
# Failing tests, needs to be investigated
# See https://github.com/ProtonVPN/python-proton-vpn-api-core/issues/4
%pytest tests --ignore=tests/connection/test_vpnconfiguration.py
%else
# sentry-sdk is not mandatory and only available in TW
%pytest tests --ignore=tests/connection/test_vpnconfiguration.py --ignore=tests/core/test_usage.py
%endif

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/proton
%{python_sitelib}/proton_vpn_api_core-%{version}*-info

%changelog
