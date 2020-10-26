#
# spec file for package python-keystoneclient
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


Name:           python-keystoneclient
Version:        4.1.1
Release:        0
Summary:        Client library for OpenStack Identity API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-keystoneclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-keystoneclient/python-keystoneclient-4.1.1.tar.gz
BuildRequires:  openssl
BuildRequires:  openstack-macros
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-lxml
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testresources
BuildRequires:  python3-testscenarios
BuildArch:      noarch

%description
Client library for interacting with Openstack Identity API.

%package -n python3-keystoneclient
Summary:        Client library for OpenStack Identity API
Group:          Development/Languages/Python
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0

%description -n python3-keystoneclient
Client library for interacting with Openstack Identity API.

%package -n python-keystoneclient-doc
Summary:        Documentation for OpenStack Identity API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-keystoneclient-doc
Documentation for the client library for interacting with Openstack
Identity API.

%prep
%autosetup -p1 -n python-keystoneclient-4.1.1
%py_req_cleanup
# disable intersphinx - no network access during build
echo "intersphinx_mapping = {}" >> doc/source/conf.py

%build
%{py3_build}

# Build HTML docs and man page
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the Sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-keystoneclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/keystoneclient
%{python3_sitelib}/*.egg-info

%files -n python-keystoneclient-doc
%doc doc/build/html
%license LICENSE

%changelog
