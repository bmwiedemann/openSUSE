#
# spec file for package python-ldappool
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
Name:           python-ldappool
Version:        2.4.1
Release:        0
Summary:        A connection pool for python-ldap
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://git.openstack.org/cgit/openstack/ldappool
Source:         https://files.pythonhosted.org/packages/source/l/ldappool/ldappool-%{version}.tar.gz
BuildRequires:  %{python_module ldap >= 3.0.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module testresources}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable
Requires:       python-ldap >= 3.0.0
BuildArch:      noarch
%python_subpackages

%description
A simple connector pool for python-ldap.

The pool keeps LDAP connectors alive and let you reuse them,
drastically reducing the time spent to initiate a ldap connection.

The pool has useful features like:

- transparent reconnection on failures or server restarts
- configurable pool size and connectors timeouts
- configurable max lifetime for connectors
- a context manager to simplify acquiring and releasing a connector

%prep
%setup -q -n ldappool-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m stestr.cli run

%files %{python_files}
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
