#
# spec file for package python-watcherclient
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


Name:           python-watcherclient
Version:        2.2.0
Release:        0
Summary:        Python API and CLI for OpenStack Watcher
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PrettyTable >= 0.7.2
BuildRequires:  python-PyYAML >= 3.12
BuildRequires:  python-cliff >= 2.11.0
BuildRequires:  python-fixtures
BuildRequires:  python-keystoneauth1 >= 3.4.0
BuildRequires:  python-mock
BuildRequires:  python-osc-lib >= 1.10.0
BuildRequires:  python-oslo.i18n >= 3.20.0
BuildRequires:  python-oslo.serialization
BuildRequires:  python-oslo.utils >= 3.36.0
BuildRequires:  python-oslotest
BuildRequires:  python-pbr >= 3.1.1
BuildRequires:  python-python-subunit
BuildRequires:  python-setuptools
BuildRequires:  python-stestr
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
Requires:       python-Babel >= 2.5.3
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-PyYAML >= 3.12
Requires:       python-cliff >= 2.11.0
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-osc-lib >= 1.10.0
Requires:       python-oslo.i18n >= 3.20.0
Requires:       python-oslo.utils >= 3.36.0
Requires:       python-pbr >= 3.1.1
Requires:       python-six >= 1.11.0
BuildArch:      noarch

%description
Client library for Watcher built on the Watcher API. It provides a Python API
(the watcherclient module) and a command-line tool (watcher).

%package doc
Summary:        Documentation for OpenStack Watcher API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description doc
Client library for Watcher built on the Watcher API. It provides a Python API
(the watcherclient module) and a command-line tool (watcher).
This package contains the documentation.

%prep
%autosetup -n %{name}-%{version}
%py_req_cleanup
sed -i 's/^warning-is-error.*/warning-is-error = 0/g' setup.cfg

%build
%py2_build

# Build HTML docs and man page
%{__python2} setup.py build_sphinx
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install

%check
%{__python2} -m stestr.cli --test-path=./watcherclient/tests/unit run

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/watcherclient
%{python2_sitelib}/*.egg-info
%{_bindir}/watcher

%files doc
%doc doc/build/html
%license LICENSE

%changelog
