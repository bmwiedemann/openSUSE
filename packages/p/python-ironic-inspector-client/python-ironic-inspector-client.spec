#
# spec file for package python-ironic-inspector-client
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global pythons %{primary_python}
Name:           python-ironic-inspector-client
Version:        5.4.0
Release:        0
Summary:        Python client and CLI tool for Ironic Inspector
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-ironic-inspector-client
Source0:        https://files.pythonhosted.org/packages/source/p/python-ironic-inspector-client/python_ironic_inspector_client-%{version}.tar.gz
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module openstacksdk}
BuildRequires:  %{python_module osc-lib}
BuildRequires:  %{python_module oslo.concurrency}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML >= 3.13
Requires:       python-openstackclient
Requires:       python-osc-lib
Requires:       python-oslo.i18n
Requires:       python-oslo.utils
Requires:       python-requests >= 2.14.2
BuildArch:      noarch
%python_subpackages

%description
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given its power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%prep
%autosetup -p1 -n python_ironic_inspector_client-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
export LC_ALL=en_US.UTF-8
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/ironic_inspector_client
%{python_sitelib}/python_ironic_inspector_client-%{version}.dist-info

%changelog
