#
# spec file for package python-openstackclient
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


Name:           python-openstackclient
Version:        5.4.0
Release:        0
Summary:        OpenStack Command-line Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-openstackclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-openstackclient/python-openstackclient-5.4.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-cinderclient >= 3.3.0
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-ddt
BuildRequires:  python3-fixtures
BuildRequires:  python3-glanceclient
BuildRequires:  python3-keystoneclient >= 3.22.0
BuildRequires:  python3-mock
BuildRequires:  python3-novaclient >= 15.1.0
BuildRequires:  python3-openstacksdk >= 0.48.0
BuildRequires:  python3-os-client-config
BuildRequires:  python3-osc-lib >= 2.0.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-requests
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 2.0.1
BuildRequires:  python3-testtools
BuildRequires:  python3-wrapt
BuildArch:      noarch

%description
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

%package -n python3-openstackclient
Summary:        OpenStack Command-line Client
Group:          Development/Languages/Python
Requires:       python3-Babel
Requires:       python3-cinderclient >= 3.3.0
Requires:       python3-cliff >= 2.8.0
Requires:       python3-glanceclient
Requires:       python3-heatclient
Requires:       python3-keystoneauth1
Requires:       python3-keystoneclient >= 3.22.0
Requires:       python3-novaclient >= 15.1.0
Requires:       python3-openstacksdk >= 0.48.0
Requires:       python3-osc-lib >= 2.0.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-six >= 1.10.0
%if 0%{?suse_version}
Obsoletes:      python2-openstackclient < 4.0.0
%endif

%description -n python3-openstackclient
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

This package contains the Python 3.x module.

%package -n python-openstackclient-doc
Summary:        Documentation for OpenStack Command-line Client
# Some clients are commented out, since they have not been built yet
# TODO(jpena): uncomment them to enable their sections in the documentation
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
#BuildRequires:  python3-aodhclient
#BuildRequires:  python3-barbicanclient
#BuildRequires:  python3-congressclient
#BuildRequires:  python3-designateclient
#BuildRequires:  python3-heatclient
#BuildRequires:  python3-ironicclient
#BuildRequires:  python3-mistralclient
#BuildRequires:  python3-muranoclient
#BuildRequires:  python3-neutronclient
BuildRequires:  python3-openstackdocstheme
#BuildRequires:  python3-ironic-inspector-client
#BuildRequires:  python3-saharaclient
#BuildRequires:  python3-zaqarclient
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-openstackclient-doc
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-openstackclient-5.4.0
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=5.4.0 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=5.4.0 %sphinx_build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}
# man page
install -p -D -m 644 doc/build/man/openstack.1 %{buildroot}%{_mandir}/man1/openstack.1

%check
python3 -m stestr.cli run

%files -n python3-openstackclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/openstackclient
%{python3_sitelib}/*.egg-info
%{_bindir}/openstack
%{_mandir}/man1/openstack.1.gz

%files -n python-openstackclient-doc
%license LICENSE
%doc doc/build/html

%changelog
