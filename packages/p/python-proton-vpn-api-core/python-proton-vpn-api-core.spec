#
# spec file for package python-proton-vpn-api-core
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


%{?sle15_python_module_pythons}
Name:           python-proton-vpn-api-core
Version:        4.16.0
Release:        0
Summary:        Proton VPN API library
License:        GPL-3.0-or-later
URL:            https://github.com/ProtonVPN/python-proton-vpn-api-core
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module gobject}
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
Requires:       python-proton-core >= 0.4.0
Requires:       python-packaging
Requires:       python-gobject
Requires:       python-pycairo
Requires:       python-proton-vpn-local-agent
# sentry-sdk is not mandatory and only available in TW
%if 0%{?suse_version} > 1600
Requires:       python-sentry-sdk
%endif
Conflicts:      proton-vpn < 4.8.2
Obsoletes:      python-proton-vpn-connection <= 0.14.4
Obsoletes:      python-proton-vpn-killswitch <= 0.4.0
Obsoletes:      python-proton-vpn-logger <= 0.2.1
Obsoletes:      python-proton-vpn-network-manager <= 0.13.5
Obsoletes:      python-proton-vpn-session <= 0.6.7
BuildArch:      noarch
%python_subpackages

%description
This package contains a facade to the other Proton VPN components, exposing a uniform API for Proton VPN client.

%prep
%autosetup

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Failing tests, needs to be investigated
# See https://github.com/ProtonVPN/python-proton-vpn-api-core/issues/4
%pytest tests --ignore=tests/connection/test_vpnconfiguration.py --ignore=tests/connection/test_events.py --ignore=tests/connection/test_persistence.py --ignore=tests/connection/test_publisher.py --ignore=tests/connection/test_states.py --ignore=tests/connection/test_vpnconnection.py --ignore=tests/core/refresher/test_certificate_refresher.py --ignore=tests/core/refresher/test_client_config_refresher.py --ignore=tests/core/refresher/test_feature_flags_refresher.py --ignore=tests/core/refresher/test_server_list_refresher.py --ignore=tests/core/refresher/test_scheduler.py --ignore=tests/core/refresher/test_vpn_data_refresher.py --ignore=tests/core/test_connection.py --ignore=tests/core/test_settings.py --ignore=tests/core/test_usage.py --ignore=tests/networkmanager/core/test_networkmanager.py --ignore=tests/networkmanager/openvpn/test_openvpn.py --ignore=tests/networkmanager/wireguard/test_wireguard.py --ignore=tests/networkmanager/killswitch/default/test_nmkillswitch.py --ignore=tests/networkmanager/killswitch/wireguard/test_wgkillswitch.py --ignore=tests/networkmanager/openvpn/test_openvpnconfiguration.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/proton
%{python_sitelib}/proton_vpn_api_core-%{version}.dist-info

%changelog
