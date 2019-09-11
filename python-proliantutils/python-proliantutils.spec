#
# spec file for package python-proliantutils
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


Name:           python-proliantutils
Version:        2.8.2
Release:        0
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/openstack/proliantutils
Source:         https://files.pythonhosted.org/packages/source/p/proliantutils/proliantutils-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  openstack-macros
BuildRequires:  python-ddt
BuildRequires:  python-devel
BuildRequires:  python-jsonschema
BuildRequires:  python-mock
BuildRequires:  python-os-testr
BuildRequires:  python-oslo.concurrency
BuildRequires:  python-oslo.serialization
BuildRequires:  python-oslo.utils
BuildRequires:  python-pbr
BuildRequires:  python-pysnmp
BuildRequires:  python-requests
BuildRequires:  python-retrying
BuildRequires:  python-rpm-macros
BuildRequires:  python-setuptools
BuildRequires:  python-six
BuildRequires:  python-sushy
BuildRequires:  python-testrepository
BuildRequires:  python-testtools
Requires:       python-jsonschema >= 2.0.0
Requires:       python-oslo.concurrency >= 3.8.0
Requires:       python-oslo.serialization >= 1.10.0
Requires:       python-oslo.utils >= 3.20.0
Requires:       python-pysnmp >= 4.2.3
Requires:       python-requests >= 2.10.0
Requires:       python-retrying >= 1.2.3
Requires:       python-six >= 1.9.0
Requires:       python-sushy >= 1.8.0
BuildArch:      noarch

%description
proliantutils is a set of utility libraries for interfacing and managing
various components (like iLO, HPSSA) for HP Proliant Servers.  This library
is used by iLO drivers in Ironic for managing Proliant Servers, though the
library can be used by anyone who wants to manage HP Proliant servers.

Please use https://bugs.launchpad.net/proliantutils to report bugs and ask
questions.

%prep
%setup -q -n proliantutils-%{version}

%build
%py2_build

%install
%py2_install
%fdupes %{buildroot}%{python_sitelib}

%check
%{__python2} setup.py testr

%files
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
