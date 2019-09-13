#
# spec file for package python-keystoneauth1
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


%global sname keystoneauth1
Name:           python-keystoneauth1
Version:        3.13.1
Release:        0
Summary:        OpenStack authenticating tools
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/keystoneauth
Source0:        https://files.pythonhosted.org/packages/source/k/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PyYAML
BuildRequires:  python2-betamax
BuildRequires:  python2-fixtures
BuildRequires:  python2-iso8601 >= 0.1.11
BuildRequires:  python2-lxml
BuildRequires:  python2-mock
BuildRequires:  python2-oauthlib
BuildRequires:  python2-os-service-types >= 1.2.0
BuildRequires:  python2-oslo.config
BuildRequires:  python2-oslo.utils
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-reno
BuildRequires:  python2-requests-kerberos
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-testresources
BuildRequires:  python2-testtools
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
BuildRequires:  python3-reno
BuildRequires:  python3-requests-kerberos
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testresources
BuildRequires:  python3-testtools
Requires:       python-PyYAML
Requires:       python-iso8601 >= 0.1.11
Requires:       python-lxml
Requires:       python-oauthlib
Requires:       python-os-service-types >= 1.2.0
Requires:       python-requests >= 2.14.2
Requires:       python-requests-kerberos
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
Tools for authenticating to an OpenStack-based cloud. These tools include:
* Authentication plugins (password, token, and federation based)
* Discovery mechanisms to determine API version support
* A session that is used to maintain client settings across requests
  (based on the requests Python library)

%package -n python-keystoneauth1-doc
Summary:        Documentation for OpenStack authenticating tools
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-keystoneauth1-doc
Documentation for OpenStack authenticating tools.

%prep
%autosetup -p1 -n %{sname}-%{version}
%py_req_cleanup

# cleanup intersphinx (we have no network during build)
echo "intersphinx_mapping = {}" >> doc/source/conf.py

%build
%{python_build}

%install
%{python_install}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
rm -v keystoneauth1/tests/unit/test_hacking_checks.py
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/%{sname}
%{python_sitelib}/*.egg-info

%files -n python-keystoneauth1-doc
%doc doc/build/html
%license LICENSE

%changelog
