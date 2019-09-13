#
# spec file for package python-congressclient
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


%global sname python-congressclient
Name:           python-congressclient
Version:        1.12.0
Release:        0
Summary:        Client library for Congress
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-congressclient/python-congressclient-1.12.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-fixtures
BuildRequires:  python-jsonpatch
BuildRequires:  python-mock
BuildRequires:  python-osc-lib
BuildRequires:  python-oslo.log >= 3.36.0
BuildRequires:  python-oslo.serialization >= 2.18.0
BuildRequires:  python-oslo.utils
BuildRequires:  python-oslotest
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-python-subunit
BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-sphinxcontrib-apidoc
BuildRequires:  python-stestr
BuildRequires:  python-testscenarios
Requires:       python-Babel >= 2.3.4
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils
Requires:       python-pbr >= 2.0.0
Requires:       python-requests
Requires:       python-six >= 1.10.0
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

%package doc
Summary:        Documentation for OpenStack Congress API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

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
%autosetup -n %{name}-%{version}
%py_req_cleanup

%build
%{py2_build}

# Build HTML docs and man page
PBR_VERSION=1.12.0 sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py2_install}

%check
stestr run

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/congressclient
%{python2_sitelib}/*.egg-info

%files doc
%doc doc/build/html
%license LICENSE

%changelog
