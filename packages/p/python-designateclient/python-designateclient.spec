#
# spec file for package python-designateclient
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-designateclient
Version:        6.0.1
Release:        0
Summary:        OpenStack DNS as a Service - Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-designateclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-designateclient/python-designateclient-6.0.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-jsonschema >= 3.2.0
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
OpenStack DNS as a Service - Client

%package -n python3-designateclient
Summary:        OpenStack DNS as a Service - Client
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six

%description -n python3-designateclient
OpenStack DNS as a Service - Client

This package contains the Python 3.x module.

%package -n python-designateclient-doc
Summary:        Documentation for the OpenStack DNS as a Service - Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-designateclient-doc
Documentation for the OpenStack DNS as a Service - Client.

%prep
%autosetup -p1 -n python-designateclient-6.0.1
%py_req_cleanup

%build
%py3_build

# generate docs
PYTHONPATH=. PBR_VERSION=6.0.1 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{openstack_stestr_run}

%files -n python3-designateclient
%license LICENSE
%doc README.rst
%{python3_sitelib}/designateclient
%{python3_sitelib}/python_designateclient-%{version}-*.egg-info

%files -n python-designateclient-doc
%license LICENSE
%doc doc/build/html ChangeLog

%changelog
