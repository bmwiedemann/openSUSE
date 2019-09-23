#
# spec file for package python-saharaclient
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


%global sname saharaclient
Name:           python-saharaclient
Version:        2.2.1
Release:        0
Summary:        Client library for OpenStack Sahara API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-keystoneclient
BuildRequires:  python-mock
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-osc-lib >= 1.11.0
BuildRequires:  python-oslo.i18n >= 3.15.3
BuildRequires:  python-oslo.log >= 3.36.0
BuildRequires:  python-oslo.serialization >= 2.18.0
BuildRequires:  python-oslo.utils >= 3.33.0
BuildRequires:  python-oslotest
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-requests >= 2.14.2
BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-stestr
BuildRequires:  python-testrepository
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-keystoneclient
Requires:       python-openstackclient >= 3.12.0
Requires:       python-osc-lib >= 1.11.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch

%description
Python client library for interacting with OpenStack Sahara API.

%package doc
Summary:        Documentation for Client library for OpenStack Sahara API
Group:          Documentation/HTML
BuildRequires:  python-Sphinx

%description doc
Python client library for interacting with OpenStack Sahara API.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%py2_build

%install
%py2_install

# Build HTML docs and man page
PBR_VERSION=2.2.1 PYTHONPATH=%{buildroot}%{python2_sitelib} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
# we don't want to depend on hacking/flake8/pep8
rm -v saharaclient/tests/unit/test_hacking.py
python2 -m stestr.cli run

%files
%license LICENSE
%doc ChangeLog README.rst
%{python2_sitelib}/saharaclient
%{python2_sitelib}/*.egg-info

%files doc
%doc doc/build/html
%license LICENSE

%changelog
