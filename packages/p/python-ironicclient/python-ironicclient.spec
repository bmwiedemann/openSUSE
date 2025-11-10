#
# spec file for package python-ironicclient
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
Name:           python-ironicclient
Version:        5.13.0
Release:        0
Summary:        Python API and CLI for OpenStack Ironic
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-ironicclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-ironicclient/python_ironicclient-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module dogpile.cache >= 0.8.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module openstacksdk}
BuildRequires:  %{python_module osc-lib >= 2.0.0}
BuildRequires:  %{python_module oslo.i18n}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module requests >= 2.14.2}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML >= 3.13
Requires:       python-appdirs
Requires:       python-dogpile.cache >= 0.8.0
Requires:       python-jsonschema >= 3.2.0
Requires:       python-keystoneauth1 >= 3.11.0
Requires:       python-osc-lib >= 2.0.0
Requires:       python-oslo.i18n
Requires:       python-oslo.serialization
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 6.0.0
Requires:       python-requests >= 2.14.2
BuildArch:      noarch
%python_subpackages

%description
OpenStack Bare Metal Provisioning API Client Library

This is a client for the OpenStack Ironic API. It provides a Python API (the
ironicclient module) and a command-line interface (ironic).

%package -n python-ironicclient-doc
Summary:        Documentation for OpenStack Ironic API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-ironicclient-doc
This is a client for the OpenStack Ironic API (Bare Metal. There's a
Python API (the ironicclient module), and a command-line script (ironic).
Each implements 100% of the OpenStack Ironic API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_ironicclient-%{version}
%py_req_cleanup

%build
%pyproject_wheel

PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python3_sitelib}/ironicclient
%{python3_sitelib}/python_ironicclient-%{version}.dist-info
%{_bindir}/baremetal

%files -n python-ironicclient-doc
%license LICENSE
%doc doc/build/html

%changelog
