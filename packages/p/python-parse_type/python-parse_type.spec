#
# spec file for package python-parse_type
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
Name:           python-parse_type
Version:        0.5.3
Release:        0
Summary:        Extension to the parse module
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jenisys/parse_type
Source:         https://github.com/jenisys/parse_type/archive/v%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with python2}
BuildRequires:  python-enum34
%endif
Requires:       python-parse >= 1.12.0
Requires:       python-six >= 1.11
%ifpython2
Requires:       python-enum34
%endif
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module parse >= 1.12.0}
BuildRequires:  %{python_module pytest >= 3.0}
BuildRequires:  %{python_module six >= 1.11}
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
%setup -q -n parse_type-%{version}

# no extra pytest options are needed
rm pytest.ini
# Remove bundled parse.py
rm parse_type/parse.py
rm tests/test_parse.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
