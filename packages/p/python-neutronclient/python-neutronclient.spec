#
# spec file for package python-neutronclient
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


Name:           python-neutronclient
Version:        7.2.1
Release:        0
Summary:        Python API and CLI for OpenStack Neutron
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/python-neutronclient/python-neutronclient-7.2.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-keystoneclient >= 3.8.0
BuildRequires:  python3-mock
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
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Client library and command line utility for interacting with OpenStack
Neutron's API.

%package -n python3-neutronclient
Summary:        Python API and CLI for OpenStack Neutron
Group:          Development/Languages/Python
Requires:       python3-Babel
Requires:       python3-cliff >= 2.8.0
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-keystoneclient >= 3.8.0
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-os-client-config >= 1.28.0
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-simplejson >= 3.5.1
Requires:       python3-six
%if 0%{?suse_version}
Obsoletes:      python2-neutronclient < 7.1.0
%endif

%description -n python3-neutronclient
Client library and command line utility for interacting with OpenStack
Neutron's API.

This package contains the Python 3.x module.

%package -n python-neutronclient-doc
Summary:        Documentation for OpenStack Neutron API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno

%description -n python-neutronclient-doc
Client library and command line utility for interacting with OpenStack
Neutron's API.

%prep
%autosetup -p1 -n %{name}-%{version}
%py_req_cleanup

%build
%{py3_build}

# Build HTML docs and man page
PBR_VERSION=7.2.1 %sphinx_build -b html doc/source doc/build/html
PBR_VERSION=7.2.1 %sphinx_build -b man doc/source doc/build/man
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-neutronclient
%license LICENSE
%{python3_sitelib}/neutronclient
%{python3_sitelib}/*.egg-info
%{_bindir}/neutron

%files -n python-neutronclient-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
