#
# spec file for package python-openstackclient
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
Name:           python-openstackclient
Version:        8.2.0
Release:        0
Summary:        OpenStack Command-line Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-openstackclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-openstackclient/python_openstackclient-%{version}.tar.gz
BuildRequires:  %{python_module cinderclient}
BuildRequires:  %{python_module cliff >= 3.5.0}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module keystoneclient}
BuildRequires:  %{python_module openstacksdk >= 4.7.1}
BuildRequires:  %{python_module os-client-config}
BuildRequires:  %{python_module osc-lib >= 2.3.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module osprofiler}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module stevedore >= 2.0.1}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module wrapt}
BuildRequires:  openstack-macros
Requires:       python-Babel
Requires:       python-cinderclient
Requires:       python-cliff >= 3.5.0
Requires:       python-keystoneclient
Requires:       python-openstacksdk >= 4.7.1
Requires:       python-osc-lib >= 2.3.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-openstackclient < %{version}
%endif
%python_subpackages

%description
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

%package -n python3-openstackclient-doc
Summary:        Documentation for OpenStack Command-line Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python3-openstackclient-doc
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python_openstackclient-%{version}

%build
%pyproject_wheel

PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=%{version} %sphinx_build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
# man page
install -p -D -m 644 doc/build/man/openstack.1 %{buildroot}%{_mandir}/man1/openstack.1

%check
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/openstackclient
%{python_sitelib}/python_openstackclient-%{version}.dist-info
%{_bindir}/openstack
%{_mandir}/man1/openstack.1.gz

%files -n python3-openstackclient-doc
%license LICENSE
%doc doc/build/html

%changelog
