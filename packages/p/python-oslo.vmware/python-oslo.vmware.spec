#
# spec file for package python-oslo.vmware
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


Name:           python-oslo.vmware
Version:        4.7.0
Release:        0
Summary:        Oslo VMware library for OpenStack projects
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.vmware
Source0:        https://files.pythonhosted.org/packages/source/o/oslo-vmware/oslo_vmware-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module eventlet >= 0.18.2}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module lxml >= 4.5.0}
BuildRequires:  %{python_module oslo.concurrency >= 3.26.0}
BuildRequires:  %{python_module oslo.context >= 2.19.2}
BuildRequires:  %{python_module oslo.i18n >= 3.15.3}
BuildRequires:  %{python_module oslo.utils >= 3.33.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module requests >= 2.14.2}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module suds-community >= 0.6}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module urllib3 >= 1.21.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-defusedxml
Requires:       python-eventlet >= 0.18.2
Requires:       python-lxml >= 4.5.0
Requires:       python-oslo.concurrency >= 3.26.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-suds-community >= 0.6
Requires:       python-urllib3 >= 1.21.1
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.vmware < %{version}
%endif
%python_subpackages

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package -n python3-oslo.vmware-doc
Summary:        Documentation for OpenStack common VMware library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python3-oslo.vmware-doc
Documentation for OpenStack common VMware library.

%prep
%autosetup -p1 -n oslo_vmware-%{version}

%build
%pyproject_wheel

# generate html docs
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install

%check
# don't want to depend on hacking for package building
rm oslo_vmware/tests/test_hacking.py
%{openstack_stestr_run}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/oslo_vmware
%{python_sitelib}/oslo_vmware-%{version}.dist-info

%files -n python3-oslo.vmware-doc
%doc doc/build/html
%license LICENSE

%changelog
