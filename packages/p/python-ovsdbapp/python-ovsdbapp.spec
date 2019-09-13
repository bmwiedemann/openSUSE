#
# spec file for package python-ovsdbapp
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


%define with_tests 0
Name:           python-ovsdbapp
Version:        0.15.0
Release:        0
Summary:        A library for creating OVSDB applications
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/ovsdbapp
Source0:        https://files.pythonhosted.org/packages/source/o/ovsdbapp/ovsdbapp-0.15.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-fixtures >= 3.0.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-ovs >= 2.8.0
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-fixtures >= 3.0.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-ovs >= 2.8.0
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-fixtures >= 3.0.0
Requires:       python-netaddr >= 0.7.18
Requires:       python-ovs >= 2.8.0
Requires:       python-pbr >= 2.0.0
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
The ovdsbapp library is useful for creating applications that communicate via
Open_vSwitchs OVSDB protocol (https://tools.ietf.org/html/rfc7047). It wraps
the Python 'ovs' and adds an event loop and friendly transactions.

%package -n python-ovsdbapp-doc
Summary:        Documentation for OpenStack log library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-ovsdbapp-doc
Documentation for the ovsdbap library.

%prep
%autosetup -p1 -n ovsdbapp-%{version}
%py_req_cleanup

%build
%{python_build}

# generate html docs
PBR_VERSION=0.15.0 PYTHONPATH=. \
    sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%{python_install}

%if 0%{?with_tests}
%check
%python_exec -m stestr.cli run
%endif

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python_sitelib}/ovsdbapp
%{python_sitelib}/*.egg-info

%files -n python-ovsdbapp-doc
%license LICENSE
%doc doc/build/html

%changelog
