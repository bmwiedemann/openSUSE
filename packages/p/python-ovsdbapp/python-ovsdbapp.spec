#
# spec file for package python-ovsdbapp
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


%define with_tests 1
Name:           python-ovsdbapp
Version:        2.2.0
Release:        0
Summary:        A library for creating OVSDB applications
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/ovsdbapp
Source0:        https://files.pythonhosted.org/packages/source/o/ovsdbapp/ovsdbapp-2.2.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-fixtures >= 3.0.0
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-oslotest
BuildRequires:  python3-ovs >= 2.10.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
The ovdsbapp library is useful for creating applications that communicate via
Open_vSwitchs OVSDB protocol (https://tools.ietf.org/html/rfc7047). It wraps
the Python 'ovs' and adds an event loop and friendly transactions.

%package -n python3-ovsdbapp
Summary:        A library for creating OVSDB applications
Requires:       python3-fixtures >= 3.0.0
Requires:       python3-netaddr >= 0.7.18
Requires:       python3-ovs >= 2.10.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-six

%description -n python3-ovsdbapp
The ovdsbapp library is useful for creating applications that communicate via
Open_vSwitchs OVSDB protocol (https://tools.ietf.org/html/rfc7047). It wraps
the Python 'ovs' and adds an event loop and friendly transactions.

%package -n python-ovsdbapp-doc
Summary:        Documentation for OpenStack log library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python-ovsdbapp-doc
Documentation for the ovsdbap library.

%prep
%autosetup -p1 -n ovsdbapp-%{version}
%py_req_cleanup

%build
%{py3_build}

# generate html docs
PBR_VERSION=2.2.0 PYTHONPATH=. \
    %sphinx_build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{py3_install}

%if 0%{?with_tests}
%check
OS_TEST_PATH=./ovsdbapp/tests/unit PYTHONPATH=. python3 -m stestr.cli run
%endif

%files -n python3-ovsdbapp
%license LICENSE
%doc ChangeLog README.rst
%{python3_sitelib}/ovsdbapp
%{python3_sitelib}/*.egg-info

%files -n python-ovsdbapp-doc
%license LICENSE
%doc doc/build/html

%changelog
