#
# spec file for package python-neutronclient
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
Name:           python-neutronclient
Version:        11.6.0
Release:        0
Summary:        Python API and CLI for OpenStack Neutron
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-neutronclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-neutronclient/python_neutronclient-%{version}.tar.gz
BuildRequires:  %{python_module cliff >= 3.4.0}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneclient}
BuildRequires:  %{python_module netaddr >= 0.7.18}
BuildRequires:  %{python_module os-client-config >= 1.28.0}
BuildRequires:  %{python_module osc-lib >= 1.12.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.log >= 3.36.0}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module osprofiler}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-Babel
Requires:       python-cliff >= 3.4.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-keystoneauth1 >= 3.8.0
Requires:       python-netaddr >= 0.7.18
Requires:       python-osc-lib >= 1.12.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-simplejson
BuildArch:      noarch
%python_subpackages

%description
Client library and command line utility for interacting with OpenStack
Neutron's API.

%package -n python3-neutronclient-doc
Summary:        Documentation for OpenStack Neutron API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno

%description -n python3-neutronclient-doc
Client library and command line utility for interacting with OpenStack
Neutron's API.

%prep
%autosetup -p1 -n python_neutronclient-%{version}

%build
%pyproject_wheel

# Build HTML docs and man page
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=%{version} %sphinx_build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%{python_sitelib}/neutronclient
%{python_sitelib}/python_neutronclient-%{version}.dist-info

%files -n python3-neutronclient-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
