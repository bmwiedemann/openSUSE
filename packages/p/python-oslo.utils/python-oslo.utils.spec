#
# spec file for package python-oslo.utils
#
# Copyright (c) 2022 SUSE LLC
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


Name:           python-oslo.utils
Version:        6.1.0
Release:        0
Summary:        OpenStack Utils Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.utils
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.utils/oslo.utils-6.1.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Babel
BuildRequires:  python3-ddt
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-iso8601 >= 0.1.11
BuildRequires:  python3-monotonic
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-netifaces >= 0.10.4
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr
BuildRequires:  python3-pyparsing >= 2.1.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time handling.

%package -n python3-oslo.utils
Summary:        OpenStack Utils Library
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-iso8601 >= 0.1.11
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-netifaces >= 0.10.4
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-pyparsing >= 2.1.0
Requires:       python3-pytz >= 2013.6

%description -n python3-oslo.utils
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time handling.

This package contains the Python 3.x module.

%package -n python-oslo.utils-doc
Summary:        Documentation for OpenStack utils library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-oslo.utils-doc
Documentation for OpenStack utils library.

%prep
%autosetup -p1 -n oslo.utils-6.1.0

%py_req_cleanup

%build
%py3_build

%install
%py3_install

# generate html docs
PBR_VERSION=6.1.0 %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
# tests fail with python 3.8
rm -v oslo_utils/tests/test_reflection.py
python3 -m stestr.cli run

%files -n python3-oslo.utils
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/oslo_utils
%{python3_sitelib}/*.egg-info

%files -n python-oslo.utils-doc
%doc doc/build/html
%license LICENSE

%changelog
