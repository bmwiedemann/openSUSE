#
# spec file for package python-oslo.utils
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


Name:           python-oslo.utils
Version:        3.40.3
Release:        0
Summary:        OpenStack Utils Library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.utils
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.utils/oslo.utils-3.40.3.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python2-Babel
BuildRequires:  python2-ddt
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-eventlet
BuildRequires:  python2-fixtures
BuildRequires:  python2-iso8601 >= 0.1.11
BuildRequires:  python2-mock
BuildRequires:  python2-monotonic >= 0.6
BuildRequires:  python2-netaddr >= 0.7.18
BuildRequires:  python2-netifaces >= 0.10.4
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-pyparsing >= 2.1.0
BuildRequires:  python2-stestr
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-Babel
BuildRequires:  python3-ddt
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-iso8601 >= 0.1.11
BuildRequires:  python3-mock
BuildRequires:  python3-netaddr >= 0.7.18
BuildRequires:  python3-netifaces >= 0.10.4
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-pyparsing >= 2.1.0
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-debtcollector >= 1.2.0
Requires:       python-iso8601 >= 0.1.11
Requires:       python-netaddr >= 0.7.18
Requires:       python-netifaces >= 0.10.4
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-pyparsing >= 2.1.0
Requires:       python-pytz >= 2013.6
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%ifpython2
Requires:       python-monotonic >= 0.6
%endif
%python_subpackages

%description
The oslo.utils library provides support for common utility type functions,
such as encoding, exception handling, string manipulation, and time handling.

%package -n python-oslo.utils-doc
Summary:        Documentation for OpenStack utils library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.utils-doc
Documentation for OpenStack utils library.

%prep
%autosetup -p1 -n oslo.utils-3.40.3

%py_req_cleanup

%build
%python_build

%install
%python_install

# generate html docs
#%{__python2} setup.py build_sphinx
PBR_VERSION=3.40.3 sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{python2_sitelib}/oslo_utils
%{python2_sitelib}/*.egg-info

%files -n python-oslo.utils-doc
%doc doc/build/html
%license LICENSE

%changelog
