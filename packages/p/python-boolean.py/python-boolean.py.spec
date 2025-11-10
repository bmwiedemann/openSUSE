#
# spec file for package python-boolean.py
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-boolean.py
Version:        5.0
Release:        0
Summary:        Module to define boolean algebras and create/parse boolean expressions
License:        BSD-2-Clause
URL:            https://github.com/bastikr/boolean.py
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sphinxcontrib-apidoc}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst html/
%{python_sitelib}/boolean
%{python_sitelib}/boolean[._]py-%{version}.dist-info

%changelog
