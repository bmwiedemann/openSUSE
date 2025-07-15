#
# spec file for package python-openapi-spec-validator
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-openapi-spec-validator
Version:        0.7.2
Release:        0
Summary:        Python module for validating OpenAPI Specs against Swagger and OAS3
License:        Apache-2.0
URL:            https://github.com/p1c2u/openapi-spec-validator
Source:         https://github.com/p1c2u/openapi-spec-validator/archive/%{version}.tar.gz#/openapi-spec-validator-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-openapi_spec_validator
Requires:       (python-jsonschema >= 4.18 with python-jsonschema < 5)
Requires:       (python-jsonschema-path >= 0.3.1 with python-jsonschema-path < 0.4)
Requires:       (python-lazy-object-proxy >= 1.7.1 with python-lazy-object-proxy < 2)
Requires:       (python-openapi-schema-validator >= 0.6.0 with python-openapi-schema-validator < 0.7)
%if %{python_version_nodots} < 39
Requires:       python-importlib-resources >= 5.8.0
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module importlib-resources >= 5.8.0 if %python-base < 3.9}
BuildRequires:  %{python_module jsonschema >= 4.18 with %python-jsonschema < 5}
BuildRequires:  %{python_module jsonschema-path >= 0.3.1 with %python-jsonschema-path < 0.4}
BuildRequires:  %{python_module lazy-object-proxy >= 1.7.1 with %python-lazy-object-proxy < 2}
BuildRequires:  %{python_module openapi-schema-validator >= 0.6.0 with %python-openapi-schema-validator < 0.7}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
OpenAPI Spec Validator is a Python library that validates
OpenAPI Specs against the OpenAPI 2.0 (aka Swagger) and
OpenAPI 3.0.0 specification. The validator aims to check
for full compliance with the Specification.

%prep
%autosetup -p1 -n openapi-spec-validator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/openapi-spec-validator
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative openapi-spec-validator

%postun
%python_uninstall_alternative openapi-spec-validator

%check
sed -i 's:tool.pytest.ini_options:hide:' pyproject.toml
%pytest -m 'not network'

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/openapi-spec-validator
%{python_sitelib}/openapi_spec_validator
%{python_sitelib}/openapi_spec_validator-%{version}.dist-info

%changelog
