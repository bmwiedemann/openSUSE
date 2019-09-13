#
# spec file for package python-mockldap
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
Name:           python-mockldap
Version:        0.3.0.post1
Release:        0
Summary:        A simple mock implementation of python-ldap
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/psagers/mockldap
Source:         https://files.pythonhosted.org/packages/source/m/mockldap/mockldap-%{version}.tar.gz
BuildRequires:  %{python_module funcparserlib >= 0.3.6}
BuildRequires:  %{python_module ldap >= 3.0}
BuildRequires:  %{python_module setuptools >= 0.6c11}
BuildRequires:  fdupes
BuildRequires:  python-mock
BuildRequires:  python-rpm-macros
Requires:       python-funcparserlib >= 0.3.6
Requires:       python-ldap >= 3.0
%ifpython2
Requires:       python-mock
%endif
BuildArch:      noarch
%python_subpackages

%description
This project provides a mock replacement for python-ldap. It's useful for any
project that would like to write unit tests against LDAP code without relying
on a running LDAP server.

%prep
%setup -q -n mockldap-%{version}
sed -i -e 's:==:>=:g' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE.rst
%{python_sitelib}/*

%changelog
