#
# spec file for package python-napalm
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
Name:           python-napalm
Version:        5.1.0
Release:        0
Summary:        Network Automation and Programmability Abstraction Layer
License:        Apache-2.0
URL:            https://github.com/napalm-automation/napalm
Source:         https://github.com/napalm-automation/napalm/archive/%{version}.tar.gz#/napalm-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-cffi >= 1.11.3
Requires:       python-junos-eznc >= 2.6.3
Requires:       python-lxml >= 4.3.0
Requires:       python-ncclient
Requires:       python-netaddr
Requires:       python-netmiko >= 4.4.0
Requires:       python-netutils >= 1.0.0
Requires:       python-paramiko >= 2.6.0
Requires:       python-pyeapi >= 0.8.2
Requires:       python-requests >= 2.7.0
Requires:       python-scp
Requires:       python-setuptools >= 38.4.0
Requires:       python-textfsm
Requires:       python-ttp
Requires:       python-ttp-templates
Requires:       python-typing_extensions
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cffi >= 1.11.3}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module junos-eznc >= 2.6.3}
BuildRequires:  %{python_module lxml >= 4.3.0}
BuildRequires:  %{python_module ncclient}
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module netmiko >= 4.4.0}
BuildRequires:  %{python_module netutils >= 1.0.0}
BuildRequires:  %{python_module paramiko >= 2.6.0}
BuildRequires:  %{python_module pyeapi >= 0.8.2}
BuildRequires:  %{python_module pytest >= 5.4.3}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module scp}
BuildRequires:  %{python_module setuptools >= 38.4.0}
BuildRequires:  %{python_module textfsm}
BuildRequires:  %{python_module ttp-templates}
BuildRequires:  %{python_module ttp}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
%python_subpackages

%description
NAPALM is a Python library that implements a set of functions to
interact with different router vendor devices using a unified API.

%prep
%autosetup -p1 -n napalm-%{version}
sed -i '1{/env python/d}' napalm/pyIOSXR/*.py
rm napalm/junos/templates/schedule_probes.j2

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/napalm
%python_clone -a %{buildroot}%{_bindir}/cl_napalm_validate
%python_clone -a %{buildroot}%{_bindir}/cl_napalm_test
%python_clone -a %{buildroot}%{_bindir}/cl_napalm_configure
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative napalm
%python_install_alternative cl_napalm_validate
%python_install_alternative cl_napalm_test
%python_install_alternative cl_napalm_configure

%postun
%python_uninstall_alternative napalm
%python_uninstall_alternative cl_napalm_validate
%python_uninstall_alternative cl_napalm_test
%python_uninstall_alternative cl_napalm_configure

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/cl_napalm_configure
%python_alternative %{_bindir}/cl_napalm_test
%python_alternative %{_bindir}/cl_napalm_validate
%python_alternative %{_bindir}/napalm
%{python_sitelib}/napalm
%{python_sitelib}/napalm-%{version}.dist-info

%changelog
