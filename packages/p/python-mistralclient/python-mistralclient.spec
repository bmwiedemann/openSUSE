#
# spec file for package python-mistralclient
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
Name:           python-mistralclient
Version:        6.0.0
Release:        0
Summary:        Python API and CLI for OpenStack Mistral
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-mistralclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_mistralclient/python_mistralclient-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module openstackclient}
BuildRequires:  %{python_module osc-lib >= 1.8.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module osprofiler}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML >= 3.13
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneclient
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-osprofiler
Requires:       python-requests >= 2.14.2
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).

%package -n python-mistralclient-doc
Summary:        Documentation for OpenStack Mistral API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-mistralclient-doc
Client library for Mistral built on the Mistral API. It provides a Python API
(the mistralclient module) and a command-line tool (mistral).
This package contains the documentation.

%prep
%autosetup -p1 -n python_mistralclient-%{version}

%build
%pyproject_wheel

# Build HTML docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%{python_sitelib}/mistralclient
%{python_sitelib}/python_mistralclient-%{version}.dist-info
%{_bindir}/mistral

%files -n python-mistralclient-doc
%license LICENSE
%doc README.rst doc/build/html

%changelog
