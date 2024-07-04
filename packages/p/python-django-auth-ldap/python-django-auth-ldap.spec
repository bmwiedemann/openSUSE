#
# spec file for package python-django-auth-ldap
#
# Copyright (c) 2024 SUSE LLC
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
%define skip_python2 1
Name:           python-django-auth-ldap
Version:        4.8.0
Release:        0
Summary:        Django LDAP authentication backend
License:        BSD-2-Clause
URL:            https://github.com/django-auth-ldap/django-auth-ldap
Source:         https://files.pythonhosted.org/packages/source/d/django-auth-ldap/django-auth-ldap-%{version}.tar.gz
BuildRequires:  %{python_module Django >= 2.2}
BuildRequires:  %{python_module ldap >= 3.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# needed for slapd binary in tests
BuildRequires:  openldap2
# needed for ldapadd binary in tests
BuildRequires:  openldap2-client
Requires:       python-Django >= 2.2
Requires:       python-ldap >= 3.1
BuildArch:      noarch
%python_subpackages

%description
This is a Django authentication backend that authenticates against an LDAP service.
Configuration can be as simple as a single distinguished name template, but there
are many rich configuration options for working with users, groups, and permissions.

%prep
%setup -q -n django-auth-ldap-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF8
export PATH=/sbin:/usr/sbin:/usr/local/bin:/usr/bin:/bin
%python_exec -m django test --settings tests.settings -v2

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
