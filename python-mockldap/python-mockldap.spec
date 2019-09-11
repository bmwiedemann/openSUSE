#
# spec file for package python-mockldap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.3.0
Release:        0
Summary:        A simple mock implementation of python-ldap
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://bitbucket.org/psagers/mockldap/
Source:         https://files.pythonhosted.org/packages/source/m/mockldap/mockldap-%{version}.tar.gz
BuildRequires:  %{python_module funcparserlib}
BuildRequires:  %{python_module ldap}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-funcparserlib
Requires:       python-ldap
Requires:       python-mock
BuildArch:      noarch
%python_subpackages

%description
This project provides a mock replacement for python-ldap. It's useful for any
project that would like to write unit tests against LDAP code without relying
on a running LDAP server.

%prep
%setup -q -n mockldap-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%{python_sitelib}/*

%changelog
