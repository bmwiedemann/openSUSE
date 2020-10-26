#
# spec file for package python-oslo.vmware
#
# Copyright (c) 2020 SUSE LLC
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
Version:        3.7.0
Release:        0
Summary:        Oslo VMware library for OpenStack projects
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.vmware
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.vmware/oslo.vmware-3.7.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Babel
BuildRequires:  python3-ddt
BuildRequires:  python3-eventlet >= 0.18.2
BuildRequires:  python3-fixtures
BuildRequires:  python3-lxml >= 4.5.0
BuildRequires:  python3-mock
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-oslo.concurrency >= 3.26.0
BuildRequires:  python3-oslo.context >= 2.19.2
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-stestr
BuildRequires:  python3-suds-jurko >= 0.6
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildRequires:  python3-urllib3 >= 1.21.1
BuildArch:      noarch

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package -n python3-oslo.vmware
Summary:        Oslo VMware library for OpenStack projects
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 3.13
Requires:       python3-eventlet >= 0.18.2
Requires:       python3-lxml >= 4.5.0
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-oslo.concurrency >= 3.26.0
Requires:       python3-oslo.context >= 2.19.2
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six
Requires:       python3-stevedore >= 1.20.0
Requires:       python3-suds-jurko >= 0.6
Requires:       python3-urllib3 >= 1.21.1

%description -n python3-oslo.vmware
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

This package contains the Python 3.x module.

%package        -n python-oslo.vmware-doc
Summary:        Documentation for OpenStack common VMware library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.vmware-doc
Documentation for OpenStack common VMware library.

%prep
%autosetup -p1 -n oslo.vmware-3.7.0
%py_req_cleanup

%build
%py3_build

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%check
# don't want to depend on hacking for package building
rm oslo_vmware/tests/test_hacking.py
python3 -m stestr.cli run

%files -n python3-oslo.vmware
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_vmware
%{python3_sitelib}/*.egg-info

%files -n python-oslo.vmware-doc
%doc doc/build/html
%license LICENSE

%changelog
