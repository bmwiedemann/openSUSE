#
# spec file for package python-boolean.py
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
Name:           python-boolean.py
Version:        3.6
Release:        0
Summary:        Module to define boolean algebras and create/parse boolean expressions
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/bastikr/boolean.py
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
"boolean.py" is a library implementing a boolean algebra. It defines
two base elements, TRUE and FALSE, and a Symbol class that can take on one of
these two values. Calculations are done in terms of AND, OR and NOT - other
compositions like XOR and NAND are not implemented but can be emulated with
AND or and NOT. Expressions are constructed from parsed strings or in Python.

%prep
%setup -q -n boolean.py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE.txt
%doc README.md CHANGELOG.rst html/
%{python_sitelib}/*

%changelog
