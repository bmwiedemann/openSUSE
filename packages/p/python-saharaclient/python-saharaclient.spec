#
# spec file for package python-saharaclient
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


Name:           python-saharaclient
Version:        3.2.1
Release:        0
Summary:        Client library for OpenStack Sahara API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-saharaclient/python-saharaclient-3.2.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-mock
BuildRequires:  python3-osc-lib >= 2.0.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testrepository
BuildArch:      noarch

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python3-saharaclient
Summary:        Client library for OpenStack Sahara API
Group:          Development/Languages/Python
Requires:       python3-Babel
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-openstackclient >= 5.2.0
Requires:       python3-osc-lib >= 2.0.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0

%description -n python3-saharaclient
Python client library for interacting with OpenStack Sahara API.

This package contains the Python 3.x module.

%package -n python-saharaclient-doc
Summary:        Documentation for Client library for OpenStack Sahara API
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-saharaclient-doc
Python client library for interacting with OpenStack Sahara API.

%prep
%autosetup -p1 -n python-saharaclient-3.2.1
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

# Build HTML docs and man page
PYTHONPATH=. PBR_VERSION=3.2.1 %sphinx_build -b html -d doc/build/doctrees doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
# we don't want to depend on hacking/flake8/pep8
rm -v saharaclient/tests/unit/test_hacking.py
python3 -m stestr.cli run

%files -n python3-saharaclient
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/saharaclient
%{python3_sitelib}/*.egg-info

%files -n python-saharaclient-doc
%doc doc/build/html
%license LICENSE

%changelog
