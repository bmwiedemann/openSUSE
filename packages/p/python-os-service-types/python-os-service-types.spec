#
# spec file for package python-os-service-types
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


Name:           python-os-service-types
Version:        1.8.1
Release:        0
Summary:        Python library for consuming OpenStack sevice-types-authority data
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/os-service-types/latest/
Source0:        https://files.pythonhosted.org/packages/source/o/os_service_types/os_service_types-%{version}.tar.gz
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pbr >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
BuildArch:      noarch
Requires:       python-typing-extensions
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-os-service-types < %{version}
%else
Conflicts:      python3-os-service-types < %{version}
%endif
%python_subpackages

%description
The OpenStack Service Types Authority contains information about official
OpenStack services and their historical service-type aliases.
The data is in JSON and the latest data should always be used. This simple
library exists to allow for easy consumption of the data, along with a built-in
version of the data to use in case network access is for some reason not
possible and local caching of the fetched data.

%package -n os-service-types-doc
Summary:        Documentation for OpenStack os-service-types library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n os-service-types-doc
The OpenStack Service Types Authority contains information about official
OpenStack services and their historical service-type aliases.
The data is in JSON and the latest data should always be used. This simple
library exists to allow for easy consumption of the data, along with a built-in
version of the data to use in case network access is for some reason not
possible and local caching of the fetched data.
This package contains the documentation.

%prep
%autosetup -p1 -n os_service_types-%{version}
%py_req_cleanup
# The TestRemote test cases must be excluded because they introduce a circular
# dependency on python-keystoneauth1.
# Using --exclude-regex with stestr is not enough because the problem occurs when
# keystoneauth is imported, not when the test is run.
rm os_service_types/tests/test_remote.py

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} %{sphinx_build} -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
export OS_TEST_PATH=os_service_types/tests
%{openstack_stestr_run}

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/os_service_types
%{python_sitelib}/os_service_types-%{version}.dist-info

%files -n os-service-types-doc
%license LICENSE
%doc doc/build/html

%changelog
