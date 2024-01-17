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


%{?sle15_python_module_pythons}
Name:           python-openapi-schema-validator
Version:        0.6.2
Release:        0
Summary:        OpenAPI schema validator for Python
License:        BSD-3-Clause
URL:            https://github.com/p1c2u/openapi-schema-validator
Source:         https://github.com/p1c2u/openapi-schema-validator/archive/%{version}.tar.gz#/openapi-schema-validator-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-openapi_schema_validator = %{version}-%{release}
Requires:       python-jsonschema-specifications >= 2023.5.2
Requires:       python-rfc3339-validator
Requires:       (python-jsonschema >= 4.19.1 with python-jsonschema < 5)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jsonschema >= 4.19.1 with %python-jsonschema < 5}
BuildRequires:  %{python_module jsonschema-specifications >= 2023.5.2}
BuildRequires:  %{python_module pytest >= 7}
BuildRequires:  %{python_module rfc3339-validator}
# /SECTION
%python_subpackages

%description
Openapi-schema-validator is a Python library that validates
schema against the OpenAPI Schema Specification v3.0 which
is an extended subset of the JSON Schema Specification
Wright Draft 00.

%prep
%autosetup -p1 -n openapi-schema-validator-%{version}
sed -i 's:tool.pytest.ini_options:hide:' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not (test_validators)'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/openapi_schema_validator-%{version}.dist-info
%{python_sitelib}/openapi_schema_validator

%changelog
