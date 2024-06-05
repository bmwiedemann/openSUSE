#
# spec file for package python-ironicclient
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-ironicclient
Version:        5.6.0
Release:        0
Summary:        Python API and CLI for OpenStack Ironic
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/python-ironicclient
Source0:        https://files.pythonhosted.org/packages/source/p/python-ironicclient/python-ironicclient-5.6.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Babel
BuildRequires:  python3-PyYAML >= 3.13
BuildRequires:  python3-appdirs
BuildRequires:  python3-dogpile.cache >= 0.8.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-jsonschema >= 3.2.0
BuildRequires:  python3-openstackclient
BuildRequires:  python3-osc-lib >= 2.0.0
BuildRequires:  python3-oslo.i18n
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-python-subunit
BuildRequires:  python3-requests >= 2.14.2
BuildRequires:  python3-requests-mock
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
OpenStack Bare Metal Provisioning API Client Library

This is a client for the OpenStack Ironic API. It provides a Python API (the
ironicclient module) and a command-line interface (ironic).

%package -n python3-ironicclient
Summary:        Python API and CLI for OpenStack Ironic
Requires:       python3-PyYAML >= 3.13
Requires:       python3-appdirs
Requires:       python3-dogpile.cache >= 0.8.0
Requires:       python3-jsonschema >= 3.2.0
Requires:       python3-keystoneauth1 >= 3.11.0
Requires:       python3-openstackclient
Requires:       python3-osc-lib >= 2.0.0
Requires:       python3-oslo.i18n
Requires:       python3-oslo.serialization
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-requests >= 2.14.2

%description -n python3-ironicclient
OpenStack Bare Metal Provisioning API Client Library.

This is a client for the OpenStack Ironic API. It provides a Python API (the
ironicclient module) and a command-line interface (ironic).

This package contains the Python 3.x module.

%package -n python-ironicclient-doc
Summary:        Documentation for OpenStack Ironic API Client
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-ironicclient-doc
This is a client for the OpenStack Ironic API (Bare Metal. There's a
Python API (the ironicclient module), and a command-line script (ironic).
Each implements 100% of the OpenStack Ironic API.
This package contains auto-generated documentation.

%prep
%autosetup -p1 -n python-ironicclient-5.6.0
%py_req_cleanup

%build
%{py3_build}

PBR_VERSION=5.6.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
%{openstack_stestr_run}

%files -n python3-ironicclient
%license LICENSE
%doc README.rst
%{python3_sitelib}/ironicclient
%{python3_sitelib}/*.egg-info
%{_bindir}/baremetal

%files -n python-ironicclient-doc
%license LICENSE
%doc doc/build/html

%changelog
