#
# spec file for package python-keystonemiddleware
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


Name:           python-keystonemiddleware
Version:        9.1.0
Release:        0
Summary:        Middleware for OpenStack Identity
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/keystonemiddleware
Source0:        https://files.pythonhosted.org/packages/source/k/keystonemiddleware/keystonemiddleware-9.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-WebTest
BuildRequires:  python3-cryptography
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.12.0
BuildRequires:  python3-keystoneclient >= 3.20.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.cache >= 1.26.0
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.context >= 2.19.2
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.messaging
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pycadf >= 1.1.0
BuildRequires:  python3-python-memcached
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore
BuildRequires:  python3-testresources
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
This package contains middleware modules designed to provide authentication
and authorization features to web services other than Keystone
The most prominent module is keystonemiddleware.auth_token. This package
does not expose any CLI or Python API features.

%package -n python3-keystonemiddleware
Summary:        Middleware for OpenStack Identity
Group:          Development/Languages/Python
Requires:       python3-WebOb >= 1.7.1
Requires:       python3-keystoneauth1 >= 3.12.0
Requires:       python3-keystoneclient >= 3.20.0
Requires:       python3-oslo.cache >= 1.26.0
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.context >= 2.19.2
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.messaging
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pycadf >= 1.1.0
Requires:       python3-python-memcached
Requires:       python3-requests >= 2.14.2
Requires:       python3-six >= 1.10.0

%description -n python3-keystonemiddleware
This package contains middleware modules designed to provide authentication
and authorization features to web services other than Keystone
The most prominent module is keystonemiddleware.auth_token. This package
does not expose any CLI or Python API features.

This package contains the Python 3.x module

%package -n python-keystonemiddleware-doc
Summary:        Documentation for Middleware for OpenStack Identity
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python-keystonemiddleware-doc
Documentation for Middleware for OpenStack Identity.

%prep
%autosetup -p1 -n keystonemiddleware-9.1.0
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

# generate html docs
export PYTHONPATH=.
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
python3 -m stestr.cli run

%files -n python3-keystonemiddleware
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/keystonemiddleware
%{python3_sitelib}/*.egg-info

%files -n python-keystonemiddleware-doc
%doc doc/build/html
%license LICENSE

%changelog
