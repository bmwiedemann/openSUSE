#
# spec file for package python-osc-lib
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


Name:           python-osc-lib
Version:        2.2.1
Release:        0
Summary:        OpenStackClient Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/osc-lib
Source0:        https://files.pythonhosted.org/packages/source/o/osc-lib/osc-lib-2.2.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-Babel
BuildRequires:  python3-cliff >= 3.2.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.14.0
BuildRequires:  python3-mock
BuildRequires:  python3-openstacksdk >= 0.15.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-simplejson >= 3.5.1
BuildRequires:  python3-six
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.  osc-lib
is a package of common support modules for writing OSC plugins.

%package -n python3-osc-lib
Summary:        OpenStackClient Library
Group:          Development/Languages/Python
Requires:       python3-Babel
Requires:       python3-cliff >= 3.2.0
Requires:       python3-keystoneauth1 >= 3.14.0
Requires:       python3-openstacksdk >= 0.15.0
Requires:       python3-oslo.i18n >= 3.15.3
Requires:       python3-oslo.utils >= 3.33.0
Requires:       python3-pbr >= 2.0.0
Requires:       python3-simplejson >= 3.5.1
Requires:       python3-six
Requires:       python3-stevedore >= 1.20.0

%description -n python3-osc-lib
OpenStackClient (aka OSC) is a command-line client for OpenStack.  osc-lib
is a package of common support modules for writing OSC plugins.

This package contains the Python 3.x module.

%package -n python-osc-lib-doc
Summary:        Documentation for the OpenStack client library
Group:          Development/Languages/Python
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme
BuildRequires:  python3-reno
BuildRequires:  python3-sphinxcontrib-apidoc

%description -n python-osc-lib-doc
Documentation for the OpenStack client library.

%prep
%autosetup -p1 -n osc-lib-2.2.1
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

# generate html docs
PBR_VERSION=%{version} PYTHONPATH=. %sphinx_build -a -E -d doc/build/doctrees -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
python3 -m stestr.cli run

%files -n python3-osc-lib
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/osc_lib
%{python3_sitelib}/*.egg-info

%files -n python-osc-lib-doc
%license LICENSE
%doc doc/build/html

%changelog
