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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-proliantutils
Version:        2.9.1
Release:        0
Summary:        Client Library for interfacing with various devices in HP Proliant Servers
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/openstack/proliantutils
Source:         https://files.pythonhosted.org/packages/source/p/proliantutils/proliantutils-%{version}.tar.gz
BuildRequires:  %{python_module ddt}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module oslo.concurrency}
BuildRequires:  %{python_module oslo.serialization}
BuildRequires:  %{python_module oslo.utils}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pysnmp}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module retrying}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module sushy}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  openstack-macros
Requires:       python-jsonschema >= 2.6.0
Requires:       python-oslo.concurrency >= 3.8.0
Requires:       python-oslo.serialization >= 1.10.0
Requires:       python-oslo.utils >= 3.20.0
Requires:       python-pysnmp >= 4.2.3
Requires:       python-requests >= 2.10.0
Requires:       python-retrying >= 1.2.3
Requires:       python-six >= 1.9.0
Requires:       python-sushy >= 1.8.0
BuildArch:      noarch
%python_subpackages

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
%python_build

%install
%python_install
%fdupes %{buildroot}%{python_sitelib}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
