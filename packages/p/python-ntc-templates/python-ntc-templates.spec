#
# spec file for package python-ntc-templates
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-ntc-templates
Version:        2.2.2
Release:        0
Summary:        Package to return structured data from the output of network devices
License:        Apache-2.0
URL:            https://github.com/networktocode/ntc-templates
Source:         https://github.com/networktocode/ntc-templates/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-textfsm >= 1.1.0
Suggests:       python-PyYAML
Suggests:       python-black
Suggests:       python-pytest
Suggests:       python-ruamel.yaml
Suggests:       python-yamllint
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pyaml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module textfsm >= 1.1.0}
# /SECTION
%python_subpackages

%description
Package to return structured data from the output of network devices.

%prep
%setup -q -n ntc-templates-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if 0%{suse_version} <= 1500
# https://github.com/networktocode/ntc-templates/issues/743
rm tests/cisco_ios/show_access-list/cisco_ios_show_access-list.raw
%endif
# https://github.com/networktocode/ntc-templates/issues/743 (closed but still an open issue)
# -> skip tests: arista_eos_show_ip_access-lists, cisco_ios_show_access-list, cisco_nxos_show_ip_bgp_neighbors, cisco_nxos_show_ip_bgp_neighbors_with_policy_names
# https://github.com/networktocode/ntc-templates/issues/958
# -> skip tests: cisco_nxos_show_environment, cisco_nxos_show_environment2
%pytest -k 'not (arista_eos_show_ip_access-lists or cisco_ios_show_access-list or cisco_nxos_show_ip_bgp_neighbors or cisco_nxos_show_environment or cisco_nxos_show_environment2 or cisco_nxos_show_ip_bgp_neighbors_with_policy_names)'

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/*

%changelog
