#
# spec file for package python-openapi-core
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


# python-Django is not present in SLE 16
%if 0%{suse_version} >= 1699
%bcond_without django
%endif

Name:           python-openapi-core
Version:        0.19.5
Release:        0
Summary:        Client- and server-side support for the OpenAPI Specification v3
License:        BSD-3-Clause
URL:            https://github.com/p1c2u/openapi-core
Source:         https://github.com/p1c2u/openapi-core/archive/%{version}.tar.gz#/openapi-core-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module aiohttp >= 3}
BuildRequires:  %{python_module asgiref >= 3.6.0}
BuildRequires:  %{python_module falcon >= 3.0}
BuildRequires:  %{python_module isodate}
BuildRequires:  %{python_module jsonschema >= 4.18.0 with %python-jsonschema < 5}
BuildRequires:  %{python_module jsonschema-path >= 0.3.1 with %python-jsonschema-path < 0.4}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module multidict >= 6.0.4}
BuildRequires:  %{python_module openapi-schema-validator >= 0.6 with %python-openapi-schema-validator < 0.7}
BuildRequires:  %{python_module openapi-spec-validator >= 0.7.1 with %python-openapi-spec-validator < 0.8}
BuildRequires:  %{python_module parse}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module responses}
%if %{with django}
BuildRequires:  %{python_module Django}
%endif
# /SECTION
Requires:       python-Werkzeug
Requires:       python-asgiref >= 3.6.0
Requires:       python-isodate
Requires:       python-more-itertools
Requires:       python-parse
Requires:       (python-jsonschema >= 4.18.0 with python-jsonschema < 5)
Requires:       (python-jsonschema-path >= 0.3.1 with python-jsonschema-path < 0.4)
Requires:       (python-openapi-schema-validator >= 0.6 with python-openapi-schema-validator < 0.7)
Requires:       (python-openapi-spec-validator >= 0.7.1 with python-openapi-spec-validator < 0.8)
BuildArch:      noarch
%python_subpackages

%description
Openapi-core is a Python library that adds client-side
and server-side support for the OpenAPI Specification
v3.0.0.

%prep
%setup -q -n openapi-core-%{version}
sed -i '/--cov/d' pyproject.toml
for f in openapi_core/contrib/falcon/views.py; do
  [ -f $f -a ! -s $f ] && echo "# empty module" > $f || exit 1
done

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if !%{with django}
rm -v tests/unit/contrib/django/test_django.py
%endif
# https://github.com/python-openapi/openapi-core/issues/1009 TestImportModelCreate::test_dynamic_model fails with Python 3.14
%pytest tests/unit -k 'not (test_dynamic_model)'

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/openapi_core
%{python_sitelib}/openapi_core-%{version}*-info

%changelog
