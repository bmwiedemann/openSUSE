#
# spec file for package python-proton-vpn-session
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
Name:           python-proton-vpn-session
Version:        0.6.7
Release:        0
Summary:        Proton VPN session library
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ProtonVPN/python-proton-vpn-session
Source:         https://github.com/ProtonVPN/python-proton-vpn-session/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module proton-core}
BuildRequires:  %{python_module proton-vpn-logger}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       python-PyNaCl
Requires:       python-cryptography
Requires:       python-distro
Requires:       python-proton-core
Requires:       python-proton-vpn-logger
BuildArch:      noarch
%python_subpackages

%description
This package contains utility classes to manage VPN sessions for Proton VPN client.

%prep
%autosetup -p1 -n python-proton-vpn-session-%{version}

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
%{python_sitelib}/proton_vpn_session-%{version}*-info

%changelog
