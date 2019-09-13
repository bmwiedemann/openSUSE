#
# spec file for package python-ironic-inspector-client
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


Name:           python-ironic-inspector-client
Version:        3.5.0
Release:        0
Summary:        Python client and CLI tool for Ironic Inspector
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-ironic-inspector-client
Source0:        https://files.pythonhosted.org/packages/source/p/python-ironic-inspector-client/python-ironic-inspector-client-3.5.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-Sphinx
BuildRequires:  python-devel
BuildRequires:  python-fixtures
BuildRequires:  python-mock
BuildRequires:  python-openstackclient
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-osc-lib >= 1.8.0
BuildRequires:  python-oslo.concurrency
BuildRequires:  python-reno
BuildRequires:  python-requests-mock
BuildRequires:  python-testrepository
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch

%description
Ironic Inspector is an auxiliary service for discovering hardware properties
for a node managed by OpenStack Ironic. Hardware introspection or hardware
properties discovery is a process of getting hardware parameters required for
scheduling from a bare metal node, given its power management credentials
(e.g. IPMI address, user name and password).

This package contains Python client and command line tool for Ironic Inspector.

%prep
%autosetup -p1 -n python-ironic-inspector-client-3.5.0
sed -i -e 's,hacking.*,,' test-requirements.txt
sed -i -e 's,coverage.*,,' test-requirements.txt
sed -i -e 's,doc8.*,,' test-requirements.txt
%py_req_cleanup

%build
%{py2_build}

%install
%{py2_install}

%check
%{__python2} setup.py test

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/ironic_inspector_client
%{python2_sitelib}/*.egg-info

%changelog
