#
# spec file for package python-sqlmodel
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-sqlmodel%{psuffix}
Version:        0.0.22
Release:        0
Summary:        SQL databases in Python, designed for simplicity, compatibility, and robustness
License:        MIT
URL:            https://github.com/fastapi/sqlmodel
Source:         https://files.pythonhosted.org/packages/source/s/sqlmodel/sqlmodel-%{version}.tar.gz
BuildRequires:  %{python_module SQLAlchemy >= 2.0.14}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pydantic >= 1.10.13}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy >= 2.0.14
Requires:       python-pydantic >= 1.10.13
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module dirty-equals}
BuildRequires:  %{python_module fastapi}
BuildRequires:  %{python_module httpx}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
%python_subpackages

%description
SQLModel is a library for interacting with SQL databases from Python code,
with Python objects. It is designed to be intuitive, easy to use, highly
compatible, and robust. SQLModel is based on Python type annotations, and
powered by Pydantic and SQLAlchemy.

%prep
%autosetup -p1 -n sqlmodel-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
export PYTHONPATH=$(pwd):$PYTHONPATH
%pytest -v tests
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/sqlmodel
%{python_sitelib}/sqlmodel-%{version}.dist-info
%endif

%changelog
