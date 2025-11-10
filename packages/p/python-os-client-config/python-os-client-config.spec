#
# spec file for package python-os-client-config
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


%bcond_with docs
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%global pythons %{primary_python}
%else
%define psuffix %{nil}
%bcond_with test
%endif

Name:           python-os-client-config%{psuffix}
Version:        2.3.0
Release:        0
Summary:        OpenStack Client Configuration Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/os-client-config
Source0:        https://files.pythonhosted.org/packages/source/o/os_client_config/os_client_config-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-keystoneauth1
Requires:       python-requestsexceptions
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module extras}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module glanceclient}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module openstacksdk}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
os-client-config is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner.
It will find cloud config for as few as 1 cloud and as many as you want
to put in a config file. It will read environment variables and config
files, and it also contains some vendor specific default values so that
you don't have to know extra info to use OpenStack.

%if %{with docs}
%package -n python-os-client-config-doc
Summary:        Documentation for OpenStack client configuration library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno

%description -n python-os-client-config-doc
Documentation for the os-client-config library.
%endif

%prep
%autosetup -p1 -n os_client_config-%{version}

%if !%{with test}
%build
%pyproject_wheel
%if %{with docs}
# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/os_client_config
%{python_sitelib}/os_client_config-%{version}.dist-info

%if %{with docs}
%files -n python-os-client-config-doc
%doc doc/build/html
%license LICENSE
%endif
%endif

%changelog
