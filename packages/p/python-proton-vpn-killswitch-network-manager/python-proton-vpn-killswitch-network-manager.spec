#
# spec file for package python-proton-vpn-killswitch-network-manager
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-proton-vpn-killswitch-network-manager
Version:        0.4.5
Release:        0
Summary:        Proton VPN kill switch interface using NetworkManager
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonVPN/python-proton-vpn-killswitch-network-manager
Source:         https://github.com/ProtonVPN/python-proton-vpn-killswitch-network-manager/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proton-vpn-killswitch}
BuildRequires:  %{python_module proton-vpn-logger}
BuildRequires:  %{python_module pycairo}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  NetworkManager-devel
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       NetworkManager
Requires:       python-gobject
Requires:       python-packaging
Requires:       python-proton-vpn-killswitch
Requires:       python-proton-vpn-logger
Requires:       python-pycairo
BuildArch:      noarch
%python_subpackages

%description
This package contains the VPN kill switch interface using NetworkManager for Proton VPN client.

%prep
%autosetup -p1 -n python-proton-vpn-killswitch-network-manager-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/proton
%{python_sitelib}/proton_vpn_killswitch_network_manager-%{version}*-info

%changelog
