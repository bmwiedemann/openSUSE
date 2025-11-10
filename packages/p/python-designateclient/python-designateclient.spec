#
# spec file for package python-designateclient
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
Name:           python-designateclient
Version:        6.3.0
Release:        0
Summary:        OpenStack DNS as a Service - Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-designateclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_designateclient/python_designateclient-%{version}.tar.gz
BuildRequires:  %{python_module jsonschema >= 3.2.0}
BuildRequires:  %{python_module keystoneauth1 >= 3.4.0}
BuildRequires:  %{python_module osc-lib >= 1.8.0}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-debtcollector >= 1.2.0
Requires:       python-jsonschema >= 3.2.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
OpenStack DNS as a Service - Client

%package -n python3-designateclient-doc
Summary:        Documentation for the OpenStack DNS as a Service - Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python3-designateclient-doc
Documentation for the OpenStack DNS as a Service - Client.

%prep
%autosetup -p1 -n python_designateclient-%{version}

%build
%pyproject_wheel

# generate docs
PYTHONPATH=. PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python3_sitelib}/designateclient
%{python3_sitelib}/python_designateclient-%{version}.dist-info

%files -n python3-designateclient-doc
%license LICENSE
%doc doc/build/html ChangeLog

%changelog
