#
# spec file for package python-oslo.config
#
# Copyright (c) 2023 SUSE LLC
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
Version:        9.1.1
Release:        0
Epoch:          0
Summary:        OpenStack common configuration library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.config
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.config/oslo.config-9.1.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 5.1
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-importlib-metadata
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-requests >= 2.18.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-rfc3986 >= 1.2.0
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

%package -n python3-oslo.config
Summary:        OpenStack common configuration library
Requires:       python3-PyYAML >= 5.1
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-importlib-metadata
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-requests >= 2.18.0
Requires:       python3-rfc3986 >= 1.2.0
Requires:       python3-stevedore >= 1.20.0
%if 0%{?suse_version}
Obsoletes:      python2-oslo.config < 8.0.1
%endif

%description -n python3-oslo.config
The Oslo project intends to produce a python library containing
infrastructure code shared by OpenStack projects. The APIs provided
by the project should be high quality, stable, consistent and generally
useful.

The oslo-config library is a command line and configuration file
parsing library from the Oslo project.

This package contains the Python 3.x module.

%package -n python-oslo.config-doc
Summary:        Documentation for OpenStack common configuration library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-oslo.config-doc
Documentation for the oslo-config library.

%prep
%autosetup -p1 -n oslo.config-9.1.1
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=9.1.1 PYTHONPATH=. \
    %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
# Requires oslo.log which we can't depend on for build cycle reasons
rm -v oslo_config/tests/test_cfg.py
%{openstack_stestr_run}

%files -n python3-oslo.config
%license LICENSE
%{_bindir}/oslo-config-generator
%{_bindir}/oslo-config-validator
%{python3_sitelib}/oslo_config
%{python3_sitelib}/*.egg-info

%files -n python-oslo.config-doc
%doc doc/build/html README.rst
%license LICENSE

%changelog
