#
# spec file for package python-ldappool
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


Name:           python-ldappool
Version:        3.0.0
Release:        0
Summary:        A connection pool for python-ldap
License:        GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://git.openstack.org/cgit/openstack/ldappool
Source:         https://files.pythonhosted.org/packages/source/l/ldappool/ldappool-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-six-dep.patch https://review.opendev.org/c/openstack/ldappool/+/805495
Patch:          remove-six-dep.patch
BuildRequires:  %{python_module ldap >= 3.0.0}
BuildRequires:  %{python_module pbr}
# SECTION stestr is only available for primary python3 flavor (openstack package)
BuildRequires:  python3-stestr
BuildRequires:  python3-testresources
BuildRequires:  python3-testtools
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ldap >= 3.0.0
Requires:       python-prettytable
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
%autosetup -p1 -n ldappool-%{version}
sed -i 's/PrettyTable<0.8,>=0.7.2/prettytable>=0.7.2/' requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/ldappool/tests

%check
python3 -m stestr.cli run

%files %{python_files}
%doc CHANGES.rst README.rst
%{python_sitelib}/ldappool
%{python_sitelib}/ldappool-%{version}*-info

%changelog
