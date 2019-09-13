#
# spec file for package python-neutronclient
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


Name:           python-neutronclient
Version:        6.12.0
Release:        0
Summary:        Python API and CLI for OpenStack Neutron
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-neutronclient/python-neutronclient-6.12.0.tar.gz
# https://review.openstack.org/585387
# Needed for osprofiler==2.3.0
BuildRequires:  openstack-macros
BuildRequires:  python2-cliff >= 2.8.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneauth1 >= 3.4.0
BuildRequires:  python2-keystoneclient >= 3.8.0
BuildRequires:  python2-mock
BuildRequires:  python2-mox3
BuildRequires:  python2-netaddr >= 0.7.18
BuildRequires:  python2-os-client-config >= 1.28.0
BuildRequires:  python2-osc-lib >= 1.8.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.log >= 3.36.0
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-osprofiler
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-keystoneclient >= 3.8.0
BuildRequires:  python3-mock
BuildRequires:  python3-mox3
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-os-client-config >= 1.28.0
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-cliff >= 2.8.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-iso8601 >= 0.1.11
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-keystoneclient >= 3.8.0
Requires:       python-netaddr >= 0.7.18
Requires:       python-os-client-config >= 1.28.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-simplejson >= 3.5.1
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
Client library and command line utility for interacting with OpenStack
Neutron's API.

%package -n python-neutronclient-doc
Summary:        Documentation for OpenStack Neutron API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description -n python-neutronclient-doc
Client library and command line utility for interacting with OpenStack
Neutron's API.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%{python_build}

# Build HTML docs and man page
PBR_VERSION=6.12.0 sphinx-build -b html doc/source doc/build/html
PBR_VERSION=6.12.0 sphinx-build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/neutron

%post
%python_install_alternative neutron

%postun
%python_uninstall_alternative neutron

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%{python_sitelib}/neutronclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/neutron

%files -n python-neutronclient-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
