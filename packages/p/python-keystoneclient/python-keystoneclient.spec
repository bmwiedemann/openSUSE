#
# spec file for package python-keystoneclient
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


Name:           python-keystoneclient
Version:        3.19.0
Release:        0
Summary:        Client library for OpenStack Identity API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-keystoneclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-keystoneclient/python-keystoneclient-3.19.0.tar.gz
BuildRequires:  openssl
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-lxml
BuildRequires:  python2-mock
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testresources
BuildRequires:  python2-testscenarios
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-devel
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
Requires:       python-debtcollector >= 1.2.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Client library for interacting with Openstack Identity API.

%package -n python-keystoneclient-doc
Summary:        Documentation for OpenStack Identity API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-keystoneclient-doc
Documentation for the client library for interacting with Openstack
Identity API.

%prep
%autosetup -p1 -n python-keystoneclient-3.19.0
%py_req_cleanup
# disable intersphinx - no network access during build
echo "intersphinx_mapping = {}" >> doc/source/conf.py

%build
%{python_build}

# Build HTML docs and man page
%{__python2} setup.py build_sphinx

%install
%{python_install}

# Delete tests
rm -fr %{buildroot}%{python2_sitelib}/tests

# Fix hidden-file-or-dir warnings
rm -fr html/.doctrees html/.buildinfo

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python2_sitelib}/keystoneclient
%{python2_sitelib}/*.egg-info

%files -n python-keystoneclient-doc
%doc doc/build/html
%license LICENSE

%changelog
