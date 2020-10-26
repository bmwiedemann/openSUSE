#
# spec file for package python-keystoneauth1
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


Name:           python-keystoneauth1
Version:        4.2.1
Release:        0
Summary:        OpenStack authenticating tools
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/keystoneauth
Source0:        https://files.pythonhosted.org/packages/source/k/keystoneauth1/keystoneauth1-4.2.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML
BuildRequires:  python3-betamax
BuildRequires:  python3-fixtures
BuildRequires:  python3-iso8601 >= 0.1.11
BuildRequires:  python3-lxml
BuildRequires:  python3-mock
BuildRequires:  python3-oauthlib
BuildRequires:  python3-os-service-types >= 1.2.0
BuildRequires:  python3-oslo.config
BuildRequires:  python3-oslo.utils
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-kerberos
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testresources
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Tools for authenticating to an OpenStack-based cloud. These tools include:
* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests
  (based on the requests Python library)

%package -n python3-keystoneauth1
Summary:        OpenStack authenticating tools
Group:          Development/Languages/Python
Requires:       python3-PyYAML
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-lxml
Requires:       python3-oauthlib
Requires:       python3-os-service-types >= 1.2.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-requests-kerberos
Requires:       python3-six >= 1.10.0
Requires:       python3-stevedore >= 1.20.0

%description -n python3-keystoneauth1
Tools for authenticating to an OpenStack-based cloud. These tools include:
* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests
  (based on the requests Python library)

This package contains the Python 3.x module.

%package -n python-keystoneauth1-doc
Summary:        Documentation for OpenStack authenticating tools
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-keystoneauth1-doc
Documentation for OpenStack authenticating tools.

%prep
%autosetup -p1 -n keystoneauth1-%{version}
%py_req_cleanup

# cleanup intersphinx (we have no network during build)
echo "intersphinx_mapping = {}" >> doc/source/conf.py

%build
%{py3_build}

%install
%{py3_install}

# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
rm -v keystoneauth1/tests/unit/test_hacking_checks.py
python3 -m stestr.cli run

%files -n python3-keystoneauth1
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/keystoneauth1
%{python3_sitelib}/*.egg-info

%files -n python-keystoneauth1-doc
%doc doc/build/html
%license LICENSE

%changelog
