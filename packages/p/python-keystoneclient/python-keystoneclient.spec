#
# spec file for package python-keystoneclient
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


Name:           python-keystoneclient
Version:        5.7.0
Release:        0
Epoch:          0
Summary:        Client library for OpenStack Identity API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-keystoneclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-keystoneclient/python_keystoneclient-%{version}.tar.gz
BuildRequires:  %{python_module debtcollector >= 1.2.0}
BuildRequires:  %{python_module keystoneauth1 >= 3.4.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module wheel}
BuildRequires:  openssl
BuildRequires:  openstack-macros
Requires:       python-debtcollector >= 1.2.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-packaging >= 20.4
Requires:       python-requests >= 2.14.2
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-keystoneclient < %{version}
%endif
%python_subpackages

%description
Client library for interacting with Openstack Identity API.

%package -n python-keystoneclient-doc
Summary:        Documentation for OpenStack Identity API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-keystoneclient-doc
Documentation for the client library for interacting with Openstack
Identity API.

%prep
%autosetup -p1 -n python_keystoneclient-%{version}

%build
%pyproject_wheel

# Build HTML docs and man page
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/keystoneclient
%{python_sitelib}/python_keystoneclient-%{version}.dist-info

%files -n python-keystoneclient-doc
%doc doc/build/html
%license LICENSE

%changelog
