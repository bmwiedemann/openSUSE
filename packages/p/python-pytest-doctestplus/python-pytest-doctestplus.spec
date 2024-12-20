#
# spec file for package python-pytest-doctestplus
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
Name:           python-pytest-doctestplus%{psuffix}
Version:        1.3.0
Release:        0
Summary:        Pytest plugin with advanced doctest features
License:        BSD-3-Clause
URL:            https://github.com/scientific-python/pytest-doctestplus
Source:         https://files.pythonhosted.org/packages/source/p/pytest-doctestplus/pytest_doctestplus-%{version}.tar.gz
# PATCH-FIX-UPSTREAM add-missing-xfail-version.patch (gh#23eb3de)
Patch0:         add-missing-xfail-version.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 17.0
Requires:       python-pytest >= 4.6
%if %{with test}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pip >= 19.3.1}
BuildRequires:  %{python_module pytest-doctestplus = %{version}}
BuildRequires:  %{python_module pytest-remotedata >= 0.3.2}
BuildRequires:  git-core
%else
BuildArch:      noarch
%endif
%python_subpackages

%description
This package contains a plugin for the pytest framework that provides
advanced doctest support and enables the testing of various text files, such
as reStructuredText (".rst"), markdown (".md"), and TeX (".tex").

%prep
%autosetup -p1 -n pytest_doctestplus-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export LANG=en_US.UTF8
export PY_IGNORE_IMPORTMISMATCH=1
%pytest tests/ --doctest-plus --doctest-rst -k "not test_remote_data_url and not test_import_mode"
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%{python_sitelib}/pytest_doctestplus
%{python_sitelib}/pytest_doctestplus-%{version}.dist-info
%endif

%changelog
