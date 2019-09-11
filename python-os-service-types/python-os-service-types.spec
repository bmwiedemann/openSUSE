#
# spec file for package python-os-service-types
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.6.0
Release:        0
Summary:        Python library for consuming OpenStack sevice-types-authority data
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/os-service-types
Source0:        https://files.pythonhosted.org/packages/source/o/os-service-types/os-service-types-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
Requires:       python-pbr >= 2.0.0
BuildArch:      noarch
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
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n os-service-types-doc
The OpenStack Service Types Authority contains information about official
OpenStack services and their historical service-type aliases.
The data is in JSON and the latest data should always be used. This simple
library exists to allow for easy consumption of the data, along with a built-in
version of the data to use in case network access is for some reason not
possible and local caching of the fetched data.
This package contains the documentation.

%prep
%autosetup -p1 -n os-service-types-1.6.0
%py_req_cleanup
# The TestRemote test cases must be excluded because they introduce a circular
# dependency on python-keystoneauth1.
# Using --black-regex with stestr is not enough because the problem occurs when
# keystoneauth is imported, not when the test is run.
rm os_service_types/tests/test_remote.py

%build
%{python_build}

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
export OS_TEST_PATH=os_service_types/tests
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/os_service_types
%{python_sitelib}/*.egg-info

%files -n os-service-types-doc
%license LICENSE
%doc doc/build/html

%changelog
