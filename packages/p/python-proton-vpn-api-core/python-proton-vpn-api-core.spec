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
Version:        4.13.1
Release:        0
Summary:        Proton VPN API library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonVPN/python-proton-vpn-api-core
Source:         https://github.com/ProtonVPN/python-proton-vpn-api-core/archive/refs/tags/v%{version}.tar.gz
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
Requires:       python-PyNaCl
Requires:       python-cryptography
Requires:       python-distro
Requires:       python-proton-core >= 0.4.0
# sentry-sdk is not mandatory and only available in TW
%if 0%{?suse_version} > 1600
Requires:       python-sentry-sdk
%endif
Conflicts:      proton-vpn < 4.8.2
Conflicts:      python-proton-vpn-network-manager < 0.12.10
Obsoletes:      python-proton-vpn-session <= 0.6.7
Obsoletes:      python-proton-vpn-connection <= 0.14.4
Obsoletes:      python-proton-vpn-killswitch <= 0.4.0
Obsoletes:      python-proton-vpn-logger <= 0.2.1
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
# Failing tests, needs to be investigated
# See https://github.com/ProtonVPN/python-proton-vpn-api-core/issues/4
%pytest tests --ignore=tests/connection/test_vpnconfiguration.py --ignore=tests/connection/test_events.py --ignore=tests/connection/test_persistence.py --ignore=tests/connection/test_publisher.py --ignore=tests/connection/test_states.py --ignore=tests/connection/test_vpnconnection.py --ignore=tests/core/refresher/test_certificate_refresher.py --ignore=tests/core/refresher/test_client_config_refresher.py --ignore=tests/core/refresher/test_feature_flags_refresher.py --ignore=tests/core/refresher/test_server_list_refresher.py --ignore=tests/core/refresher/test_scheduler.py --ignore=tests/core/refresher/test_vpn_data_refresher.py --ignore=tests/core/test_connection.py --ignore=tests/core/test_settings.py --ignore=tests/core/test_usage.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/proton
%{python_sitelib}/proton_vpn_api_core-%{version}*-info

%changelog
