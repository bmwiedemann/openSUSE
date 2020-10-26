#
# spec file for package python-monascaclient
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


Name:           python-monascaclient
Version:        2.2.1
Release:        0
Summary:        Python API and CLI for OpenStack Monasca
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-monascaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-monascaclient/python-monascaclient-2.2.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.concurrency
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API (the ``monascaclient`` module) and a command-line tool
(``monasca``).

%package -n python3-monascaclient
Summary:        Python API and CLI for OpenStack Monasca
Group:          Development/Languages/Python
Requires:       python3-Babel >= 2.3.4
Requires:       python3-PrettyTable >= 0.7.2
Requires:       python3-PyYAML >= 3.12
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-osc-lib >= 1.8.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests
Requires:       python3-six >= 1.10.0
%if 0%{?suse_version}
Obsoletes:      python2-monascaclient < 2.0.0
%endif

%description -n python3-monascaclient
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API (the ``monascaclient`` module) and a command-line tool
(``monasca``).

The Monasca Client was written using the OpenStack Heat Python client as a framework.

%prep
%autosetup -p1 -n python-monascaclient-2.2.1
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%check
python3 -m stestr.cli run

%files -n python3-monascaclient
%doc README.rst
%license LICENSE
%{python3_sitelib}/monascaclient
%{python3_sitelib}/*.egg-info
%{_bindir}/monasca

%changelog
