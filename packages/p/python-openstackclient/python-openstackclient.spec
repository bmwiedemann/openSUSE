#
# spec file for package python-openstackclient
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


Name:           python-openstackclient
Version:        3.18.0
Release:        0
Summary:        OpenStack Command-line Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-openstackclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-openstackclient/python-openstackclient-3.18.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-cinderclient >= 3.3.0
BuildRequires:  python2-cliff >= 2.8.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-glanceclient >= 2.8.0
BuildRequires:  python2-keystoneclient >= 3.17.0
BuildRequires:  python2-mock
BuildRequires:  python2-novaclient >= 10.0.0
BuildRequires:  python2-openstacksdk >= 0.17.0
BuildRequires:  python2-os-client-config
BuildRequires:  python2-osc-lib >= 1.10.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-osprofiler
BuildRequires:  python2-requests
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python2-stevedore
BuildRequires:  python2-testtools
BuildRequires:  python2-wrapt
BuildRequires:  python3-cinderclient >= 3.3.0
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-glanceclient >= 2.8.0
BuildRequires:  python3-keystoneclient >= 3.17.0
BuildRequires:  python3-mock
BuildRequires:  python3-novaclient >= 10.0.0
BuildRequires:  python3-openstacksdk >= 0.17.0
BuildRequires:  python3-os-client-config
BuildRequires:  python3-osc-lib >= 1.10.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-requests
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore
BuildRequires:  python3-testtools
BuildRequires:  python3-wrapt
Requires:       python-Babel >= 2.3.4
Requires:       python-cinderclient >= 3.3.0
Requires:       python-cliff >= 2.8.0
Requires:       python-glanceclient >= 2.8.0
Requires:       python-heatclient
Requires:       python-keystoneauth1 >= 3.6.2
Requires:       python-keystoneclient >= 3.17.0
Requires:       python-novaclient >= 10.0.0
Requires:       python-openstacksdk >= 0.17.0
Requires:       python-osc-lib >= 1.10.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.

%package -n python-openstackclient-doc
Summary:        Documentation for OpenStack Command-line Client
# Some clients are commented out, since they have not been built yet
# TODO(jpena): uncomment them to enable their sections in the documentation
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
#BuildRequires:  python-aodhclient
#BuildRequires:  python-barbicanclient
#BuildRequires:  python-congressclient
#BuildRequires:  python-designateclient
#BuildRequires:  python-heatclient
#BuildRequires:  python-ironicclient
#BuildRequires:  python-mistralclient
#BuildRequires:  python-muranoclient
#BuildRequires:  python-neutronclient
BuildRequires:  python-openstackdocstheme
#BuildRequires:  python-ironic-inspector-client
#BuildRequires:  python-saharaclient
#BuildRequires:  python-zaqarclient
BuildRequires:  python-sphinxcontrib-apidoc

%description -n python-openstackclient-doc
python-openstackclient is a unified command-line client for the OpenStack APIs.
It is a thin wrapper to the stock python-*client modules that implement the
actual REST API client actions.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-openstackclient-3.18.0
%py_req_cleanup

%build
%{python_build}

PBR_VERSION=3.18.0 sphinx-build -b html doc/source doc/build/html
PBR_VERSION=3.18.0 sphinx-build -b man doc/source doc/build/man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
# man page
install -p -D -m 644 doc/build/man/openstack.1 %{buildroot}%{_mandir}/man1/openstack.1
%python_clone -a %{buildroot}%{_bindir}/openstack
%python_clone -a %{buildroot}%{_mandir}/man1/openstack.1

%post
%{python_install_alternative openstack openstack.1}

%postun
%python_uninstall_alternative openstack

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/openstackclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/openstack
%python_alternative %{_mandir}/man1/openstack.1

%files -n python-openstackclient-doc
%license LICENSE
%doc doc/build/html

%changelog
