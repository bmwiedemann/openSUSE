#
# spec file for package python-ironic-inspector-client
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


Name:           python-ironic-inspector-client
Version:        4.3.0
Release:        0
Summary:        Python client and CLI tool for Ironic Inspector
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://files.pythonhosted.org/packages/source/p/python-ironic-inspector-client/python-ironic-inspector-client-4.3.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-osc-lib
BuildRequires:  python3-oslo.concurrency
BuildRequires:  python3-reno
BuildRequires:  python3-requests-mock
BuildRequires:  python3-testrepository
BuildArch:      noarch

%description
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given its power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%package -n python3-ironic-inspector-client
Summary:        Python client and CLI tool for Ironic Inspector
Group:          Development/Languages/Python
Requires:       python3-PyYAML >= 3.13
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-openstackclient
Requires:       python3-osc-lib
Requires:       python3-oslo.i18n
Requires:       python3-oslo.utils
Requires:       python3-requests >= 2.14.2

%description -n python3-ironic-inspector-client
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given its power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

This package contains the Python 3.x module.

%prep
%autosetup -p1 -n python-ironic-inspector-client-4.3.0
sed -i -e 's,hacking.*,,' test-requirements.txt
sed -i -e 's,coverage.*,,' test-requirements.txt
sed -i -e 's,doc8.*,,' test-requirements.txt
%py_req_cleanup

%build
%py3_build

%install
%py3_install

%check
%{python_expand rm -rf .testrepository
python3 -m unittest discover ironic_inspector_client
}

%files -n python3-ironic-inspector-client
%doc README.rst
%license LICENSE
%{python3_sitelib}/ironic_inspector_client
%{python3_sitelib}/*.egg-info

%changelog
