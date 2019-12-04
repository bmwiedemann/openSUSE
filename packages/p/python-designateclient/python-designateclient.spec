#
# spec file for package python-designateclient
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


%global sname python-designateclient
Name:           python-designateclient
Version:        3.0.0
Release:        0
Summary:        OpenStack DNS as a Service - Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-jsonschema >= 2.6.0
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python3-jsonschema >= 2.6.0
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
Requires:       python-cliff >= 2.8.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-jsonschema >= 2.6.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
OpenStack DNS as a Service - Client

%package -n python-designateclient-doc
Summary:        Documentation for the OpenStack DNS as a Service - Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-designateclient-doc
Documentation for the OpenStack DNS as a Service - Client.

%prep
%autosetup -n %{sname}-%{version}
%py_req_cleanup

%build
%python_build

# generate docs
PYTHONPATH=. PBR_VERSION=3.0.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python_install

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/designateclient
%{python_sitelib}/python_designateclient-%{version}-*.egg-info

%files -n python-designateclient-doc
%license LICENSE
%doc doc/build/html ChangeLog

%changelog
