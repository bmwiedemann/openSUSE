#
# spec file for package python-barbicanclient
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
Name:           python-barbicanclient
Version:        7.2.0
Release:        0
Summary:        Client for the Barbican Key Management API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-barbicanclient
Source0:        https://files.pythonhosted.org/packages/source/p/python_barbicanclient/python_barbicanclient-%{version}.tar.gz
BuildRequires:  %{python_module cliff >= 2.8.0}
BuildRequires:  %{python_module keystoneauth1 >= 5.1.1}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.14.2}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildArch:      noarch
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneauth1 >= 5.1.1
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
%if 0%{?suse_version}
Obsoletes:      python2-barbicanclient < 4.10.0
%endif
%python_subpackages

%description
This is a client for the Barbican Key Management API. This package includes a
Python library for accessing the API (the barbicanclient module), and a
command-line script (barbican).

%package -n python-barbicanclient-doc
Summary:        Documentation for OpenStack Key Management API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python-barbicanclient-doc
Documentation for the client library for interacting with
Openstack Key Management API

%prep
%autosetup -p1 -n python_barbicanclient-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# Remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
%{openstack_stestr_run} \
    --exclude-regex 'barbicanclient.tests.test_barbican.WhenTestingBarbicanCLI.test_should_show_usage_with_help_flag'

%files %{python_files}
%license LICENSE
%{_bindir}/barbican
%{python_sitelib}/python_barbicanclient-%{version}.dist-info
%{python_sitelib}/barbicanclient

%files -n python-barbicanclient-doc
%doc README.rst doc/build/html
%license LICENSE

%changelog
