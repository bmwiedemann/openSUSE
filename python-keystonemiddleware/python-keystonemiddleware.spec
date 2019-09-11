#
# spec file for package python-keystonemiddleware
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


%global sname keystonemiddleware
Name:           python-keystonemiddleware
Version:        6.0.0
Release:        0
Summary:        Middleware for OpenStack Identity
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/k/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openssl
BuildRequires:  openstack-macros
BuildRequires:  python2-WebOb >= 1.7.1
BuildRequires:  python2-WebTest
BuildRequires:  python2-cryptography
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-keystoneclient >= 3.8.0
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.cache >= 1.26.0
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.context >= 2.19.2
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.messaging
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pycadf >= 1.1.0
BuildRequires:  python2-python-memcached
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-requests-mock
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-stevedore
BuildRequires:  python2-testresources
BuildRequires:  python2-testtools
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-WebTest
BuildRequires:  python3-cryptography
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-keystoneclient >= 3.8.0
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
Requires:       python-WebOb >= 1.7.1
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-keystoneclient >= 3.8.0
Requires:       python-oslo.cache >= 1.26.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.context >= 2.19.2
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pycadf >= 1.1.0
Requires:       python-python-memcached
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
This package contains middleware modules designed to provide authentication
and authorization features to web services other than Keystone
The most prominent module is keystonemiddleware.auth_token. This package
does not expose any CLI or Python API features.

%package -n python-keystonemiddleware-doc
Summary:        Documentation for Middleware for OpenStack Identity
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-sphinxcontrib-apidoc

%description -n python-keystonemiddleware-doc
Documentation for Middleware for OpenStack Identity.

%prep
%autosetup -p1 -n %{sname}-%{version}
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}

# generate html docs
export PYTHONPATH=.
PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%python_exec -m stestr.cli run

%files %python_files
%license LICENSE
%doc ChangeLog README.rst
%{python2_sitelib}/%{sname}
%{python2_sitelib}/*.egg-info

%files -n python-keystonemiddleware-doc
%doc doc/build/html
%license LICENSE

%changelog
