#
# spec file for package python-senlinclient
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


Name:           python-senlinclient
Version:        1.10.1
Release:        0
Summary:        Python API and CLI for OpenStack Senlin
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-senlinclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-senlinclient/python-senlinclient-1.10.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-Babel >= 2.3.4
BuildRequires:  python2-PrettyTable >= 0.7.2
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-fixtures
BuildRequires:  python2-heatclient >= 1.10.0
BuildRequires:  python2-mock
BuildRequires:  python2-openstackclient
BuildRequires:  python2-openstacksdk >= 0.24.0
BuildRequires:  python2-osc-lib >= 1.8.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests >= 2.14.2
BuildRequires:  python2-requests-mock
BuildRequires:  python2-stestr
BuildRequires:  python3-Babel >= 2.3.4
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-heatclient >= 1.10.0
BuildRequires:  python3-mock
BuildRequires:  python3-openstackclient
BuildRequires:  python3-openstacksdk >= 0.24.0
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-PyYAML >= 3.12
Requires:       python-heatclient >= 1.10.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-openstackclient
Requires:       python-openstacksdk >= 0.24.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
OpenStack Clustering service Provisioning API Client Library

This is a client for the OpenStack Senlin API.
It provides a Python API (the senlinclient module).

%package -n python-senlinclient-doc
Summary:        Documentation for OpenStack Senlin API Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description -n python-senlinclient-doc
This is a client for the OpenStack Senlin API.
It implements 100% of the OpenStack Senlin API. This package contains
auto-generated documentation.

%prep
%autosetup -p1 -n python-senlinclient-1.10.1
%py_req_cleanup

%build
%{python_build}

%{__python2} setup.py build_sphinx
PBR_VERSION=%version sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/senlinclient
%{python_sitelib}/*.egg-info

%files -n python-senlinclient-doc
%license LICENSE
%doc doc/build/html

%changelog
