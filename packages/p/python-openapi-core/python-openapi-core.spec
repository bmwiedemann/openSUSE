#
# spec file for package python-openapi-core
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


Name:           python-openapi-core
Version:        0.17.2
Release:        0
Summary:        Client- and server-side support for the OpenAPI Specification v3
License:        BSD-3-Clause
URL:            https://github.com/p1c2u/openapi-core
Source:         https://files.pythonhosted.org/packages/source/o/openapi-core/openapi_core-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module Django >= 3.0}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module aiohttp >= 3.0}
BuildRequires:  %{python_module asgiref >= 3.6}
BuildRequires:  %{python_module falcon >= 3.0}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module jsonschema-spec >= 0.1.6}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module openapi-schema-validator >= 0.3.0}
BuildRequires:  %{python_module openapi-spec-validator >= 0.5.0}
BuildRequires:  %{python_module parse >= 1.14.0}
BuildRequires:  %{python_module pytest-aiohttp}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module responses}
# /SECTION
Requires:       python-Werkzeug
Requires:       python-asgiref >= 3.6
Requires:       python-isodate
Requires:       python-jsonschema-spec >= 0.1.6
Requires:       python-more-itertools
Requires:       python-openapi-schema-validator >= 0.3.0
Requires:       python-openapi-spec-validator >= 0.5.0
Requires:       python-parse >= 1.14.0
BuildArch:      noarch
%python_subpackages

%description
Openapi-core is a Python library that adds client-side
and server-side support for the OpenAPI Specification
v3.0.0.

%prep
%setup -q -n openapi_core-%{version}
sed -i '/--cov/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit -k 'not (test_read_only_properties_invalid or test_write_only_properties_invalid)'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/openapi_core
%{python_sitelib}/openapi_core-%{version}*-info

%changelog
