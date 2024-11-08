#
# spec file for package python-fastapi
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


# Keep extra test requirements out of Ring1
%bcond_with ringdisabled
%{?sle15_python_module_pythons}
Name:           python-fastapi
Version:        0.115.2
Release:        0
Summary:        FastAPI framework
License:        MIT
URL:            https://github.com/tiangolo/fastapi
Source:         https://files.pythonhosted.org/packages/source/f/fastapi/fastapi-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Remove two unknown classifiers
Patch0:         remove-classifiers.patch
# PATCH-FIX-OPENSUSE Allow new starlette
Patch1:         allow-new-starlette.patch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic-settings >= 2.0.0}
BuildRequires:  %{python_module starlette >= 0.37.2 with %python-starlette < 0.41.1}
BuildRequires:  %{python_module typing_extensions >= 4.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pydantic >= 1.8.2
Requires:       python-typing_extensions >= 4.8.0
Requires:       (python-starlette >= 0.37.2 with python-starlette < 0.41.1)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module Flask >= 1.1.2}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module anyio >= 3.2.1}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module httpx >= 0.23.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-multipart >= 0.0.7}
BuildRequires:  %{python_module trio}
%if !%{with ringdisabled}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module databases >= 0.3.2}
BuildRequires:  %{python_module email-validator >= 1.1.1}
BuildRequires:  %{python_module inline-snapshot}
BuildRequires:  %{python_module orjson >= 3.2.1}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module peewee >= 3.13.0}
BuildRequires:  %{python_module python-jose >= 3.3}
BuildRequires:  %{python_module sqlmodel}
BuildRequires:  %{python_module ujson >= 5.6}
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
%python_clone -a %{buildroot}/%{_bindir}/fastapi
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# more warnings as expected
donttest="test_warn_duplicate_operation_id"
# https://github.com/tiangolo/fastapi/discussions/9934
donttest+=" or test_dependency_gets_exception"
# python-fastapi-cli packages doesn't exists in openSUSE
donttest+=" or test_fastapi_cli"
donttest+=" or test_openapi"
%if %{with ringdisabled}
ignorefiles="$ignorefiles --ignore tests/test_default_response_class.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_async_sql_databases/test_tutorial001.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_custom_response/test_tutorial009c.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_cookie_param_models/test_tutorial001.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_cookie_param_models/test_tutorial002.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_header_param_models/test_tutorial001.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_header_param_models/test_tutorial002.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_query_param_models/test_tutorial001.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_query_param_models/test_tutorial002.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_response_model/test_tutorial003.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_response_model/test_tutorial003_py310.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005_py39.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005_py310.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005_an.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005_an_py39.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_security/test_tutorial005_an_py310.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_sql_databases/test_tutorial001.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_sql_databases/test_tutorial002.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_sql_databases_peewee"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_response_model/test_tutorial003_01.py"
ignorefiles="$ignorefiles --ignore tests/test_tutorial/test_response_model/test_tutorial003_01_py310.py"

donttest="$donttest or test_orjson_response_class"
donttest="$donttest or (test_tutorial001 and test_get_custom_response)"
%endif
%pytest -W ignore::DeprecationWarning -W ignore::PendingDeprecationWarning -W ignore::ResourceWarning $ignorefiles -k "not ($donttest)" tests

%post
%python_install_alternative fastapi

%postun
%python_uninstall_alternative fastapi

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fastapi
%{python_sitelib}/fastapi-%{version}.dist-info
%python_alternative %{_bindir}/fastapi

%changelog
