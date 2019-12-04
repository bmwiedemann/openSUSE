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


Name:           python-saharaclient
Version:        2.3.0
Release:        0
Summary:        Client library for OpenStack Sahara API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-saharaclient/python-saharaclient-2.3.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-mock
BuildRequires:  python2-osc-lib >= 1.11.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.log >= 3.36.0
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-requests-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testrepository
BuildRequires:  python3-mock
BuildRequires:  python3-osc-lib >= 1.11.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testrepository
Requires:       python-Babel >= 2.3.4
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-openstackclient >= 3.12.0
Requires:       python-osc-lib >= 1.11.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
Python client library for interacting with OpenStack Sahara API.

%package -n python-saharaclient-doc
Summary:        Documentation for Client library for OpenStack Sahara API
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-saharaclient-doc
Python client library for interacting with OpenStack Sahara API.

%prep
%autosetup -p1 -n python-saharaclient-2.3.0
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}

# Build HTML docs and man page
PYTHONPATH=. PBR_VERSION=2.3.0 %sphinx_build -b html -d doc/build/doctrees doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
# we don't want to depend on hacking/flake8/pep8
rm -v saharaclient/tests/unit/test_hacking.py
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/saharaclient
%{python_sitelib}/*.egg-info

%files -n python-saharaclient-doc
%doc doc/build/html
%license LICENSE

%changelog
