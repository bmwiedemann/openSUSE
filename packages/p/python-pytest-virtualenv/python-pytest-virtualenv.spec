#
# spec file for package python-pytest-virtualenv
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
# https://github.com/man-group/pytest-plugins/issues/220
%define skip_python312 1
%define skip_python313 1
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-pytest-virtualenv%{psuffix}
Version:        1.8.0
Release:        0
Summary:        Virtualenv fixture for pytest
License:        MIT
URL:            https://github.com/man-group/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-virtualenv/pytest-virtualenv-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove dependency on the external module virtualenv
Patch0:         remove_virtualenv.patch
%if %{with test}
BuildRequires:  %{python_module pytest-virtualenv = %{version}}
%endif
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-pytest
Requires:       python-pytest-fixture-config
Requires:       python-pytest-shutil
BuildArch:      noarch
%python_subpackages

%description
Create a Python virtual environment in your test that cleans up on
teardown. The fixture has utility methods to install packages and list
what's installed.

%prep
%autosetup -p1 -n pytest-virtualenv-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# Requires network access
%pytest -k 'not (test_installed_packages or test_install_)'
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/pytest_virtualenv.py
%pycache_only %{python_sitelib}/__pycache__/pytest_virtualenv*.pyc
%{python_sitelib}/pytest_virtualenv-%{version}.dist-info
%endif

%changelog
