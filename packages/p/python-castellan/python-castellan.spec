#
# spec file for package python-castellan
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


Name:           python-castellan
Version:        5.0.0
Release:        0
Summary:        Generic Key Manager interface for OpenStack
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/castellan
Source0:        https://files.pythonhosted.org/packages/source/c/castellan/castellan-5.0.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-barbicanclient >= 5.5.0
BuildRequires:  python3-cryptography >= 2.7
BuildRequires:  python3-keystoneauth1 >= 3.4.0
BuildRequires:  python3-oslo.config >= 6.4.0
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-reno
BuildRequires:  python3-requests >= 2.18.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
Generic Key Manager interface for OpenStack.

%package -n python3-castellan
Summary:        Generic Key Manager interface for OpenStack
Requires:       python3-Babel
Requires:       python3-barbicanclient >= 5.5.0
Requires:       python3-cryptography >= 2.7
Requires:       python3-keystoneauth1 >= 3.4.0
Requires:       python3-oslo.config >= 6.4.0
Requires:       python3-oslo.context >= 2.19.2
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-requests >= 2.18.0
Requires:       python3-stevedore >= 1.20.0

%description -n python3-castellan
Generic Key Manager interface for OpenStack.

This package includes the Python 3.x module.

%package -n python-castellan-doc
Summary:        Documentation for castellan
Group:          Documentation/HTML
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-sphinxcontrib-svg2pdfconverter

%description -n python-castellan-doc
Castellan is a generic Key Manager interface for OpenStack.
This package contains the documentation

%prep
%autosetup -p1 -n castellan-5.0.0
%py_req_cleanup

%build
%{py3_build}
# generate html docs
PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%check
%{openstack_stestr_run}

%files -n python3-castellan
%license LICENSE
%{python3_sitelib}/castellan
%{python3_sitelib}/*.egg-info

%files -n python-castellan-doc
%license LICENSE
%doc README.rst doc/build/html

%changelog
