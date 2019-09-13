#
# spec file for package python-pyshould
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


%define modname pyshould
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{modname}
Version:        0.7.1
Release:        0
Summary:        Should style asserts
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/drslump/%{modname}
Source:         https://files.pythonhosted.org/packages/source/p/pyshould/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-hamcrest
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hamcrest}
BuildRequires:  %{python_module nose}
# /SECTION
%python_subpackages

%description
PyShould is a Python DSL allowing to write expectations or assertions
in almost natural language. The goal is to offer an expressive yet
readable syntax to define the expectations in detail.

Under the hood it uses the PyHamcrest library of matchers to build
complex matching predicates and great explanations when there is a
mismatch.

Its primary use case is in unit testing, replacing the need for
Python's native assertX methods. Its use is completely transparent
to the unit testing runner used, since mismatches are reported using
the standard AssertionError.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
# We shouldn't install tests
%python_expand rm -rvf %{buildroot}%{$python_sitelib}/tests

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}*

%changelog
