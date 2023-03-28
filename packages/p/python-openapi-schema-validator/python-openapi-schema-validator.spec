#
# spec file for package python-openapi-schema-validator
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-openapi-schema-validator
Version:        0.3.4
Release:        0
Summary:        OpenAPI schema validator for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/p1c2u/openapi-schema-validator
Source:         https://github.com/p1c2u/openapi-schema-validator/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-isodate
Requires:       python-jsonschema
Requires:       python-setuptools
Requires:       python-strict-rfc3339
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module strict-rfc3339}
# /SECTION
%python_subpackages

%description
Openapi-schema-validator is a Python library that validates
schema against the OpenAPI Schema Specification v3.0 which
is an extended subset of the JSON Schema Specification
Wright Draft 00.

%prep
%setup -q -n openapi-schema-validator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
sed -i 's:tool.pytest.ini_options:hide:' pyproject.toml
# no rfc3339-validator installed
%pytest -k 'not test_string_format_datetime_rfc3339_validator'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*openapi_schema_validator*/

%changelog
