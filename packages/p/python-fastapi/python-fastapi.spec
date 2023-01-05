#
# spec file for package python-fastapi
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


# Keep extra test requirements out of Ring1
%bcond_with ringdisabled
Name:           python-fastapi
Version:        0.88.0
Release:        0
Summary:        FastAPI framework
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tiangolo/fastapi
Source:         https://files.pythonhosted.org/packages/source/f/fastapi/fastapi-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 1.8.2}
BuildRequires:  %{python_module starlette >= 0.22.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 1.8.2
Requires:       python-starlette >= 0.22.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module Flask >= 1.1.2}
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module SQLAlchemy >= 1.3.18}
BuildRequires:  %{python_module anyio >= 3.2.1}
BuildRequires:  %{python_module httpx >= 0.23.0}
BuildRequires:  %{python_module python-multipart >= 0.0.5}
BuildRequires:  %{python_module trio}
%if !%{with ringdisabled}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module databases >= 0.3.2}
BuildRequires:  %{python_module email-validator >= 1.1.1}
BuildRequires:  %{python_module orjson >= 3.2.1}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module peewee >= 3.13.0}
BuildRequires:  %{python_module python-jose >= 3.3}
BuildRequires:  %{python_module ujson >= 5.2}
%endif
# /SECTION
%python_subpackages

%description
Python FastAPI framework.

%prep
%autosetup -p1 -n fastapi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# more warnings as expected
donttest="test_warn_duplicate_operation_id"
%if %{with ringdisabled}
ignorefiles="$ignorefiles --ignore tests/test_default_response_class.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_async_sql_databases/test_tutorial001.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_custom_response/test_tutorial009c.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_response_model/test_tutorial003.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_response_model/test_tutorial003_py310.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005_py39.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005_py310.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_sql_databases_peewee"
donttest="$donttest or test_orjson_response_class"
donttest="$donttest or (test_tutorial001 and test_get_custom_response)"
%endif
%pytest -W ignore::DeprecationWarning $ignorefiles -k "not ($donttest)" tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fastapi
%{python_sitelib}/fastapi-%{version}.dist-info

%changelog
