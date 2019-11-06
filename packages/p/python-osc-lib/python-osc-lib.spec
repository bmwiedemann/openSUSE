#
# spec file for package python-osc-lib
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


Name:           python-osc-lib
Version:        1.14.1
Release:        0
Summary:        OpenStackClient Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/developer/osc-lib
Source0:        https://files.pythonhosted.org/packages/source/o/osc-lib/osc-lib-1.14.1.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-Babel >= 2.3.4
BuildRequires:  python2-cliff >= 2.8.0
BuildRequires:  python2-fixtures
BuildRequires:  python2-keystoneauth1 >= 3.7.0
BuildRequires:  python2-mock
BuildRequires:  python2-openstacksdk >= 0.15.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-osprofiler
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-requests-mock
BuildRequires:  python2-simplejson >= 3.5.1
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-stevedore >= 1.20.0
BuildRequires:  python2-testtools
BuildRequires:  python3-Babel >= 2.3.4
BuildRequires:  python3-cliff >= 2.8.0
BuildRequires:  python3-fixtures
BuildRequires:  python3-keystoneauth1 >= 3.7.0
BuildRequires:  python3-mock
BuildRequires:  python3-openstacksdk >= 0.15.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-osprofiler
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-requests-mock
BuildRequires:  python3-simplejson >= 3.5.1
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-testtools
Requires:       python-Babel >= 2.3.4
Requires:       python-cliff >= 2.8.0
Requires:       python-keystoneauth1 >= 3.7.0
Requires:       python-openstacksdk >= 0.15.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-simplejson >= 3.5.1
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%python_subpackages

%description
OpenStackClient (aka OSC) is a command-line client for OpenStack.  osc-lib
is a package of common support modules for writing OSC plugins.

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
%autosetup -p1 -n osc-lib-1.14.1
%py_req_cleanup

%build
%{python_build}

%install
%{python_install}

# generate html docs
PBR_VERSION=%{version} PYTHONPATH=. %sphinx_build -a -E -d doc/build/doctrees -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/osc_lib
%{python_sitelib}/*.egg-info

%files -n python-osc-lib-doc
%license LICENSE
%doc doc/build/html

%changelog
