#
# spec file for package python-napalm
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-napalm
Version:        3.0.1
Release:        0
Summary:        Network Automation and Programmability Abstraction Layer
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/napalm-automation/napalm
Source:         https://github.com/napalm-automation/napalm/archive/%{version}.tar.gz#/napalm-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-cffi >= 1.11.3
Requires:       python-ciscoconfparse
Requires:       python-future
Requires:       python-junos-eznc >= 2.2.1
Requires:       python-netaddr
Requires:       python-netmiko >= 2.4.2
Requires:       python-paramiko >= 2.4.2
Requires:       python-pyeapi >= 0.8.2
Requires:       python-requests >= 2.7.0
Requires:       python-scp
Requires:       python-setuptools >= 38.4.0
Requires:       python-textfsm
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module cffi >= 1.11.3}
BuildRequires:  %{python_module ciscoconfparse}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module junos-eznc >= 2.2.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module netaddr}
BuildRequires:  %{python_module netmiko >= 2.4.2}
BuildRequires:  %{python_module paramiko >= 2.4.2}
BuildRequires:  %{python_module pyeapi >= 0.8.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.7.0}
BuildRequires:  %{python_module scp}
BuildRequires:  %{python_module selectors2 >= 2.0.1}
BuildRequires:  %{python_module setuptools >= 38.4.0}
BuildRequires:  %{python_module textfsm}
# /SECTION
%python_subpackages

%description
NAPALM is a Python library that implements a set of functions to
interact with different router vendor devices using a unified API.

%prep
%setup -q -n napalm-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# FIXME: JunOS related unit tests are know to be broken with junos-eznc-2.3.0.
# Do not run those for now. https://github.com/napalm-automation/napalm/issues/1060
rm -Rf test/junos/
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%python3_only %{_bindir}/cl_napalm_configure
%python3_only %{_bindir}/cl_napalm_test
%python3_only %{_bindir}/cl_napalm_validate
%python3_only %{_bindir}/napalm
%{python_sitelib}/*

%changelog
