#
# spec file for package python-senlinclient
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


Name:           python-senlinclient
Version:        2.1.1
Release:        0
Summary:        Python API and CLI for OpenStack Senlin
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-senlinclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-senlinclient/python-senlinclient-2.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Babel
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-PyYAML >= 3.13
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-heatclient >= 1.10.0
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient
BuildRequires:  python3-openstacksdk >= 0.24.0
BuildRequires:  python3-osc-lib >= 1.11.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildArch:      noarch

%description
OpenStack Clustering service Provisioning API Client Library

This is a client for the OpenStack Senlin API.
It provides a Python API (the senlinclient module).

%package -n python3-senlinclient
Summary:        Python API and CLI for OpenStack Senlin
Group:          Development/Languages/Python
Requires:       python3-Babel
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-PyYAML >= 3.13
Requires:       python3-heatclient >= 1.10.0
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-openstackclient
Requires:       python3-openstacksdk >= 0.24.0
Requires:       python3-osc-lib >= 1.11.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests >= 2.14.2
Requires:       python3-six

%description -n python3-senlinclient
OpenStack Clustering service Provisioning API Client Library

This is a client for the OpenStack Senlin API.
It provides a Python API (the senlinclient module).

This package provides the Python 3.x module.

%package -n python-senlinclient-doc
Summary:        Documentation for OpenStack Senlin API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno

%description -n python-senlinclient-doc
This is a client for the OpenStack Senlin API.
It implements 100% of the OpenStack Senlin API. This package contains
auto-generated documentation.

%prep
%autosetup -p1 -n python-senlinclient-2.1.1
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=%version %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-senlinclient
%license LICENSE
%doc README.rst
%{python3_sitelib}/senlinclient
%{python3_sitelib}/*.egg-info

%files -n python-senlinclient-doc
%license LICENSE
%doc doc/build/html

%changelog
