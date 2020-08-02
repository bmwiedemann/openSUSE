#
# spec file for package python-muranoclient
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


Name:           python-muranoclient
Version:        1.2.0
Release:        0
Summary:        Python API and CLI for OpenStack Murano
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PrettyTable >= 0.7.2
BuildRequires:  python-fixtures
BuildRequires:  python-glanceclient >= 2.8.0
BuildRequires:  python-keystoneclient >= 3.8.0
BuildRequires:  python-mock
BuildRequires:  python-murano-pkg-check >= 0.3.0
BuildRequires:  python-osc-lib >= 1.8.0
BuildRequires:  python-oslo.log >= 3.36.0
BuildRequires:  python-oslo.serialization >= 2.18.0
BuildRequires:  python-oslo.utils >= 3.33.0
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-pyOpenSSL >= 17.1.0
BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-stestr
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
BuildRequires:  python-yaql >= 1.1.3
Requires:       python-Babel >= 2.3.4
Requires:       python-PrettyTable >= 0.7.2
Requires:       python-PyYAML >= 3.12
Requires:       python-glanceclient >= 2.8.0
Requires:       python-iso8601 >= 0.1.11
Requires:       python-keystoneclient >= 3.8.0
Requires:       python-murano-pkg-check >= 0.3.0
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pbr >= 2.0.0
Requires:       python-pyOpenSSL >= 17.1.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-yaql >= 1.1.3
BuildArch:      noarch

%description
Client library for Murano built on the Murano API. It provides a Python API
(the muranoclient module) and a command-line tool (murano).

%package doc
Summary:        Documentation for OpenStack Magnum API client libary
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme
BuildRequires:  python-reno

%description doc
Client library for Murano built on the Murano API. It provides a Python API
(the muranoclient module) and a command-line tool (murano).
This package contains the documentation.

%prep
%autosetup -n %{name}-%{version}
%py_req_cleanup

%build
%py2_build

# Build HTML docs and man page
PBR_VERSION=%version sphinx-build -b html doc/source doc/build/html
rm -r doc/build/html/.{doctrees,buildinfo}

%install
%py2_install

%check
stestr run

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/muranoclient
%{python2_sitelib}/*.egg-info
%{_bindir}/murano

%files doc
%doc doc/build/html
%license LICENSE

%changelog
