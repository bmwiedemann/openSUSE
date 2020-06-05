#
# spec file for package python-congressclient
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


Name:           python-congressclient
Version:        2.0.1
Release:        0
Summary:        Client library for Congress
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-congressclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-congressclient/python-congressclient-2.0.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-osc-lib
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-sphinxcontrib-apidoc
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
This package is client for Congress component.
Congress is an open policy framework for the cloud.
Congress fetches information about VMs from Nova,
and network state from Neutron, etc. Congress then
feeds input data from those services into its policy
engine where Congress verifies that the cloud's actual
state abides by the cloud operator's policies. Congress
is designed to work with any policy and any cloud service.

%package -n python3-congressclient
Summary:        Client library for OpenStack Congress
Group:          Development/Languages/Python
Requires:       python3-Babel >= 2.3.4
Requires:       python3-cliff >= 2.8.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests
Requires:       python3-six >= 1.10.0

%description -n python3-congressclient
Client library for interacting with Openstack Congress API.

%package doc
Summary:        Documentation for OpenStack Congress API client libary
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description doc
This package is client for Congress component.
Congress is an open policy framework for the cloud.
Congress fetches information about VMs from Nova,
and network state from Neutron, etc. Congress then
feeds input data from those services into its policy
engine where Congress verifies that the cloud's actual
state abides by the cloud operator's policies. Congress
is designed to work with any policy and any cloud service.
This package contains the documentation.

%prep
%autosetup -p1 -n python-congressclient-%{version}
%py_req_cleanup

%build
%{py3_build}

# Build HTML docs and man page
PBR_VERSION=2.0.1 %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
%{__python3} -m stestr.cli run

%files -n python3-congressclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/congressclient
%{python3_sitelib}/*.egg-info

%files doc
%doc doc/build/html
%license LICENSE

%changelog
