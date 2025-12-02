#
# spec file for package python-fastapi
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-fastapi%{psuffix}
Version:        0.122.0
Release:        0
Summary:        FastAPI framework
License:        MIT
URL:            https://github.com/fastapi/fastapi
Source:         https://files.pythonhosted.org/packages/source/f/fastapi/fastapi-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-annotated-doc >= 0.0.2
Requires:       python-pydantic >= 1.8.2
Requires:       python-typing_extensions >= 4.8.0
Requires:       (python-starlette >= 0.40.0 with python-starlette < 0.50.0)
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Flask >= 1.1.2}
BuildRequires:  %{python_module PyJWT}
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module aiosqlite}
BuildRequires:  %{python_module anyio >= 3.2.1}
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module email-validator >= 1.1.1}
BuildRequires:  %{python_module fastapi = %{version}}
BuildRequires:  %{python_module httpx >= 0.23.0}
BuildRequires:  %{python_module inline-snapshot}
BuildRequires:  %{python_module orjson >= 3.2.1}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module peewee >= 3.13.0}
BuildRequires:  %{python_module pwdlib >= 0.2.1}
BuildRequires:  %{python_module pydantic-settings >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-jose >= 3.3}
BuildRequires:  %{python_module python-multipart >= 0.0.18}
BuildRequires:  %{python_module sqlmodel}
BuildRequires:  %{python_module trio}
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
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}/%{_bindir}/fastapi
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# more warnings as expected
donttest="test_warn_duplicate_operation_id"
# fails because of changed (cosmetic) body format in httpx 0.28 (technically not suppoerted yet upstream)
donttest+=" or test_exception_handler_body_access"
# python-fastapi-cli packages doesn't exists in openSUSE
donttest+=" or test_fastapi_cli"
donttest+=" or test_openapi"
# seems to hang in OBS and only for 3.9 which we don't support anymore
donttest+=" or test_tutorial003_py39.py"
%pytest -W ignore::DeprecationWarning -W ignore::PendingDeprecationWarning -W ignore::ResourceWarning -k "not ($donttest)" tests
%endif

%pre
%python_libalternatives_reset_alternative fastapi

%post
%python_install_alternative fastapi

%postun
%python_uninstall_alternative fastapi

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/fastapi
%{python_sitelib}/fastapi-%{version}.dist-info
%python_alternative %{_bindir}/fastapi
%endif

%changelog
