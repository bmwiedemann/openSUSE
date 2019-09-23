#
# spec file for package python-monascaclient
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


Name:           python-monascaclient
Version:        1.15.0
Release:        0
Summary:        Python API and CLI for OpenStack Monasca
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/python-monascaclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-monascaclient/python-monascaclient-1.15.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-PrettyTable >= 0.7.2
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneclient
BuildRequires:  python2-mock
BuildRequires:  python2-mox3
BuildRequires:  python2-openstackdocstheme
BuildRequires:  python2-osc-lib >= 1.8.0
BuildRequires:  python2-oslo.concurrency
BuildRequires:  python2-oslo.config
BuildRequires:  python2-oslo.i18n
BuildRequires:  python2-oslo.log
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-setuptools
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PrettyTable >= 0.7.2
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-mock
BuildRequires:  python3-mox3
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-osc-lib >= 1.8.0
BuildRequires:  python3-oslo.concurrency
BuildRequires:  python3-oslo.config
BuildRequires:  python3-oslo.i18n
BuildRequires:  python3-oslo.log
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-PyYAML >= 3.12
Requires:       python-keystoneclient
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.concurrency
Requires:       python-oslo.config
Requires:       python-oslo.i18n
Requires:       python-oslo.log
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-requests
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
This is a client library for Monasca built to interface with the Monasca API. It
provides a Python API (the ``monascaclient`` module) and a command-line tool
(``monasca``).

The Monasca Client was written using the OpenStack Heat Python client as a framework.

%prep
%autosetup -p1 -n python-monascaclient-1.15.0
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/monasca

%post
%python_install_alternative monasca

%postun
%python_uninstall_alternative monasca

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/monascaclient
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/monasca

%changelog
