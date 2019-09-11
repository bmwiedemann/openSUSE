#
# spec file for package python-oslo.config
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


Name:           python-oslo.config
Version:        6.8.1
Release:        0
Summary:        OpenStack common configuration library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.config
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.config/oslo.config-6.8.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-mock
BuildRequires:  python2-netaddr >= 0.7.18
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr
BuildRequires:  python2-requests >= 2.18.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-rfc3986 >= 1.2.0
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stevedore >= 1.20.0
BuildRequires:  python2-testrepository
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-devel
BuildRequires:  python3-fixtures
BuildRequires:  python3-mock
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-requests >= 2.18.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-rfc3986 >= 1.2.0
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-testrepository
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-PyYAML >= 3.12
Requires:       python-debtcollector >= 1.2.0
Requires:       python-netaddr >= 0.7.18
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-requests >= 2.18.0
Requires:       python-rfc3986 >= 1.2.0
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%ifpython2
BuildRequires:  python2-enum34 >= 1.0.4
Requires:       python-enum34 >= 1.0.4
%endif
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
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package -n python-oslo.config-doc
Summary:        Documentation for OpenStack common configuration library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.config-doc
Documentation for the oslo-config library.

%prep
%autosetup -p1 -n oslo.config-6.8.1
%py_req_cleanup

%build
%{python_build}

PBR_VERSION=6.8.1 PYTHONPATH=. \
    sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/oslo-config-generator
%python_clone -a %{buildroot}%{_bindir}/oslo-config-validator

%post
%{python_install_alternative oslo-config-generator oslo-config-validator}

%postun
%python_uninstall_alternative oslo-config-generator

%check
# Requires oslo.log which we can't depend on for build cycle reasons
rm -v oslo_config/tests/test_cfg.py
%{python_expand rm -rf .testrepository
$python setup.py testr
}

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/oslo-config-generator
%python_alternative %{_bindir}/oslo-config-validator
%{python_sitelib}/oslo_config
%{python_sitelib}/*.egg-info

%files -n python-oslo.config-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
