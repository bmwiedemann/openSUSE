#
# spec file for package python-troveclient
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


Name:           python-troveclient
Version:        2.17.0
Release:        0
Summary:        Client library for OpenStack DBaaS API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PrettyTable >= 0.7.2
BuildRequires:  python-Sphinx
BuildRequires:  python-httplib2
BuildRequires:  python-keystoneauth1 >= 3.4.0
BuildRequires:  python-mistralclient >= 3.1.0
BuildRequires:  python-mock
BuildRequires:  python-oslo.utils >= 3.33.0
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-requests >= 2.14.2
BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-simplejson >= 3.5.1
BuildRequires:  python-sphinxcontrib-apidoc
BuildRequires:  python-stestr
BuildRequires:  python-swiftclient >= 3.2.0
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-mistralclient >= 3.1.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-simplejson >= 3.5.1
Requires:       python-six >= 1.10.0
Requires:       python-swiftclient >= 3.2.0
BuildArch:      noarch

%description
This is a client for the Trove API. There's a Python API (the
troveclient module), and a command-line script (trove). Each
implements 100% (or less ;) ) of the Trove API.

%package doc
Summary:        Documentation for OpenStack DBaaS API.
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description doc
Documentation for the client library for interacting with Openstack
DBaaS API.

%prep
%autosetup -n %{name}-%{version}
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%py2_build
# Generate html docs
PBR_VERSION=%version sphinx-build -b html doc/source doc/build/html
# Remove the Sphinx-build leftovers
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%py2_install

%check
stestr run

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/python_troveclient-*.egg-info
%{python2_sitelib}/troveclient
%{_bindir}/trove

%files doc
%doc doc/build/html
%license LICENSE

%changelog
