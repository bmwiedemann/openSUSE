#
# spec file for package python-oslo.vmware
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


Name:           python-oslo.vmware
Version:        2.32.2
Release:        0
Summary:        Oslo VMware library for OpenStack projects
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.vmware
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.vmware/oslo.vmware-2.32.2.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-Babel
BuildRequires:  python2-ddt
BuildRequires:  python2-eventlet >= 0.18.2
BuildRequires:  python2-fixtures
BuildRequires:  python2-lxml >= 3.4.1
BuildRequires:  python2-mock
BuildRequires:  python2-mox3
BuildRequires:  python2-netaddr >= 0.7.18
BuildRequires:  python2-oslo.concurrency >= 3.26.0
BuildRequires:  python2-oslo.context >= 2.19.2
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-python-subunit
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-stestr
BuildRequires:  python2-suds-jurko >= 0.6
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python2-urllib3 >= 1.21.1
BuildRequires:  python3-Babel
BuildRequires:  python3-ddt
BuildRequires:  python3-devel
BuildRequires:  python3-eventlet >= 0.18.2
BuildRequires:  python3-fixtures
BuildRequires:  python3-lxml >= 3.4.1
BuildRequires:  python3-mock
BuildRequires:  python3-mox3
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
Requires:       python-PyYAML >= 3.12
Requires:       python-eventlet >= 0.18.2
Requires:       python-lxml >= 3.4.1
Requires:       python-netaddr >= 0.7.18
Requires:       python-oslo.concurrency >= 3.26.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
Requires:       python-suds-jurko >= 0.6
Requires:       python-urllib3 >= 1.21.1
BuildArch:      noarch
%ifpython3
BuildRequires:  python3-dbm
%endif
%python_subpackages

%description
The Oslo project intends to produce a python library containing infrastructure
code shared by OpenStack projects. The APIs provided by the project should be
high quality, stable, consistent and generally useful.

The Oslo VMware library offers session and API call management for VMware ESX/VC
server.

%package        -n python-oslo.vmware-doc
Summary:        Documentation for OpenStack common VMware library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
Requires:       %{name} = %{version}

%description -n python-oslo.vmware-doc
Documentation for OpenStack common VMware library.

%prep
%autosetup -p1 -n oslo.vmware-2.32.2
%py_req_cleanup

%build
%python_build

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python2_sitelib}/oslo_vmware
%{python2_sitelib}/*.egg-info

%files -n python-oslo.vmware-doc
%doc doc/build/html
%license LICENSE

%changelog
