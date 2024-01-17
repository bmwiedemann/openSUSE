#
# spec file for package python-ldap3
#
# Copyright (c) 2021 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-ldap3
Version:        2.9.1
Release:        0
Summary:        A strictly RFC 4511 conforming LDAP V3 pure Python client
License:        LGPL-3.0-only
URL:            https://github.com/cannatag/ldap3
Source:         https://github.com/cannatag/ldap3/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip-missing-LDAP-server.patch gh#cannatag/ldap3#843 mcepl@suse.com
# skip over tests failing because of the missing local LDAP server running
Patch0:         skip-missing-LDAP-server.patch
BuildRequires:  %{python_module pyasn1 >= 0.4.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-testsuite
Requires:       python-pyasn1 >= 0.4.6
BuildArch:      noarch
%python_subpackages

%description
ldap3 is a strictly RFC 4511 conforming LDAP V3 pure Python **client**.
The same codebase works with Python, Python 3, PyPy and PyPy3.

This project was formerly named **python3-ldap**.
The name has been changed to avoid confusion with the python-ldap library.

%prep
%setup -q -n ldap3-%{version}
%autopatch -p1

dos2unix COPYING.LESSER.txt COPYING.txt README.rst LICENSE.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export STRATEGY=SYNC SERVER=EDIR DECODER=INTERNAL
%pytest test/test*.py

%files %{python_files}
%license COPYING.LESSER.txt COPYING.txt LICENSE.txt
%doc README.rst
%{python_sitelib}/ldap3
%{python_sitelib}/ldap3-*-py*.egg-info

%changelog
