#
# spec file for package python-pyinstaller-hooks-contrib
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -%{flavor}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-pyinstaller-hooks-contrib%{psuffix}
Version:        2024.11
Release:        0
Summary:        Community maintained hooks for PyInstaller
License:        Apache-2.0 OR GPL-2.0-only
URL:            https://github.com/pyinstaller/pyinstaller-hooks-contrib
Source:         https://files.pythonhosted.org/packages/source/p/pyinstaller_hooks_contrib/pyinstaller_hooks_contrib-%{version}.tar.gz
# conftest.py not present in the tarball
Source1:        https://raw.githubusercontent.com/pyinstaller/pyinstaller-hooks-contrib/refs/heads/master/tests/conftest.py
BuildRequires:  %{python_module setuptools >= 30.3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyInstaller}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyinstaller-hooks-contrib = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  timezone
# SECTION optional, the depending tests would be skipped without these
# most of the libraries enable only two tests, so adding just scikit-learn to run at least any tests
BuildRequires:  %{python_module scikit-learn}
# /SECTION
%endif
%python_subpackages

%description
Community maintained hooks for PyInstaller

%prep
%autosetup -p1 -n pyinstaller_hooks_contrib-%{version}
cp %{SOURCE1} tests/

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# pytest-runner is dead in Python 3.13
%pytest -k "not pytest_runner"
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/_pyinstaller_hooks_contrib
%{python_sitelib}/pyinstaller_hooks_contrib-%{version}*-info
%endif

%changelog
