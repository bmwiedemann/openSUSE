#
# spec file for package python-parse_type
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


%bcond_without python2
Name:           python-parse_type
Version:        0.6.3
Release:        0
Summary:        Extension to the parse module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jenisys/parse_type
Source:         https://github.com/jenisys/parse_type/archive/v%{version}.tar.gz
# to remove python 2 is the goal of 0.7.0
# https://github.com/jenisys/parse_type/blob/main/CHANGES.txt
# https://github.com/jenisys/parse_type/pull/24
Patch0:         python-parse_type-remove-python2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-parse >= 1.12.0
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34
%endif
%ifpython2
Requires:       python-enum34
%endif
# SECTION test requirements
BuildRequires:  %{python_module parse >= 1.12.0}
BuildRequires:  %{python_module pytest >= 3.0}
# /SECTION
%python_subpackages

%description
parse_type extends the parse module (opposite of string.format()) with
the following features:

  * build type converters for common use cases (enum/mapping, choice)
  * build a type converter with a cardinality constraint (0..1, 0..*, 1..*)
    from the type converter with cardinality=1.
  * compose a type converter from other type converters
  * an extended parser that supports the CardinalityField naming schema
    and creates missing type variants (0..1, 0..*, 1..*) from the
    primary type converter

%prep
%autosetup -p1 -n parse_type-%{version}

# no extra pytest options are needed
rm pytest.ini
# Remove bundled parse.py
rm parse_type/parse.py
sed -i 's:from parse_type import parse:import parse:' \
  tests/*.py tests/parse_tests_with_parse_type/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/parse_type
%{python_sitelib}/parse_type-%{version}*-info

%changelog
