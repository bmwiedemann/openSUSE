#
# spec file for package python-pytest-asyncio
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
Name:           python-pytest-asyncio%{psuffix}
Version:        0.23.7
Release:        0
Summary:        Pytest support for asyncio
License:        Apache-2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source:         https://github.com/pytest-dev/pytest-asyncio/archive/v%{version}.tar.gz#/pytest-asyncio-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-pytest >= 7.0.0 with python-pytest < 9)
%if 0%{?python_version_nodots} < 38
Requires:       python-typing-extensions >= 3.7.2
%endif
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module hypothesis >= 5.7.1}
BuildRequires:  %{python_module pytest >= 7.0.0 with %python-pytest < 9}
BuildRequires:  %{python_module pytest-asyncio = %{version}}
%endif
%python_subpackages

%description
pytest-asyncio is a Python library used for testing asyncio code with pytest.

asyncio code is usually written in the form of coroutines, which makes it
slightly more difficult to test using normal testing tools. pytest-asyncio
provides useful fixtures and markers to make testing easier.

%prep
%autosetup -p1 -n pytest-asyncio-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%if !%{with test}
%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_asyncio
%{python_sitelib}/pytest_asyncio-%{version}.dist-info
%endif

%changelog
